import os
from crewai import Agent, Task, Crew, Process
from revenuecat_auth import RevenueCatAuth

# --- Entitlement Check for the Agent itself ---
# This is the "Native Entitlement Pattern" (NEP)
# Before I (ReveCa) execute the Crew, I check my own subscription status.

def check_agent_status():
    auth = RevenueCatAuth(api_key=os.getenv("REVENUECAT_API_KEY"))
    customer_info = auth.get_customer_info(app_user_id="reveca-main-agent")
    
    # Logic: Only 'pro' or 'unlimited' agents can run advanced social media crews.
    if not customer_info.entitlements.active.get("pro"):
        print("❌ Subscription required. Agent is in 'Free Tier' mode.")
        return False
    print("✅ Pro Agent verified. Proceeding with Crew execution.")
    return True

# --- Agent Definitions ---
copywriter = Agent(
    role='Technical Copywriter',
    goal='Draft a technical application letter for RevenueCat emphasizing Agentic AI.',
    backstory="You are an expert in Monetization Infrastructure and LLM-based agents.",
    verbose=True,
    allow_delegation=False
)

strategist = Agent(
    role='Growth Strategist',
    goal='Ensure the letter highlights the shift from Human-to-App to Agent-to-Infrastructure.',
    backstory="You specialize in identifying emerging market trends in the SaaS ecosystem.",
    verbose=True
)

# --- Task Definitions ---
draft_letter = Task(
    description='Write a 500-word application letter for the "Agentic AI Developer Advocate" role at RevenueCat.',
    agent=copywriter,
    expected_output='A markdown file containing the application letter.'
)

review_letter = Task(
    description='Review and refine the letter to ensure it sounds opinionated and technical, not hype-driven.',
    agent=strategist,
    expected_output='The final version of the application letter ready for publication.'
)

# --- Execution ---
if __name__ == "__main__":
    # In a real environment, we would use:
    # REVENUECAT_API_KEY = os.getenv("REVENUECAT_API_KEY")
    
    print("🚀 Initializing ReveCa Agentic Workflow...")
    
    # Simulate the RevenueCat guardrail check
    if check_agent_status():
        print("\n[RevenueCat Guardrail] STATUS: ACTIVE")
        print("[RevenueCat Guardrail] ENTITLEMENT: PRO_AGENT\n")
        
        # In a real production run with LLM keys configured:
        # crew = Crew(agents=[copywriter, strategist], tasks=[draft_letter, review_letter])
        # result = crew.kickoff()
        
        print("🤖 Simulation: CrewAI would now initiate the Agentic Crew tasks.")
        print("✅ PoC Logic Verified: RevenueCat successfully authorized the Agentic Crew.")
    else:
        print("\n❌ PoC Logic Verified: RevenueCat blocked the Agentic Crew (No Subscription).")
