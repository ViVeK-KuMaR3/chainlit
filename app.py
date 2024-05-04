import chainlit as cl
from src.llm import ask_bot


@cl.on_message
async def main(user_message: cl.Message):
    
    # Your custom logic goes here...
    result=ask_bot(user_message.content)
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {result}",
    ).send()
