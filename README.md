<div align="center">

# Kaizen Hive — Generative & Agentic AI Internship

**A spec-driven implementation of 45 Python tasks spanning prompt engineering, retrieval systems, and autonomous agent architecture.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Tasks](https://img.shields.io/badge/Tasks-45%2F45-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

---

## Overview

This repository documents the practical work completed during my **Generative & Agentic AI Internship** at [Kaizen Hive](https://www.linkedin.com/company/kaizen-hive/).

Rather than isolated script experiments, every task followed a **spec-driven development process**:

> Define the specification → Implement the logic → Run against designated inputs → Verify output matches expected behavior

This input/output validation discipline reflects how reliable AI systems are actually built — through precise logic, explicit state management, and strict output verification, rather than trial-and-error prompting.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Module Breakdown](#module-breakdown)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Skills Demonstrated](#skills-demonstrated)
- [Acknowledgements](#acknowledgements)

## Architecture Overview

The 45 tasks are grouped into three architectural pillars that mirror how real generative AI systems are composed:

| Pillar | Modules | Focus |
|---|---|---|
| **Core LLM Logic** | 01 – 03 | Prompt engineering, text processing, chatbot design |
| **Retrieval Systems** | 04 – 05 | Vector embeddings, similarity search, RAG pipelines |
| **Autonomous Architecture** | 06 – 09 | Function calling, planning, memory, workflow automation |

## Module Breakdown

| # | Module | Focus |
|---|---|---|
| 01 | `Practical_Task_01` | **Prompt Engineering** — role/task/constraint prompts, prompt length validation, few-shot prompting |
| 02 | `Practical_Task_02` | **Text Processing** — summarization, keyword extraction, formalization, generative descriptions |
| 03 | `Practical_Task_03` | **Chatbot Architecture** — intent detection, rule-based response logic, conversation transcripts |
| 04 | `Practical_Task_04` | **Vector Embeddings & Similarity** — cosine similarity, dimension validation, semantic matching |
| 05 | `Practical_Task_05` | **Retrieval-Augmented Generation** — context retrieval, grounded prompting, source citation |
| 06 | `Practical_Task_06` | **Function / Tool Calling** — tool selection logic, structured function calls, argument validation |
| 07 | `Practical_Task_07` | **Task Planning & Decomposition** — goal breakdown, step sequencing, action-to-tool mapping |
| 08 | `Practical_Task_08` | **Memory Management** — preference storage, conversation state tracking |
| 09 | `Practical_Task_09` | **Workflow Automation** — multi-stage pipelines, agent stopping conditions |

Each module contains 5 self-contained tasks (`Task_1` – `Task_5`).

## Repository Structure

```
Kaizen_Hive_Internship/
├── Practical_Task_01/
│   ├── Task_1/task1.py
│   ├── Task_2/task2.py
│   ├── Task_3/task3.py
│   ├── Task_4/task4.py
│   └── Task_5/task5.py
├── Practical_Task_02/
│   └── ...
├── ...
└── Practical_Task_09/
    └── ...
```

## Getting Started

**Requirements:** Python 3.x (no external dependencies beyond the standard library)

```bash
# Clone the repository
git clone https://github.com/hashim212-cs/Kaizen_Hive_Internship.git
cd Kaizen_Hive_Internship

# Run any task
python Practical_Task_0X/Task_Y/taskY.py
```

Most scripts are interactive and prompt for input via the terminal — follow the on-screen prompts to see the logic execute.

## Skills Demonstrated

- Structuring and validating prompts for LLM consumption
- Rule-based NLP techniques for intent detection and text transformation
- Computing and applying vector similarity for semantic search
- Designing RAG pipelines with grounded, context-restricted answering
- Implementing structured function/tool-calling schemas
- Decomposing goals into sequenced, tool-mapped action plans
- Managing conversational memory and agent state
- Building deterministic, multi-stage automated workflows

## Acknowledgements

Thanks to [Kaizen Hive](https://www.linkedin.com/company/kaizen-hive/) for providing a structured, hands-on learning track that shaped the design and scope of this work.

---

<div align="center">

*One milestone completed. Ready for the next build.*

</div>
