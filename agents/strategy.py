
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_strategy(enriched_lead):
    prompt = f"""
    You are a B2B sales strategist.
    Create a 3-step drip campaign for this lead:
    {enriched_lead}
    """

    resp = client.chat.completions.create(
        model="gpt-5.3",
        messages=[{"role": "user", "content": prompt}]
    )

    return resp.choices[0].message.content
