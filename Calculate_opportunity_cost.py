```python
"""
===============================================================================
Project : 3GT: Logistics Liquidity Engine
Module  : calculate_opportunity_cost.py

Purpose:
--------
This module estimates the financial impact of delayed logistics invoice
payments by calculating:

1. Days Taken to Receive Payment
2. Lost Opportunity Cost (Simple Interest @ 12% p.a.)
3. Potential Capital Recovery if every invoice were paid within 15 days.

The report is designed for business presentations and pilot demonstrations.

Author : Your Name
Version: 1.0
===============================================================================
"""

import os
import pandas as pd


# =============================================================================
# CONFIGURATION
# =============================================================================

ANNUAL_INTEREST_RATE = 0.12      # 12% Annual Simple Interest
TARGET_PAYMENT_DAYS = 15         # Desired billing cycle

INPUT_FILE = "logistics_invoices.csv"
OUTPUT_FILE = "logistics_invoice_analysis.csv"


# =============================================================================
# DUMMY DATA GENERATOR
# =============================================================================

def generate_dummy_data(filename: str) -> None:
    """
    Creates sample logistics invoice data.

    This allows the module to run immediately without requiring
    an external CSV file.
    """

    sample_data = {
        "Invoice_ID": [
            "INV001",
            "INV002",
            "INV003",
            "INV004",
            "INV005",
            "INV006"
        ],

        "Invoice_Amount": [
            150000,
            225000,
            340000,
            175000,
            420000,
            260000
        ],

        "Submission_Date": [
            "2025-01-01",
            "2025-01-08",
            "2025-01-18",
            "2025-02-01",
            "2025-02-10",
            "2025-03-01"
        ],

        "Payment_Received_Date": [
            "2025-01-30",
            "2025-02-22",
            "2025-03-12",
            "2025-03-18",
            "2025-04-15",
            "2025-04-22"
        ]
    }

    pd.DataFrame(sample_data).to_csv(filename, index=False)

    print(f"Sample dataset created -> {filename}")


# =============================================================================
# DATA LOADING
# =============================================================================

def load_invoice_data(filename: str) -> pd.DataFrame:
    """
    Reads invoice information from CSV.

    Converts date columns into datetime objects for arithmetic.
    """

    df = pd.read_csv(filename)

    df["Submission_Date"] = pd.to_datetime(df["Submission_Date"])
    df["Payment_Received_Date"] = pd.to_datetime(
        df["Payment_Received_Date"]
    )

    return df


# =============================================================================
# CALCULATION ENGINE
# =============================================================================

def calculate_financial_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates:

    1. Actual payment duration
    2. Lost opportunity cost
    3. Potential capital recovery if payment is reduced to 15 days
    """

    # Number of days customer took to pay
    df["Days_Taken_to_Pay"] = (
        df["Payment_Received_Date"]
        - df["Submission_Date"]
    ).dt.days

    # Current opportunity cost
    df["Lost_Opportunity_Cost"] = (
        df["Invoice_Amount"]
        * ANNUAL_INTEREST_RATE
        * df["Days_Taken_to_Pay"]
        / 365
    )

    # Delay beyond target payment cycle
    df["Excess_Delay_Days"] = (
        df["Days_Taken_to_Pay"] - TARGET_PAYMENT_DAYS
    ).clip(lower=0)

    # Recoverable interest if delay is eliminated
    df["Potential_Capital_Recovery"] = (
        df["Invoice_Amount"]
        * ANNUAL_INTEREST_RATE
        * df["Excess_Delay_Days"]
        / 365
    )

    return df


# =============================================================================
# BUSINESS SUMMARY
# =============================================================================

def print_business_report(df: pd.DataFrame) -> None:
    """
    Prints a professional executive summary suitable for
    management presentations.
    """

    total_invoice = df["Invoice_Amount"].sum()

    average_cycle = df["Days_Taken_to_Pay"].mean()

    total_recovery = df["Potential_Capital_Recovery"].sum()

    total_opportunity = df["Lost_Opportunity_Cost"].sum()

    print("\n")
    print("=" * 78)
    print("                     3GT: LOGISTICS LIQUIDITY ENGINE")
    print("                FINANCIAL OPPORTUNITY ANALYSIS REPORT")
    print("=" * 78)

    print(f"{'Total Invoiced Amount':40} : ₹ {total_invoice:,.2f}")

    print(f"{'Average Billing Cycle Duration':40} : {average_cycle:.2f} Days")

    print(f"{'Total Lost Opportunity Cost':40} : ₹ {total_opportunity:,.2f}")

    print(
        f"{'Total Potential Capital Recovery':40} : ₹ {total_recovery:,.2f}"
    )

    print("-" * 78)

    print(
        "Business Insight:\n"
        "If invoice collections are consistently reduced to a "
        f"{TARGET_PAYMENT_DAYS}-day payment cycle, the organisation "
        "could potentially recover the above financing cost that is "
        "currently locked due to delayed customer payments."
    )

    print("=" * 78)
    print()


# =============================================================================
# EXPORT RESULTS
# =============================================================================

def export_results(df: pd.DataFrame, filename: str) -> None:
    """
    Saves the detailed invoice analysis to CSV.
    """

    df.to_csv(filename, index=False)

    print(f"Detailed analysis exported to: {filename}")


# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """
    Main execution workflow.
    """

    # Automatically create sample data for demonstration
    if not os.path.exists(INPUT_FILE):
        generate_dummy_data(INPUT_FILE)

    # Load invoice dataset
    invoices = load_invoice_data(INPUT_FILE)

    # Perform financial calculations
    invoices = calculate_financial_metrics(invoices)

    # Export detailed results
    export_results(invoices, OUTPUT_FILE)

    # Display executive summary
    print_business_report(invoices)


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
```
    
