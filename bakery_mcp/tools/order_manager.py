import pandas as pd
from pydantic import BaseModel
import uuid
import json
import os
import dotenv
dotenv.load_dotenv()
from typing import List
from tools.knowledge import order_information_requirements


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

import json
import re



from google import genai



class Order(BaseModel):
    order_id: str = None
    name: str
    address: str
    user_id: str
    contact_number: str
    date: str
    time: str
    item_ordered: str
    delivery_notes: str
    order_type: str


class OrderLineItem(BaseModel):
    item_name: str
    quantity: int
    price: float


class OrderManager:
    def __init__(self):
        self.storage = "orders.csv"
        try:
            self.df = pd.read_csv(self.storage)
        except FileNotFoundError:
            # Create empty DataFrame with order columns
            self.df = pd.DataFrame()

    def create_order(self, order: Order, order_line_items: List[OrderLineItem]):
        """Create an order with line items stored in the same row with _line_{n} suffix"""
        if order.order_id is None:
            order.order_id = str(uuid.uuid4())
        
        # Start with the order data
        row_data = order.model_dump()
        
        # Add line items with _line_{n} suffix
        for i, item in enumerate(order_line_items, 1):
            for key, value in item.model_dump().items():
                row_data[f"{key}_line_{i}"] = value
        
        # Convert to DataFrame and append
        new_row = pd.DataFrame([row_data])
        if self.df.empty:
            self.df = new_row
        else:
            self.df = pd.concat([self.df, new_row], ignore_index=True)
        
        self.df.to_csv(self.storage, index=False)
        return order.order_id

    def get_order(self, user_id: str):
        """Get orders by user_id"""
        return self.df[self.df["user_id"] == user_id].to_dict(orient="records")

    def get_order_by_id(self, order_id: str):
        """Get a specific order by order_id"""
        result = self.df[self.df["order_id"] == order_id]
        if result.empty:
            return None
        return result.to_dict(orient="records")[0]

    def get_all_orders(self):
        """Get all orders"""
        return self.df.to_dict(orient="records")

    def update_order(self, order_id: str, order: Order, order_line_items: List[OrderLineItem] = None):
        """Update an existing order"""
        if order_id not in self.df["order_id"].values:
            return False
        
        # Update order details
        for key, value in order.model_dump().items():
            if key in self.df.columns:
                self.df.loc[self.df["order_id"] == order_id, key] = value
        
        # Update line items if provided
        if order_line_items:
            # Remove existing line item columns for this order
            row_index = self.df[self.df["order_id"] == order_id].index[0]
            line_columns = [col for col in self.df.columns if "_line_" in col]
            for col in line_columns:
                self.df.at[row_index, col] = None
            
            # Add new line items
            for i, item in enumerate(order_line_items, 1):
                for key, value in item.model_dump().items():
                    col_name = f"{key}_line_{i}"
                    if col_name not in self.df.columns:
                        self.df[col_name] = None
                    self.df.at[row_index, col_name] = value
        
        self.df.to_csv(self.storage, index=False)
        return True

    def delete_order(self, order_id: str):
        """Delete an order by order_id"""
        initial_length = len(self.df)
        self.df = self.df[self.df["order_id"] != order_id]
        self.df.to_csv(self.storage, index=False)
        return len(self.df) < initial_length

    def create_order_from_text(self, user_order: str):
        """Create an order from natural language text using LLM"""
        prompt = f"""
        You are an expert order manager.
        You will be given a user order.
        You will need to create an order.

        User Order: {user_order}

        Return the order details in the following format:
        {Order.model_json_schema()}

        And Order Line Items in the following format (as a list):
        [{OrderLineItem.model_json_schema()}]

        Note:
        - You will only return the order details and order line items. Do not return any other text.
        - Return details in plain text. Do not use markdown.
        - Always return in JSON format.
        - Generate a unique user_id if not provided
        - Fill in reasonable defaults for missing information

        Return JSON:
        {{
            "order": { {name: field.annotation for name, field in Order.model_fields.items()}},
            "order_line_items": [{ {name: field.annotation for name, field in OrderLineItem.model_fields.items()}}]
        }}
        """

        # try:
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.

        client = genai.Client(api_key=GEMINI_API_KEY)

        data = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        data = data.candidates[0].content.parts[0].text

        json_response = json.loads(data)

        order_data = json_response["order"]
        order_line_items_data = json_response["order_line_items"]

        # Create Order and OrderLineItem objects
        order = Order(**order_data)
        order_line_items = [OrderLineItem(**item) for item in order_line_items_data]

        # Create the order
        order_id = self.create_order(order, order_line_items)
        return order_id

        # except Exception as e:
        #     print(f"Error creating order from text: {e}")
        #     return None

    
    def are_order_details_complete(self, customer_order_details: str) -> bool:
        """
        Check if the order details are complete.
        """
        prompt = f"""
        You are an expert order manager.
        Your job is to check the order details and check if the order details are complete.
        If the order details are complete, return True.
        If the order details are not complete, return False.

        You will be given the order details and the required order details.

        Order Details: {customer_order_details}

        Required Order Details: {order_information_requirements()}

        Return True or False.
        """

        client = genai.Client(api_key=GEMINI_API_KEY)
        data = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        data = data.candidates[0].content.parts[0].text
        return data


    def extract_line_items_from_order(self, order_data: dict):
        """Extract line items from a row that contains _line_{n} suffixed columns"""
        line_items = []
        line_numbers = set()
        
        # Find all line numbers
        for col in order_data.keys():
            if "_line_" in col:
                line_num = col.split("_line_")[-1]
                try:
                    line_numbers.add(int(line_num))
                except ValueError:
                    continue
        
        # Extract line items
        for line_num in sorted(line_numbers):
            item_data = {}
            for key in ["item_name", "quantity", "price"]:
                col_name = f"{key}_line_{line_num}"
                if col_name in order_data and pd.notna(order_data[col_name]):
                    item_data[key] = order_data[col_name]
            
            if item_data:  # Only add if we have data
                line_items.append(OrderLineItem(**item_data))
        
        return line_items

    def get_order_with_line_items(self, order_id: str):
        """Get an order with its line items extracted"""
        order_data = self.get_order_by_id(order_id)
        if not order_data:
            return None
        
        # Extract order details (non-line item columns)
        order_details = {k: v for k, v in order_data.items() if "_line_" not in k}
        order = Order(**order_details)
        
        # Extract line items
        line_items = self.extract_line_items_from_order(order_data)
        
        return {
            "order": order,
            "line_items": line_items,
            "raw_data": order_data
        }
        

    def pounds_to_kilograms(pounds: float) -> float:
        """
        Convert pounds to kilograms.
        """
        kilograms = pounds * 0.45359237
        return kilograms


    def kilograms_to_pounds(kilograms: float) -> float:
        """
        Convert kilograms to pounds.
        """
        return kilograms / 0.45359237
    
