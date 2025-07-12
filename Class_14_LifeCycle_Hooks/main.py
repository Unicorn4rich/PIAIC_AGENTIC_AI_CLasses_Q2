from dotenv import load_dotenv # types: ignore
from agents import Agent, Runner, RunContextWrapper, function_tool, RunHooks, AgentHooks # types: ignore
load_dotenv()
from dataclasses import dataclass
import rich
from typing import Any
import asyncio

#---------------------------------------------------------

@dataclass
class User_info: 
    name: str
    age: int
    uid: int
    
#instance/object of User_info    
user_information = User_info("azlaan", 23, 117759)


#---------------------------------------------------------
# Custom Hook


class CustomRunHook(RunHooks):
    async def on_agent_start(self, ctx: RunContextWrapper[User_info], agent: Agent)-> None:
        rich.print("🤑 CustomRunHook -- on_agent_start", )
        rich.print(f"### Agent {agent.name} started. Usage: {ctx.usage}, userName: {ctx.context.name}")
        rich.print("\n\n")
        
    async def on_agent_end(self, ctx: RunContextWrapper[User_info], agent: Agent, output: Any)-> None:
        rich.print("🤑 CustomRunHook -- on_agent_end", )
        rich.print(f"### Agent {agent.name} ended. Usage: {ctx.usage}, userName: {ctx.context.name}")
        rich.print("\n\n")
        
        
start_hook = CustomRunHook()
#---------------------------------------------------------


class CustomAgentHook(AgentHooks):
    async def on_start(self, ctx: RunContextWrapper[User_info], agent: Agent) -> None:
        rich.print("🤖 CustomAgentHook -- on_start")
        rich.print(f"### Agent {agent.name} started. Usage: {ctx.usage},  userName: {ctx.context.name}")
        rich.print("\n\n")
        
    async def on_end(self, ctx: RunContextWrapper[User_info], agent: Agent, output: Any) -> None:
        rich.print("🤖 CustomAgentHook -- on_end")
        rich.print(f"### Agent {agent.name} started. Usage: {ctx.usage},  userName: {ctx.context.name}")
        rich.print("\n\n")


#---------------------------------------------------------
# Initialize the agent
agent = Agent[User_info](
    name="my_agent",
    instructions="You are a helpful assistant",
    model="gpt-4.1-mini",
    # hooks=CustomAgentHook()
)

#---------------------------------------------------------    


result =  Runner.run_sync(agent, "hi", context=user_information, hooks=start_hook) 
print("\n\n")
print(result.final_output) 




#-----------------------------------------------------------------------------------------------------------

# LifeCycle => Initialization -> Start -> Run -> End -> Final Output
# Initialization + Execute + Terminate
# hmara agent Runner chlata hai or tab tak chlata rehta hai jab tak jawab naa jaye.
# Runner ka aik lifeCycle hai zinda hota hota hai chalta hai or marr kata hai isi tarhn Agent ka bhi same isi tarhn hota hai hota hai.
# Output of Life Cycle:

# 🤑 CustomRunHook -- on_agent_start
# ### Agent my_agent started. Usage: Usage(requests=0, input_tokens=0, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=0, 
# output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=0), userName: azlaan



# 🤖 CustomAgentHook -- on_start
# ### Agent my_agent started. Usage: Usage(requests=0, input_tokens=0, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=0, 
# output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=0),  userName: azlaan



# 🤑 CustomRunHook -- on_agent_end
# ### Agent my_agent ended. Usage: Usage(requests=1, input_tokens=17, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=10,   
# output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=27), userName: azlaan



# 🤖 CustomAgentHook -- on_end
# ### Agent my_agent started. Usage: Usage(requests=1, input_tokens=17, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=10, 
# output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=27),  userName: azlaan
