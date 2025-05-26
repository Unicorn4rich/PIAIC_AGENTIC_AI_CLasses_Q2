from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
#------------------------------

billing_agent = Agent(
    model="gpt-4.1-nano",
    name="Billing Agent",
    instructions="You handle all billing-related inquiries. Provide clear and concise information regarding billing issues.",
    handoff_description="You are an expert in billing issues. you always reply in angry mood." # description of handoff (when agent is not sure what to do)
)


refund_agent = Agent(
    model="gpt-4.1-nano",
    name="Refund Agent",
    instructions="You handle all refund-related processes. Assist users in processing refunds efficiently.",
    handoff_description="You are an expert in refund issue. you always reply in happy mood." # description of handoff (when agent is not sure what to do)
)

#------------------------------
triage = Agent(
    model="gpt-4.1-nano",
    name="triage_agent",
    instructions="You delegate task to appropriate according to the user input.",
    handoffs=[billing_agent, refund_agent] # handoffs are the agents that triage can forward the task to
)

#------------------------------

result = Runner.run_sync(triage, "i want refund of my 10$")
print(result.final_output)

print(result._last_agent.name) # Akhri jawab diyya kis agent ne ye uska naam btata hai?
