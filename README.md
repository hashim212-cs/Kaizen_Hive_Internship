# Kaizen Hive — Generative & Agentic AI Internship

Python coding exercises completed during my **Generative & Agentic AI Internship** at [Kaizen Hive](https://www.linkedin.com/company/kaizen-hive/).

Rather than isolated script experiments, each task followed a spec-driven process: implement a defined logic → run it against designated inputs → verify the output matches the expected result. The goal was to build a practical, ground-up understanding of how LLM-powered systems and agents are actually assembled — one deterministic building block at a time.

## Structure

The repo is organized into **9 architectural modules**, each containing **5 tasks**, for **45 tasks total**.

| Module | Focus |
|---|---|
| `Practical_Task_01` | Prompt Engineering — role/task/constraint prompts, prompt validation, few-shot prompting |
| `Practical_Task_02` | Text Processing — summarization, keyword extraction, text formalization, description generation |
| `Practical_Task_03` | Chatbot Architecture — intent detection, rule-based responses, conversation transcripts |
| `Practical_Task_04` | Vector Embeddings & Similarity — cosine similarity, dimension checks, semantic matching |
| `Practical_Task_05` | Retrieval-Augmented Generation (RAG) — context retrieval, grounded prompting, source citation |
| `Practical_Task_06` | Function/Tool Calling — tool selection, structured function calls, argument validation |
| `Practical_Task_07` | Task Planning & Decomposition — goal breakdown, step sequencing, action-to-tool mapping |
| `Practical_Task_08` | Memory Management — preference storage, conversation state tracking |
| `Practical_Task_09` | Workflow Automation — multi-stage pipelines, agent stopping conditions |

Each task lives in its own folder (`Task_1` – `Task_5`) as a standalone Python script.

## What This Covers

- **Core LLM Logic** — advanced prompt engineering, text processing, chatbot design
- **Retrieval Systems** — vector embeddings, similarity search, RAG pipelines
- **Autonomous Architecture** — function calling, task planning, memory management, workflow automation

## Running a Task

Each script is self-contained and runs with plain Python 3:

```bash
python Practical_Task_0X/Task_Y/taskY.py
```

Most scripts prompt for input via the terminal (`input()`), so run them interactively and follow the prompts.

## Acknowledgements

Thanks to [Kaizen Hive](https://www.linkedin.com/company/kaizen-hive/) for the structured, hands-on learning track that shaped this repo.
