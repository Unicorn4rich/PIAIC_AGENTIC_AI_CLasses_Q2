from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, RunContextWrapper, FunctionToolResult, ToolsToFinalOutputResult, function_tool, ModelSettings, set_tracing_disabled
import rich
from pydantic import BaseModel


#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
set_tracing_disabled(disabled=True)
#---------------------------------

# @function_tool(name_override="Weather_of_Karachi", description_override="tool gives you weather info")
@function_tool(use_docstring_info=False) # dock string ko function schema mein pass hony se rokta hai.
def weather_info(city: str):
    """ This tool is forn weather info"""
    return f"{city} weather is dusty"

#---------------------------------
# # is se ham final_output ke response ko control kar sakty hain over-ride ya modify jo chahen wahi output dega.
# def toool_behavior(ctx:RunContextWrapper, my_list: list[FunctionToolResult] ) -> ToolsToFinalOutputResult:
#     print("\n\n")
#     rich.print("😘", my_list[0].output)
#     print("\n\n")            # if its then not over-ride + tool output ko over-ride kar diyya -> ab final_output mein isi text ko return kiyya jaega.
#     # return ToolsToFinalOutputResult(is_final_output=False, final_output="shoaib is a boy") # jab tak final_output mein value nahi ati tool ko bar bar call kiyya jata hai jab tak value nahi aa jati.
#     return ToolsToFinalOutputResult(is_final_output=True, final_output=my_list[0].output) # jab tak final_output mein value nahi ati tool ko bar bar call kiyya jata hai jab tak value nahi aa jati.
# #---------------------------------

hinglish_agent = Agent(
    name="agent",
    instructions="You are a helpfull assistant",
    model="gpt-4.1-nano",
)
# #---------------------------------

agent = Agent( 
    name="agent",
    instructions="when user ask in hinlish delegate to the hinglish_agent, You are a helpfull assistant",
    model="gpt-4.1-nano",
    # tool_use_behavior=toool_behavior, # is behavior mein agr ham custom tool bana kar pass kar den to output modify kiyya ja sakta hai user question kuch bhi ho or real tool answer kuch bhi ham apni marzi ka jawab dilwa sakty hain.
    tools=[weather_info],
    model_settings=ModelSettings(tool_choice="required"), # ye tool ki setting required hogi to reset_tool_choice kaam karega bar bar warna nahi.
    reset_tool_choice=True,   # isko hmesha True rakhna hai warna jab tak llm ko iska tool call kar ke iska return nahi milta wo isy bar bar call karta rhega False par or ye rukega nahi yani loop mein phans jaega or tab jab hmare max_turn=10 khatam honge yani ke by-dfault 10 hoty hain agr zada honge to ye chalta rhega. 
    # tools=[ hinglish_agent.as_tool(
    #     name="hinglish_agent", # transfer_to_hinglish_agent -> ye likh dega jab llm ko pass karega.
    #     tool_description="You reply in hinglish"
    # )]
)  
#-------------------------------
# Clone_agent = agent.clone( # iska use ham dosra runner bana kar kar sakty hain ke aik agent ke runner se result aye usko dosry agent ke runner mein as input daal do.
#     name="Clone_agent"
# )
#-------------------------------

result =  Runner.run_sync(agent, input="hi, what is the weather of karachi") 
# result =  Runner.run_sync(Clone_agent, input="hi, what is the weather of karachi") 
rich.print("😈", result.final_output) # 😈 







# ============================================================================================================
# LLM context see and not see


# class User_Info(BaseModel):
#     user_name: str
#     user_age: int
#     mother_name: str
#     father_name: str
    
# user_info = User_Info(user_name="shoaib", user_age=21, mother_name="ammi", father_name="bashir")    
# #---------------------------------
# # llm can see this
# @function_tool
# def user_name(ctx: RunContextWrapper[User_Info]):
#     return f"user name is {ctx.context.user_name}"


# @function_tool
# def user_age(ctx: RunContextWrapper[User_Info]):
#     return f"user age is {ctx.context.user_age}"


# @function_tool
# def user_mother(ctx: RunContextWrapper[User_Info]):
#     return f"user mother name is {ctx.context.mother_name}"


# @function_tool
# def user_father(ctx: RunContextWrapper[User_Info]):
#     return f"user father name is {ctx.context.father_name}"


# #---------------------------------
# # llm can not see your complete information exceptt your user name
# # isme ham function nahi lagenge to ye context llm ko nhi milega or isy han instruction mein pass karenge.

# # @function_tool # ye data llm ko jaega or agr ham isme @function_tool lagaenge to isy tools=[] mein pass kar sakty hain
# def dyn_ins(ctx: RunContextWrapper[User_Info], agent: Agent) -> str:
#     return f"You are a helpful assiatnt, user name is {ctx.context.user_name}"

# #---------------------------------
# agent = Agent[User_Info]( 
#     name="agent",
#     instructions=dyn_ins,
#     model="gpt-4.1-mini", 
#     # tools=[dyn_ins]  # yahn ham context ko ley rhy hain function tool ki wajah se
#     tools=[user_name, user_age, user_mother, user_father]  # 
# )  
  
# #-------------------------------

# # my_runner = Runner()
# # my_runner.run_sync

# while True:
#     user_input = input("enter your name: ")
#     result =  Runner.run_sync(agent, input=user_input, context=user_info) # TresponseInputItem -> chatcompletion input style
#     rich.print("😈", result.final_output) # 
#   # rich.print("😈", result.to_input_list()) # bana bnaya object form mein user or assitant conversation.


# ============================================================================================================
# 

# @function_tool
# def weather_info():
#     return "Karachi weather is green"

# #---------------------------------

# agent = Agent( 
#     name="agent",
#     instructions="You are a helpfull assistant",
#     tools=[weather_info]
# )  
  
# #-------------------------------

# config = RunConfig(
#     model="gpt-4.1-mini",
#     tracing_disabled=True,
#     workflow_name="shoaib Agent", # traing agent name in dashboard
#     trace_include_sensitive_data=False # OpnaAi dashboard mein sensitive data save nahi hoga
# )

# result =  Runner.run_sync(agent, input="hi what is the weather of katrchi", run_config=config) 
# rich.print("😈", result.final_output) # 
  








#-------------------------------
# Notes:

