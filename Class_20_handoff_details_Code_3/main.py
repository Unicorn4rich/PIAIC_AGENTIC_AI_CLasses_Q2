import json
from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, Handoff, RunContextWrapper
from agents.extensions import handoff_filters
import rich
from pydantic import BaseModel


#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------

# is agent ko User_Info ke structure form mein input data milega.
customer_agent = Agent( # handoff pe chalea ye agent but iske pass jo conversation history ya baqi cheezen aengi wo modify ho kar aengi.
    name="customer_agent",
    instructions="you help user in customer support queries",
    model="gpt-4.1-mini",  
    handoff_description="You do customer support"  # ye override ho jaegi Handsoff class ki description se.
)

#---------------------------------
class User_Info(BaseModel): # pydantic ki class mein data keyword rgument ki shakal mein pass karen positional nahi. ()"shoaib" -> name="shoib")
    name: str  # ye value LLM se aegi.
    query: str # ye value LLM se aegi

#---------------------------------
async def my_invoke(wrapper: RunContextWrapper, arguments: str) -> Agent:  # arguments -> iske andar data jason string object ki form mein aa rha hai.
    # ye sab hamne sirf apne dekhny e liye likha warna return mein sirf agent karna tha.
    user_data = json.loads(arguments) # ye trpple quote jason string object ko tripple quote se hata kar normal jason pbject bnata hai.
    user_info = User_Info(**user_data) # User_Info(**{"name": "shoaib"}) -> yahn is tarhn data pass ho rha hai taky User_Info ki ke attributes mein value jaa saky.
    
    # print to see the structured data
    rich.print(f"User name: {user_info.name}")
    rich.print(f"Raw arguments: : {arguments}")
    rich.print(f"Parsed User_Info object: {user_info}")
    
    customer_agent.instructions = f"You are helping {user_info.name} with customer support queries. Address them by name." 
    
    return customer_agent


#---------------------------------
schema = User_Info.model_json_schema() # ye peroprty dictionery bana degi.
schema["additionalProperties"] = False
#---------------------------------

# beech ka matlab handsoff se pehly modification karne wali class.
customer_agent_handoff = Handoff( # handoff karte waqt isko structure form mein input diyya jaye User_Info ki class se.
    agent_name=customer_agent.name, # handoff agent ka naam  
    tool_name="customer_agent_handoff",
    tool_description="You are customer support agent, when user ask for customer support then you help them", # description ye wali li jaengi main tool mein jahn handoff ho rha hai uski description override ho jaegi.
    input_json_schema=schema, # requred property -> jo handoff ko input milega wo object structured form mein hoga -> isko lgana zrori hai but agr isko empty bhi rakhen tab bhi error nahi dega.
    on_invoke_handoff=my_invoke, # requred property -> agent yahn se pass kar rhy hain. or value argument bhi yahn se llm bhejega.
    is_enabled=False, # tool hata dega LLM ko nahi bhejega. -> tools[] -> tool hai hi nahi triage_agent mein bhi show nahi hoa.
    strict_json_schema=True # help karta hai structre bnaty waqt.
) # is class ki propertys over-ride karti hain agent ki propertys ko.  

#---------------------------------
# is method ka ye faida hai e jab ye handoffs kar rha hota hai aik agent se dosry agent ko to ye msg generate kar ke btata hai ke handoffs ho rha hai user friendly msg.
print("😈", customer_agent_handoff.get_transfer_message(customer_agent)) # 😈 {"assistant": "customer_agent"}
#---------------------------------

triage_agent = Agent( 
    name="triage_agent",
    instructions="you are a helpful assistant",
    model="gpt-4.1-mini",
    handoffs=[customer_agent_handoff],
)
#-------------------------------
result = Runner.run_sync(triage_agent, input="HI, I am shoaib, and I need help with customer support") 
rich.print(result.final_output)














