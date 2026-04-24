import ast
import re
from datetime import datetime

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Extract docstrings and comments from legacy Python code.

def extract_logic_from_code(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        source_code = f.read()
    # ------------------------------------------
    
    parsed = ast.parse(source_code)
    business_rules = []
    
    for node in ast.walk(parsed):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            if docstring:
                business_rules.append(f"Function {node.name} docstring: {docstring}")
                
    comments = re.findall(r'#.*', source_code)
    for comment in comments:
        business_rules.append(f"Comment: {comment}")
            
    content = "\n".join(business_rules)
    
    doc = {
        "document_id": "legacy-code-001",
        "content": content,
        "source_type": "Code",
        "author": "Senior Dev",
        "timestamp": datetime.now().isoformat(),
        "source_metadata": {
            "parsed_functions": [node.name for node in ast.walk(parsed) if isinstance(node, ast.FunctionDef)]
        }
    }
    
    return doc

