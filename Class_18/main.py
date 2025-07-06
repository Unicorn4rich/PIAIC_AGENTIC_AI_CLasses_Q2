import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, RunContextWrapper
import rich

#-------------------------------
load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#---------------------------------

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
#-------------------------------
agent = Agent( 
    name="myagent",
    instructions="you are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite", openai_client=client),
)
#-------------------------------
result = Runner.run_sync(agent, "what is the usr name and age?") 
print(result.final_output)
rich.print(result)



