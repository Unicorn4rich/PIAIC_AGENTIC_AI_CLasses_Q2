from dotenv import load_dotenv
from agents import Agent, Runner, input_guardrail, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
from pydantic import BaseModel
import asyncio

load_dotenv()
#-----------------------

class Slangs_check_output(BaseModel):
    is_slang: bool
    reasoning: str

#-----------------------

guardrail_agent = Agent(
    model="gpt-4.1-mini",
    name="Guardrail check",
    instructions="Check if the user is using slangs in any language",
    output_type=Slangs_check_output
)
#-----------------------

@input_guardrail # ye decorator import karna parta hai guardrail lgane ke liye.       isme ham object ya imae ya file ki shakal mein input dey sakty hain
async def slangs_guardrails(ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    
    result = await Runner.run(guardrail_agent, input, context=ctx.context) # ye purani ya currunt agent ki info hai agly agent ko pass karne ke liye.
    
    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered = result.final_output.is_slang         # isme ham yes ya no mein karenge
    )


#-----------------------

async def main():
    agent = Agent(
    model="gpt-4.1-mini",
    name="my_agent",
    instructions="You are a helpful assistant.",
    input_guardrails=[slangs_guardrails]
)

#-----------------------
    try:
        result =  await Runner.run(agent, "how are you")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("user is using bad langauge: ", e)
    

if __name__ == "__main__":
    asyncio.run(main())    
