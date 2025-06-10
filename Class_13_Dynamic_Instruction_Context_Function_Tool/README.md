1. Agent instruction ya to string leta hai ya phir dynamic function jo return kar rha hoga string.
2. guardrails in parallel => runner agent ke sath sath guardrails ko bhi chlata reta hai agr usy runnner mein pass 
   katy hain to.

3. What is the purpose of the RECOMMENDED_PROMPT_PREFIX in handoffs?
Ans. ye hmare diyye huy prompt ko enhance kar deta hai usy acha bana kar deta hai.

4. What is the role of the handoff_filters.remove_all_tools function?
Ans. jab handsof hota hai to pehla wala agent apni sari history utha kar dosry agent ko det deta hai ke ye meri 
     baat hui user se or sath sath system prompt intsutions function_tools sab utha kar dey deta hai dosry agent ko
     or agr koi aisa tool dosry agent ke pass chala gaya jo uskepass nahi to wo error dey dega. (remove_all_tools) iska use kar ke ham pichly agent ke sary tools ko remove kar ke new waly agent ko without tool wali history provide karty hain.

5. .to_input_list() => is list ke andar (role: user) or (role: asistant) sab ki conversation history aa rhi hoti 
    hai. or jo assitant hamen jawab dey rha hota hai wo usme id laga kar deta hai apne jawab mein 
    agr ham bhi user ko id dey den to multiple coversations thread ko control kar sakty hain.


-------------------------------------------------------------------------------------------------------------------
Context => building ki tunki jo har flat ko pani deti hai.

1. 