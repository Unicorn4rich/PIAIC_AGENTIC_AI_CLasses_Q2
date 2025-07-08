User Prompt      -> user query
System Prompt    -> agent persona
Tools            -> handoffs/as_tools/function_tool
Tool_description -> tool call se aya return


1. Swarm ke andar just gpt ke models laga sakty thy but SDK mein GEMINI or baqi models bhi laga sakty hain
   Agent SDK upgraded version hai swarm ka.

2. Aik Agent jab koi kaam dosry agent ko handsoff karta hai to uski pori conversation history bhi dosry agent
   ko jati hai taky usy pata chaly ke kya baat hui thi or kya chahiye user ko.

3. Main Agent jab dosry agent ko handsoff dega to us agent ka naam kya rakhega by-deault ->
   (transfer_to_)refund_agent.

4. Custom handoff() mein input_type laga kar next hansdoff agent ko jo input dena chahen wahi strucre pydantic
   se bana kar dey sakty hain.  (input_filter) next agent ko ham conversation mein se kuch cheezen filter kar ke dety hain jo uske kaam ki hain.   

5.  handoff_filters.remove_all_tools -> ye filter tool calls ko remove karta hai agly agent ko conversation 
    history deny se pehly.

6. input guardrails run in a multi-agent workflow -> sirf pehla agent input check karta hai user ka baqi 
   ke agent nahi karty.

7. guardrails -> agent ke sath paralel chalty hain matlab user ne kuch kaha runner agent ko us question ke
   jawab ke liye chala deta hai or same time guardrail bhi chal jata hai ke input jo aya hai user ka kya 
   wo sahi hai ya nahi ar sahi hai to agent jo apna kaam kar rha tha usy karne deta hai warna uska execution rok deta hai guradrail.

8. guardrail function kya return karta hai? -> ye return karta hai (GuardrailFunctionOutput) jo ke 
   OpenAI se import hoti hai ye class.

9. sandboxed environment?  -> Agent SDK ka CodeInterpreterTool

10. Top-K -> 100 words mein se 5 words select kar ke deta hai 
11. Top-P -> Un 5 words mein se aik word ko select karta hai
12. Temprature -> kam karenge to cretivity km hogi agr ziyada rakhenge to cretivity ziyada hoi 0 se 2 tak     
    kar sakty hain
13. Zero shot prompting
14. One shot promting  


Openai AgentHook Link -> https://github.com/openai/openai-agents-python/blob/main/examples/basic/agent_lifecycle_example.py

visit this repo for aent life scycle info


16. runner mein agent chalta hai or Agent mein sab se pehly on_start() ka method chalta hai ham usy customize
    kar ke usme mein RunContextWrapper laga kar usme se agent ka data get kar sakty hain jo jo wo kar rha hai.

17. AgentHook -> Aik Bank hai usme aik user aya usne apni id or query enter ki agent mein ab ham us id ko agent
    Agent mein jane se pehly CustomAgent class life sycle mein database call krwa ke us id se related data mangwa lenge database se or us hisab se user ko treat karenge.
    Ab agr ham aisa nahi karty to user id deta wo id agent jaa kar database mein check karta phir wahn se wapas
    ata or user ko treat karta is se hmare token bohut ziyada zaya honge. aik agent se dosry agent ko handsoff
    karte waqt bhi context ko update kar ke aagy bhej sakty hain. 

18. Same to Same RunnerHook bhi aisy hi kaam karta hai isme bhi sari cheezen Agent hook ki tarhn hoti hain 
    but ye RUnner mein pass kiyya jata hai.    

PIAIC Class

1. Agent ki Class LLM se kese baat karti hai kya kya propertys use hoti hain sab A-Z
2. Agent Propertys + Agent and LLM baat cheet + Streaming
3. Openai tracing support karta hai or -> Gemini tracing ko support nahi karta.


----------------------------------------------------------------------------------------------------
Agent SDK -> Experiment

1. name -> required hota hai or ye just string leta hai but agr 123 bhi den to ye chal jata hai or empty string bhi
   string bhi bhej sakty hain list bhi bhej sakty and also put None value but got soft warning not error.
   Gemini key se bane agent mein sirf name deny se agent nahi chalta balke name or model 2no cheezen provide karne se chalta hai but instruction ke bagher bhi chal jata hai.
   OpenAi ki (Key) se bnaye agent mein sirf name provide karne se agent chal jata hai.

2. instruction-> String + Callble function + by-default None
   dynamic function bana kar pass kar sakty hain. normal function bhi ley lega but return ho rha
   rha hoga to warna dynamic function mein hamen 2 parameter bhi pass karne parte hain wrapper or agent.
   isme ham string ki jagah number ya koi si bhi data type (list, dict) denge to wo bhi pass kar sakty hain but ye error nahi soft warning dega or hmara answer bhi dega.

3. model -> OpenAi ke agent mein Model paramter pass na karo to wo by-dfault OpenAi GPT-4o model ley leta hai.
   but dosry Model waly agents mein ye paramter pass karna zrori hota hai. 

4. Runner -> Runner RunResult return karta hai. 

5. Context -> LLM ko updated deta dena ya khud ka data dena jispe agent kaam karega.
   
6. name="My_Agent" -> "My_Agent"     <=+=>    instruction="You are a helpful assistant"  -> "You are a helpful assistant"
   Agent mein ham bagher variable ke bhi name or instruction dey sakty hain just string bana kar.   

7. custom_output_extractor: Callable[[RunResult], Awaitable[str]] | None = None
   iska matlab hai ke ham isme async function hi pass kar sakty hain ya by-default ye None lega.

8. context: RunContextWrapper[TContext]   
   (RunContextWrapper) -> ke andar hmara rakha hua context/data ata hai or (TContext) ka matlab hai Generic type matlab
   awami ke iske andar all data type ki values aa sakti hain (str, num, true/false, dict, pydantic, list, tuple etc). 
   ye har tarhn ki type ka data accept karta hai.
   (context) data sirf is parameter se bhi access kar sakty hain jabke (RunContextWrapper) run time pe values ki suggestion ke liye hota hai (TContext) kisi bhi datatype kki values lega. or agr isme am pydantic class ka naam dety
   hain to to wrappper mein sirf us pydantic class ki datatype ka data aega context sirf Runner mein pass hoga. 
   
9. usage: Usage = field(default_factory=Usage)
    isme hamary tokens ka records ata hai by-default isme tokens 0 hotay hain or ApenAI se ye tokens ka records laa kr
    hamen dikhata hai.  

10. agent.get_system_prompt -> ye method hi hmara instuction hota hai
    or iska getsystem_prompt terminal mein leny ka code class 17 mein hai

11. prompt={"id": "pmpt_jbj423vbr2h3verhdvwhdhvdh}
    ye prompt ki property ham agent mein set karte hain or ye jo prompt id hai ye hamne OpenAi ke dashboard pe prompt
    bana kar save karne ke bad hasil ki hai iska faida ye hai ke hmare token km zaya hoty hain agr prommpt wahn bana kar save kar len to.    

12. input_filter -> ye filter tool calls ko remove karta hai agly agent ko conversation history deny se pehly
    kiyun ke ham nahi chahty ke dosry handsoff waly agent ko jab conversation history mily or usme tool calls ka zikar
    ho or wo confuse ho jaye kiyun ke uske pass to woo tools honge nahi is se hamen answer unexpected mil sakta hai.

13. input_filter=handoff_filters.remove_all_tools -> ye filter tool calls ko remove karta hai agly agent k0   conversation history deny se pehly    

14. Turn Limit -> for example Agent ke pass (user prompt, system prompt, tools, tool_description, handsooff) ye sab hai
    User ne sirf ("hi kese ho") bola to agent sari cheezen ley kar LLM ke pass pohnch gaya or LLM ne is swal ka jawab foran dey diyya isko ham (1 Turn) kahenge.
    Agr User ne bola ke mujhe ("weather ke bare mein btao") to LLM ne dekha ke agent ke pass aik weather ka tools moujood 
    hai to usne agent ko kaha ke ye tool call karo or iska jo return jawab aye wo mere pass ley kar aao to isko ham 
    (2 Turn) kahenge kiyun ke Agent 2 dafa LLM ke pass gaya or aisy hi agr LLM ne 3sri dafa agent ko koi kaam kar ke uska
    return laany ka bla to ye (3 Turn) ho jaega.
    Notes -> Agr Agent ke pass 3 tools function moujoood hain or LLM ne dekha ke user ka jo question hai usme hamen 3eeno
    tool functions ko call karna parega to wo aik sath aik hi truen pe agent se wo tools call karwaega paralel mein aisy
    nahi ke aik Turn mein aik tool call krwaya or dosry Turn mein dosra or 3eesry Turn mein teesra.

15. tool_messages -> ye hamara agent ke pass jo tool function hota hai uska return hai.

16. handoff_description="A, B" -> 2 tarhn ki instruction leta hai aik hi prompt mein -> 
    (A) Wo kya karta hai. (B) -> Kab  isko chlana hai.
    ye jis agent mein lagaty hain us llm ke bare mein infoarmation deta hai ke ye karta kya hoga.

17. trace -> have multiple spans.
    hmara jo Runner agent se kaam krwa kar jawab deta hai usy trace kehty hain. but wo jo kaam complete krwata hai usme bohut sary kaam huy hoty hain matlab agent tools call karta hai or handoff karta hai to in sab ka aik aik span banta jata hai. ye sari cheezen ham verbose se dekh kar debug kar sakty hain.

18. LLM -> handoff ko nahi samjhta isliye hmara handoff wala agent bhi tool ki  shakal mein jata hai LLM ke pass. 

19. input_filter=handoff_filters.remove_all_tools -> ye import hota hai
    iska kaam ye hai ke conversation history mein tool call ki history or tool calls ka output wo sab khatam kar deta hai.

20. handoffs agents + as_tool agents
    in dono main faraq ye hai ke handoffs mein jab triage agent mein tool call hota hai to to dosra agent aa kar triage agent ki jagah sambhal leta hai matlab triage agent hatt jata hai or sara control us dosry handoffs kiyye gaye agent ke pass aa jata hai.
    lekin jab ham agent ko as_tool bana kar pass karte hain to jo hmara triage_agent hai sara control usi ke pass rehta hai baqi ke agent sara kaam kar ke usko laa kar dety hain.
    aik or main baat handoffs mein LLM jab tool call karne ke liye kehta hai to aik time mein sirf aik hi agent ko call kar sakty hain kiyun ke aik hatega to dosra aa kar uski jagah bethega.
    but agr ham agents ko as_tool bnaty hain to LLM aik sath sary as_tool agents ko paralal mein run karwa sakta hai aik sath.

21. is_enabled=False  -> isko False rakhny se ye handoff function ko ko aagy pass nahi karega matlab ye function bana hi  nahi aisy lagega matlan function On/Off -> by-default ye True hota hai matlab aagy pass hota hai.

22. input_filter -> ye streaming mein work nahi karta.
















----------------------------------------------------------------------------------------------------
Agent SDK -> Verbose showing agent llm working flow -> 1 turn flow

PSD:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_19_handoff_details_Code_2> uv run app.py -> run 
Creating trace Agent workflow with id trace_bd0b8b45b3a445d282e5f7def2cbafcf -> OpenAi dashboard pe ye Complete trace create hua hoga.
Setting current trace: trace_bd0b8b45b3a445d282e5f7def2cbafcf
Creating span <agents.tracing.span_data.AgentSpanData object at 0x000002C023B2BE80> with id None -> Agent span
Running agent triage_agent (turn 1)->Agent aik dafa apna sab kuch llm ke pass laya or llm ne response diyya ye 1 turn hai.
Creating span <agents.tracing.span_data.ResponseSpanData object at 0x000002C0223D3050> with id Non  e -> response span
Calling LLM gpt-4.1-mini with input: -> Agent LLm ko call kar ke keh rha hai ke 
[
  {
    "content": "hi", -> mere pass user ka question hai
    "role": "user"   -> user ne ye kaha hai
  }
]
Tools:  -> mere pass ye aik Agent bhi hai jisko ye tool bana kar llm ko dihaa rha hai.
[
  {
    "name": "transfer_to_customer_support", -> Agent tool name
    "parameters": {
      "additionalProperties": false,
      "type": "object",
      "properties": {},
      "required": []
    },
    "strict": true,
    "type": "function",
    "description": "Handoff to the customer_support agent to handle the request. "
  }
]
Stream: False  -> streaming nahi ho rhi.
Tool choice: NOT_GIVEN -> ye bhi nahi diyyya hamne
Response format: NOT_GIVEN -> ye bhi nahi diyyya hamne
Previous response id: None -> ye bhi nahi diyyya hamne

LLM resp:  -> Ab LLM ne wo sab cheezen dekh kar jo Agent ne di thi uske mutabik response create kar ke diyya hai.
[
  {
    "id": "msg_686bc057a8d4819aa4d0d3b98e78bb0e05cd14ab2ea7a09d", -> tracking id ye hai
    "content": [
      {
        "annotations": [],
        "text": "Hello! How can I assist you today?", -> ye answer hai jo LLM ne diyyya hai user ke question ka
        "type": "output_text",
        "logprobs": []
      }
    ],
    "role": "assistant",  -> ye jawab LLM ne diyya
    "status": "completed", -> Completed quesry
    "type": "message"
  }
]

Resetting current trace
Shutting down trace provider
Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x000002C0222B5400>
Exported 1 items
Exported 2 items
PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_19_handoff_details_Code_2>


----------------------------------------------------------------------------------------------------
Agent SDK -> Verbose showing agent llm working flow -> 2 turn flow


D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_19_handoff_details_Code_2> uv run app.py -> run
Creating trace Agent workflow with id trace_5fcc9a20465c4f02b5fdeea4fd6eae0b -> OpenAi dashboard pe ye Complete trace 
Setting current trace: trace_5fcc9a20465c4f02b5fdeea4fd6eae0b
Creating span <agents.tracing.span_data.AgentSpanData object at 0x000001A466BEC280> with id None -> Agent span
Running agent triage_agent (turn 1)
Creating span <agents.tracing.span_data.ResponseSpanData object at 0x000001A466BD2710> with id None -> response span
Calling LLM gpt-4.1-mini with input: => Agent LLm ko call kar ke keh rha hai ke 
[
  {
    "content": "call customer_support tool, i Need help", => mere pass user ka question hai
    "role": "user" -> user ne ye kaha hai
  }
]
Tools: => mere pass ye aik Agent bhi hai jisko ye tool bana kar llm ko dihaa rha hai.
[
  {
    "name": "transfer_to_customer_support", -> Agent tool name
    "parameters": {
      "additionalProperties": false,
      "type": "object",
      "properties": {},
      "required": []
    },
    "strict": true,
    "type": "function",
    "description": "Handoff to the customer_support agent to handle the request. "
  }
]
Stream: False  -> streaming nahi ho rhi.
Tool choice: NOT_GIVEN -> ye bhi nahi diyyya hamne
Response format: NOT_GIVEN -> ye bhi nahi diyyya hamne
Previous response id: None -> ye bhi nahi diyyya hamne

LLM resp: => LLM ne response diyya ke user ki query ke mutabik apke pass ye tool hai isko call karo or return la do mujhe.
[
  {
    "arguments": "{}",
    "call_id": "call_xvckE2WC2qrIBmHW9bkiw0KZ", -> calling id ye hai
    "name": "transfer_to_customer_support",  => jisko call karna hai wo ye agent tool hai
    "type": "function_call", => matlab isko call karo
    "id": "fc_686bc35478e4819abc566d4a08ba50030dbcfdaa9e60e06c",
    "status": "completed"
  }
]

Creating span <agents.tracing.span_data.HandoffSpanData object at 0x000001A466BD1950> with id None -> handoff span
Creating span <agents.tracing.span_data.AgentSpanData object at 0x000001A46714A5D0> with id None -> Agent span
Running agent customer_support (turn 2) => ab triage agent hatt gaya or uski jagah customer_support agent aa kar beth gaya
Creating span <agents.tracing.span_data.ResponseSpanData object at 0x000001A467117E90> with id None
Calling LLM gpt-4.1-mini with input: => customer_support agent llm ko call kar rha hai.
[
  {
    "content": "call customer_support tool, i Need help", -> wahi user ki quesry dikha rha hai
    "role": "user"
  },
  {   => ye object history wala object hai jab LLM ne triage agent ko tool agent call karne ko kaha tha or ye dubara hamen
      isliye show ho rha hai kiyunke handoff karty hi sari conversation history bhi dosry agent ko mil jati hai. 
    "arguments": "{}",
    "call_id": "call_xvckE2WC2qrIBmHW9bkiw0KZ",
    "name": "transfer_to_customer_support",
    "type": "function_call",
    "id": "fc_686bc35478e4819abc566d4a08ba50030dbcfdaa9e60e06c",
    "status": "completed"
  },
  {
    "call_id": "call_xvckE2WC2qrIBmHW9bkiw0KZ",
    "output": "{\"assistant\": \"customer_support\"}", => isko call karna hai wo ye agent tool hai
    "type": "function_call_output"
  }
]
Tools:  => is handoff agent ke pass koi tool nahi isliye ye khali hai.
[]
Stream: False
Tool choice: NOT_GIVEN
Response format: NOT_GIVEN
Previous response id: None

Exported 4 items
LLM resp:  => LLm ne response diyya handoff agent chlany ke bad.
[
  {
    "id": "msg_686bc35809ec819a980f66dcd93e2cde0dbcfdaa9e60e06c",
    "content": [
      {
        "annotations": [], => neechy line wala jawab llm ne diyya hai handoff agent ke return ke mutabik.
        "text": "I am transferring you to a customer support agent who will assist you further. Please hold on a moment.",
        "type": "output_text",
        "logprobs": []
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  }
]

Resetting current trace
Shutting down trace provider
Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x000001A465139400>
Exported 2 items
PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_CLasses_Q2\Class_19_handoff_details_Code_2> 





