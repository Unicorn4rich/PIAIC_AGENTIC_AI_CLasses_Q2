import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, RunContextWrapper
import rich
import asyncio
from pydantic import BaseModel 


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
class User_Info(BaseModel):
    name: str
    age: int
    
#-----------------------------
user_name = input("Enter user name: ")
user_age = input("Enter user age: ")
#-----------------------------    
user_Information = User_Info(name=user_name, age=user_age) 
   
#-----------------------------
def DynamicPrompt(wrapper: RunContextWrapper[User_Info], agent):
    return f"user name is {wrapper.context.name} and age is {wrapper.context.age} "

#-----------------------------
agent = Agent( 
    name="myagent",
    instructions=DynamicPrompt,
    # prompt={"id": "pmpt_jbj423vbr2h3verhdvwhdhvdh}
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash-lite", openai_client=client),
)
#-------------------------------
result = Runner.run_sync(agent, "what is the usr name and age?", context=user_Information) 
print(result.final_output)
rich.print(result)



#-------------------------------
# Get seystem prompt

async def main():
    my_context = RunContextWrapper(context="shoaibbbbbbbbbbbbbbbbbb")
    sys = await agent.get_system_prompt(my_context)
    rich.print("😈", sys) # 😈 You are a helpful assistant.
    
    result = await Runner.run(agent, "hi", context=my_context) 
    print(result.final_output) # Hi there! How can I help you today?
    print("\n")
    rich.print("❌", result) 
    
asyncio.run(main())