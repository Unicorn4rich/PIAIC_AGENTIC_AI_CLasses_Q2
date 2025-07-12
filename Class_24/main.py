from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings, enable_verbose_stdout_logging, FunctionTool, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, input_guardrail, trace
from pydantic import BaseModel
import rich
from typing import Any

#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------

class Weather_pydantic(BaseModel):
    city: str

# ---------------------------------
without function_tool create function

def weather_tool(city: str):
    return f"{city} weather is sunny"

# ---------------------------------

async def run_waether_tool(ctx: RunContextWrapper[Any], arg: str): # arg mein -> json string object ata hai usy ham real object bana kar pydantic class mein pass kar rhy hain.
    
    parsed = Weather_pydantic.model_validate_json(arg) # convert json to -> traditional python object
    return weather_tool(parsed.city)

#---------------------------------
weather_pydantic_schema =Weather_pydantic.model_json_schema()
weather_pydantic_schema["additionalProperties"] = False
#---------------------------------

class PrimeMinister_Check(BaseModel):
    is_prime_minister: bool
    
# #---------------------------------

guardRail_agent = Agent( 
    name="guardRail_agent",
    instructions="always check if user is asking about prime minister.",
    model="gpt-4.1-mini",   
    output_type=PrimeMinister_Check 
)  

#---------------------------------

@input_guardrail
async def prime_minister(wrapper: RunContextWrapper, agent: Agent, input: str | TResponseInputItem) -> GuardrailFunctionOutput:
    
    response = await Runner.run(guardRail_agent, input=input, context=wrapper.context)
    
    return GuardrailFunctionOutput(
        output_info= response.final_output,
        tripwire_triggered= response.final_output.is_prime_minister
    )

# #---------------------------------
second_agent = Agent(
    name="second_agent",
    instructions="when ever user ask about presedent you also add additional information about prime minister, for example(xyz person is a prime miniter) you are a helpful assitant.",
    model="gpt-4.1-mini",
    input_guardrails=[prime_minister] # ye input guardrail yahn work nahi karega kiyun ke ye just first agent mein work karta hai.
)
# #---------------------------------

triage_agent = Agent( 
    name="triage_agent",
    instructions="you are a helpful assitant.",
    model="gpt-4.1-mini",
    
    tools=[FunctionTool(
        name="weather_tool",
        description="This tool to get weather information.",
        params_json_schema=weather_pydantic_schema, # ye structre form mein argument fill krwata hai -> weather_pydantic_schema
        on_invoke_tool=run_waether_tool, # return tool jo bhi aega wo chalaega yahn pe -> run_waether_tool
        strict_json_schema=True, # helps to validate json object
        is_enabled=True, # tool On/Off
        
    )]
    
    input_guardrails=[prime_minister],
    handoffs=[second_agent]
    
)  
  
#-------------------------------
async def main():
    with trace("my_trace"):
        try:
            result = await Runner.run(triage_agent, input="who is the presedent of pakistan, handoffs to second_agent") 
            rich.print(result.final_output)
    
        #     result2 = await Runner.run(second_agent, input=result.to_input_list() ) # sirf aik runner use karenge.
        #     # rich.print(result.final_output) 
        #     rich.print("🤖", result) 
        
        except InputGuardrailTripwireTriggered as e:
            rich.print("❌ Please dont ask me about prime minister", e)



if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


#-------------------------------------------------------------------------------------------------------------------
# Notes:

