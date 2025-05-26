from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, RunContextWrapper
from dataclasses import dataclass
import rich

load_dotenv()
#-----------------------------------------

# ye ham aik context set kar rhy hain agent ke liye jispe hmari baat cheet hogi agent se.
@dataclass  # is class ka ye faida hai ke isme hamen init/constructor waghera nahi bnana parta or ye khud hi attributes mein value set kar deta hai.
class User_info():  # this is class object
    name: str
    age: int
    address: str
    
# instance/object of User_info class jo ham RUnner ko pass karenge.
user_information = User_info("shoaib", 23, "Gaaoun")

#-----------------------------------------

# Runner mein jo context data pass kiyya wo data LLM ne nahi uthaya jabhi han ye fyunction create kar rhy hain taky wo data LLM ko mily.
@function_tool
async def fetch_user_info(wrapper: RunContextWrapper[User_info]) -> str:
    # database se data mangwaya.
    # list ke andar data store kiyye.
    # list ko filter kiyya.
    # if condition > se apne kaam ki cheez nikali.
    # or return mein usko mention kar diyya.
    return f"username is {wrapper.context.name} and user age is {wrapper.context.age} and the address is {wrapper.context.address}" 
    
#---------------------------------------    

agent = Agent[User_info](
    model="gpt-4.1-nano",
    name="my_agent",
    instructions="your are helpfull assistent",
    tools=[fetch_user_info] # function tool waly function ko yahn pass karenge.
)

#-----------------------------------------
#                                                                          ye object uth kar function_tool ke wrapper patameter ke andar chala gaya.                                 
response = Runner.run_sync(agent, "what is the name and age and address of the user?", context=user_information)
rich.print(response.final_output)  # rich.print se output ko achi tarah print karwayenge.