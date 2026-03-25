import os
from groq import Groq

def analyze_log(log_text):
    try:
        print("➡️ Sending request to Groq...")

        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            print("❌ No API key")
            return {"error": "Missing API key"}

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[{"role": "user", "content": log_text}],
    timeout=10
)

        print("✅ Response received from Groq")

        return response.choices[0].message.content

    except Exception as e:
        print("❌ Groq error:", str(e))
        return {"error": str(e)}