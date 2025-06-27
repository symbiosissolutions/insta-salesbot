import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Instagram Sales Assistant")


@fast.agent(
    name="insta_dm_manager",
    instruction=(
        """
        You are an Instagram DM Manager at Pumpernickel Bakery.
        You handle and relay all direct messages from Instagram users to the Agent Bakery Assistant for coming up with response.
        You only act on Instagram DMs and forward messages/responses.
        Get chats that are unread.
        read messages of one of the chat. get the full message history (chronological order)
        Package and forward this full message list to the Bakery Manager Assistant Agent
        Wait for the Bakery Manager Assistant Agent to return a reply.
        After the Bakery Manager Assistant returns the reply, send the reply message and the username to the message sender agent.
        """
    ),
    model="azure.gpt-4.1-nano",
    servers=["agent_bakery_assistant", "insta_mcp"],
)
@fast.agent(
    name="message_sender",
    instruction="""
            Your only task is to send a message to the given username.
            From the information you receive, extract the username (recipient) and
            the message (text to send).
            Send the exact message to the specified username without modifying it.
            Use the send_message tool from insta_mcp to send the message to the user.
            """,
    model="azure.gpt-4.1-nano",
    servers=["insta_mcp"],
)
@fast.chain(name="insta_message_chain", sequence=["insta_dm_manager", "message_sender"])
async def main():
    async with fast.run() as agent:
        await agent.interactive("insta_message_chain")


if __name__ == "__main__":
    asyncio.run(main())
