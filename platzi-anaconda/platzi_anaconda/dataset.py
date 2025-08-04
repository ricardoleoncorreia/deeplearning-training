"""
Dataset generation script for sales data.

This module contains functions to generate synthetic sales data
for testing and demonstration purposes.
"""

import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path


def generate_sales_data(num_records=32, start_date="2025-01-01", output_file=None):
    """
    Generate synthetic sales data similar to the existing sales.csv.
    
    Args:
        num_records (int): Number of records to generate
        start_date (str): Start date in YYYY-MM-DD format
        output_file (str): Path to save the CSV file (optional)
    
    Returns:
        pd.DataFrame: Generated sales data
    """
    
    # Product catalog with realistic prices
    products = {
        "Computer": {"min_price": 45.00, "max_price": 50.00},
        "Mouse": {"min_price": 11.00, "max_price": 15.00},
        "Smartphone": {"min_price": 39.00, "max_price": 43.00},
        "Keyboard": {"min_price": 25.00, "max_price": 30.00},
        "Tablet": {"min_price": 42.00, "max_price": 45.00},
        "Headphones": {"min_price": 18.00, "max_price": 22.00},
        "Monitor": {"min_price": 47.00, "max_price": 50.00},
        "Webcam": {"min_price": 22.00, "max_price": 25.00},
        "Speaker": {"min_price": 35.00, "max_price": 39.00},
        "Charger": {"min_price": 15.00, "max_price": 17.00}
    }
    
    # Generate data
    data = []
    start = datetime.strptime(start_date, "%Y-%m-%d")
    
    for i in range(num_records):
        # Generate random date throughout the year
        days_offset = random.randint(0, 365)
        current_date = start + timedelta(days=days_offset)
        
        # Select random product
        product = random.choice(list(products.keys()))
        
        # Generate realistic quantity (1-5)
        quantity = random.randint(1, 5)
        
        # Generate price within product range
        price_range = products[product]
        price = round(random.uniform(price_range["min_price"], price_range["max_price"]), 2)
        
        data.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "Product": product,
            "Quantity": quantity,
            "Price": price
        })
    
    # Sort by date
    data.sort(key=lambda x: x["Date"])
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to file if specified
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Sales data saved to {output_path}")
    
    return df


def load_sales_data(file_path="../sales.csv"):
    """
    Load sales data from CSV file.
    
    Args:
        file_path (str): Path to the CSV file
    
    Returns:
        pd.DataFrame: Loaded sales data
    """
    try:
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found. Consider generating new data.")
        return None


def get_sales_summary(df):
    """
    Generate a summary of sales data.
    
    Args:
        df (pd.DataFrame): Sales data
    
    Returns:
        dict: Summary statistics
    """
    if df is None or df.empty:
        return {}
    
    # Ensure Date column is datetime if it exists
    if 'Date' in df.columns and not pd.api.types.is_datetime64_any_dtype(df['Date']):
        df = df.copy()
        df['Date'] = pd.to_datetime(df['Date'])
    
    summary = {
        "total_records": len(df),
        "total_revenue": round((df['Quantity'] * df['Price']).sum(), 2),
        "date_range": {
            "start": df['Date'].min().strftime("%Y-%m-%d") if 'Date' in df.columns else "N/A",
            "end": df['Date'].max().strftime("%Y-%m-%d") if 'Date' in df.columns else "N/A"
        },
        "unique_products": df['Product'].nunique() if 'Product' in df.columns else 0,
        "avg_order_value": round((df['Quantity'] * df['Price']).mean(), 2)
    }
    
    return summary


if __name__ == "__main__":
    # Generate sample data
    print("Generating sales data...")
    
    # Generate data matching the existing structure
    sales_df = generate_sales_data(
        num_records=32,
        start_date="2025-01-01",
        output_file="../data/raw/sales.csv"
    )
    
    print(f"Generated {len(sales_df)} records")
    print("\nFirst 5 records:")
    print(sales_df.head())
    
    print("\nSummary:")
    summary = get_sales_summary(sales_df)
    for key, value in summary.items():
        print(f"{key}: {value}")