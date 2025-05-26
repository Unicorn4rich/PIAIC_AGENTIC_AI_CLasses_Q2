# 🧠 Agent Setup Guide with OpenAI Tools

## ✅ 1. Agent Creation

After successfully creating your agent with all dependencies and code, you should see a success output.

---

## 🔧 2. Required Tools & OpenAI API Key

To use the following tools, you need to **buy an OpenAI API key**:

* **WebSearchTool**
  Fetches updated data from the internet, as LLMs do not have real-time information.

* **FileSearchTool**
  Allows the agent to explore locally uploaded files from your computer.

* **ComputerTool**
  *(Description missing – please update)*

👉 Get your OpenAI API key here: [https://platform.openai.com/usage](https://platform.openai.com/usage)

---

## 🎖️ 3. WebDev Arena Leaderboard

Visit the **WebDev Arena Leaderboard website** to see the rankings of the world’s best LLMs.

---

## 🌐 4. Create Vector Store on OpenAI

1. Go to: [https://platform.openai.com/storage](https://platform.openai.com/storage)
2. Switch to the **Vector Stores** tab
3. Click **Create**
4. Name your store (e.g., `shoaib_store`)

You have now successfully created a vector store. However, it is empty at this stage.

---

## 📂 5. Upload Files to Vector Store

1. Switch to the **Files** tab
2. Click **Upload File** (top right corner)
3. In the uploader text box:

   * Choose the file
   * Set the purpose to **assistant**
4. Wait until your file name appears in the box
5. Then click **Upload**

---

## 📊 6. Get File & Vector Store IDs

* From the **Files** tab, you can get the `file_id`
* From the **Vector Stores** tab, get the `vector_store_id`

💰 Pricing: If the data size is large (e.g., GBs), the cost is around `$0.1 per day`.

Example Vector Store ID: `vs_682f423617e08191988710059619d612`

---

## 📃 7. Attach Files to Agent Tool

1. Copy the Vector Store ID
2. Paste the ID when creating a tool in the agent

If you uploaded the **wrong file**:

* Delete it from the **Files** tab
* Go to **Vector Stores > Add File > Upload > Attach**
* Re-copy the new vector ID and paste it again

> **Note:** Always upload files from the **Vector Store** tab. In the **Files** tab, make sure the purpose is set to **assistant**.

---

## 🔢 8. Running the Code

Run your code and ask questions about the file. The agent will respond based on your uploaded data.

---

## 📈 9. OpenAI Pricing

Visit the official [OpenAI pricing page](https://openai.com/pricing) to check the cost for different LLMs.

---




-----------------------------------------------------------------------------------------------------------------------

1. After Create Successfully Agent with all dependencess and Code => Success Output

2. if you want to use theese tools then => buy OpenAi API key:
   . WebSearchToo    => Internet par jaa kar updated data search kar ke lata hai kiyun ke hmare LLM ke pass updated data nahi hota.
   . FileSearchTool  => hmare computer se upload ki hui local file ko explore karta hai.
   . ComputerTool    => 

3. WebDev Arena Leaderboard website => here worlds best LLM showing ranks 

4. Get OpenAi key => https://platform.openai.com/usage => Pay for key and get => OpenAi Key => benifit short code for create agent

5. platform.openai.com/storage => switch to => Vector stores => create => write store name like => shoaib_store

6. Now you successfully create vector store but it is empty => switch to => Files tab again => in top right => Upload File =>
   in text box of file uploader => select purpose => assistant

8. For upload drag/choose file => wait untill show your file name in text box of Vector then click upload 

9. File tab => you can get file_id => Vector stores => tou can get vector store id => agr GB ka data hai to itne pese changrge karega => $0.1 per day

10. Copy Vector ID => vs_682f423617e08191988710059619d612 => create tool in agent then => past this id

11. if wrong file uploaded => delete from File => and go to => Vectore store tab => Add file => Upload => Attach => again copt vextor id and past

12. Note => Always file upload from (Vector store) tab => in (File) tab => apki file ka purpose assistent hona chahiye. 

13. Run code and question about your given file CHat will response you about your data.

14. OpenAi pricing models website => check price of any OpenAi LLM
 