# AI-Powered TB → COA Mapping & Validation System

## Overview

This project is a finance workflow automation prototype designed to map Trial Balance (TB) accounts to a standardized Chart of Accounts (COA) while maintaining auditability, validation controls, and explainability.

The system combines deterministic financial validation logic with AI-assisted semantic reasoning to handle ambiguous mappings, low-confidence classifications, and messy accounting data.

The workflow is intentionally validation-first and designed to simulate production-aware finance operations where reliability and traceability are critical.

---

# Features

* Automated TB → COA account mapping
* Fuzzy matching using RapidFuzz
* Confidence scoring for mappings
* Validation engine for accounting controls
* Detection of unmapped accounts
* Journal entry balance validation
* Groq LLM-powered reasoning layer
* Human review escalation workflow
* Audit traceability output generation
* Validation report generation
* Deterministic + AI hybrid architecture

---

# Architecture Summary

```text
Input Files
    ↓
Validation Layer
    ↓
TB → COA Mapping Engine
    ↓
Self-Correction & Escalation Layer
    ↓
LLM Reasoning Layer
    ↓
Human Review Workflow
    ↓
Audit Reports & Traceability Outputs
```

---

# Deterministic vs LLM Boundary

The workflow intentionally separates deterministic accounting controls from probabilistic AI reasoning.

### Deterministic Components

* debit-credit validation
* journal balancing
* confidence threshold checks
* mapping validation
* audit trace generation

### LLM Components

* semantic interpretation of ambiguous accounts
* explanation generation
* low-confidence mapping reasoning
* escalation context generation

LLMs are intentionally excluded from arithmetic validation and financial calculations because probabilistic outputs are unsuitable for deterministic accounting controls.

---

# Tech Stack

* Python
* Pandas
* RapidFuzz
* Groq API
* python-dotenv
* JSON
* CSV-based financial datasets

---

# Project Structure

```text
COA/
│
├── data/
│   ├── chart_of_accounts.csv
│   ├── trial_balance.csv
│   ├── prior_period_tb.csv
│   ├── fx_rates.csv
│   └── manual_adjustments.json
│
├── docs/
│   └── architecture.md
│
├── output/
│   ├── validation_report.txt
│   └── audit_trace.csv
│
├── src/
│   ├── loader.py
│   ├── mapper.py
│   ├── validator.py
│   ├── llm_reasoning.py
│   └── main.py
│
├── README.md
├── reflection.md
├── requirements.txt
└── .gitignore
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-finance-tb-coa-mapping.git
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside the `src/` folder.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5. Run the Project

```bash
python src/main.py
```

---

# Example Outputs

The workflow generates:

## Mapping Results

* automated TB → COA mappings
* confidence scores
* approval status

## Validation Reports

Generated file:

```text
output/validation_report.txt
```

Includes:

* low-confidence mappings
* unmapped accounts
* journal imbalance detection
* escalation decisions
* LLM reasoning summaries

## Audit Traceability Output

Generated file:

```text
output/audit_trace.csv
```

Contains:

* source lineage
* mapping traceability
* validation status
* confidence tracking

---

# Validation & Auditability

The system is designed with auditability as a core principle.

Features include:

* traceable mapping outputs
* validation-first processing
* human escalation workflows
* deterministic financial controls
* explainable AI-assisted reasoning

---

# Current Limitations

* Prototype focuses on a single workflow slice
* No ERP/API integrations
* Limited FX remediation logic
* No database persistence
* No multi-entity consolidation support
* No orchestration framework

---

# Future Improvements

Potential future enhancements include:

* RAG-based accounting policy retrieval
* Vector embeddings for semantic account matching
* LangGraph orchestration workflows
* Streamlit dashboards
* Approval workflow engine
* Persistent audit database
* Retry orchestration
* Multi-entity financial consolidation
* Real ERP integrations

---

# Reflection

Additional architectural reasoning, trade-offs, and scalability considerations are documented in:

```text
reflection.md
```

---

# Author

Harshit Thapa

AI/ML • Data Analytics • Financial Workflow Automation
