import os
from dotenv import load_dotenv # type: ignore
from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI # type: ignore
from openai.types.responses import ResponseTextDeltaEvent  # type: ignore
import rich  # type: ignore
import chainlit as cl  # type: ignore


load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#----------------------------------------------------------------------------

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1:free", openai_client=client),
    name="Sir_Taha__Agent",
    instructions="You are a just Agentic AI Sir Taha Teacher"
)

#----------------------------------------------------------------------------
# memory

history: list = []
#----------------------------------------------------------------------------

# rich.print(jawab.final_output) => run_streamed ka jawab aisy finali_output mein nahi ata 

@cl.on_message
async def main(message: cl.Message):
    user_question = message.content
    
    history.append({"role": "user", "content": history})
    
    response_message = cl.Message(content="") #aik empty message object banata hai jo UI me live streaming ke liye placeholder hai.
     
    # run_streamed => LLM direct apne pass code likh kar hamen screen par show krwa deta tha but (run_streamed) se ham wo jese line by line likhta jaea hamen wo code display hota jaega.
    LLM_answer = Runner.run_streamed(starting_agent=agent, input=user_question) # agentic loop => agent ke kehny pe jab LLM jawab create karta hai to 1/2 lines likh kar loop rok deta hai phir dubara kuch lines likhkar loop rok deta hai aisy chalta rehta hai.
    
    history.append({"role": "assistant", "content": LLM_answer.final_output})
    
    # for loop ka use kar ke ham jawab ko laty hain LLM se line by line or async isliye lgaya ke sabar karo jab tak LLM se jawab nahi ata jab tak jawab khatam nahi hota tab tak chalty rho uske bad ruk jana..
    async for event in LLM_answer.stream_events(): # jo bhi jawab ata jata hai wo ye method event ke variable ko deta jata hai.
        #                                                    data ka instance agr is class se bana ho tab chalna => ResponseTextDeltaEvent
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            # sari lines aik aik word ban kar hamen delta ke andar milti hain.
            # rich.print(event.data.delta, end="", flush=True)  #
            await response_message.stream_token(event.data.delta) # har streaming token ko turant UI me display karta hai, live typing effect banata hai.

   





