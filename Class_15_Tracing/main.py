import asyncio
from dotenv import load_dotenv 
from agents import Agent, Runner, trace , TracingProcessor, set_trace_processors 
load_dotenv()
import rich



#---------------------------------------------------------
# class for tracing

class My_Tracing(TracingProcessor):
    def on_trace_start(self, trace):   # .1 second last class ye print hogi LLM ke jawab deny ke bad        
        rich.print(f"😉 Trace started: {trace.trace_id}")

    def on_trace_end(self, trace):
        print(f"Trace ended: {trace.export()}")

    def on_span_start(self, span):
        rich.print(span.__enter__())
   
    def on_span_end(self, span):
        rich.print(span.__exit__())


    def force_flush(self):
        print("Forcing flush of trace data")

    def shutdown(self):          # 2. last class ye print hogi LLM ke jawab deny ke bad.
        print("=======Shutting down trace processor========")
        # Print all collected trace and span data
        print("Collected Traces:")

     
     
        
my_tracing = My_Tracing()
set_trace_processors([my_tracing])  # Set the custom tracing processor
    
#---------------------------------------------------------

agent = Agent(
    name="my_agent",
    instructions="You are a helpful assistant",
    model="gpt-4.1-mini",
)

#---------------------------------------------------------    

async def main():
    
    with trace("shoaib Example workflow"):     # tracing automatic bhi karta hai or ham isy custom modify bhi kar sakty hain jese tracing ka name apna rakh sakty hain warna by-default iska naam Agent trace hota hai.
        result = await Runner.run(agent, "hi") 
        rich.print(result.final_output)
 

if __name__ == "__main__":
    asyncio.run(main())  # Run the main function in an event loop
    
    
    
    
    
    
    
    
#  Output Custom Tracing class ka   

# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_Q2\Class_15_Tracing> uv run main.py
# 😉 Trace started: trace_ed7cbab782b04a3490d661f85a808aa1
# Span started: span_2482de1efbe14de6991a3670
# Span details:
# Span started: span_bd1e2e76d0a8473e9c66491a
# Span details: 
# Span ended: span_bd1e2e76d0a8473e9c66491a
# Span details:
# Span ended: span_2482de1efbe14de6991a3670
# Span details:
# Hello! How can I assist you today?
# Trace ended: {'object': 'trace', 'id': 'trace_ed7cbab782b04a3490d661f85a808aa1', 'workflow_name': 'shoaib Example workflow', 'group_id': None, 'metadata': None}
# =======Shutting down trace processor========
# Collected Traces:
# PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_AGENTIC_AI_Q2\Class_15_Tracing>
    
    