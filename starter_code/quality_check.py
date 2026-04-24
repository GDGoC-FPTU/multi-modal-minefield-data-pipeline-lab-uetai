# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================
# Task: Implement quality gates to reject corrupt data or logic discrepancies.

def run_quality_gate(document_dict):
    content = document_dict.get('content', '')
    
    if len(content) < 20:
        return False
        
    toxic_strings = ['Null pointer exception', 'Fatal Error', 'Exception:']
    for toxic in toxic_strings:
        if toxic in content:
            return False
            
    if '8%' in content and '0.10' in content:
        print(f"WARNING: Discrepancy detected in {document_dict.get('document_id')}")
        
    return True
