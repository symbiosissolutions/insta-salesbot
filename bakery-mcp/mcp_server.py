import logging
from datetime import datetime, time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


INSTRUCTIONS = """
Pumpernickel Bakery MCP Server
A comprehensive Model Context Protocol server for managing bakery operations,
product information, and customer service tools.
"""

mcp = FastMCP(name="Pumpernickel Bakery", instructions=INSTRUCTIONS)

# ===============================
# Data Models and Enums
# ===============================


class ProductCategory(Enum):
    CHOCOLATE_CAKE = "chocolate_cake"
    CHEESECAKE = "cheesecake"
    SPECIALTY_CAKE = "specialty_cake"
    SEASONAL = "seasonal"


class ProductSize(Enum):
    SMALL = "5inch"
    LARGE = "8inch"


@dataclass
class Product:
    name: str
    category: ProductCategory
    sizes: Dict[str, int]  # size -> price mapping
    weights: Dict[str, str]  # size -> weight mapping
    description: str
    tags: List[str]
    allergens: List[str]
    available: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convert product to dictionary format"""
        return {
            "name": self.name,
            "category": self.category.value,
            "sizes": self.sizes,
            "weights": self.weights,
            "description": self.description,
            "tags": self.tags,
            "allergens": self.allergens,
            "available": self.available,
        }


@dataclass
class BusinessInfo:
    name: str
    established: int
    tagline: str
    location: str
    address: str
    phone: str
    whatsapp: str
    email: str
    maps_link: str
    hours: str
    about: str


# ===============================
# Business Data
# ===============================

BUSINESS_INFO = BusinessInfo(
    name="Pumpernickel Bakery",
    established=1986,
    tagline="Freshly Made, Classic Taste",
    location="Thamel, Kathmandu",
    address="Thamel, Kathmandu, Nepal",
    phone="+977 9826045931",
    whatsapp="http://wa.me/9779826045931",
    email="customer.service@pumpernickel.com.np",
    maps_link="https://maps.app.goo.gl/iUnUcJW7ZMGeHd3P8",
    hours="6:30 AM - 9:00 PM (Open all day)",
    about="""
    It all began in 1986, nestled in the heart of Thamel,
    when Pumpernickel Bakery first opened its doors.
    What started as a small, family-owned bakery has grown
    into a beloved institution, cherished by locals and
    travelers alike. For nearly four decades, we've poured our
    heart into every loaf of bread, every slice of cake, and
    every cup of coffee, staying true to the simple joy
    of baking from scratch.""",
)

# Product catalog
PRODUCT_CATALOG = [
    Product(
        name="Triple Chocolate Cake",
        category=ProductCategory.CHOCOLATE_CAKE,
        sizes={"8inch": 1950, "5inch": 1450},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Indulge in the ultimate treat with our premium chocolate cake, crafted for true chocolate lovers. Made with the finest, ethically sourced cocoa, this cake offers a rich, velvety texture that melts in your mouth. The layers are infused with smooth, dark chocolate ganache, providing a perfect balance of sweetness and depth.",
        tags=["top_pick", "popular", "chocolate"],
        allergens=["wheat", "milk", "eggs"],
    ),
    Product(
        name="Blueberry Cheesecake",
        category=ProductCategory.CHEESECAKE,
        sizes={"8inch": 3250, "5inch": 2250},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Blueberry cheesecake is a delightful dessert that combines the rich, creamy texture of classic cheesecake with the sweet, tangy flavor of fresh blueberries. The base is typically made from a buttery graham cracker crust, which adds a satisfying crunch and complements the smoothness of the filling.",
        tags=["fruity", "creamy"],
        allergens=["wheat", "milk", "eggs"],
    ),
    Product(
        name="Strawberry Cheesecake",
        category=ProductCategory.CHEESECAKE,
        sizes={"8inch": 3250, "5inch": 2250},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Our strawberry cheesecake is a delightful blend of creamy, smooth texture and vibrant, fruity flavor. Made with a rich and silky cream cheese filling, this dessert sits on a buttery graham cracker crust that adds the perfect crunch to every bite.",
        tags=["fruity", "creamy", "fresh"],
        allergens=["wheat", "milk", "eggs"],
    ),
    Product(
        name="Brownie Cake",
        category=ProductCategory.CHOCOLATE_CAKE,
        sizes={"8inch": 1850, "5inch": 1350},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Fudgy dark chocolate brownie with a hint of crunch from walnuts.",
        tags=["fudgy", "nuts", "chocolate"],
        allergens=["wheat", "milk", "eggs", "walnuts"],
    ),
    Product(
        name="Scarlet Cheesecake",
        category=ProductCategory.SPECIALTY_CAKE,
        sizes={"8inch": 3790, "5inch": 2790},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Our Scarlet Cheesecake is a decadent creation featuring a red velvet biscuit mold base and a luscious cream cheese whipped cream exterior. This rich fusion of textures and flavors combines the classic allure of red velvet with the creamy indulgence of cheesecake.",
        tags=["specialty", "red_velvet", "premium"],
        allergens=["wheat", "milk", "eggs"],
    ),
    Product(
        name="Raffaello Cake",
        category=ProductCategory.SPECIALTY_CAKE,
        sizes={"8inch": 2100, "5inch": 1550},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="The Raffaello Cake is a luscious, creamy dessert inspired by the popular Raffaello coconut-almond confectionery. This elegant cake features layers of soft, moist sponge infused with a delicate coconut flavor, complemented by a velvety white chocolate and almond cream.",
        tags=["coconut", "almond", "elegant"],
        allergens=["wheat", "milk", "eggs", "almonds"],
    ),
    Product(
        name="Snickers Delight",
        category=ProductCategory.SPECIALTY_CAKE,
        sizes={"8inch": 1950, "5inch": 1450},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="The Snicker Cake is a decadent dessert inspired by the beloved Snickers candy bar. It features layers of rich chocolate cake, creamy caramel, crunchy peanuts, and a smooth peanut butter frosting, all topped with a luscious chocolate ganache.",
        tags=["caramel", "peanuts", "chocolate"],
        allergens=["wheat", "milk", "eggs", "peanuts"],
    ),
    Product(
        name="Pistachio Cake",
        category=ProductCategory.SPECIALTY_CAKE,
        sizes={"8inch": 3790, "5inch": 2790},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Our Nutty Pistachio Cake features a soft pistachio sponge with crushed pistachios inside, layered with smooth vanilla cream and pistachio mousse, topped with a sprinkle of pistachio crumbs for the perfect finish.",
        tags=["specialty", "nuts", "premium"],
        allergens=["wheat", "milk", "eggs", "pistachios"],
    ),
    Product(
        name="Tiramisu",
        category=ProductCategory.SPECIALTY_CAKE,
        sizes={"8inch": 1950, "5inch": 1450},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="Our tiramisu cake is a luscious, multi-layered dessert that offers a perfect balance of rich flavors and creamy textures. It features soft, coffee-soaked layers of delicate sponge cake, topped with a smooth, airy mascarpone cream.",
        tags=["coffee", "italian", "creamy"],
        allergens=["wheat", "milk", "eggs"],
    ),
    Product(
        name="Mango Mousse",
        category=ProductCategory.SEASONAL,
        sizes={"8inch": 3250, "5inch": 2250},
        weights={"8inch": "1 Pound", "5inch": "0.5 Pound"},
        description="The Mango Mousse cake is light, luscious, and topped with fresh mangoes. We're here to cool down your summer cravings, one slice at a time.",
        tags=["seasonal", "tropical", "light"],
        allergens=["milk", "eggs"],
    ),
]

# ===============================
# Utility Functions
# ===============================


def get_product_by_name(name: str) -> Optional[Product]:
    """Find a product by name (case-insensitive)"""
    for product in PRODUCT_CATALOG:
        if product.name.lower() == name.lower():
            return product
    return None


def format_price(price: int) -> str:
    """Format price in Nepalese Rupees"""
    return f"Rs. {price:,}"


def is_business_open() -> bool:
    """Check if business is currently open"""
    now = datetime.now().time()
    open_time = time(6, 30)  # 6:30 AM
    close_time = time(21, 0)  # 9:00 PM
    return open_time <= now <= close_time


@mcp.tool()
def pounds_to_kilograms(pounds: float) -> float:
    """
    Convert pounds to kilograms.
    """
    kilograms = pounds * 0.45359237
    return kilograms


@mcp.tool()
def kilograms_to_pounds(kilograms: float) -> float:
    """
    Convert kilograms to pounds.
    """
    return kilograms / 0.45359237


# ===============================
# MCP Tools - Product Management
# ===============================


@mcp.tool()
def get_full_menu() -> Dict[str, Any]:
    """
    Get the complete menu with all available products, organized by category.
    Returns detailed information about each product including prices, descriptions, and allergen information.
    """
    try:
        products = [product.to_dict() for product in PRODUCT_CATALOG]
        return {
            "products": products,
            "total_products": len(products),
        }
    except Exception as e:
        logger.error(f"Error getting menu: {e}")
        return {"error": "Failed to retrieve menu"}


@mcp.tool()
def search_products(
    query: str = "",
    category: str = "",
    max_price: int = 0,
    min_price: int = 0,
    use_semantic: bool = True,
) -> Dict[str, Any]:
    """
    Search products by name, category, or price range. Supports semantic similarity search if enabled.

    Args:
        query: Search term to match against product names and descriptions
        category: Filter by category (chocolate_cake, cheesecake, specialty_cake, seasonal)
        max_price: Maximum price filter (0 = no limit)
        min_price: Minimum price filter (0 = no limit)
        use_semantic: If True, use semantic similarity for query (default: True)
    """
    try:
        results = []
        product_texts = [f"{p.name}. {p.description}" for p in PRODUCT_CATALOG]
        matched_products = []

        if query and use_semantic:
            try:
                # --- Semantic search using sentence-transformers ---
                # pip install sentence-transformers
                from sentence_transformers import SentenceTransformer, util
                import numpy as np

                # You may want to cache/load the model globally in production
                model = SentenceTransformer("all-MiniLM-L6-v2")
                query_emb = model.encode(query, convert_to_tensor=True)
                product_embs = model.encode(product_texts, convert_to_tensor=True)
                cosine_scores = (
                    util.pytorch_cos_sim(query_emb, product_embs)[0].cpu().numpy()
                )
                # Rank products by similarity
                ranked = np.argsort(-cosine_scores)
                for idx in ranked:
                    product = PRODUCT_CATALOG[idx]
                    score = float(cosine_scores[idx])
                    # Filter by category and price
                    if category and product.category.value != category:
                        continue
                    price_8inch = product.sizes.get("8inch", 0)
                    if max_price > 0 and price_8inch > max_price:
                        continue
                    if min_price > 0 and price_8inch < min_price:
                        continue
                    matched_products.append((product, score))
                # Only include products with a reasonable similarity threshold
                results = [
                    p.to_dict() | {"similarity": s}
                    for p, s in matched_products
                    if s > 0.3
                ][:10]
            except ImportError:
                # Fallback to keyword search if sentence-transformers not installed
                use_semantic = False

        if not use_semantic or not query:
            for product in PRODUCT_CATALOG:
                # Check if product matches search criteria
                if (
                    query
                    and query.lower() not in product.name.lower()
                    and query.lower() not in product.description.lower()
                ):
                    continue
                if category and product.category.value != category:
                    continue
                price_8inch = product.sizes.get("8inch", 0)
                if max_price > 0 and price_8inch > max_price:
                    continue
                if min_price > 0 and price_8inch < min_price:
                    continue
                results.append(product.to_dict())

        return {
            "results": results,
            "total_found": len(results),
            "search_criteria": {
                "query": query,
                "category": category,
                "price_range": f"{min_price}-{max_price}"
                if min_price or max_price
                else "any",
                "semantic": use_semantic,
            },
        }
    except Exception as e:
        logger.error(f"Error searching products: {e}")
        return {"error": "Failed to search products"}


@mcp.tool()
def get_product_details(product_name: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific product.

    Args:
        product_name: Name of the product to get details for
    """
    try:
        product = get_product_by_name(product_name)
        if not product:
            return {"error": f"Product '{product_name}' not found"}

        return {
            "product": product.to_dict(),
            "pricing": {
                "8inch": format_price(product.sizes["8inch"]),
                "5inch": format_price(product.sizes["5inch"]),
            },
            "availability": "Available"
            if product.available
            else "Currently unavailable",
        }
    except Exception as e:
        logger.error(f"Error getting product details: {e}")
        return {"error": "Failed to retrieve product details"}


@mcp.tool()
def get_recommendations(
    preferences: str = "", budget: int = 0, occasion: str = ""
) -> Dict[str, Any]:
    """
    Get personalized product recommendations based on preferences and budget.

    Args:
        preferences: Customer preferences (e.g., "chocolate", "fruity", "coffee")
        budget: Budget in NPR (0 = no budget limit)
        occasion: Special occasion (e.g., "birthday", "anniversary", "casual")
    """
    try:
        recommendations = []

        for product in PRODUCT_CATALOG:
            score = 0

            # Score based on preferences
            if preferences:
                pref_lower = preferences.lower()
                if any(tag in pref_lower for tag in product.tags):
                    score += 3
                if (
                    pref_lower in product.name.lower()
                    or pref_lower in product.description.lower()
                ):
                    score += 2

            # Score based on occasion
            if occasion:
                occ_lower = occasion.lower()
                if (
                    occ_lower in ["birthday", "celebration"]
                    and "premium" in product.tags
                ):
                    score += 2
                if occ_lower == "casual" and product.sizes["5inch"] < 2000:
                    score += 1

            # Score popular items
            if "top_pick" in product.tags or "popular" in product.tags:
                score += 1

            # Filter by budget
            if budget > 0:
                if product.sizes["5inch"] <= budget:
                    score += 1
                elif product.sizes["8inch"] > budget:
                    continue  # Skip if over budget

            if score > 0:
                recommendations.append(
                    {
                        "product": product.to_dict(),
                        "score": score,
                        "reason": f"Matches your preferences and budget",
                    }
                )

        # Sort by score
        recommendations.sort(key=lambda x: x["score"], reverse=True)

        return {
            "recommendations": recommendations[:5],  # Top 5
            "criteria": {
                "preferences": preferences,
                "budget": budget,
                "occasion": occasion,
            },
        }
    except Exception as e:
        logger.error(f"Error getting recommendations: {e}")
        return {"error": "Failed to get recommendations"}


# ===============================
# MCP Tools - Business Information
# ===============================


@mcp.tool()
def get_business_info() -> Dict[str, Any]:
    """Get complete business information including hours, location, and contact details."""
    try:
        return {
            "name": BUSINESS_INFO.name,
            "established": BUSINESS_INFO.established,
            "tagline": BUSINESS_INFO.tagline,
            "location": BUSINESS_INFO.location,
            "address": BUSINESS_INFO.address,
            "contact": {
                "phone": BUSINESS_INFO.phone,
                "whatsapp": BUSINESS_INFO.whatsapp,
                "email": BUSINESS_INFO.email,
            },
            "hours": BUSINESS_INFO.hours,
            "maps_link": BUSINESS_INFO.maps_link,
            "currently_open": is_business_open(),
            "about": BUSINESS_INFO.about,
        }
    except Exception as e:
        logger.error(f"Error getting business info: {e}")
        return {"error": "Failed to retrieve business information"}


@mcp.tool()
def get_contact_options() -> Dict[str, Any]:
    """Get all available contact methods for the bakery."""
    try:
        return {
            "phone": {
                "number": BUSINESS_INFO.phone,
                "description": "Call for orders and inquiries",
            },
            "whatsapp": {
                "link": BUSINESS_INFO.whatsapp,
                "description": "Chat with us on WhatsApp for quick orders",
            },
            "email": {
                "address": BUSINESS_INFO.email,
                "description": "Email us for general inquiries",
            },
            "visit": {
                "address": BUSINESS_INFO.address,
                "maps_link": BUSINESS_INFO.maps_link,
                "hours": BUSINESS_INFO.hours,
            },
        }
    except Exception as e:
        logger.error(f"Error getting contact options: {e}")
        return {"error": "Failed to retrieve contact information"}


# ===============================
# MCP Tools - Order Management
# ===============================


@mcp.resource()
def order_information_requirements() -> Dict[str, Any]:
    """
    Resource describing the information required from a customer to place an order.
    """
    return {
        "fields": [
            {"name": "name", "required": True, "description": "Customer's full name."},
            {
                "name": "address",
                "required": "Required for delivery",
                "description": "Delivery address. Not needed for pickup.",
            },
            {
                "name": "item_ordered",
                "required": True,
                "description": "Item(s) ordered. Try to extract from message and/or image.",
            },
            {
                "name": "contact_number",
                "required": True,
                "description": "Customer's primary contact number.",
            },
            {
                "name": "alternative_number",
                "required": False,
                "description": "Alternative contact number (optional).",
            },
            {
                "name": "delivery_or_pickup",
                "required": True,
                "description": "Specify 'delivery' or 'pickup'.",
            },
            {
                "name": "date",
                "required": True,
                "description": "Preferred date for delivery or pickup.",
            },
            {
                "name": "time",
                "required": True,
                "description": "Preferred time for delivery or pickup.",
            },
            {
                "name": "payment_method",
                "required": True,
                "description": "Payment method: Fonepay QR, Stripe, Khalti (directs to website).",
            },
            {
                "name": "message_on_cake",
                "required": False,
                "description": "Optional message to be written on the cake.",
            },
        ],
        "notes": [
            "Address is only required for delivery orders.",
            "Try to extract item ordered from customer message or image if possible.",
            "Offer both delivery and pickup options, with calendar date & time.",
            "Ask for contact number if not available.",
            "Alternative number and cake message are optional fields.",
            "Payment methods supported: Fonepay QR, Stripe, Khalti (directs to payment website).",
        ],
    }


@mcp.tool()
def receive_order_details(
    name: str = "",
    address: str = "",
    item_ordered: str = "",
    contact_number: str = "",
    alternative_number: str = "",
    delivery_or_pickup: str = "",
    date: str = "",
    time: str = "",
    payment_method: str = "",
    message_on_cake: str = "",
) -> Dict[str, Any]:
    """
    Receive and validate order details from the customer.

    Args:
        name: Customer's name (required)
        address: Delivery address (required for delivery)
        item_ordered: Item(s) ordered (try to extract from message/image)
        contact_number: Customer's contact number (required)
        alternative_number: Optional alternative contact number
        delivery_or_pickup: 'delivery' or 'pickup' (required)
        date: Preferred date for delivery/pickup (required)
        time: Preferred time for delivery/pickup (required)
        payment_method: Payment method (Fonepay QR, Stripe, Khalti, Card)
        message_on_cake: Optional message to be written on the cake
    """
    try:
        errors = []
        if not name:
            errors.append("Name is required.")
        if not item_ordered:
            errors.append("Item ordered is required.")
        if not contact_number:
            errors.append("Contact number is required.")
        if not delivery_or_pickup:
            errors.append("Please specify delivery or pickup.")
        if not date:
            errors.append("Date is required.")
        if not time:
            errors.append("Time is required.")
        if delivery_or_pickup.lower() == "delivery" and not address:
            errors.append("Address is required for delivery.")
        if not payment_method:
            errors.append("Payment method is required.")

        if errors:
            return {"error": "Missing required fields.", "details": errors}

        order_summary = {
            "name": name,
            "address": address if delivery_or_pickup.lower() == "delivery" else "N/A",
            "item_ordered": item_ordered,
            "contact_number": contact_number,
            "alternative_number": alternative_number,
            "delivery_or_pickup": delivery_or_pickup,
            "date": date,
            "time": time,
            "payment_method": payment_method,
            "message_on_cake": message_on_cake,
        }

        # Payment method links (for reference)
        payment_links = {
            "fonepay qr": "https://fonepay.com/qr",
            "stripe": "https://stripe.com/pay",
            "khalti": "https://khalti.com/",
        }
        payment_link = payment_links.get(payment_method.lower(), "")
        if payment_link:
            order_summary["payment_link"] = payment_link

        return {
            "order_summary": order_summary,
            "status": "Order details received successfully. Please confirm to proceed.",
        }
    except Exception as e:
        logger.error(f"Error receiving order details: {e}")
        return {"error": "Failed to receive order details."}


@mcp.tool()
def calculate_order_total(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate the total cost of an order.

    Args:
        items: List of items with format [{"product_name": str, "size": str, "quantity": int}]
    """
    try:
        order_items = []
        subtotal = 0

        for item in items:
            product = get_product_by_name(item["product_name"])
            if not product:
                return {"error": f"Product '{item['product_name']}' not found"}

            size = item["size"]
            quantity = item["quantity"]

            if size not in product.sizes:
                return {"error": f"Size '{size}' not available for {product.name}"}

            item_price = product.sizes[size]
            item_total = item_price * quantity
            subtotal += item_total

            order_items.append(
                {
                    "product": product.name,
                    "size": size,
                    "quantity": quantity,
                    "unit_price": format_price(item_price),
                    "total": format_price(item_total),
                }
            )

        # Add service charge (10%)
        service_charge = int(subtotal * 0.10)
        total = subtotal + service_charge

        return {
            "items": order_items,
            "subtotal": format_price(subtotal),
            "service_charge": format_price(service_charge),
            "total": format_price(total),
            "currency": "NPR",
        }
    except Exception as e:
        logger.error(f"Error calculating order total: {e}")
        return {"error": "Failed to calculate order total"}


# ===============================
# MCP Tools - Customer Service
# ===============================


@mcp.tool()
def get_faq() -> Dict[str, Any]:
    """Get frequently asked questions and answers."""
    try:
        return {
            "faqs": [
                {
                    "question": "What are your operating hours?",
                    "answer": "We're open every day from 6:30 AM to 9:00 PM.",
                },
                {
                    "question": "Do you take custom orders?",
                    "answer": "Yes! Please contact us at least 24 hours in advance for custom orders.",
                },
                {
                    "question": "Do you deliver?",
                    "answer": "Currently, we offer pickup only from our Thamel location. You can order via WhatsApp for easy pickup scheduling.",
                },
                {
                    "question": "What payment methods do you accept?",
                    "answer": "We accept cash on delivery, eSewa, Khalti, Stripe and major credit/debit cards.",
                },
                {
                    "question": "Can I see allergen information?",
                    "answer": "Yes! All our products include detailed allergen information. Common allergens include wheat, milk, eggs, and nuts.",
                },
                {
                    "question": "How far in advance should I order?",
                    "answer": "For regular items, we offer same-day orders/delivery. For custom cakes or large orders, please give us 24-48 hours notice.",
                },
                {
                    "question": "Do you offer sugar-free or vegan options?",
                    "answer": "We currently focus on our classic recipes. Please tell us about your special dietary requirements.",
                },
                {
                    "question": "Can I modify cake designs?",
                    "answer": "Yes! We can customize decorations and messages on our cakes. Please tell us your requirements.",
                },
            ],
            "contact_for_more": {
                "phone": BUSINESS_INFO.phone,
                "whatsapp": BUSINESS_INFO.whatsapp,
                "email": BUSINESS_INFO.email,
            },
        }
    except Exception as e:
        logger.error(f"Error getting FAQ: {e}")
        return {"error": "Failed to retrieve FAQ"}


@mcp.tool()
def check_allergen_info(product_name: str, allergen: str = "") -> Dict[str, Any]:
    """
    Check allergen information for a specific product or all products.

    Args:
        product_name: Name of the product to check allergens for
        allergen: Specific allergen to check for (optional)
    """
    try:
        if product_name:
            product = get_product_by_name(product_name)
            if not product:
                return {"error": f"Product '{product_name}' not found"}

            result = {
                "product": product.name,
                "allergens": product.allergens,
                "allergen_free": len(product.allergens) == 0,
            }

            if allergen:
                allergen_present = allergen.lower() in [
                    a.lower() for a in product.allergens
                ]
                result["specific_allergen"] = {
                    "allergen": allergen,
                    "present": allergen_present,
                    "message": f"{'Contains' if allergen_present else 'Does not contain'} {allergen}",
                }

            return result
        else:
            # Return allergen summary for all products
            all_allergens = set()
            product_allergens = {}

            for product in PRODUCT_CATALOG:
                all_allergens.update(product.allergens)
                product_allergens[product.name] = product.allergens

            return {
                "all_allergens": sorted(list(all_allergens)),
                "product_allergens": product_allergens,
                "allergen_free_products": [
                    p.name for p in PRODUCT_CATALOG if len(p.allergens) == 0
                ],
            }
    except Exception as e:
        logger.error(f"Error checking allergen info: {e}")
        return {"error": "Failed to retrieve allergen information"}


@mcp.tool()
def generate_pickup_reminder(
    order_items: List[Dict[str, Any]], pickup_time: str = ""
) -> Dict[str, Any]:
    """
    Generate a pickup reminder message for customers.

    Args:
        order_items: List of ordered items
        pickup_time: Preferred pickup time
    """
    try:
        order_calc = calculate_order_total(order_items)
        if "error" in order_calc:
            return order_calc

        if not pickup_time:
            pickup_time = "during business hours (6:30 AM - 9:00 PM)"

        reminder = f"🔔 *Pickup Reminder - Pumpernickel Bakery*\n\n"
        reminder += f"Your order is ready for pickup!\n\n"
        reminder += "*Order Summary:*\n"

        for item in order_calc["items"]:
            reminder += f"• {item['product']} ({item['size']}) x{item['quantity']}\n"

        reminder += f"\n💰 Total: {order_calc['total']}\n\n"
        reminder += f"📍 Pickup Location: {BUSINESS_INFO.address}\n"
        reminder += f"🕒 Pickup Time: {pickup_time}\n"
        reminder += f"📞 Contact: {BUSINESS_INFO.phone}\n\n"
        reminder += "Thank you for choosing Pumpernickel Bakery! 🥧"

        return {
            "reminder_message": reminder,
            "pickup_location": BUSINESS_INFO.address,
            "contact_info": {
                "phone": BUSINESS_INFO.phone,
                "whatsapp": BUSINESS_INFO.whatsapp,
            },
            "maps_link": BUSINESS_INFO.maps_link,
        }
    except Exception as e:
        logger.error(f"Error generating pickup reminder: {e}")
        return {"error": "Failed to generate pickup reminder"}


@mcp.tool()
def schedule_delivery_with_calendar(
    name: str,
    address: str,
    contact_number: str,
    date: str,
    time: str,
    item_ordered: str,
    delivery_notes: str = "",
) -> Dict[str, Any]:
    """
    Schedule a delivery for an order using Google Calendar integration.

    Args:
        name: Customer's name
        address: Delivery address
        contact_number: Customer's contact number
        date: Delivery date (YYYY-MM-DD)
        time: Delivery time (HH:MM, 24-hour format)
        item_ordered: Item(s) ordered
        delivery_notes: Optional notes for delivery
    Returns:
        Confirmation and calendar event link (if successful)
    """
    try:
        # Combine date and time for event start
        from datetime import datetime, timedelta

        event_start = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        event_end = event_start + timedelta(hours=1)

        event = {
            "summary": f"Delivery for {name}",
            "location": address,
            "description": f"Order: {item_ordered}\nContact: {contact_number}\nNotes: {delivery_notes}",
            "start": {
                "dateTime": event_start.isoformat(),
                "timeZone": "Asia/Kathmandu",
            },
            "end": {"dateTime": event_end.isoformat(), "timeZone": "Asia/Kathmandu"},
        }

        # --- Google Calendar API integration placeholder ---
        # Here you would use the Google Calendar API to insert the event.
        # For example, using google-api-python-client:
        # service.events().insert(calendarId='primary', body=event).execute()
        # For now, we'll return a mock event link.
        event_link = f"https://calendar.google.com/calendar/r/eventedit?text=Delivery+for+{name.replace(' ', '+')}&dates={event_start.strftime('%Y%m%dT%H%M%S')}/{event_end.strftime('%Y%m%dT%H%M%S')}&details=Order:+{item_ordered.replace(' ', '+')}+Contact:+{contact_number}+Notes:+{delivery_notes.replace(' ', '+')}&location={address.replace(' ', '+')}"

        return {
            "status": "Delivery scheduled (mock)",
            "event_link": event_link,
            "event_details": event,
            "note": "Replace mock integration with Google Calendar API for production use.",
        }
    except Exception as e:
        logger.error(f"Error scheduling delivery: {e}")
        return {"error": "Failed to schedule delivery."}


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
