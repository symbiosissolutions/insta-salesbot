from enum import Enum
from dataclasses import dataclass
import logging
from typing import Dict, Any, List, Optional


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


def get_product_by_name(name: str) -> Optional[Product]:
    """Get product by name from the catalog"""
    for product in PRODUCT_CATALOG:
        if product.name.lower() == name.lower():
            return product
    return None


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
                "description": "Specify 'delivery' or 'pickup'. This is important for the order manager to know.",
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
                    "answer": "We offer both pickup and delivery. For delivery, we charge 100 NPR per delivery. For pickup, we don't charge anything.",
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
