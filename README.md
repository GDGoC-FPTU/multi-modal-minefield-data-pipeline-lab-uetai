# Multi-Modal Minefield: Data Pipeline Lab

**Student Name:** Nguyen Minh Hieu  
**Student ID:** 2A202600180  
**Team:** 1 member  
**GithubName**: nmhieuhieuhieu

**Email**: minhhieutrumhoa1@gmail.com
## Project Overview
This project implements a robust data pipeline to ingest, normalize, and validate unstructured data from multiple sources (PDF, CSV, HTML, Text Transcripts, and Legacy Python code). The goal is to build a high-quality Knowledge Base for AI Agents while ensuring data integrity and quality through semantic checks.

## Key Features
- **Multi-Modal Ingestion:** Handles diverse data formats using specialized extractors.
- **Gemini AI Integration:** Utilizes Google's Gemini API for complex PDF data extraction (Title, Author, Summaries).
- **Schema Harmonization:** Unifies all data into a standardized Pydantic-based schema (`UnifiedDocument`).
- **Quality Control:** Implements "Semantic Gates" to filter out toxic data, error logs, and malformed content.
- **SLA Tracking:** Monitors processing time for each stage of the pipeline.

## Directory Structure
- `starter_code/`: Core implementation files for the pipeline.
- `raw_data/`: Source documents and data files.
- `forensic_agent/`: Tools for auditing and grading the pipeline output.
- `processed_knowledge_base.json`: The final unified output.

## How to Run
1. Configure your API key in a `.env` file:
   ```env
   GEMINI_API_KEY=your_actual_key_here
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the pipeline:
   ```bash
   python starter_code/orchestrator.py
   ```
4. Verify results:
   ```bash
   python forensic_agent/agent_forensic.py
   ```

---
*Developed as part of the Data Pipeline Engineering Lab.*
