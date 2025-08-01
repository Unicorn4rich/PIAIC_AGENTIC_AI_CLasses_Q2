from dotenv import load_dotenv
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging, output_guardrail, RunContextWrapper, GuardrailFunctionOutput
import rich
from typing import Any
from pydantic import BaseModel


#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------
@function_tool
def weather_info(city: str):
    """This function is about to tell weather report"""
    
    return f"{city} is sunny"


#---------------------------------
class Weather_Output_Check(BaseModel):
    is_weather: bool
    reason: str

#---------------------------------
output_guardrail_agent = Agent(
    name="output_guardrail_agent",
    instructions="You always check if agent response has weather or any information related to weather",
    model="gpt-4.1-mini", 
    output_type=Weather_Output_Check
)

#---------------------------------
@output_guardrail
async def weather_check(wrapper: RunContextWrapper, agent: Agent, output: Any) -> GuardrailFunctionOutput: 
    
    # yahn par ham run_sync nahi laga sakty supported nahi hai or ye Runner return karta hai -> OutputGuardrailResult
    response = await Runner.run(starting_agent=output_guardrail_agent, input=output, context=wrapper)
    
    return GuardrailFunctionOutput(
        output_info=response.final_output, # wajah aegi 
        tripwire_triggered=response.final_output.is_weather # True false aega.
        
    )
#---------------------------------

second_agent = Agent( 
    name="second_agent",
    instructions="when ever user ask for weather you use tool for fetching weather data.",
    model="gpt-4.1-mini", 
    tools=[weather_info],
    output_guardrails=[weather_check],
    handoff_description="You Support user query for weather information"
)  

#---------------------------------

triage_agent = Agent( 
    name="triage_agent",
    instructions="first call weather_info tool after showing the result of weather_info then you delegate to second_agentwhen ever user ask for weather you use tool for fetching weather data, must delegate task tho second_agent.",
    model="gpt-4.1-mini", 
    tools=[weather_info],
    output_guardrails=[weather_check],
    handoffs=[second_agent]
)  
  
#-------------------------------
result =  Runner.run_sync(triage_agent, input="call weather info tool then call second_agent, what is the weather of karachi?, call second_agent") 
rich.print("😈", result.final_output)

#-------------------------------------------------------------------------------------------------------------------
# Notes:

# Input guardrail sirf first agent pe work karta hai kisi or pe nahi
# Output guardrail sab agents mein lgaty hain taky jo llm response laye usme wo bhi ghalat baat na akr rha ho 
# or jo agent jawab dega output guardrail wahn pe chal jata hai llm se output any ke bad bhi.

