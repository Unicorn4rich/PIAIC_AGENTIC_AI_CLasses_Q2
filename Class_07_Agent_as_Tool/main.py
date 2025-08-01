from agents import Agent, Runner, function_tool # type: ignore
from dotenv import load_dotenv  # type: ignore
import rich



# Agents => functions ko ham tools kehty hain => hmare bnaye huy functions call kar sakty hain 
# un functions mein api call, sanity, ya kuch bhi mangwa sakty hain.


load_dotenv()

#------------------------------------------------------------------
# weather function for calling

@function_tool   # ye openAi se import hota hai or ye jis function ke opar lgaya jata hai wo agent ke hwaly ho jata hai.
def weather_karachi(): # isy function ko agent naam se pehchanega  LLM mein ham jo naam denge us naam se aa kar is function ko identify kiyya jaega..
    """This function will return the weather in Karachi""" # ye function description hai jise dosra developer or LLM parh sakta hai.
    print("Weather in Karachi is -0 degrees celcius")
    
#------------------------------------------------------------------
# prime minsiter function

@function_tool   # ye openAi se import hota hai or ye jis function ke opar lgaya jata hai wo agent ke hwaly ho jata hai.
def prime_minister_of_pakistan(): # isy function ko agent naam se pehchanega or agr input mein ham is function ka naam ghalat ya phir word mistake bhi kar denge tab bhi agent isy identify kar ke chala dega.
    print("Prime minister of pakistan is Azlaan")

#------------------------------------------------------------------

agent = Agent(
    model="gpt-4.1-mini",
    name="Azlaan_AGent",
    instructions="Your are a helpful assistent",
    tools=[weather_karachi, prime_minister_of_pakistan] # agent naam se functions ko pehchanta hai ke usy konsa tool call karna hai.
)

#------------------------------------------------------------------

res = Runner.run_sync(agent, "who is the prime minister?")
rich.print(res)




#=============================================================================================================--
# Agent as tool Work here 

english_agent = Agent(
    model="gpt-4.1-mini",
    name="english_agent",
    instructions="Your are a expert in english",
)

#------------------------------------------------------------------

triage_agent = Agent(
    model="gpt-4.1-mini",
    name="my_agent",
    instructions="You route user queries to the appropriate department agent.",
    tools=[
        english_agent.as_tool(tool_name="english_agent", tool_description="Your are a expert in english")
        ] # isme hamne aik agent ko as a tool bana kar pass kar diyya hai.
)
#------------------------------------------------------------------

res = Runner.run_sync(triage_agent, "what is the meaing of life?")
rich.print(res)




