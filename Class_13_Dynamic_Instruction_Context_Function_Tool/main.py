from dotenv import load_dotenv # types: ignore
from agents import Agent, Runner, RunContextWrapper, function_tool # types: ignore
load_dotenv()
from dataclasses import dataclass

#---------------------------------------------------------

@dataclass
class User_info:  # 1
    name: str
    age: int
    uid: int
    
#instance/object of User_info    
user_information = User_info("azlaan", 23, 117759)

#---------------------------------------------------------
# context bnany ka sab se bara faida ye hai ke hamne apne database ko call kiyya wahn se names mangwaye
# or unke instance bana kar Runner ko pass karty gaye Runner se wo RunContextWrapper[User_info] mein aty gaye
# phir wahn se ham ne names nikalay or wo instruction mein pass huy or jab ham names ke bare mein agent se swal pochenge to hamen ye laa kar dega yahn se nikly huy name.

DB = ["shoiab", "azlaan", "ali", "usman", "sami"] # ye hamara database hai jahan se ham names uthayen gy.


#---------------------------------------------------------
# LLM Context 
# llm ko agent bhejta hai ye 4 cheezen User prompt, System prompt, Tools, Tool description, yani Tool mein likha hua msg dock string wala. 
         
@function_tool
def user_age(ctx: RunContextWrapper[User_info]):
    return f"user age is {ctx.context.age}"

#---------------------------------------------------------
# Local Context 
# ye wo function hai jo LLM ko nahi jaa rha. Or agr iske opar @function_tool laga den to ye bhi phir LLM ko jae ga.

# ctx: RunContextWrapper[User_info] => ctx ke andar RunContextWrapper ke anadr aya data hai jo ke User_info class ke object se aa rha hai.
# [User_info] => ye data type btata hai ke ye function kis type ka context lega.
         
def dynamic_instruction(ctx: RunContextWrapper[User_info], agent: Agent)-> str: # 3 ye us data ki tanki ka null hai jis se data nikalty hain RunContextWrapper ke zariye jahn chahy access kar sakty hain. agent likh kar paramater mein agent ko ko function ke bare mein bata rhy hain.
    return f"when user asked for age you use user_age tool and user name is {ctx.context.name}" # ctx ke andar context wrapper ke andar aya object hai jiske andar se name ki value get kar rhy hain.


#---------------------------------------------------------
# Initialize the agent
agent = Agent[User_info](
    name="my_agent",
    instructions=dynamic_instruction, # dynamic instruction function
    model="gpt-4.1-mini",
    tools=[user_age]
)

#---------------------------------------------------------    2
result = Runner.run_sync(agent, "what is the age of the user?", context=user_information) # yahn hamne wo data ki tanki bhar di yani sab se pehly data yahn aya.
print(result.final_output) # The name of the user is Azlaan.



#-------------------------------------------------------------------------------------------------------------
# Notes:


# 1. 2 types ke context hoty hain (local context) & (LLM context) jinme se aik context LLM ko jata hai or dosra nahi jata.
# 2. Generic[TContext] => Generic mean awami koi bhi aa sakta hai. TContext => kisi bhi type ki class ham laga sakty hain.

# 3. @function_tool # ye agent ko ye wala function schema bana kar bhejta hai
# 4. uv add function_schema => install this  
# is tarhn pass hota hai ye function schema bana kar agent ko.

# {
#   "name": "dynamic_instruction",
#   "description": "This is a function of dynamic_instruction ",
#   "parameters": {
#     "type": "object",
#     "properties": {
#       "valueeee": {
#         "type": "string",
#         "description": "The valueeee parameter",
#         "default": "azlaan"
#       }
#     },
#     "required": []
#   }
# }