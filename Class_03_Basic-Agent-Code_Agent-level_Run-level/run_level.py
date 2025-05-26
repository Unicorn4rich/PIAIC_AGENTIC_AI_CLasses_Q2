# This is => 2. RUN LEVEL

import os
from agents.run import RunConfig
from dotenv import load_dotenv 
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled  

#----------------------------------------------------------------------------

load_dotenv() # env file ke andar rakhi keys is se mangwaty hain.

set_tracing_disabled(disabled=True) # for this extra chat => OPENAI_API_KEY is not set, skipping trace export

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY: # agr API key na mily to ye error aye.
    raise ValueError("OPENROUTER_API_KEY is not set")

#----------------------------------------------------------------------------

agent = Agent(
    name="kuch_bhi_agent",
    instructions="your are a helpful assistent",
)

#----------------------------------------------------------------------------

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,              # OpenRouter API key => this is ticket
    base_url="https://openrouter.ai/api/v1", # Openrouter base URL => this is gate           
)

# configration setting
config = RunConfig( 
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client),
    model_provider=client,
    tracing_disabled=True
)

jawab = Runner.run_sync(agent, "What is your name?", run_config=config)
   
print(jawab.final_output)    
    
    


# Runner.run_sync => use when we create single agent 
# Runner.run => use when we create multiple agents    