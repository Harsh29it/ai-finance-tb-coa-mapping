# Architecture Document

# AI-Powered TB → COA Mapping & Validation System

---

# 1. Introduction

This project is a finance workflow automation prototype designed to solve the Trial Balance (TB) to Chart of Accounts (COA) mapping problem using a hybrid architecture that combines deterministic accounting controls with AI-assisted reasoning.

The primary objective of the system is to:

* automate account mapping
* detect validation failures
* maintain auditability
* provide explainable outputs
* escalate ambiguous cases for human review

The workflow is intentionally validation-first and designed to simulate production-aware finance operations where reliability, traceability, and control mechanisms are critical.

---

# 2. Problem Statement

Financial systems frequently receive messy Trial Balance datasets containing:

* inconsistent account naming
* unmapped accounts
* duplicate semantics
* adjustment errors
* incomplete metadata
* ambiguous classifications

A fully deterministic rules-based system struggles with semantic ambiguity, while a fully LLM-driven system introduces unacceptable reliability and auditability risks.

The challenge is to design a workflow that:

* leverages AI where semantic reasoning is useful
* preserves deterministic validation for accounting controls
* supports audit traceability
* enables human-in-the-loop escalation

---

# 3. System Architecture

The system follows a modular single-orchestrator workflow architecture.

```text id="arc1"
Input Files
    ↓
Data Loader
    ↓
Validation Layer
    ↓
TB → COA Mapping Engine
    ↓
Confidence Scoring
    ↓
Self-Correction / Escalation Layer
    ↓
LLM Reasoning Layer
    ↓
Audit Trace Generator
    ↓
Validation Report Generator
```

---

# 4. Architecture Components

## 4.1 Data Loader

File: `loader.py`

Responsibilities:

* load TB dataset
* load COA dataset
* load prior-period TB
* load FX rates
* load manual adjustments

Supported formats:

* CSV
* JSON

The loader layer isolates ingestion logic from business logic to improve maintainability and extensibility.

---

# 4.2 Validation Layer

File: `validator.py`

The validation layer performs deterministic financial controls before downstream processing.

Validation checks include:

* missing value detection
* duplicate account checks
* debit-credit imbalance detection
* missing COA mappings
* journal entry balance validation
* FX data completeness checks

This layer acts as the first reliability boundary in the workflow.

---

# 4.3 TB → COA Mapping Engine

File: `mapper.py`

The mapping engine performs semantic account matching between Trial Balance accounts and standardized COA accounts.

The workflow uses:

* fuzzy string matching
* confidence scoring
* threshold-based approval logic

Mapping outputs include:

* matched COA account
* account type
* confidence score
* approval status

Example statuses:

* Auto Approved
* Needs Review
* Unmapped

---

# 4.4 Confidence Scoring

The system assigns confidence scores to each account mapping.

High-confidence mappings are automatically approved.

Low-confidence mappings trigger:

* validation flags
* escalation workflows
* LLM-assisted reasoning

This reduces the risk of silent financial misclassification.

---

# 4.5 Self-Correction & Escalation Layer

The workflow includes a self-correction validation gate.

Before final outputs are generated, the system evaluates:

* mapping validation failures
* journal balance violations
* unmapped accounts
* low-confidence mappings

If validation failures exist:

* the workflow escalates for human review
* approval is withheld
* issues are included in audit reports

This simulates production-grade financial control workflows.

---

# 4.6 LLM Reasoning Layer

File: `llm_reasoning.py`

The LLM layer uses Groq-hosted language models to generate:

* semantic interpretation
* ambiguity explanations
* human-readable escalation context

LLM reasoning is intentionally limited to:

* low-confidence mappings
* ambiguous account interpretation
* explanation generation

The system avoids using LLMs for:

* arithmetic validation
* journal balancing
* financial calculations
* deterministic accounting logic

This boundary is critical for maintaining reliability and auditability.

---

# 5. Deterministic vs LLM Boundary

The architecture intentionally separates deterministic financial controls from probabilistic AI reasoning.

## Deterministic Components

Handled through code-based validation:

* debit-credit balancing
* adjustment validation
* confidence threshold checks
* mapping approvals
* traceability generation
* workflow escalation

## LLM Components

Handled through AI reasoning:

* semantic ambiguity interpretation
* account explanation generation
* escalation context
* human-readable summaries

LLMs are intentionally excluded from arithmetic validation because probabilistic outputs are unsuitable for deterministic accounting controls.

This hybrid boundary improves:

* explainability
* reliability
* auditability
* operational trust

---

# 6. Audit Traceability Design

The workflow generates audit trace outputs for every mapping.

Generated file:

```text id="arc2"
output/audit_trace.csv
```

Traceability includes:

* source account
* matched COA account
* confidence score
* validation status
* source file lineage

This allows auditors to trace outputs back to originating source rows.

---

# 7. Validation & Failure Handling

The system is designed to explicitly handle production failure scenarios.

Examples:

* unmapped accounts
* ambiguous mappings
* debit-credit mismatches
* missing FX data
* invalid journal entries

Failure handling workflow:

1. detect issue
2. block auto-approval
3. escalate for human review
4. generate explanation
5. include issue in validation report

This prevents silent propagation of financial errors.

---

# 8. Human-in-the-Loop Design

The workflow intentionally supports human override and review.

Cases escalated to humans:

* low-confidence mappings
* ambiguous semantics
* invalid adjustments
* unresolved accounts

The objective is not full automation, but controlled automation with governance.

---

# 9. Why a Hybrid Architecture Was Chosen

A fully deterministic workflow cannot reliably handle semantic ambiguity in messy financial data.

A fully LLM-driven workflow introduces:

* hallucination risk
* non-deterministic outputs
* weak auditability
* poor financial reliability

The hybrid approach balances:

* deterministic controls
* AI-assisted interpretation
* operational explainability
* financial governance

---

# 10. Current Limitations

The current prototype has several limitations:

* no ERP integration
* no persistent database
* limited FX remediation
* no multi-entity consolidation
* no orchestration framework
* limited scalability testing
* no real-time approval workflows

The system is designed as a workflow prototype rather than a production deployment.

---

# 11. Future Improvements

With additional development time, the following improvements would be implemented:

* vector embeddings for semantic account matching
* RAG-based accounting policy retrieval
* LangGraph orchestration
* approval workflow engine
* dashboard visualizations
* database persistence
* retry orchestration
* multi-entity consolidation
* ERP/API integrations
* automated reconciliation workflows

---

# 12. Conclusion

This project demonstrates a validation-first finance workflow architecture that combines deterministic accounting controls with AI-assisted reasoning.

The system prioritizes:

* reliability
* explainability
* auditability
* traceability
* human oversight

rather than attempting unsafe full automation.

The architecture was intentionally designed to reflect how AI systems should operate in high-trust financial environments where deterministic correctness and operational governance are essential.
