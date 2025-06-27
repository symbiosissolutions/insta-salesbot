from google import genai
import os
import json
import logging
from typing import Dict, Any, List, Optional
from tools.knowledge import (
    PRODUCT_CATALOG, 
    BUSINESS_INFO, 
    get_faq, 
    order_information_requirements,
)

# Configure logging
logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

class ProductManager:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self._prepare_knowledge_base()
    
    def _prepare_knowledge_base(self):
        """Prepare comprehensive knowledge base for Gemini"""
        self.knowledge_base = {
            "business_info": {
                "name": BUSINESS_INFO.name,
                "established": BUSINESS_INFO.established,
                "tagline": BUSINESS_INFO.tagline,
                "location": BUSINESS_INFO.location,
                "address": BUSINESS_INFO.address,
                "phone": BUSINESS_INFO.phone,
                "whatsapp": BUSINESS_INFO.whatsapp,
                "email": BUSINESS_INFO.email,
                "maps_link": BUSINESS_INFO.maps_link,
                "hours": BUSINESS_INFO.hours,
                "about": BUSINESS_INFO.about
            },
            "products": [product.to_dict() for product in PRODUCT_CATALOG],
            "faq": get_faq(),
            "order_requirements": order_information_requirements(),
            "size_guidelines": {
                "5inch": "Serves 4-6 people, perfect for small gatherings",
                "8inch": "Serves 8-12 people, ideal for medium gatherings",
                "serving_estimates": {
                    "small_gathering": "4-6 people: 5inch cake",
                    "medium_gathering": "8-12 people: 8inch cake", 
                    "large_gathering": "12+ people: Multiple 8inch cakes or custom orders"
                }
            },
            "pricing_info": {
                "currency": "NPR (Nepalese Rupees)",
                "price_ranges": {
                    "budget_friendly": "1350-1850 NPR (5inch)",
                    "mid_range": "1950-3250 NPR (8inch)",
                    "premium": "3250-3790 NPR (specialty cakes)"
                }
            }
        }

    def get_product_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get product details by name"""
        for product in PRODUCT_CATALOG:
            if product.name.lower() == name.lower():
                return product.to_dict()
        return None

    def _create_product_prompt(self, user_query: str) -> str:
        """Create prompt for product and allergy related queries"""
        base_prompt = f"""
        You will be responsible to handling cake related enquires.  
        You will not be comminicating with humans but with other agents.
        The agent will ask you question about what all products do we have, detail about specific product, price, size, allergens, etc.

       !!! IMPORTATANT NOTE: If there is a product not mentioned in the product catalog but you it is generally easy to make with ingredients we have, you can mention it.
       In this case tell the agent that we can make it for you. We do make custom cakes. Also recommend similar cakes we have if they want readymade.

        Respond to the query with the product details:

AVAILABLE PRODUCTS:
"""
        
        # Add product information
        for product in PRODUCT_CATALOG:
            base_prompt += f"""
- {product.name} ({product.category.value})
  Sizes & Prices: {product.sizes}
  Weights: {product.weights}
  Description: {product.description}
  Tags: {', '.join(product.tags)}
  Allergens: {', '.join(product.allergens) if product.allergens else 'None'}
  FAQ: {get_faq()}
"""
        
        base_prompt += f"""

SIZE GUIDELINES:
- 5inch cakes: Serve 4-6 people, perfect for small gatherings
- 8inch cakes: Serve 8-12 people, ideal for medium gatherings
- For larger groups: Consider multiple cakes or custom orders

PRICING:
- Budget-friendly: 1350-1850 NPR (5inch cakes)
- Mid-range: 1950-3250 NPR (8inch cakes)  
- Premium: 3250-3790 NPR (specialty cakes)

USER QUERY: {user_query}


"""
        return base_prompt

    def _create_company_prompt(self, user_query: str) -> str:
        """Create prompt for company and business related queries"""
        base_prompt = f"""
You are an expert bakery business manager for {BUSINESS_INFO.name}, a beloved bakery established in {BUSINESS_INFO.established} in {BUSINESS_INFO.location}.

BUSINESS INFORMATION:
Name: {BUSINESS_INFO.name}
Established: {BUSINESS_INFO.established}
Tagline: {BUSINESS_INFO.tagline}
Location: {BUSINESS_INFO.location}
Address: {BUSINESS_INFO.address}
Phone: {BUSINESS_INFO.phone}
WhatsApp: {BUSINESS_INFO.whatsapp}
Email: {BUSINESS_INFO.email}
Maps Link: {BUSINESS_INFO.maps_link}
Operating Hours: {BUSINESS_INFO.hours}
###Delivery Options: pickup, delivery

ABOUT US:
{BUSINESS_INFO.about}

FAQ INFORMATION:
"""
        
        # Add FAQ information
        faq_data = get_faq()
        if "faqs" in faq_data:
            for faq in faq_data["faqs"]:
                base_prompt += f"""
Q: {faq['question']}
A: {faq['answer']}
"""
        
        base_prompt += f"""

ORDER REQUIREMENTS:
"""
        
        # Add order requirements
        order_req = order_information_requirements()
        if "fields" in order_req:
            for field in order_req["fields"]:
                base_prompt += f"""
- {field['name']}: {field['description']} (Required: {field['required']})
"""
        
        base_prompt += f"""

USER QUERY: {user_query}

Please provide a helpful, informative response about business operations, ordering process, company information, or any business-related questions. Be conversational, professional, and always include relevant contact information when applicable.
"""
        return base_prompt

    def handle_product_inquiry(self, query: str) -> str:
        """
        You will be responsible to handling cake related enquires.
        You will not be comminicating with humans but with other agents.
        The agent will ask you question about what all products do we have, detail about specific product, price, size, etc.

        Respond to the query with the product details:
        """
        try:
            prompt = self._create_product_prompt(query)
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            
            return response.candidates[0].content.parts[0].text
        except Exception as e:
            logger.error(f"Error handling product inquiry: {e}")
            return "I apologize, but I'm having trouble processing your product inquiry right now. Please contact us directly at our phone number or WhatsApp for immediate assistance."

    def handle_company_inquiry(self, query: str) -> str:
        """
        Handle company and business-related queries including:
        - Business information and history
        - Operating hours and location
        - Contact information
        - FAQ responses
        - Ordering process and requirements
        - Delivery and pickup options
        - Payment methods
        - Custom order information
        """
        try:
            prompt = self._create_company_prompt(query)
            
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
            )
            
            return response.candidates[0].content.parts[0].text
        except Exception as e:
            logger.error(f"Error handling company inquiry: {e}")
            return "I apologize, but I'm having trouble processing your business inquiry right now. Please contact us directly at our phone number or WhatsApp for immediate assistance."