from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, function_tool, handoff, Handoff, RunContextWrapper
from agents.extensions import handoff_filters
import rich

#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#--------------------------------


@function_tool
def greeting(name: str):
    return f"hello nice to meet you {name}"

#---------------------------------
def enable_status(wrapper: RunContextWrapper, agent: Agent): # ham kisi condition par iska use kar sakty hain ke ye handoff pass ho ya na ho
    # return True
    name = input("enter your name: ") # Input mein shoaib denge to tool terimnal mein nahi dikhega or agr koi or value denge to tool dikha dega.
    if name == "shoaib":
        return False
    return True
#---------------------------------
customer_support = Agent( # handoff pe chalea ye agent but iske pass jo conversation history ya baqi cheezen aengi wo modify ho kar aengi.
    name="customer_support",
    instructions="always greet user first with greeting tool, you are a customer support agent",
    model="gpt-4.1-mini",    
    tools=[greeting]
)
#---------------------------------
# ye handoff karty waqt tools ko remove kar dega. ye dono same agent ko handoff mofications kar ke dey rhy hain.
customer_support_filter = handoff(
    agent_name=customer_support,
    input_filter=handoff_filters.remove_all_tools,  # second agent ko handoff ke bad history share karty huy is method ka kaam ye hai ke conversation history mein tool call ki history or tool calls ka output wo sab khatam kar deta hai   
    tool_name_override="customer_support_filter" # name lazim dena hai agr modifcation behavier achive karna hai to kiyunke llm in alag alag handoff functions ko same naam se parhega or wo confuse hoa.
)
#---------------------------------
# ye handoff karty waqt tools ko remove nahi karega.
customer_support_no_filter = Handoff(
    agent=customer_support,
    tool_name="customer_support_no_filter", # name required beacuse llm is going to confuse.
    tool_description="you are a customer support agent",
    # is_enabled=False  # isko False rakhny se ye handoff function ko ko aagy pass nahi karega matlab ye function bana hi nahi aisy lagega matlan function On/Off -> by-default ye True hota hai matlab aagy pass hota hai.-> 
    is_enabled=enable_status  # ye khud functions call karta hai callble hai.

)
#---------------------------------
triage_agent = Agent( 
    name="triage_agent",
    instructions="always greet user with greeting tool, you are a helpful assistant",
    model="gpt-4.1-mini",
    handoffs=[customer_support_filter, customer_support_no_filter],
    tools=[greeting]
)
#-------------------------------
result = Runner.run_sync(triage_agent, input="i am shoaib, call customer_support_filter tool") 
# result = Runner.run_sync(triage_agent, input="i am shoaib, call customer_support_no_filter tool") 

print("===" * 30)

#--------------------------------------------------------------------------------------------------------------------
# Example 1 simple handoffs













