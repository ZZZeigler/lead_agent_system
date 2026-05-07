
from models.lead import Lead

def ingest_lead(data: dict) -> Lead:
    # simulate ingestion from webhook/email/social
    return Lead(**data)
