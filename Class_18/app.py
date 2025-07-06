from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging, handoff, Handoff
import rich

#-------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#---------------------------------

#--------------------------------------------------------------------------------------------------------------------
# Example 2

hinglish_agent = Agent( 
    name="hinglish_agent",
    instructions="you are a hinglish_agent, you answer user query in hinglish.",
    handoff_description="You answer user quesry in hinglish, you reply user query when user ask question in hinglish.",
)
# handoff_description= -> is llm ke bare mein infoarmation deta hai ke ye karta kya hoga.
#---------------------------------
# ye handoff karne wala mthod hai iske pass 5 propertys hoti hain.
roman_urdu_agent_handoff = handoff( # ye hinglish_agent ki propertys ko override kar rha hai matlab change kar rha hai. iska use ham handoff karte waqt kuch cheezen customize karne ke liye karte hain.
    agent=hinglish_agent, # reuried parameter and positnoal parmater iske ilawa baqi ke optional paramter hoty hain.
    tool_name_override="roman_urdu_agent" # 
    tool_description_override="you replay in roman urdu."
)

#---------------------------------
triage_agent = Agent( 
    name="triage_agent",
    instructions="you are a helpful assistant",
    model="gpt-4.1-mini",
    handoffs=[roman_urdu_agent_handoff], 
)
#-------------------------------
result = Runner.run_sync(triage_agent, "kese ho ap?") 
rich.print("❤", result.final_output)
rich.print("😈", result)


#--------------------------------------------------------------------------------------------------------------------
# Example 1 simple handoffs

# def des():
#     return "You answer user quesry in hinglish, you reply user query when user ask question in hinglish."
# #---------------------------------

# hinglish_agent = Agent( 
#     name="hinglish_agent",
#     instructions="you are a hinglish_agent, you answer user query in hinglish.",
#     handoff_description=des,
# )

# #---------------------------------
# triage_agent = Agent( 
#     name="triage_agent",
#     instructions="you are a helpful assistant",
#     model="gpt-4.1-mini",
#     handoffs=[hinglish_agent],  # Handoff to the hinglish agent
# )
# #-------------------------------
# result = Runner.run_sync(triage_agent, "kese ho ap?") 
# rich.print("❤", result.final_output)
# rich.print("😈", result)


















#----------------------------------------------------------------------------------------
# verbose -> explain talk between agent and llm

# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_18> uv run app.py
# Creating trace Agent workflow with id trace_111facaafa0a47cca3d3a7cb2b274209
# Setting current trace: trace_111facaafa0a47cca3d3a7cb2b274209
# Creating span <agents.tracing.span_data.AgentSpanData object at 0x000001F35FE40410> with id None
# Running agent triage_agent (turn 1)
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x000001F35FE20A10> with id None
# Calling LLM gpt-4.1-mini with input:
# [
#   {
#     "content": "kese ho ap?",
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
#     "description": "Handoff to the hinglish_agent agent to handle the request. <function des at 0x000001F35A968720>"
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
#     "call_id": "call_FgynLAIn4MNnP30K8trnJrJj",
#     "name": "transfer_to_hinglish_agent",
#     "type": "function_call",
#     "id": "fc_686ac452a8948198825e631eface706703f9bb8bed340ee9",
#     "status": "completed"
#   }
# ]

# Creating span <agents.tracing.span_data.HandoffSpanData object at 0x000001F360265D90> with id None
# Creating span <agents.tracing.span_data.AgentSpanData object at 0x000001F3603AA530> with id None
# Running agent hinglish_agent (turn 2)
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x000001F35FE214D0> with id None
# Calling LLM gpt-4o with input:
# [
#   {
#     "content": "kese ho ap?",
#     "role": "user"
#   },
#   {
#     "arguments": "{}",
#     "call_id": "call_FgynLAIn4MNnP30K8trnJrJj",
#     "name": "transfer_to_hinglish_agent",
#     "type": "function_call",
#     "id": "fc_686ac452a8948198825e631eface706703f9bb8bed340ee9",
#     "status": "completed"
#   },
#   {
#     "call_id": "call_FgynLAIn4MNnP30K8trnJrJj",
#     "output": "{\"assistant\": \"hinglish_agent\"}",
#     "type": "function_call_output"
#   }
# ]
# Tools:
# []
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN
# Previous response id: None

# LLM resp:
# [
#   {
#     "id": "msg_686ac453e7d48198a5953b0fa25ba19703f9bb8bed340ee9",
#     "content": [
#       {
#         "annotations": [],
#         "text": "Main theek hoon, aap kaise ho?",
#         "type": "output_text",
#         "logprobs": []
#       }
#     ],
#     "role": "assistant",
#     "status": "completed",
#     "type": "message"
#   }
# ]

# Resetting current trace
# ❤ Main theek hoon, aap kaise ho?




#----------------------------------------------------------------------------------------
# Runner Result-> explain talk between agent and llm
# 😈
# RunResult(
#     input='kese ho ap?',
#     new_items=[
#         HandoffCallItem(
#             agent=Agent(
#                 name='triage_agent',
#                 instructions='you are a helpful assistant',
#                 prompt=None,
#                 handoff_description=None,
#                 handoffs=[
#                     Agent(
#                         name='hinglish_agent',
#                         instructions='you are a hinglish_agent, you answer user query in hinglish.',
#                         prompt=None,
#                         handoff_description=<function des at 0x000001F35A968720>,
#                         handoffs=[],
#                         model=None,
#                         model_settings=ModelSettings(
#                             temperature=None,
#                             top_p=None,
#                             frequency_penalty=None,
#                             presence_penalty=None,
#                             tool_choice=None,
#                             parallel_tool_calls=None,
#                             truncation=None,
#                             max_tokens=None,
#                             reasoning=None,
#                             metadata=None,
#                             store=None,
#                             include_usage=None,
#                             response_include=None,
#                             extra_query=None,
#                             extra_body=None,
#                             extra_headers=None,
#                             extra_args=None
#                         ),
#                         tools=[],
#                         mcp_servers=[],
#                         mcp_config={},
#                         input_guardrails=[],
#                         output_guardrails=[],
#                         output_type=None,
#                         hooks=None,
#                         tool_use_behavior='run_llm_again',
#                         reset_tool_choice=True
#                     )
#                 ],
#                 model='gpt-4.1-mini',
#                 model_settings=ModelSettings(
#                     temperature=None,
#                     top_p=None,
#                     frequency_penalty=None,
#                     presence_penalty=None,
#                     tool_choice=None,
#                     parallel_tool_calls=None,
#                     truncation=None,
#                     max_tokens=None,
#                     reasoning=None,
#                     metadata=None,
#                     store=None,
#                     include_usage=None,
#                     response_include=None,
#                     extra_query=None,
#                     extra_body=None,
#                     extra_headers=None,
#                     extra_args=None
#                 ),
#                 tools=[],
#                 mcp_servers=[],
#                 mcp_config={},
#                 input_guardrails=[],
#                 output_guardrails=[],
#                 output_type=None,
#                 hooks=None,
#                 tool_use_behavior='run_llm_again',
#                 reset_tool_choice=True
#             ),
#             raw_item=ResponseFunctionToolCall(
#                 arguments='{}',
#                 call_id='call_FgynLAIn4MNnP30K8trnJrJj',
#                 name='transfer_to_hinglish_agent',
#                 type='function_call',
#                 id='fc_686ac452a8948198825e631eface706703f9bb8bed340ee9',
#                 status='completed'
#             ),
#             type='handoff_call_item'
#         ),
#         HandoffOutputItem(
#             agent=Agent(
#                 name='triage_agent',
#                 instructions='you are a helpful assistant',
#                 prompt=None,
#                 handoff_description=None,
#                 handoffs=[
#                     Agent(
#                         name='hinglish_agent',
#                         instructions='you are a hinglish_agent, you answer user query in hinglish.',
#                         prompt=None,
#                         handoff_description=<function des at 0x000001F35A968720>,
#                         handoffs=[],
#                         model=None,
#                         model_settings=ModelSettings(
#                             temperature=None,
#                             top_p=None,
#                             frequency_penalty=None,
#                             presence_penalty=None,
#                             tool_choice=None,
#                             parallel_tool_calls=None,
#                             truncation=None,
#                             max_tokens=None,
#                             reasoning=None,
#                             metadata=None,
#                             store=None,
#                             include_usage=None,
#                             response_include=None,
#                             extra_query=None,
#                             extra_body=None,
#                             extra_headers=None,
#                             extra_args=None
#                         ),
#                         tools=[],
#                         mcp_servers=[],
#                         mcp_config={},
#                         input_guardrails=[],
#                         output_guardrails=[],
#                         output_type=None,
#                         hooks=None,
#                         tool_use_behavior='run_llm_again',
#                         reset_tool_choice=True
#                     )
#                 ],
#                 model='gpt-4.1-mini',
#                 model_settings=ModelSettings(
#                     temperature=None,
#                     top_p=None,
#                     frequency_penalty=None,
#                     presence_penalty=None,
#                     tool_choice=None,
#                     parallel_tool_calls=None,
#                     truncation=None,
#                     max_tokens=None,
#                     reasoning=None,
#                     metadata=None,
#                     store=None,
#                     include_usage=None,
#                     response_include=None,
#                     extra_query=None,
#                     extra_body=None,
#                     extra_headers=None,
#                     extra_args=None
#                 ),
#                 tools=[],
#                 mcp_servers=[],
#                 mcp_config={},
#                 input_guardrails=[],
#                 output_guardrails=[],
#                 output_type=None,
#                 hooks=None,
#                 tool_use_behavior='run_llm_again',
#                 reset_tool_choice=True
#             ),
#             raw_item={'call_id': 'call_FgynLAIn4MNnP30K8trnJrJj', 'output': '{"assistant": "hinglish_agent"}', 'type': 'function_call_output'},
#             source_agent=Agent(
#                 name='triage_agent',
#                 instructions='you are a helpful assistant',
#                 prompt=None,
#                 handoff_description=None,
#                 handoffs=[
#                     Agent(
#                         name='hinglish_agent',
#                         instructions='you are a hinglish_agent, you answer user query in hinglish.',
#                         prompt=None,
#                         handoff_description=<function des at 0x000001F35A968720>,
#                         handoffs=[],
#                         model=None,
#                         model_settings=ModelSettings(
#                             temperature=None,
#                             top_p=None,
#                             frequency_penalty=None,
#                             presence_penalty=None,
#                             tool_choice=None,
#                             parallel_tool_calls=None,
#                             truncation=None,
#                             max_tokens=None,
#                             reasoning=None,
#                             metadata=None,
#                             store=None,
#                             include_usage=None,
#                             response_include=None,
#                             extra_query=None,
#                             extra_body=None,
#                             extra_headers=None,
#                             extra_args=None
#                         ),
#                         tools=[],
#                         mcp_servers=[],
#                         mcp_config={},
#                         input_guardrails=[],
#                         output_guardrails=[],
#                         output_type=None,
#                         hooks=None,
#                         tool_use_behavior='run_llm_again',
#                         reset_tool_choice=True
#                     )
#                 ],
#                 model='gpt-4.1-mini',
#                 model_settings=ModelSettings(
#                     temperature=None,
#                     top_p=None,
#                     frequency_penalty=None,
#                     presence_penalty=None,
#                     tool_choice=None,
#                     parallel_tool_calls=None,
#                     truncation=None,
#                     max_tokens=None,
#                     reasoning=None,
#                     metadata=None,
#                     store=None,
#                     include_usage=None,
#                     response_include=None,
#                     extra_query=None,
#                     extra_body=None,
#                     extra_headers=None,
#                     extra_args=None
#                 ),
#                 tools=[],
#                 mcp_servers=[],
#                 mcp_config={},
#                 input_guardrails=[],
#                 output_guardrails=[],
#                 output_type=None,
#                 hooks=None,
#                 tool_use_behavior='run_llm_again',
#                 reset_tool_choice=True
#             ),
#             target_agent=Agent(
#                 name='hinglish_agent',
#                 instructions='you are a hinglish_agent, you answer user query in hinglish.',
#                 prompt=None,
#                 handoff_description=<function des at 0x000001F35A968720>,
#                 handoffs=[],
#                 model=None,
#                 model_settings=ModelSettings(
#                     temperature=None,
#                     top_p=None,
#                     frequency_penalty=None,
#                     presence_penalty=None,
#                     tool_choice=None,
#                     parallel_tool_calls=None,
#                     truncation=None,
#                     max_tokens=None,
#                     reasoning=None,
#                     metadata=None,
#                     store=None,
#                     include_usage=None,
#                     response_include=None,
#                     extra_query=None,
#                     extra_body=None,
#                     extra_headers=None,
#                     extra_args=None
#                 ),
#                 tools=[],
#                 mcp_servers=[],
#                 mcp_config={},
#                 input_guardrails=[],
#                 output_guardrails=[],
#                 output_type=None,
#                 hooks=None,
#                 tool_use_behavior='run_llm_again',
#                 reset_tool_choice=True
#             ),
#             type='handoff_output_item'
#         ),
#         MessageOutputItem(
#             agent=Agent(
#                 name='hinglish_agent',
#                 instructions='you are a hinglish_agent, you answer user query in hinglish.',
#                 prompt=None,
#                 handoff_description=<function des at 0x000001F35A968720>,
#                 handoffs=[],
#                 model=None,
#                 model_settings=ModelSettings(
#                     temperature=None,
#                     top_p=None,
#                     frequency_penalty=None,
#                     presence_penalty=None,
#                     tool_choice=None,
#                     parallel_tool_calls=None,
#                     truncation=None,
#                     max_tokens=None,
#                     reasoning=None,
#                     metadata=None,
#                     store=None,
#                     include_usage=None,
#                     response_include=None,
#                     extra_query=None,
#                     extra_body=None,
#                     extra_headers=None,
#                     extra_args=None
#                 ),
#                 tools=[],
#                 mcp_servers=[],
#                 mcp_config={},
#                 input_guardrails=[],
#                 output_guardrails=[],
#                 output_type=None,
#                 hooks=None,
#                 tool_use_behavior='run_llm_again',
#                 reset_tool_choice=True
#             ),
#             raw_item=ResponseOutputMessage(
#                 id='msg_686ac453e7d48198a5953b0fa25ba19703f9bb8bed340ee9',
#                 content=[ResponseOutputText(annotations=[], text='Main theek hoon, aap kaise ho?', type='output_text', logprobs=[])],
#                 role='assistant',
#                 status='completed',
#                 type='message'
#             ),
#             type='message_output_item'
#         )
#     ],
#     raw_responses=[
#         ModelResponse(
#             output=[
#                 ResponseFunctionToolCall(
#                     arguments='{}',
#                     call_id='call_FgynLAIn4MNnP30K8trnJrJj',
#                     name='transfer_to_hinglish_agent',
#                     type='function_call',
#                     id='fc_686ac452a8948198825e631eface706703f9bb8bed340ee9',
#                     status='completed'
#                 )
#             ],
#             usage=Usage(
#                 requests=1,
#                 input_tokens=71,
#                 input_tokens_details=InputTokensDetails(cached_tokens=0),
#                 output_tokens=15,
#                 output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
#                 total_tokens=86
#             ),
#             response_id='resp_686ac451fab88198ab1bb1d860bd6f2403f9bb8bed340ee9'
#         ),
#         ModelResponse(
#             output=[
#                 ResponseOutputMessage(
#                     id='msg_686ac453e7d48198a5953b0fa25ba19703f9bb8bed340ee9',
#                     content=[ResponseOutputText(annotations=[], text='Main theek hoon, aap kaise ho?', type='output_text', logprobs=[])],
#                     role='assistant',
#                     status='completed',
#                     type='message'
#                 )
#             ],
#             usage=Usage(
#                 requests=1,
#                 input_tokens=66,
#                 input_tokens_details=InputTokensDetails(cached_tokens=0),
#                 output_tokens=13,
#                 output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
#                 total_tokens=79
#             ),
#             response_id='resp_686ac453755881989b63761642a4920f03f9bb8bed340ee9'
#         )
#     ],
#     final_output='Main theek hoon, aap kaise ho?',
#     input_guardrail_results=[],
#     output_guardrail_results=[],
#     context_wrapper=RunContextWrapper(
#         context=None,
#         usage=Usage(
#             requests=2,
#             input_tokens=137,
#             input_tokens_details=InputTokensDetails(cached_tokens=0),
#             output_tokens=28,
#             output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
#             total_tokens=165
#         )
#     ),
#     _last_agent=Agent(
#         name='hinglish_agent',
#         instructions='you are a hinglish_agent, you answer user query in hinglish.',
#         prompt=None,
#         handoff_description=<function des at 0x000001F35A968720>,
#         handoffs=[],
#         model=None,
#         model_settings=ModelSettings(
#             temperature=None,
#             top_p=None,
#             frequency_penalty=None,
#             presence_penalty=None,
#             tool_choice=None,
#             parallel_tool_calls=None,
#             truncation=None,
#             max_tokens=None,
#             reasoning=None,
#             metadata=None,
#             store=None,
#             include_usage=None,
#             response_include=None,
#             extra_query=None,
#             extra_body=None,
#             extra_headers=None,
#             extra_args=None
#         ),
#         tools=[],
#         mcp_servers=[],
#         mcp_config={},
#         input_guardrails=[],
#         output_guardrails=[],
#         output_type=None,
#         hooks=None,
#         tool_use_behavior='run_llm_again',
#         reset_tool_choice=True
#     )
# )
# Shutting down trace provider
# Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x000001F35E385400>
# Exported 4 items
# Exported 2 items