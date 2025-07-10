from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings, enable_verbose_stdout_logging
import rich

#-------------------------------
load_dotenv()
# enable_verbose_stdout_logging()
#---------------------------------

triage_agent = Agent( 
    name="triage_agent",
    instructions="always use greet tool first and then show exactly tool answer.",
    model="gpt-4.1-mini",
    model_settings=ModelSettings(max_tokens=100) # -> output 16 alfaz ka hi answer milega or ye minmum value yahn se start hoi max_token ki.
    model_settings=ModelSettings(truncation="auto") # input -> beech ki history ura deta hai.
    model_settings=ModelSettings(truncation="disabled") # truncation input hai hmara -> sari history rakhta hai.
    model_settings=ModelSettings(reasoning={"effort": "high"}) # low, medium, high, teeno tarhn se reasning krwa sakty hain.
    
    model_settings=ModelSettings(metadata={ # ye llm ko nahi jata ye bas track rakhny ke liye use hota hai developers ke.
        "team": "web-dev",
        "name": "shoaib",
    }) 
    
    model_settings=ModelSettings(store=True) # tracing dashboard pe show krwa rha hai is se.
    model_settings=ModelSettings(store=False)  # tracing dashboard pe na save hoti hai or na show hoti hai is se.
)  
  
#-------------------------------
result = Runner.run_sync(triage_agent, input="hi, how are you, show me metdata") 
# rich.print(result.final_output) 
rich.print(result._last_agent.model_settings.metadata) # we can use this for debuggin -> check konsi team ne kaam kiyya hai -> {'team': 'web-dev', 'name': 'shoaib'}





#-------------------------------------------------------------------------------------------------------------------
# Notes:

# 1. Input -> context window -> gpt-4.1 -> 1 Million -> 10 lakh words/tokens as a input leta hai.
# 2. Output -> LLM ki marzi jitne alfaz/token mein hamen jawab deta hai -> isy ham (Max_tokens) ke zariye iska output
#    limit kar sakty hain. max_token km denge to km alfaz mein baat karega or agr ziyada ho to ziyada alfazo mein baat karega lambi.

#3. max_tokens=16 -> minmum limit hai token ki 16 hai lazim deni hai warna error aega. or agr hamne prompt mein 10 lines of
#   story sentense create karne ka bola or max_token=16 bhi kam rakha to hmara jawab compress ho kar nahi aega balke ye apne
#   flow mein story btaega or jahn token khatam ye wahi rok dega adhori story ko or ye token mein space or comma ko bhi count karta hai.

#4. truncation= "auto" + "disabled" -> truncation input hai hmara
#   auto mean 1 million context token input or ye conversation history mein se starting or end ki history rakh kar baqi ki sari
#   beech ki history hata dega (truncation="auto") mein
#   (truncation="disabled") pori history rakhega or jab 1 million tokens fill ho jaenge input ya conversation mein to ye rok dega aagy ki chat ko.

#5. Reasoning -> sirf (o serease) ke models mein ye reasoning ko support karta hai kiyun ke wo reasning models hain uske ialwa nahi
#   or ham is property ka use llm ke reasning ko control karne ke liye karte hain.

#6. Metadata -> ye llm ko nahi jata ye bas track rakhny ke liye use hota hai developers ke -> {'team': 'web-dev', 'name': 'shoaib'}
#   is se ham agents or unke workflow ko bhi track kar sakty hain ke konsa gent kya kar rha hai.

#7. include_usage -> 