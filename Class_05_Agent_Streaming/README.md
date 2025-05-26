1. uv init
2. uv run main.py
3. uv add python-dotenv
4. uv add openai-agents
5. write code
6. uv run main.py => run agent
7. Now we discuss events jo hamen run_streamed mein mily
   event: AgentUpdatedStreamEvent / RawResponsesStreamEvent / RunItemStreamEvent
   find event.type => in second RawResponsesStreamEvent => we find => raw_response_event

8. uv add chainlit
9. go to chainlit web for get hooks => API Reference => on_message => copy hook code in your main.py
   import chainlit as cl

   @cl.on_message
  def main(message: cl.Message):
    content = message.content
    # your code

10. active verual envoirment
11. chainlit run main.py -w => for run agent in chainlit => now code show in terimnial

12. on_chat_start => answer show in screen display decorater.