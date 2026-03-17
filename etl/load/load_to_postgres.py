import os
import pandas as pd
from sqlalchemy import text
from etl.utils.db_connection import engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")


def load_table(file_name, table_name):
    file_path = os.path.join(PROCESSED_DIR, file_name)
    df = pd.read_csv(file_path)

    with engine.connect() as connection:
        connection.execute(text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE"))
        connection.commit()

    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"{table_name} loaded successfully")


def main():
    load_table("customers_clean.csv", "customers")
    load_table("orders_clean.csv", "orders")
    load_table("marketing_campaigns_clean.csv", "marketing_campaigns")
    load_table("support_tickets_clean.csv", "support_tickets")


if __name__ == "__main__":
    main()