from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, AgentHooks, RunContextWrapper, function_tool, ModelSettings
import rich
from pydantic import BaseModel, Field
from typing import Literal, List, Optional, Any
import datetime


#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------

time = datetime.datetime.now()
#---------------------------------

@function_tool
def weather_tool(city: str):
    return f"{city} weather is very bad and hot"
#---------------------------------

@function_tool
def currunt_time():
    global time
    return f"currunt time is {time} "
#---------------------------------

agent = Agent( 
    name="agent",
    instructions="You are a helpful assiatnt",
    model="gpt-4.1-mini", 
    tools=[weather_tool, currunt_time],
    # tools=StopAtTools([shoaib_exam_result, weather_tool]), # koi bhi aik tool call hoga to baqi sab tools nahi chalenge ruk jaenge.
    
    # sare tool use karo jo user input mein hain or user input ne jo pehla tool mention kiyya hai us tool ka pehly result show karo.
    tool_use_behavior="stop_on_first_tool", # after call the tools and start do not extra modifications -> matlab tool ka jo jawab aa rha hai wo dena llm ka nahi dena.
    # tool_use_behavior="run_llm_again" # llm isko use kar ke modifications kar sakta hai tool ke answer ke sath.
    # tool_use_behavior=["weather_tool", "currunt_time"]
    
    model_settings=ModelSettings(parallel_tool_calls=True)
)  
  
#-------------------------------
try:
    result =  Runner.run_sync(agent, input="hi what is the currunt time?  what is the weather today in karachi") 
    rich.print("😈", result.final_output)

except Exception as e:
    print("😒", e)


#-------------------------------
# Notes:

# turn 1 agent apni sari cheeze ley kar llm ke pass gaya jisme uske functions bhi thy jinme paramter required thy
# llm ne un function tools ke schema mein paramters ki value return kar ke bheji ke in functions ko chala do phir
# usi 1 turn ke andar hi ye function chal jaty hain un values ke sath or return krwa dety hain apna output or agr 
# hamne (tool_use_behavior="stop_on_first_tool") lgaya hua hai to phir ye user ne input mein jis tool ko pehly
# mention kiyya hoga sirf uska result show hoga final output mein or wahi user ko diyya jaega jese aya.
# But agr ham (tool_use_behavior="stop_on_first_tool") nahi lgate to un function ka jo return aya hai usko (turn=2) mein
# mein dubara llm ko diyya jata hai phir llm un answers mein thori or modification karta hai or user ko jawab dey deta hai.