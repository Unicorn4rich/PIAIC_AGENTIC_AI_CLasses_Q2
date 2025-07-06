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