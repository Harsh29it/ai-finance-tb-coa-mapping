# Architecture Document  
## AI-Powered TB → COA Mapping & Validation System

---

# 1. Problem Overview

Enterprise financial reporting systems often receive accounting data from multiple ERP exports, spreadsheets, and manual journal adjustments. While the arithmetic involved in financial reporting is deterministic, the data itself is frequently inconsistent, incomplete, or poorly classified.

One of the most common challenges in financial close processes is mapping Trial Balance (TB) accounts to a standardized Chart of Accounts (COA). This becomes difficult when account names differ across systems, temporary suspense accounts exist, or manual adjustments are entered inconsistently.

The objective of this system is to automate the TB → COA mapping process while maintaining auditability, validation controls, and human oversight for uncertain cases.

The system intentionally combines deterministic accounting logic with AI-assisted semantic reasoning instead of relying entirely on an LLM.

---

# 2. System Objectives

The proposed system is designed to:

- Load and validate accounting datasets
- Detect inconsistencies in financial data
- Map Trial Balance accounts to Chart of Accounts categories
- Generate confidence scores for mappings
- Escalate uncertain mappings for human review
- Use LLM reasoning only for ambiguous classification tasks
- Produce audit-friendly validation reports

The architecture prioritizes reliability, traceability, and controlled automation over fully autonomous decision-making.

---

# 3. System Architecture

```text
Input Files
    ↓
Data Loader
    ↓
Validation Layer
    ↓
TB → COA Mapping Agent
    ↓
Confidence Scoring
    ↓
LLM Reasoning Layer (Groq)
    ↓
Human Review Queue
    ↓
Output Reports
```

# 4. System Components

## 4.1 Data Loader

The Data Loader is responsible for ingesting structured accounting datasets from CSV and JSON sources.

Inputs
Trial Balance
Chart of Accounts
Prior Period Trial Balance
FX Rates
Manual Journal Adjustments
Responsibilities
Read CSV and JSON files
Normalize column structures
Convert data into pandas DataFrames
Prepare datasets for downstream validation

This layer acts as the system’s ingestion boundary.

## 4.2 Validation Layer

The Validation Layer performs deterministic accounting checks before any AI-assisted processing occurs.

Validation Checks
Missing values
Duplicate accounts
Missing COA mappings
Trial Balance imbalance detection
Invalid journal entries
Missing FX data
Example Findings
Suspense accounts not mapped to COA
Journal entries where debit ≠ credit
Missing metadata fields

This layer prevents invalid accounting data from propagating further into the workflow.

## 4.3 TB → COA Mapping Agent

The Mapping Agent performs account classification between Trial Balance accounts and the Chart of Accounts hierarchy.

Mapping Strategy

The prototype uses:

Exact matching
Fuzzy string similarity matching using RapidFuzz
Example
"Sales Rev" → "Sales Revenue"
Outputs
Suggested COA account
Account type
Confidence score
Approval status

The mapping logic is deterministic and reproducible.

## 4.4 Confidence Scoring

Each mapping is assigned a confidence score based on string similarity.

Confidence Thresholds
Score Range	Action
90–100	Auto Approved
70–89	Needs Review
Below 70	Unmapped

This layer acts as a safety boundary before AI reasoning is invoked.

## 4.5 LLM Reasoning Layer

The system integrates Groq-hosted LLM inference for semantic reasoning in low-confidence scenarios.

The LLM is intentionally isolated behind confidence thresholds and is not used for deterministic accounting operations.

LLM Responsibilities
Explain ambiguous mappings
Suggest likely accounting categories
Generate human-readable reasoning
Recommend whether human review is required
Example
Account: Suspense - Unmapped

Reasoning:
The account appears to represent temporary unresolved transactions
and cannot be confidently classified without manual review.
Why an LLM is Used Here

Semantic ambiguity is difficult to solve using rule-based systems alone. The LLM layer improves explainability and supports human reviewers during reconciliation workflows.

# 5. AI vs Deterministic Logic

The system intentionally separates deterministic accounting operations from probabilistic AI reasoning.

Deterministic Logic Used For
Arithmetic calculations
Debit/Credit balancing
Trial Balance validation
Duplicate detection
Confidence scoring
Exact/fuzzy matching
LLM Reasoning Used For
Ambiguous account interpretation
Semantic classification
Human-readable explanations
Review recommendations

This separation reduces hallucination risk and improves financial reliability.

LLM outputs are never directly trusted for accounting arithmetic or financial statement generation.
# 6. Failure Handling Strategy

The architecture is designed to fail safely rather than silently producing unreliable outputs.

Failure Scenarios
Missing COA mappings
Low-confidence matches
Suspense accounts
Unbalanced journal entries
Missing FX rates
Invalid adjustment entries
Handling Approach
Log issue
Flag for validation
Escalate to human review
Prevent automatic approval

Uncertain cases are intentionally routed to manual review workflows.

# 7. Human Review Queue

The Human Review Queue acts as a control layer for mappings that cannot be safely automated.

Review Triggers
Confidence score below threshold
Unmapped accounts
Suspense accounts
Validation failures

This design reflects real-world financial control processes where material accounting decisions require oversight.

# 8. Auditability & Traceability

Auditability is a core design principle of the system.

Every mapping decision is logged with:

Source TB account
Suggested COA mapping
Confidence score
Validation status
LLM-generated reasoning

The system also generates:

Mapping output reports
Validation reports
Adjustment validation summaries

Persisting AI-generated explanations alongside validation findings improves traceability during financial reviews.

# 9. Scalability Considerations

Although the prototype focuses on a single workflow slice, the architecture is designed for future scalability.

Potential future enhancements include:

Multi-entity ERP support
Vector embedding search for semantic mapping
RAG-based accounting memory
LangGraph orchestration
Async validation pipelines
Workflow approval dashboards
ERP integrations

The modular design allows individual agents to scale independently.

# 10. Conclusion

This prototype demonstrates a hybrid finance AI architecture that combines deterministic accounting controls with targeted LLM-assisted reasoning.

Rather than replacing accounting controls with AI, the system uses AI selectively for semantic interpretation while preserving validation, auditability, and human oversight.

The result is a safer and more production-aligned approach to financial workflow automation.