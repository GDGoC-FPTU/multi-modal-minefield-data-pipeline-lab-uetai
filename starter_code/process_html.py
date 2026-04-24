from bs4 import BeautifulSoup

from datetime import datetime

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Extract product data from the HTML table, ignoring boilerplate.

def parse_html_catalog(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    # ------------------------------------------
    
    table = soup.find('table', id='main-catalog')
    documents = []
    
    if table:
        tbody = table.find('tbody')
        if tbody:
            for row in tbody.find_all('tr'):
                cols = row.find_all('td')
                if len(cols) >= 6:
                    product_id = cols[0].text.strip()
                    name = cols[1].text.strip()
                    category = cols[2].text.strip()
                    price = cols[3].text.strip()
                    stock = cols[4].text.strip()
                    rating = cols[5].text.strip()
                    
                    if price in ['N/A', 'Liên hệ']:
                        price_val = 0.0
                    else:
                        try:
                            price_val = float(price.replace('VND', '').replace(',', '').strip())
                        except ValueError:
                            price_val = 0.0

                    content = f"Product: {name}, Category: {category}, Price: {price}, Stock: {stock}, Rating: {rating}"
                    doc = {
                        "document_id": f"html-{product_id}",
                        "content": content,
                        "source_type": "HTML",
                        "author": "System",
                        "timestamp": datetime.now().isoformat(),
                        "source_metadata": {
                            "price_vnd": price_val,
                            "stock": stock
                        }
                    }
                    documents.append(doc)
                    
    return documents

