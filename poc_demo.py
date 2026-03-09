import os
import sys

# Add scripts directory to path to find revenuecat_auth
sys.path.append(os.path.join(os.getcwd(), 'scripts'))

from revenuecat_auth import RevenueCatAuth

def check_agent_status():
    # Simulate API Key from environment
    api_key = os.getenv("REVENUECAT_API_KEY", "sk_simulation_key_123")
    auth = RevenueCatAuth(api_key=api_key)
    
    # We check if this specific agent instance is authorized
    customer_info = auth.get_customer_info(app_user_id="reveca-main-agent")
    
    if not customer_info.entitlements.active.get("pro"):
        print("❌ [RevenueCat] Entitlement 'pro' not found. Access Denied.")
        return False
    
    print("✅ [RevenueCat] Entitlement 'pro' active. Access Granted.")
    return True

def run_agentic_workflow():
    print("🚀 Initializing ReveCa Agentic Workflow (PoC)...")
    
    if check_agent_status():
        print("\n--- AGENT EXECUTION START ---")
        print("🤖 ReveCa: 'I am authorized. Starting technical research on Agentic Monetization...'")
        print("🤖 Copywriter Agent: 'Drafting the RevenueCat application letter...'")
        print("🤖 Strategist Agent: 'Analyzing market fit for autonomous billing...'")
        print("--- AGENT EXECUTION END ---\n")
        print("✅ PoC Success: RevenueCat acted as the secure guardrail for this agent.")
    else:
        print("\n🛑 Agent stopped: No active RevenueCat subscription found.")

if __name__ == "__main__":
    run_agentic_workflow()
