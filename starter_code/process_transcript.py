import re

from datetime import datetime

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Clean the transcript text and extract key information.

def clean_transcript(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # ------------------------------------------
    
    # Remove noise tokens and speaker tags
    text = re.sub(r'\[.*?\]', '', text)
    
    # Remove "Speaker X:" text
    text = re.sub(r'Speaker \d+:', '', text)
    
    price_vnd = 0
    if "năm trăm nghìn" in text.lower() or "500,000" in text:
        price_vnd = 500000
        
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    cleaned_content = "\n".join(lines)
    
    doc = {
        "document_id": "transcript-001",
        "content": cleaned_content,
        "source_type": "Video",
        "author": "System",
        "timestamp": datetime.now().isoformat(),
        "source_metadata": {
            "detected_price_vnd": price_vnd
        }
    }
    
    return doc
