# Inventory Management System (Demo)

This is a simplified implementation of the given case study.

## Tech Stack
- FastAPI
- In-memory storage (no real DB)

## Assumptions
- Data is stored in memory for demonstration
- No authentication implemented
- Single warehouse supported per request
- Threshold is fixed for simplicity

## Why In-Memory?
The goal is to demonstrate business logic and API structure,
not production persistence.

## How to Run
pip install -r requirements.txt
uvicorn main:app --reload
