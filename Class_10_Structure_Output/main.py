from dotenv import load_dotenv
from agents import Agent, Runner, WebSearchTool
from pydantic import BaseModel # structre bnany ke liye isko import kiyya hai.
import rich

load_dotenv()
#--------------------------
# create database
db = []
#--------------------------

class BookInfo(BaseModel): # hmara jo agent hai wo is structure ke andar jawab dega iska faida ye hai ke ham ispe (if else) ki condition bhi lag sakty hain. 
  title: str
  author: str
  published_year: int
  genre: str
    
#--------------------------

agent = Agent(
    model="gpt-4.1-mini",
    name="my_agent",
    instructions="you are a weather agent",
    output_type=BookInfo,  # yahan humne output type ko BookInfo class se link kiya hai taky structure wesa ho jesa ham chahty hain.
    tools=[WebSearchTool()] # normally LLM se ham paksitani book (khushbu) dhond nahi paa rhy the phir jab hamne WebSearchTool use kiya to hamen wo book or uski details mil gai.
)

#--------------------------

while True:
    user_input = input("Enter your question: ")
    result = Runner.run_sync(agent, user_input)

    db.append(result.final_output.model_dump()) # ab ham result ko database mein store kar rhy hain.
    rich.print(db) # ab hamara database print hoga jo ke ek list hai aur ismein hamaray results store honge.

    

#--------------------------------------------------------------------------------------------------------
# JAB YE CODE RUN KARNA HO TO YAHN SE NEECHY KA SARA CODE COMMENT KAR DEN YE EXTRA HAI.

result = Runner.run_sync(agent, "Tell me about the pakistani book 'khushbu'?")
# rich.print(result.final_output.model_dump()) # object ke format mein result milega. 

db.append(result.final_output.model_dump()) # ab ham result ko database mein store kar rhy hain.
print(db) # ab hamara database print hoga jo ke ek list hai aur ismein hamaray results store honge.

# output: -> hmara jo output aega LLM se wo hmare define kiyye huy pydantic class ke attributes ke andar aega.
        # [{'title': 'Khushbu', 'author': 'Parveen Shakir', 'published_year': 1976, 'genre': 'Poetry'}]
        
#--------------------------------------------------------------------------------------------------------

if result.final_output.temperature_c > 30:
    rich.print("its hot")
else:
    rich.print("its cold")    

#--------------------------------------------------------------------------------------------------------
# Structured Output => Consistant jawab mily har dafa aik jesa isliye ham ye structure bnaty hain.
# user question -> hello how are you?
# agent response -> Hello! I'm doing well, thank you. How can I assist you today?

# ab masla ye hai ke agent har dafa alag alag tariqe se jawab deta hai jis se meri ye if condition fail hony ke bohut chancess hain.

if result.final_output == "Hello! I'm doing well, thank you. How can I assist you today?":
    print("Test Passed")
else:
    print("Test Failed")    