# Imports--------------------------------------------------------------
import os # Import os for environment variable management
from dotenv import load_dotenv # this import for environment variables from .env file
from agents import Agent, Runner, set_tracing_disabled  
from agents.extensions.models.litellm_model import LitellmModel # LitellmModel => this is class

# Environment Variables Setupt---------------------------------------------

load_dotenv() # Load environment variables from .env file
set_tracing_disabled(disabled=True) # Disable tracing for the agent => this is for comming with response => OPENAI_API_KEY is not set, skipping trace export
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # Get the API key from environment variables.

if not GEMINI_API_KEY: # Check if the API key is set and if not, raise an exception error
    raise Exception("API key not found. Please set the GEMINI_API_KEY environment variable.")



# Agent create--------------------------------------------------------------
# we are making single agent.


agent = Agent( # Create an instance of the Agent class with a name.
              model = LitellmModel(model="gemini/gemini-2.0-flash", api_key=GEMINI_API_KEY), 
              name ="shoaib_Agent", # Name of the agent
              instructions="You are a helpful assistant" # Instructions for the agent / yani Systemt prompt
) 



# Agent ko chalaya-------------------------------- ---------------------------

# Create a runner instance to manage the agent's execution
res = Runner.run_sync(agent, "I am shoaib who are you?") # get 2 parameters => agent => ka naam or 2nd => user input.

print(res.final_output)