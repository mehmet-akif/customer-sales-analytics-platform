import os
import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(RAW_DIR, exist_ok=True)

NUM_CUSTOMERS = 1000
NUM_ORDERS = 5000
NUM_CAMPAIGNS = 2000
NUM_TICKETS = 1500

countries = ["Canada", "USA", "UK", "Germany", "France"]
product_categories = ["Electronics", "Home", "Fitness", "Books", "Clothing"]
payment_methods = ["Credit Card", "PayPal", "Debit Card"]
marketing_channels = ["Google Ads", "Facebook", "Email", "LinkedIn", "Referral"]
issue_types = ["Billing", "Shipping", "Login Problem", "Refund", "Product Issue"]


def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def create_customers():
    data = []

    start = datetime(2023, 1, 1)
    end = datetime(2025, 12, 31)

    for i in range(1, NUM_CUSTOMERS + 1):

        email = fake.email()

        if i % 120 == 0:
            email = None

        data.append({
            "customer_id": i,
            "full_name": fake.name(),
            "email": email,
            "country": random.choice(countries),
            "signup_date": random_date(start, end).date()
        })

    df = pd.DataFrame(data)

    df.to_csv(os.path.join(RAW_DIR, "customers_raw.csv"), index=False)

    print("customers_raw.csv created")


def create_orders():
    data = []

    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    for i in range(1, NUM_ORDERS + 1):

        amount = round(random.uniform(20, 1000), 2)

        if i % 200 == 0:
            amount = None

        data.append({
            "order_id": i,
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "order_date": random_date(start, end).date(),
            "product_category": random.choice(product_categories),
            "amount": amount,
            "payment_method": random.choice(payment_methods)
        })

    df = pd.DataFrame(data)

    df.to_csv(os.path.join(RAW_DIR, "orders_raw.csv"), index=False)

    print("orders_raw.csv created")


def create_campaigns():
    data = []

    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    for i in range(1, NUM_CAMPAIGNS + 1):

        data.append({
            "campaign_id": i,
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "channel": random.choice(marketing_channels),
            "campaign_date": random_date(start, end).date(),
            "campaign_cost": round(random.uniform(5, 200), 2)
        })

    df = pd.DataFrame(data)

    df.to_csv(os.path.join(RAW_DIR, "marketing_campaigns_raw.csv"), index=False)

    print("marketing_campaigns_raw.csv created")


def create_tickets():
    data = []

    start = datetime(2024, 1, 1)
    end = datetime(2025, 12, 31)

    for i in range(1, NUM_TICKETS + 1):

        resolution = round(random.uniform(1, 72), 1)

        data.append({
            "ticket_id": i,
            "customer_id": random.randint(1, NUM_CUSTOMERS),
            "ticket_date": random_date(start, end).date(),
            "issue_type": random.choice(issue_types),
            "resolution_hours": resolution,
            "satisfaction_score": random.randint(1, 5)
        })

    df = pd.DataFrame(data)

    df.to_csv(os.path.join(RAW_DIR, "support_tickets_raw.csv"), index=False)

    print("support_tickets_raw.csv created")


if __name__ == "__main__":

    create_customers()
    create_orders()
    create_campaigns()
    create_tickets()

    print("All raw datasets generated")
