import os
from google import genai
from tools.knowledge import PRODUCT_CATALOG
import dotenv

dotenv.load_dotenv()


class CustomerOrderParser:
    def __init__(self):
        self.gemini_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    def parse_order(self, customer_inquiry: str):
        product_texts = [f"{p.name}. {p.description}" for p in PRODUCT_CATALOG]
        prompt = f"""
            You are an intelligent bakery staff whose job is to translate customer inquiry to order details.
            The customer will ask for products and your job is to tell if the product is available.
            If available you will describe the product and its price. If the product is not available, you will tell the customer that the product is not available.

            Sometimes there might be typos in the customer inquiry. You job is to fix it.

            I will give you the list of products and their details.
            {product_texts}

            Customer Inquiry: {customer_inquiry}

            Note:
            - You will only return the order details. Do not return any other text.
            - Return details in plain text. Do not use markdown.
            - The user might ask for multiple products. You will return the order details for each product.
            - You need to think step by step and return the order details in a structured way.
            - You should support multiple products in the same order.
            - Donot confuse about the language slangs and the cake types.

            Note: If there is something which is not in the product list, tell the user that we also make custom cakes.
            You need to validate if the customer query is making sense and than tell him that we do make such cake.
            Return order details as custom cake preparation and mention that it is doable.
        """

        response = self.gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        order_details = response.candidates[0].content.parts[0].text

        return {
            "order_details": order_details
        }