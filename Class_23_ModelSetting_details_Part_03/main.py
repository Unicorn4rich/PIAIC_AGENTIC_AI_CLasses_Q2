from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings, enable_verbose_stdout_logging
import rich

#-------------------------------
load_dotenv()
# enable_verbose_stdout_logging()
#---------------------------------

# Combine bhi ho rha hai or over_ride bhi ho rha hai.
base = ModelSettings(temperature=0.3, max_tokens=100) # max_token ko uthaya..
over_ride = ModelSettings(temperature=0.7, store=True) # temprature ko uthaya -> isne override kar diyya hai base ko.

final_setting = base.resolve(over_ride)


rich.print(final_setting.to_json_dict()) # ModelSettings ki propertys ki dictionary form mein convert kar rhy hain.
#---------------------------------

triage_agent = Agent( 
    name="triage_agent",
    instructions="you are a helpful assitant.",
    model="gpt-4.1-mini",
    model_settings=ModelSettings(include_usage=True) # Token use management
    model_settings=ModelSettings(response_include=["message.output_text.logprobs"]) # model response mein additonl cheezen add karta hai matlab har aik token/alfaz ki information top_p ki probbality bhi iske percentage se hoti hai -> Logprob(token='Hello', bytes=[72, 101, 108, 108, 111], logprob=-0.061968, top_logprobs=[]
    
    model_settings=final_setting 
)  
  
#-------------------------------
result = Runner.run_sync(triage_agent, input="hi, how are you") 
rich.print(result.final_output) 
rich.print("🤖", result) 





#-------------------------------------------------------------------------------------------------------------------
# Notes:

# 1. include_usage -> tokens count karta hai True mein dikhata hai or False mein chupata hai.
# 2. response_include -> isme hamen or extra information milti hai LLM or agent beavier ki jese tokens top-p waghera
# 3. extra_query -> APi Call mein kuch cheezen bhej ya get kar sakty hain inke zariye.
#    extra_body
#    extra_headers
#    extra_args

# 4. 