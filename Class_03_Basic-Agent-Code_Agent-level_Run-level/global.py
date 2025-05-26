# This is => 2. RUN LEVEL

import os
from agents.run import RunConfig
from dotenv import load_dotenv 
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, set_default_openai_client, set_default_openai_api  

#----------------------------------------------------------------------------

load_dotenv() # env file ke andar rakhi keys is se mangwaty hain.

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

#----------------------------------------------------------------------------
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,              # OpenRouter API key => this is ticket
    base_url="https://openrouter.ai/api/v1", # Openrouter base URL => this is gate           
    )

set_default_openai_client(client)
    
    
agent = Agent(
    name="kuch_bhi_agent",
    instructions="your are a helpful assistent",
    model="google/gemini-2.0-flash-exp:free"   # here chnges
)

#----------------------------------------------------------------------------




jawab = Runner.run_sync(agent, "What is your name?")
print(jawab.final_output)    
    
    

# Runner.run_sync => use when we create single agent 
# Runner.run => use when we create multiple agents    