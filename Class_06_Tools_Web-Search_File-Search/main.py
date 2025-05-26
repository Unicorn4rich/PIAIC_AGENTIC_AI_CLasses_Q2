
from dotenv import load_dotenv # type: ignore
from agents import Agent, Runner, WebSearchTool, FileSearchTool  # type: ignore
import chainlit as cl # type: ignore



load_dotenv()

agent = Agent(
    model="gpt-4.1-mini",
    name="my_aent",
    instructions="You are a helpful asisstent, always search in file for information",
    tools=[WebSearchTool()] # latest information chahiye to ye tool call karenge kiyun ke LLM ke pass updated data nahi.
    # tools=[FileSearchTool(
    #     max_num_results=3,
    #     vector_store_ids=["vs_682f4555a7d08191bc21f23985a4f154"]
    # )]
)

#----------------------------------------------------------------------------

@cl.on_message
async def main(message: cl.Message):
    user_question = message.content
    
    res = Runner.run_sync(agent, user_question) 
    # print(res.final_output)
    await cl.Message(content= res.final_output).send()
    





