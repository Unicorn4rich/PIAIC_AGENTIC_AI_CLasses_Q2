from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, AgentHooks, RunContextWrapper, function_tool
import rich
from pydantic import BaseModel, Field
from typing import Literal, List, Optional, Any
import datetime


#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------

# class My_Name(BaseModel):
#     # is_name: bool
#     # name: str
    
#     is_order: bool
#     type: Optional[Literal["Pizza", "Burger"]] = None
#     ingredients: List[str] = Field(default_factory=list)
    
#---------------------------------
currunt_time = datetime.datetime.now()
#---------------------------------

class AgentCustom_Hook(AgentHooks): # AgentHooks -> agent hook ke tamam methods is class mein access kar sakty hain.
    async def on_start(self, context, agent):
        rich.print(currunt_time)
        print("I am on_start..........")


    async def on_end(self, context: RunContextWrapper, agent: Agent, output: Any):
        rich.print(currunt_time)
        print("I am on_end..........")
        
        
    async def on_handoff(self, context, agent, source):
        rich.print(currunt_time) 
        print("I am on_handoff..........")   
        
     
    async def on_tool_start(self, context, agent, tool):
        rich.print(currunt_time)
        print("I am on_tool_start..........")  
        
        
    async def on_tool_end(self, context, agent, tool, output):
        rich.print(currunt_time)
        print("I am on_tool_end..........")    
    
#---------------------------------
@function_tool
def weather_tool(city: str):
    return f"{city} weather is very bad and hot"
#---------------------------------
hinglish_agent = Agent( 
    name="hinglish_agent",
    instructions="You always answer in hinglish.",
    model="gpt-4.1-mini", 
    handoff_description="reply in hinglish",
    hooks=AgentCustom_Hook(),   
    tools=[weather_tool] 
)  
#---------------------------------

agent = Agent( 
    name="agent",
    instructions="You are a helpful assiatnt ",
    model="gpt-4.1-mini", 
    # output_type=My_Name
    hooks=AgentCustom_Hook(),
    handoffs=[hinglish_agent]
)  
  
#-------------------------------
result =  Runner.run_sync(agent, input="hi i am shoaib please call hinglish agent, what is the weather today in karachi") 
rich.print(currunt_time)
rich.print("😈", result.final_output)


#-------------------------------
# Coding with Agent answer:

# name_check = result.final_output

# rich.print(name_check) # My_Name(is_name=True, name='shoaib')

# if name_check.name == "shoaib":
#     print(f"✔ Hi {name_check.name}")





#-------------------------------------------------------------------------------------------------------------------
# Notes:

# AentHooks workflows output:

# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_27> uv run main.py
# 2025-07-17 17:24:40.525061
# I am on_start..........
# 2025-07-17 17:24:40.525061
# I am on_handoff.......... 
# 2025-07-17 17:24:40.525061
# I am on_start..........
# 2025-07-17 17:24:40.525061
# I am on_tool_start..........
# 2025-07-17 17:24:40.525061
# I am on_tool_end..........
# 2025-07-17 17:24:40.525061
# I am on_end..........
# 2025-07-17 17:24:40.525061
# 😈 Hi Shoaib! Karachi ka mausam aaj bohat garam aur behtreen nahi hai. Kuch aur madad chahiye ho to batao!
# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_27>


#--------------------------------------------------------------
# VerBose Workflow:
    

# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_27> uv run main.py
# Creating trace Agent workflow with id trace_c6b5e4a928d543a589a36c773d208c38
# Setting current trace: trace_c6b5e4a928d543a589a36c773d208c38
# Creating span <agents.tracing.span_data.AgentSpanData object at 0x00000208B8839720> with id None
# Running agent agent (turn 1)
# 2025-07-17 17:26:59.551169
# I am on_start..........
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x00000208B871AE90> with id None
# Calling LLM gpt-4.1-mini with input:
# [
#   {
#     "content": "hi i am shoaib please call hinglish agent, what is the weather today in karachi",
#     "role": "user"
#   }
# ]
# Tools:
# [
#   {
#     "name": "transfer_to_hinglish_agent",
#     "parameters": {
#       "additionalProperties": false,
#       "type": "object",
#       "properties": {},
#       "required": []
#     },
#     "strict": true,
#     "type": "function",
#     "description": "Handoff to the hinglish_agent agent to handle the request. reply in hinglish"
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN
# Previous response id: None

# LLM resp:
# [        
#   {
#     "arguments": "{}",
#     "call_id": "call_D3P0FMyO2vs9JF9kYozYHa0K",
#     "name": "transfer_to_hinglish_agent",
#     "type": "function_call",
#     "id": "fc_6878ec171ed0819890c8e72b48902f960c71872060b91e99",
#     "status": "completed"
#   }
# ]

# Creating span <agents.tracing.span_data.HandoffSpanData object at 0x00000208B883C310> with id None
# 2025-07-17 17:26:59.551169
# I am on_handoff..........
# Creating span <agents.tracing.span_data.AgentSpanData object at 0x00000208B8839D10> with id None
# Running agent hinglish_agent (turn 2)
# 2025-07-17 17:26:59.551169
# I am on_start..........
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x00000208B8F2BD50> with id None
# Calling LLM gpt-4.1-mini with input:
# [
#   {
#     "content": "hi i am shoaib please call hinglish agent, what is the weather today in karachi",
#     "role": "user"
#   },
#   {
#     "arguments": "{}",
#     "call_id": "call_D3P0FMyO2vs9JF9kYozYHa0K",
#     "name": "transfer_to_hinglish_agent",
#     "type": "function_call",
#     "id": "fc_6878ec171ed0819890c8e72b48902f960c71872060b91e99",
#     "status": "completed"
#   },
#   {
#     "call_id": "call_D3P0FMyO2vs9JF9kYozYHa0K",
#     "output": "{\"assistant\": \"hinglish_agent\"}",
#     "type": "function_call_output"
#   }
# ]
# Tools:
# [
#   {
#     "name": "weather_tool",
#     "parameters": {
#       "properties": {
#         "city": {
#           "title": "City",
#           "type": "string"
#         }
#       },
#       "required": [
#         "city"
#       ],
#       "title": "weather_tool_args",
#       "type": "object",
#       "additionalProperties": false
#     },
#     "strict": true,
#     "type": "function",
#     "description": ""
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN
# Previous response id: None

# LLM resp:
# [
#   {
#     "arguments": "{\"city\":\"Karachi\"}",
#     "call_id": "call_Dauk0ZRJrijNB3zZfpHC3X7A",
#     "name": "weather_tool",
#     "type": "function_call",
#     "id": "fc_6878ec1839a88198b47a84120ce9fd980c71872060b91e99",
#     "status": "completed"
#   }
# ]

# Creating span <agents.tracing.span_data.FunctionSpanData object at 0x00000208B8EB9F90> with id None
# 2025-07-17 17:26:59.551169
# I am on_tool_start..........
# Invoking tool weather_tool with input {"city":"Karachi"}
# Tool call args: ['Karachi'], kwargs: {}
# Tool weather_tool returned Karachi weather is very bad and hot
# 2025-07-17 17:26:59.551169
# I am on_tool_end..........
# Running agent hinglish_agent (turn 3)
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x00000208B92F8CD0> with id None
# Calling LLM gpt-4.1-mini with input:
# [
#   {
#     "content": "hi i am shoaib please call hinglish agent, what is the weather today in karachi",
#     "role": "user"
#   },
#   {
#     "arguments": "{}",
#     "call_id": "call_D3P0FMyO2vs9JF9kYozYHa0K",
#     "name": "transfer_to_hinglish_agent",
#     "type": "function_call",
#     "id": "fc_6878ec171ed0819890c8e72b48902f960c71872060b91e99",
#     "status": "completed"
#   },
#   {
#     "call_id": "call_D3P0FMyO2vs9JF9kYozYHa0K",
#     "output": "{\"assistant\": \"hinglish_agent\"}",
#     "type": "function_call_output"
#   },
#   {
#     "arguments": "{\"city\":\"Karachi\"}",
#     "call_id": "call_Dauk0ZRJrijNB3zZfpHC3X7A",
#     "name": "weather_tool",
#     "type": "function_call",
#     "id": "fc_6878ec1839a88198b47a84120ce9fd980c71872060b91e99",
#     "status": "completed"
#   },
#   {
#     "call_id": "call_Dauk0ZRJrijNB3zZfpHC3X7A",
#     "output": "Karachi weather is very bad and hot",
#     "type": "function_call_output"
#   }
# ]
# Tools:
# [
#   {
#     "name": "weather_tool",
#     "parameters": {
#       "properties": {
#         "city": {
#           "title": "City",
#           "type": "string"
#         }
#       },
#       "required": [
#         "city"
#       ],
#       "title": "weather_tool_args",
#       "type": "object",
#       "additionalProperties": false
#     },
#     "strict": true,
#     "type": "function",
#     "description": ""
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN
# Previous response id: None

# Exported 4 items
# LLM resp:
# [
#   {
#     "id": "msg_6878ec1928ec8198bda9ae24b285a1d10c71872060b91e99",
#     "content": [
#       {
#         "annotations": [],
#         "text": "Hi Shoaib! Karachi ka aaj ka mausam bahut garam aur kharab hai. Kuch aur madad chahiye?",
#         "type": "output_text",
#         "logprobs": []
#       }
#     ],
#     "role": "assistant",
#     "status": "completed",
#     "type": "message"
#   }
# ]

# 2025-07-17 17:26:59.551169
# I am on_end..........
# Resetting current trace
# 2025-07-17 17:26:59.551169
# 😈 Hi Shoaib! Karachi ka aaj ka mausam bahut garam aur kharab hai. Kuch aur madad chahiye?
# Shutting down trace provider
# Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x00000208B6D116A0>
# Exported 2 items
# Exported 2 items
# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_27>
