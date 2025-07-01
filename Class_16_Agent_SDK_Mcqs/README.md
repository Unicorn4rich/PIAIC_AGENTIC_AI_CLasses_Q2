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