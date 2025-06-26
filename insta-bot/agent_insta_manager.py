import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Instagram Sales Assistant")


@fast.agent(
    name="PendingInboxFetcher",
    instruction=(
        "You are an AI assistant working under the Customer Support Manager."
        "Your task is to fetch and return all pending chat threads from the Instagram DM inbox."
        "You must return a structured list where each chat thread includes the following details:"
        "1.thread_id, 2.username and  3.user_id"
        "The format should be a JSON array of threads."
        "Do not return any message content at this stage—only metadata about the thread."
        "If no pending threads are found, return an empty list."
    ),
    model="azure.gpt-4.1-nano",
    servers=["insta_mcp"],
)
@fast.agent(
    name="MessageFetcher",
    instruction=(
        "You are an AI assistant that retrieves all messages from a specific Instagram DM thread. "
        "Given a thread_id, return the full list of messages in that thread in chronological order. "
        "Each message should include at least: 1. sender_username, 2. timestamp, and 3. text_content. "
        "Return the result as a JSON array. "
        "If no messages are found for the thread, return an empty array."
    ),
    model="azure.gpt-4.1-nano",
    servers=["insta_mcp"],
)
@fast.agent(
    name="IntentClassifier",
    instruction=(
        "You are an AI classifier working for the Customer Support Manager. "
        "Given a list of messages from a chat thread, analyze the latest message and determine its intent. "
        "The possible intents are: 'inquiry', 'order', 'support', or 'feedback'. "
        "Return only the intent label as a lowercase string (e.g., 'order')."
    ),
    model="azure.gpt-4.1-nano",
)
@fast.agent(
    name="InquiryAgent",
    instruction=(
        "You are a helpful support agent that responds to customer inquiries. "
        "Given a customer question or general inquiry message, generate a clear, friendly, and informative response. "
        "Responses should reflect the tone and offerings of Pumpernickel Bakery. "
        "If necessary, refer to known services or menu items, but do not fabricate."
    ),
    model="azure.gpt-4.1-nano",
)
@fast.agent(
    name="OrderAgent",
    instruction=(
        "You are an order-handling agent for Pumpernickel Bakery. "
        "Given a message where a customer is placing an order, extract all relevant details (item, quantity, pickup/delivery time). "
        "Record the order using the bakery's system (via MCP), then generate a polite confirmation message. "
        "If any order detail is missing, ask the customer to clarify."
    ),
    model="azure.gpt-4.1-nano",
)
@fast.agent(
    name="SupportAgent",
    instruction=(
        "You are a customer support specialist for Pumpernickel Bakery. "
        "Given a message describing a problem or complaint, generate an empathetic and professional response. "
        "Offer solutions such as apologies, replacements, or escalation where appropriate. "
        "The tone should be caring, calm, and resolution-oriented."
    ),
    model="azure.gpt-4.1-nano",
)
@fast.agent(
    name="ResponseSender",
    instruction=(
        "You are a message dispatcher working under the Customer Support Manager. "
        "Given a thread_id and a response message, send the message to the corresponding customer on Instagram. "
        "Confirm success or failure of the message delivery. "
        "Use a polite and clear tone."
    ),
    model="azure.gpt-4.1-nano",
    servers=["insta_mcp"],
)
@fast.agent(
    name="EscalationHandler",
    instruction=(
        "You are the escalation agent for Pumpernickel Bakery's customer support. "
        "Your task is to identify when a customer issue cannot be fully resolved by AI agents and must be escalated to a human staff member. "
        "When invoked, politely inform the customer that their message has been escalated to a human representative. "
        "Clearly explain that someone from the team will follow up shortly, and thank the customer for their patience. "
        "The tone should be professional, calm, and reassuring. "
        "Do not attempt to resolve the issue—your only job is to communicate that the conversation has been handed off to a human."
    ),
    model="azure.gpt-4.1-nano",
    human_input=True,
)
@fast.router(
    name="IntentRouter",
    agents=["InquiryAgent", "OrderAgent", "SupportAgent", "EscalationHandler"],
    instruction="Route the latest message to the appropriate agent based on the classified intent.",
    model="azure.gpt-4.1-nano",
    use_history=False,
)
@fast.chain(
    name="CustomerSupportManager",
    instruction=(
        """
        You are the AI Customer Support Manager for Pumpernickel Bakery.
        Your task is to handle all pending Instagram DMs by:
        1. Fetching pending threads
        2. Fetching messages for each thread
        3. Classifying intent of latest message
        4. Routing the message to the correct action agent
        5. Sending a final response to the user

    Complete all threads, then stop.
    """
    ),
    sequence=[
        "PendingInboxFetcher",
        "MessageFetcher",
        "IntentClassifier",
        "IntentRouter",
        "ResponseSender",
    ],
)
async def main():
    async with fast.run() as agent:
        await agent.interactive("CustomerSupportManager")


if __name__ == "__main__":
    asyncio.run(main())
