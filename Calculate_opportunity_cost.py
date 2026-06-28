import pandas as pd
import os

def calculate_liquidity():
    # Configuration
    ANNUAL_INTEREST_RATE = 0.12
    TARGET_PAYMENT_DAYS = 15
    INPUT_FILE = "logistics_invoices.csv"
    
    # Check if data exists
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    df = pd.read_csv(INPUT_FILE)
    
    # Date conversion
    df["Submission_Date"] = pd.to_datetime(df["Submission_Date"])
    df["Payment_Received_Date"] = pd.to_datetime(df["Payment_Received_Date"])

    # Calculations
    df["Days_Taken_to_Pay"] = (df["Payment_Received_Date"] - df["Submission_Date"]).dt.days
    df["Lost_Opportunity_Cost"] = df["Invoice_Amount"] * ANNUAL_INTEREST_RATE * df["Days_Taken_to_Pay"] / 365
    df["Excess_Delay_Days"] = (df["Days_Taken_to_Pay"] - TARGET_PAYMENT_DAYS).clip(lower=0)
    df["Potential_Capital_Recovery"] = df["Invoice_Amount"] * ANNUAL_INTEREST_RATE * df["Excess_Delay_Days"] / 365

    # Report
    print("3GT: LOGISTICS LIQUIDITY ENGINE - ANALYSIS COMPLETE")
    print(f"Total Opportunity Cost: {df['Lost_Opportunity_Cost'].sum():,.2f}")
    print(f"Potential Recovery: {df['Potential_Capital_Recovery'].sum():,.2f}")

if __name__ == "__main__":
    calculate_liquidity()
    
