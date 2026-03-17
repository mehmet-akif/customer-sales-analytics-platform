import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(PROCESSED_DIR, exist_ok=True)


def clean_customers():
    df = pd.read_csv(os.path.join(RAW_DIR, "customers_raw.csv"))

    df = df.drop_duplicates(subset=["customer_id"])
    df["email"] = df["email"].fillna("unknown@example.com")
    df["full_name"] = df["full_name"].str.strip()
    df["country"] = df["country"].str.strip()
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

    df.to_csv(os.path.join(PROCESSED_DIR, "customers_clean.csv"), index=False)
    print("customers_clean.csv created")


def clean_orders():
    df = pd.read_csv(os.path.join(RAW_DIR, "orders_raw.csv"))

    df["amount"] = df["amount"].fillna(df["amount"].median())
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["product_category"] = df["product_category"].str.strip()
    df["payment_method"] = df["payment_method"].str.strip()

    df.to_csv(os.path.join(PROCESSED_DIR, "orders_clean.csv"), index=False)
    print("orders_clean.csv created")


def clean_campaigns():
    df = pd.read_csv(os.path.join(RAW_DIR, "marketing_campaigns_raw.csv"))

    df["campaign_date"] = pd.to_datetime(df["campaign_date"], errors="coerce")
    df["channel"] = df["channel"].str.strip()

    df.to_csv(os.path.join(PROCESSED_DIR, "marketing_campaigns_clean.csv"), index=False)
    print("marketing_campaigns_clean.csv created")


def clean_tickets():
    df = pd.read_csv(os.path.join(RAW_DIR, "support_tickets_raw.csv"))

    df["ticket_date"] = pd.to_datetime(df["ticket_date"], errors="coerce")
    df["issue_type"] = df["issue_type"].str.strip()

    df.to_csv(os.path.join(PROCESSED_DIR, "support_tickets_clean.csv"), index=False)
    print("support_tickets_clean.csv created")


if __name__ == "__main__":
    clean_customers()
    clean_orders()
    clean_campaigns()
    clean_tickets()
    print("All datasets cleaned successfully.")