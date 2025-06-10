from dotenv import load_dotenv
from agents import Agent, Runner, input_guardrail, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, output_guardrail, OutputGuardrailTripwireTriggered
import asyncio
from pydantic import BaseModel 

load_dotenv()
#-------------------------


#=========================================================================================================
# This is Input Guardrail Code


class Slang_guardrail_check(BaseModel):
    is_slang: bool
    reason: str
#-------------------------

guardrail_agent = Agent(
    model="gpt-4.1-mini",
    name="my_agent",
    instructions="You always check user is using slang or abusive in any language",
    output_type=Slang_guardrail_check  # consistent output LLM se

)

#-------------------------
@input_guardrail
async def slang_guardrail(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered = result.final_output.is_slang
    )

#-------------------------

agent = Agent(
    model="gpt-4.1-mini",
    name="my_agent",
    instructions="You are a helpful assistant",
    input_guardrails=[slang_guardrail]
)

#-------------------------
async def main():
    try:
        result = await Runner.run(agent, "fucker")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("trip ho gaya: ", e)

if __name__ == "__main__":
    asyncio.run(main())    
    
    
    
#=========================================================================================================
# This is Output Guardrail Code 


class Message_Output(BaseModel):
    response: str
#-------------------------

class Prime_minister_check(BaseModel):
    is_primeMinister: bool
    Reason: str
    
#-------------------------

guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="you always check is user is askingabout prime minister",
    model="gpt-4.1-mini",
    output_type=Prime_minister_check
)

#-------------------------
@output_guardrail
async def prime_minister_guardrail(ctx: RunContextWrapper, agent: Agent, output: Message_Output)-> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info= result.final_output,
        tripwire_triggered=result.final_output.is_primeMinister
    )   
#-------------------------


agent = Agent(
    name="my_agent",
    instructions="you are a helpful assistant",
    model="gpt-4.1-mini",
    output_type=Message_Output,
    output_guardrails=[prime_minister_guardrail]
)   

#-------------------------
async def main():
    try:
        result = await Runner.run(agent, "who is the prime minister of pakistan?")
        print(result.final_output.response)
    except OutputGuardrailTripwireTriggered as e:
        print("I am not allowed to talk about prime minister: ", e)   
    
    
if __name__ == "__main__":
    asyncio.run(main())    