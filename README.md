
# Intelligent Lead Automation Agent

## Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoint
POST /lead

Example:
{
  "name": "John",
  "email": "john@example.com",
  "company": "ABC Corp",
  "message": "Interested in your product"
}
