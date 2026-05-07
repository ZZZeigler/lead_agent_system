
from fastapi import FastAPI
from agents.listener import ingest_lead
from agents.enrichment import enrich_lead
from agents.strategy import generate_strategy
from agents.execution import generate_email, send_email

app = FastAPI()

@app.post("/lead")
def process_lead(data: dict):
    lead = ingest_lead(data)
    enriched = enrich_lead(lead)
    strategy = generate_strategy(enriched)
    email = generate_email(strategy, enriched)
    send_email(email, lead.email)

    return {
        "status": "processed",
        "strategy": strategy,
        "email_preview": email
    }
