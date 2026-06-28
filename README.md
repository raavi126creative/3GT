# 3GT: Logistics Liquidity Engine

## Project Overview
This module estimates the financial impact of delayed logistics invoice payments by calculating lost opportunity costs and potential capital recovery if payments are streamlined to a 15-day cycle.

## Project Structure
- `cost.py`: Core calculation engine.
- `requirements.txt`: Required Python dependencies.
- `logistics_invoices.csv`: Input data (format: Invoice_ID, Invoice_Amount, Submission_Date, Payment_Received_Date).

## Getting Started
1. Clone this repository.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the engine:
   `python cost.py`
   
