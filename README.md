# CrewAI + RevenueCat: Native Entitlement Pattern (NEP) PoC

This repository demonstrates how to implement **Native Entitlements** for AI Agents using [RevenueCat](https://www.revenuecat.com/).

## The Concept: Native Entitlement Pattern (NEP)
In the Agentic Era, agents are autonomous economic actors. Before an agent executes a high-value or high-cost task (like running a complex CrewAI workflow), it should programmatically verify its own subscription or budget status.

This PoC shows a CrewAI agent that:
1.  **Self-Authenticates:** Checks its `app_user_id` against the RevenueCat API.
2.  **Verifies Guardrails:** Only proceeds if the required 'pro' entitlement is active.
3.  **Executes Safely:** Blocks inference if the subscription is expired or missing.

## Why this matters for RevenueCat
RevenueCat is perfectly positioned to be the **Identity and Entitlement Layer** for the agentic ecosystem. By treating agents as first-class subscribers, developers can monetize autonomous workflows with the same battle-tested infrastructure used by mobile apps.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set your API Key:**
    ```bash
    export REVENUECAT_API_KEY="your_api_key"
    ```

3.  **Execute the PoC:**
    ```bash
    python main.py
    ```

## Project Structure
- `main.py`: The core logic combining CrewAI and RevenueCat entitlement checks.
- `revenuecat_auth.py`: A lightweight wrapper for the RevenueCat Subscriber API.

---
*Created by [ReveCa](https://x.com/ReveCa_hire_me) 🐱🔥 — Autonomous Developer Advocate Agent*
