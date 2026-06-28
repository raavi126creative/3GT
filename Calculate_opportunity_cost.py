"""
Opportunity Cost Calculator for Delayed Logistics Payments

Formula Used:
Lost Opportunity Cost =
Invoice Amount × Annual Interest Rate × (Days Taken to Pay / 365)

Author: Your Name
"""

import os
import pandas as pd


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------
INTEREST_RATE = 0.12  # 12% annual simple interest
INPUT_FILE = "logistics_payments.csv"
OUTPUT_FILE = "logistics_payments_with_opportunity_cost.csv"


# ---------------------------------------------------------------------
# Dummy Data Generator
# ---------------------------------------------------------------------
def generate_dummy_data(filename):
    """Generate sample invoice data for testing."""

    data = {
        "Invoice_ID": [
            "INV001",
            "INV002",
            "INV003",
            "INV004",
            "INV005"
        ],
        "Invoice_Amount": [
            150000,
            250000,
            180000,
            320000,
            275000
        ],
        "Submission_Date": [
            "2025-01-01",
            "2025-01-10",
            "2025-02-01",
            "2025-02-15",
            "2025-03-01"
        ],
        "Payment_Received_Date": [
            "2025-01-31",
            "2025-02-25",
            "2025-03-15",
            "2025-04-20",
            "2025-05-05"
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Dummy data created: {filename}")


# ---------------------------------------------------------------------
# Load Data
# ---------------------------------------------------------------------
def load_data(filename):
    """Load invoice data from CSV."""

    df = pd.read_csv(filename)

    df["Submission_Date"] = pd.to_datetime(df["Submission_Date"])
    df["Payment_Received_Date"] = pd.to_datetime(
        df["Payment_Received_Date"]
    )

    return df


# ---------------------------------------------------------------------
# Calculate Metrics
# ---------------------------------------------------------------------
def calculate_metrics(df, annual_interest_rate):
    """Calculate payment duration and opportunity cost."""

    df["Days_Taken_to_Pay"] = (
        df["Payment_Received_Date"] -
        df["Submission_Date"]
    ).dt.days

    df["Lost_Opportunity_Cost"] = (
        df["Invoice_Amount"]
        * annual_interest_rate
        * df["Days_Taken_to_Pay"]
        / 365
    )

    return df


# ---------------------------------------------------------------------
# Summary Report
# ---------------------------------------------------------------------
def print_summary(df):
    """Print overall financial summary."""

    total_invoice_amount = df["Invoice_Amount"].sum()
    average_days = df["Days_Taken_to_Pay"].mean()
    total_opportunity_cost = df["Lost_Opportunity_Cost"].sum()

    print("\n" + "=" * 60)
    print("LOGISTICS PAYMENT OPPORTUNITY COST SUMMARY")
    print("=" * 60)

    print(f"Total Invoiced Amount        : ₹{total_invoice_amount:,.2f}")
    print(f"Average Days to Payment      : {average_days:.2f} days")
    print(f"Total Lost Opportunity Cost  : ₹{total_opportunity_cost:,.2f}")

    print("=" * 60)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():

    if not os.path.exists(INPUT_FILE):
        generate_dummy_data(INPUT_FILE)

    df = load_data(INPUT_FILE)

    df = calculate_metrics(df, INTEREST_RATE)

    df.to_csv(OUTPUT_FILE, index=False)

    print_summary(df)

    print("\nDetailed results:")
    print(df)

    print(f"\nProcessed data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
