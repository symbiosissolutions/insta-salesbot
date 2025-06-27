import logging

from typing import Dict, Any
from tools.customer_order_parser import CustomerOrderParser

from fastmcp import FastMCP
from tools.order_manager import OrderManager
from tools.knowledge import PRODUCT_CATALOG
from tools.product_manager import ProductManager



# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


INSTRUCTIONS = """
This is a MCP server for Pumpernickel Bakery.
This server is responsible for the following things:
- Translating customer inquiry to order details.
- Managing the order.
- Checking if the order details are complete.
- Providing intelligent product information and recommendations.
- Handling customer queries about products, pricing, and services.
- Providing business information and company details.

You have following tools to use:

**Order Management Tools:**
1. customer_inquiry_to_order_translator: Converts full customer inquiry to structured order details.
2. order_manager: Places the order when customer confirms.
3. order_faq_tools: Translates customer inquiry to order details with product knowledge.
4. order_are_order_details_complete: Checks if all required order details are available. Returns *True* or *False*.

**Product & Company Information Tools:**
5. handle_product_inquiry: Use this for ALL product-related questions including:
   - Product information and descriptions
   - Pricing and size recommendations  
   - Allergen information and dietary concerns
   - Product recommendations and suggestions
   - Size estimation for parties and gatherings
   - Cake flavors and options

6. handle_company_inquiry: Use this for ALL business and company-related questions including:
   - Business information and history
   - Operating hours and location
   - Contact information and directions
   - FAQ responses (delivery, payment, custom orders)
   - Ordering process and requirements
   - Delivery and pickup options
   - Payment methods
   - Custom order information

7. get_product_catalog: Get the product catalog.

**When to Use Which Tool:**
- **Product Questions**: Use `handle_product_inquiry` for anything about cakes, flavors, prices, sizes, allergens
- **Business Questions**: Use `handle_company_inquiry` for anything about the company, hours, location, ordering process
- **Order Placement**: Use order management tools when customer is ready to place an order
"""

mcp = FastMCP(name="Pumpernickel Bakery", instructions=INSTRUCTIONS)

# Initialize ProductManager
product_manager = ProductManager()

@mcp.tool()
def customer_inquiry_to_order_translator(customer_inquiry: str) -> Dict[str, Any]:
    """
    Translate customer inquiry to order details.
    """
    customer_order_parser = CustomerOrderParser()
    order_details = customer_order_parser.parse_order(customer_inquiry)
    return order_details


@mcp.tool()
def order_manager(order_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Manage the order.
    """
    order_manager = OrderManager()
    order_id = order_manager.create_order_from_text(order_details)
    return order_id


@mcp.tool()
def order_are_order_details_complete(customer_order_details: str) -> bool:
    """
    Check if the order details are complete.
    """
    order_manager = OrderManager()
    return order_manager.are_order_details_complete(customer_order_details)


@mcp.tool()
def get_product_catalog() -> Dict[str, Any]:
    """
    Get the product catalog.
    """
    product_catalog = [product.to_dict() for product in PRODUCT_CATALOG]
    return product_catalog


@mcp.tool()
def handle_product_inquiry(query: str) -> str:
    """
    Handle ALL product-related queries including:
    - Product information and descriptions
    - Pricing and size recommendations
    - Allergen information and dietary concerns
    - Product recommendations and suggestions
    - Size estimation for parties and gatherings
    - Cake flavors and options
    
    Use this for any question about cakes, flavors, prices, sizes, allergens, etc.
    """
    return product_manager.handle_product_inquiry(query)


@mcp.tool()
def handle_company_inquiry(query: str) -> str:
    """
    Handle ALL business and company-related queries including:
    - Business information and history
    - Operating hours and location
    - Contact information and directions
    - FAQ responses (delivery, payment, custom orders)
    - Ordering process and requirements
    - Delivery and pickup options
    - Payment methods
    - Custom order information
    
    Use this for any question about the company, hours, location, ordering process, etc.
    """
    return product_manager.handle_company_inquiry(query)


if __name__ == "__main__":
    try:
        mcp.run(
            transport="streamable-http",
            host="127.0.0.1",
            port=4300,
            path="/bakery-mcp",
            log_level="debug",
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        print(f"Error: Failed to start Server - {str(e)}")
        exit(1)
