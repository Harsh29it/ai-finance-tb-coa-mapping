# Reflection

## 1. What Worked Well

One of the strongest aspects of this project was the modular architecture. Splitting the system into separate components such as the loader, mapper, validator, and LLM reasoning layer made the workflow easier to build, debug, and extend. Each module had a clearly defined responsibility, which improved maintainability and reduced complexity during development.

Another area that worked well was the validation-first design approach. Before introducing any AI-assisted reasoning, the system performs deterministic checks such as Trial Balance balancing, duplicate detection, journal validation, and missing mapping checks. This significantly improved reliability because invalid accounting data is identified early in the workflow rather than propagating downstream.

The hybrid AI plus deterministic logic architecture also proved effective. Instead of relying entirely on an LLM, the system uses traditional programming for arithmetic and accounting controls while reserving AI reasoning for ambiguous account interpretation. This separation made the prototype more aligned with real-world financial system requirements.

The confidence-scoring mechanism also helped create safer automation boundaries. High-confidence mappings are auto-approved, while uncertain cases are escalated for review. This reduced the risk of blindly trusting automated outputs.

Finally, the addition of validation reports and persisted LLM reasoning improved auditability and explainability. The system generates traceable outputs that explain why certain accounts were flagged or escalated.

---

## 2. Biggest Challenge

The biggest challenge during the project was balancing explainability with automation reliability. Initially, it seemed attractive to automate more parts of the workflow using AI, but financial systems require deterministic guarantees for arithmetic operations and accounting controls.

Another major challenge was handling inconsistent ERP-style accounting data. Account names were not always standardized, some accounts were temporary or ambiguous, and manual adjustment entries sometimes contained balancing issues. Designing a workflow that could identify these problems while still remaining flexible required multiple validation layers.

Integrating the LLM layer responsibly was also challenging. A major concern was avoiding over-reliance on AI-generated outputs. To address this, the system intentionally isolates LLM usage behind confidence thresholds and human review steps instead of directly trusting model outputs.

---

## 3. Where the Prototype Breaks at Scale

Although the prototype works well for the current workflow slice, several limitations would appear in large-scale enterprise environments.

One limitation is handling very large ERP datasets containing thousands of accounts, millions of transactions, and multiple reporting periods. The current implementation processes data sequentially and would require optimization for large-scale workloads.

Another challenge would be highly customized Charts of Accounts. Different organizations often use unique naming conventions, entity-specific account structures, and region-specific accounting rules. Traditional fuzzy matching alone may not scale effectively across those scenarios.

Cross-entity consolidations would also introduce significant complexity. Large organizations often require intercompany eliminations, subsidiary-level reporting, currency translation, and multi-entity reconciliation workflows that are not currently implemented in the prototype.

The current prototype also lacks persistent workflow state management, approval tracking, and distributed processing pipelines that would be expected in production finance systems.

---

## 4. How AI Helped

AI played an important role in improving semantic reasoning and handling ambiguous mapping scenarios. While deterministic matching works well for exact or near-exact account names, ambiguous or poorly named accounts benefit from contextual interpretation provided by the LLM layer.

The Groq-hosted LLM integration helped generate human-readable explanations for low-confidence mappings and provided recommendations about whether manual review was required. This improved explainability without compromising accounting reliability.

AI also helped accelerate prototyping. It enabled faster experimentation with semantic classification workflows and reduced the need for building overly complex rule-based mapping systems for every edge case.

Another important contribution of AI was mapping ambiguity resolution. Temporary suspense accounts and unclear adjustment accounts are difficult to classify deterministically, and the LLM layer provided additional reasoning support for those cases.

---

## 5. Risks of AI in Finance

One of the most important lessons from the project was understanding the risks of AI in financial systems.

The biggest risk is hallucination. LLMs can generate confident-sounding responses that may not be factually or financially correct. In accounting workflows, this can create serious reliability issues if outputs are trusted without validation.

Another risk is overconfidence in automated systems. Financial workflows require strong controls, auditability, and traceability. Blindly automating decisions without review mechanisms can introduce material reporting risks.

LLMs also lack deterministic guarantees. The same prompt may produce slightly different outputs across runs, which makes them unsuitable for arithmetic validation, balancing logic, or compliance-critical financial calculations.

Because of these risks, the system intentionally restricts AI usage to semantic reasoning tasks while keeping validation and accounting controls deterministic.

The project reinforced the idea that AI in finance should augment human decision-making rather than replace financial controls entirely.

---

## 6. What I Would Improve in 3 Months

If more development time were available, several improvements could significantly strengthen the system.

One major improvement would be adding Retrieval-Augmented Generation (RAG) using accounting standards, historical mappings, and ERP-specific documentation. This would improve reasoning quality and reduce hallucination risk.

I would also introduce vector embeddings for semantic account search. Embedding-based similarity matching would likely outperform traditional fuzzy matching for complex or inconsistent account names.

Another improvement would be building approval workflows and reviewer dashboards. A production-ready system should allow finance teams to approve mappings, track escalations, and review audit logs through a user interface.

Workflow orchestration would also be important. Adding retry orchestration, review queues, and state management using frameworks such as LangGraph could improve reliability and scalability.

Additional future improvements would include:
- Multi-entity ERP support
- Async validation pipelines
- Persistent audit logging
- Versioned mapping history
- API integrations with ERP systems
- Role-based approval controls

Overall, the project demonstrated that hybrid AI systems are most effective when combined with deterministic validation layers, strong human oversight, and audit-focused architecture design.