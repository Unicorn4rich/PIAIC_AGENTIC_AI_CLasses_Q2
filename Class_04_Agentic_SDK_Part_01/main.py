# importing required modules
import os  # for interacting with operating system
from dotenv import load_dotenv  # for loading environment variables from .env file
# importing required Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, set_tracing_disabled classes
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, set_tracing_disabled
import chainlit as cl  # importing chainlit module for creating user interface


# loading environment variables from .env file
load_dotenv()

# setting tracing disabled
set_tracing_disabled(disabled=True)

# getting Open Router API key from environment variables
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

#-------------------------------------------------------------------------------------
# create history to store conversations

# creating a list to store history of conversations
history = []


#-------------------------------------------------------------------------------------
# create Agent

# creating an instance of AsyncOpenAI class
client = AsyncOpenAI(
    api_key=OPEN_ROUTER_API_KEY,  # passing Open Router API key
    base_url='https://openrouter.ai/api/v1'  # passing base URL
)

# creating an instance of Agent class
agent = Agent(  # this class is from openAi agent SDK
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free", openai_client=client),  # passing model and openai client
    name="my_agent",  # giving a name to agent
    instructions="You are a helpfull assistent"  # giving instructions to agent
) 


#-------------------------------------------------------------------------------------
# create chainlit ui for Agent

# creating a function to handle messages
@cl.on_message
async def main(message: cl.Message):
    # getting the content of message
    ui_question = message.content
    
    # appending user's question to history list
    history.append({"role": "user", "content": ui_question})
    
    # getting the response from agent
    jawab = await Runner.run(agent, history)
    # print(jawab.final_output)
    
    # appending agent's response to history list
    history.append({"role": "system", "content": jawab.final_output})
    
    # sending the response to user display
    await cl.Message(content=jawab.final_output,).send()  # showing the response on the screen

