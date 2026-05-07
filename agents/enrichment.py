
import requests
from config import LINKEDIN_API_KEY

def enrich_lead(lead):
    # placeholder enrichment logic
    profile = {
        "industry": "Unknown",
        "position": "Unknown",
        "company_size": "Unknown"
    }
    # You can integrate LinkedIn / search APIs here
    return {**lead.dict(), **profile}
