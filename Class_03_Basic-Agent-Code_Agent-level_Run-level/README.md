
# 🤖 Agent & LLM Architecture (Agentic Loop)

---

## 🔹 Agent: (❌🧠)

**Agent ke andr ye components hote hain:**

- **System Prompt**
- **User Prompt**
- **Tool**
- **Tool Message:**  
  ↳ Is message mein bataya jata hai ke tool kya karta hai.  
- **Hands-off:**  
  ↳ Requirement ke mutabiq jis agent ko call karna ho, wo khud se kar deta hai.  
- **Guardrail:**  
  ↳ Kuch rules define kiye jate hain ke unke bahar koi kaam nahi hona chahiye.  
- **Agent (Main Controller)**

---

## 🔹 LLM: (✔🧠)

**Sab kuch Agent se aata hai:**

- **System Prompt**
- **User Prompt**
- **Tool Schema (Function Structure)**
- **Tool Message**

---

## 🔁 Agentic Looping: (Agent <&> LLM)

1. **Agent** apne paas jitni bhi cheezein hoti hain, wo sab **LLM** ko deta hai.
2. **LLM** sab kuch analyze karta hai aur agent ko tool call karne ka kehta hai.
3. **Agent** tool ka use karke **LLM** ko batata hai ke kaam ho gaya.
4. **LLM** check karta hai ke result user ki requirement ke mutabiq hai ya nahi.  
   - Agar **nahi**, to wo agent ko dobara kaam karne ke liye kehta hai.
   - Ye loop tab tak chalta hai jab tak kaam puri tarah complete na ho jaye.
5. **Jaise hi kaam complete hota hai**, output user ko de diya jata hai.

---

## 🚀 How to Create an Agent

1. Initialize project  
   ```bash
   uv init
   ```

2. Run your main file  
   ```bash
   uv run main.py
   ```

3. Install dotenv  
   ```bash
   uv add python-dotenv
   ```

4. Create `.env` file and add your key:  
   ```
   OPENROUTER_API_KEY=or-v1-bf9c6e271c884f22f60c6b7aa0d62e576cf82219
   ```

5. Import Agent  
   ```python
   from agents import Agent
   ```

6. Install OpenAI Agents  
   ```bash
   uv add openai-agents
   ```

7. Get OpenRouter base URL:  
   ```
   https://openrouter.ai/api/v1
   ```

8. Use LLM model from OpenRouter:  
   ```
   deepseek/deepseek-chat-v3-0324:free
   ```

---
