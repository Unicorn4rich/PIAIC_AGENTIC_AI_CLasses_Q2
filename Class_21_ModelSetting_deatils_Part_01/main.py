from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings, function_tool, enable_verbose_stdout_logging
import rich

#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------
@function_tool
def greet(name: str): # llm se is paramter ki value aegi user ke input se ley kar.
    """Greet the user."""
    return f"🖐 Nice tooo meet you {name}, I am Robot"
#---------------------------------

triage_agent = Agent( 
    name="triage_agent",
    instructions="always use greet tool first and then show exactly tool answer.",
    model="gpt-4.1-mini",
    model_settings=ModelSettings(temperature=2) # Settings to use when calling an LLM. -> Isy har Model support nahi karta pehly check karen bad mein use karen dosry llm ke liye.
    model_settings=ModelSettings(top_p=10) # 0 se 1 tak iski value hoti hai 
    model_settings=ModelSettings(top_k=5) # top_k= 0 to 1 million -> 10 lakh -> Model denpended tokens -> have error? it is not in SDK 
    # aik sath ye 3eno propetys use nahi ho sakti.
       
    model_settings=ModelSettings(frequency_penalty=-2), # -2.0 to 2.0
    # tools=[greet],
    # # model_settings=ModelSettings(tool_choice="auto") # tumhari marzi tool use karna chaho ya nahi tool use hony ke bad reset ho jaye check from verbose enabled.
    # # model_settings=ModelSettings(tool_choice="required") # lazim tool ka use karo instruction lazim deni hai warna ye tool call nahi hoga reset after tool use.
    # # model_settings=ModelSettings(tool_choice="none") # tool call mat karo.
    
    model_settings=ModelSettings(tool_choice="greet") # tool call karny ke bad agent terminal mein uski setting reset kar deta hai matlab turn 1 mein jo tool_choice di gai wo turn 2 mein hata di jaegi reset hogi..
    # instructions mein hamne choice sirf (greet function) ko chlany ki di isliye agent llm ko tools mein sirf greet dikhaega dosra koi function nahi.
    # isliye just greet ka output lega llm agent se iske bad jab turn 2 chlaega or sari history dubara se agent llm ko dega ke pehly hamne ye kiyya tha llm check karega ke
    # tolls mein usy ab dosry function mily hain kiyun ke wo rest ho gaye choice mein jabhi ab baqi ke function bhi use honge
    
    model_settings=ModelSettings(parallel_tool_calls=True) # paralel aik sath tools call kar sakty hain.
    model_settings=ModelSettings(parallel_tool_calls=False) # Paralel tool calls rok deta hai aik sath sary functions chlany se.
    
    model_settings=ModelSettings(truncation={"type": "auto", "last_messages": 1}) # conversation history ko control karta hai

)    
#-------------------------------
result = Runner.run_sync(triage_agent, input="hi, i am shoaib") 
rich.print(result.final_output)





#-------------------------------------------------------------------------------------------------------------------
# Notes:


#1. temperature= 0 to 2 -> pagal = Creative
#2. top_k= 0 to 1 million -> 10 lakh -> Model denpended tokens 
#3. top_p= 0 to 1       -> Choose Best Word

#1. temperature= maximum value 0 se 2 tak hoti hai. -> recommended value is 0.7 from LLMs.
#   temperature=-1 -> client se halti ho to ye error ata hai -> Error code: 400

#2. top_k= 0 to 1 million -> 10 lakh -> Model denpended tokens 
#   isme ye ya arta hai ke agr user ke (how are you) ka jawab dena hai to ye top_k ko 5 set karne ki wajah se 
#   5 words utha lega -> fine, awesome, good, okay, perfect, -> if we set in agent then have error? it is not in SDK 

#3. top_p=0 -> 0 se 1 tak iski value hoti hai 
#   words ki selection karta hai -> 5 words hain -> fine, awesome, good, okay, perfect, or ye (top_p) in sary words mein se
#   jo best ziyada suitble word hoga jiski probablity ziyada hogi usy get kar ke sentence mein lgata hai (i am fine). 

#4. frequency_penalty -> mean words -> range (-2.0 to 2.0) but accept koi bhi number of value error nahi deta.
#   LLM ke answer mein koi word bar bar aa rha hai repatedly to ham (0.0 se 2.0) ke darmiyan rakhenge to wo repat nahi hoga. 
#   - se nechy ki value jese -2 se 0 tak repation of words ziyada honge
#   0 se 2 tak repation of words km honge 
#   positive > 0 -> repation of words km honge
#   nagitive < 0 -> repation of words ziyada honge

#5. presence_penalty -> means sentense
#   positive grater then 0 -> sentnse topic change honge har dafa.
#   nagitive less then 0 -> sentnse topic change nahi honge har dafa same topic use kiyya jaa sakta hai. 
   
#6. model_settings=ModelSettings(parallel_tool_calls=False) # Paralel tool calls rok deta hai aik sath sary functions chlany se.

#7. truncation ->