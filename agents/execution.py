
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_email(strategy_text, lead):
    prompt = f"""
    Write a personalized B2B email based on:
    Strategy: {strategy_text}
    Lead: {lead}
    """

    resp = client.chat.completions.create(
        model="gpt-5.3",
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message.content

def send_email(email_content, to_email):
    # placeholder for email sending API
    print(f"Sending email to {to_email}...")
    print(email_content)
