>1. jab ham koi project bnaty hain streamlit ya koi next.js ka to jab ham usy kisi ko dikhany ke liye github pe
   push karte hain to wahn par hmare Next.js project ke andar (Node modules) package wali file upload nahi hoti
   isi tarh streamlit ki bhi (.env) vertual envoirment ki file upload nahi hoti to uske liye ham github se project
   clone karne ke bad dubara se Node module file or or .env file install karte hain taky project chala saken.
   lekin kya ho agr ham (node module) file or (.env) file ko project ke sath upload kar den or samny walay ko project
   clone karne ke bad inki installation na karni pare.
   iske liye ham apne pore project folder ko code or packages ke sath aik container bana akr upload kar dety hain
   or jisko dekhna hota hai wo usy clone kar ke dekh sakya hai without installation.   

>2. project folder ko ham package container bana kar (dockerhub) par upload kar denge or jise wo project chahiye usy
   ham link denge to wo banda link ke zariye installation karenge to wo pora project wala container usy mil jaega all packages ke sath chalta hua. 

>3. is container ki ham multiple copy bana kar alag alag servers pe bhi upload kar sakty hain taky jitna zada    
   treafic aye manage ho jaye or agr trafic km ho to sary servers off ho jaen chalty na rehn.

>4. kuberntes hi wo cheez hai jo zada trafic pe hmari website ke liye zada servers on kart hai or jab trafic km   
   ho to unko off kar deta hai matlab jitni traffic uske hisab se srvers ka use     
   kuberntes ka aik unit hai pod jiska kaam hai hmare container ko manage karna is pod ke andar hi container ko rakhty hain traffic zada any pr kuberntes zada pods create kar deti hai or agr traffic km hai to extra pods ko hata deti hai
   container ke andar moujod project ko chlany ke liye internet or hardware provide karta hai ye pod.

>5. pod ke andar rakhy container mein moujod jo project hai agr wo koi external activity perform kar rha hai yani ke
   bahar kisi server par rakhy database mein moujod cheezen lana bhjena to is cheez ke liye ham aik or chora sa container bnaty hain jo ye bahar ke sary kaam dekhta hai jiska naam hai (Dapr-Side-Container) 

>6. Ab swal ye hai ke (Dapr-Side-Container) ko kesy pata ke konse database meins e data ko lana hai isliye ham   
   Container ke andar .ymal ki file likhty hain ye file Dapr ko btati hai ke data kahn se bhaga ke lana hai
   ye jitni bhi cheezen ho rhi hain in sab ko pod sambhalta hai.

>7. Container jo hai wo docker bhi chlata hai or rencher bhi chlata hai inke opar hoga (Dapr-Side-Container) or 
   is Dapr container ko (Kubernetes) chlata hai or ye jo hmare project ke sath bany huy conatiner hain 
   wo (Azure Coatainer) server par rakhy hoty hain ya kisi or pe jese (AWS), (Google cloud runner) ke opar. or jo servers hamen kubernetes ki support provide karty hain unke opar.   



#                                  Use OpenRouter With OpenAI Agents SDK   

>OpenRouter LLMs Provide karta hai or Agent-SDK framework hai agent bnany ka or ab ham dono ke aik sath use karenge.

1. uv init 
2. uv run main.py
3. Create .env and make variable => OPENROUTER_API_KEY=your_openrouter_api_key
4. write code in main.py
5. install => uv add python-dotenv
6. create => env_example => OPENROUTER_API_KEY=  => kisi ko btane ke liye ke is file mein API key ke variable ka   
   naam hai.
7. install for making agents => uv add openai-agents
8. uv run main.py

9. Ye bhi OpenRouter ki tarhn LLM provider hai => LiteLLM Agent SDK with Google Gemini
10. Create app.py file for another agent => copy same agent code and make changes.
11. Go to => Google AI studio get GEmini API key => AIzaSyC7VFY39k_6VxR_ZMod1NZonn4G8A2Q9Fk
12. 2no agents aik hi folder mein error denge => uv remove openai-agents
13. intsallation => uv add "openai-agents[litellm]" 
14. if get error run this => $Env:PYTHONUTF8 = '1'; python -X utf8 app.py 
