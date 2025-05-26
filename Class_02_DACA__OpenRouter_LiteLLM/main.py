# Imports--------------------------------------------------------------
import os # Import os for environment variable management
from dotenv import load_dotenv # this import for environment variables from .env file
# Agent => agent ko banega or Runner => agent ko chlaega or OpenAIChatCompletionsModel => this is class 
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled # AsyncOpenAI => this is class


# Environment Variables Setupt---------------------------------------------

load_dotenv() # Load environment variables from .env file
set_tracing_disabled(disabled=True) # Disable tracing for the agent => this is for comming with response => OPENAI_API_KEY is not set, skipping trace export
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") # Get the API key from environment variables.

if not OPENROUTER_API_KEY: # Check if the API key is set and if not, raise an exception error
    raise Exception("API key not found. Please set the OPENROUTER_API_KEY environment variable.")



# Agent create--------------------------------------------------------------
# we are making single agent.

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY, # Set the API key for the OpenAI client.
    base_url="https://openrouter.ai/api/v1", # Base URL for the OpenRouter API
) 

agent = Agent( # Create an instance of the Agent class with a name.
              model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client), # requred to paramaters => model => model set kar rhy hain. + openai_client => jahn se model hamne mil rha hai uski setting.
              name="shoaib_Agent", # Name of the agent
              instructions="You are a helpful assistant" # Instructions for the agent / yani Systemt prompt
) 



# Agent ko chalaya-------------------------------- ---------------------------

# Create a runner instance to manage the agent's execution
res = Runner.run_sync(agent, "I am shoaib who are you?") # get 2 parameters => agent => ka naam or 2nd => user input.

print(res.final_output)