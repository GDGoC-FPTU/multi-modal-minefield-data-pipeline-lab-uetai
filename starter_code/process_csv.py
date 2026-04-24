import pandas as pd

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Process sales records, handling type traps and duplicates.

def process_sales_csv(file_path):
    # --- FILE READING (Handled for students) ---
    df = pd.read_csv(file_path)
    # ------------------------------------------
    
    df = df.drop_duplicates(subset=['id'])
    
    documents = []
    for index, row in df.iterrows():
        # Clean 'price' column
        price_val = row['price']
        try:
            if pd.isna(price_val):
                price_float = 0.0
            elif isinstance(price_val, str):
                price_str = price_val.lower().replace('$', '').replace(',', '').strip()
                if price_str == 'five dollars':
                    price_float = 5.0
                elif price_str == 'n/a' or price_str == 'liên hệ' or price_str == 'null':
                    price_float = 0.0
                else:
                    price_float = float(price_str)
            else:
                price_float = float(price_val)
        except ValueError:
            price_float = 0.0

        # Normalize 'date_of_sale' into a single format (YYYY-MM-DD)
        try:
            date_obj = pd.to_datetime(row['date_of_sale'], format='mixed', dayfirst=False)
            date_iso = date_obj.isoformat()
        except Exception:
            try:
                date_obj = pd.to_datetime(row['date_of_sale'])
                date_iso = date_obj.isoformat()
            except Exception:
                date_iso = None

        doc_id = f"csv-{row['id']}"
        content = f"Product: {row['product_name']}, Category: {row['category']}, Price: {price_float}"
        
        doc = {
            "document_id": doc_id,
            "content": content,
            "source_type": "CSV",
            "author": str(row['seller_id']),
            "timestamp": date_iso,
            "source_metadata": {
                "original_price_str": str(row['price']),
                "price_float": price_float,
                "stock_quantity": row['stock_quantity'] if pd.notna(row['stock_quantity']) else 0
            }
        }
        documents.append(doc)
    
    return documents

