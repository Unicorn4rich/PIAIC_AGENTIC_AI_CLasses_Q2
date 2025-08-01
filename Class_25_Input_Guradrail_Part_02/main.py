from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, input_guardrail, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput
import rich
from pydantic import BaseModel


#---------------------------------------------------
load_dotenv()
# enable_verbose_stdout_logging()
#---------------------------------------------------

class Prime_Minister_Check(BaseModel): # 8
    is_prime_minister: bool
    reason: str

#---------------------------------------------------

input_guardrail_agent = Agent( # 6
    name="input_guardrail_agent",
    instructions="you are a helpful assistant",
    model="gpt-4.1-mini",
    output_type=Prime_Minister_Check, # 7
)
#---------------------------------------------------

@input_guardrail # 4                                           user input isme direct aa gaya yahn pe.
async def prime_minister(ctx: RunContextWrapper, agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput: # in sab paramters ko value agent/llm khud provide karty hain.
    
    # rich.print("ctx: ", ctx)
    # rich.print("agent: ", agent)
    # rich.print("input: ", input)
#     9                                                   5    
    response = await Runner.run(input_guardrail_agent, input, context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info=response.final_output, # optional/additional
        #                                              10
        tripwire_triggered= response.final_output.is_prime_minister # agent ne true ya false bhej hai wo yahn aega agr value (True) ai to main aegnt nahi chalega or agr false aai to chalega.
    )
    
#---------------------------------------------------
main_agent = Agent( # 2
    name="main_agent",
    instructions="you are a helpful assitant.",
    model="gpt-4.1-mini",
    # 3
    input_guardrails=[prime_minister], # list hai iska matlab isme multiple cheezo ko rokny ke liye guardrail lgaya jaa sakta hai phir kisi bhi aik mein error aya to sara program ruk jaega.
)  
  
#---------------------------------------------------
# True -> Stop process
# False -> Continue process
result = Runner.run_sync(main_agent, input="hi my name is shoaib") # 1
rich.print(result.final_output)


#-------------------------------------------------------------------------------------------------------------------
# Notes:

