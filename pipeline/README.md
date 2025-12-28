# Data Engineering Zoomcamp — My Notes & Homework (DataTalks.Club)

This repository tracks my learning journey through the **DataTalks.Club Data Engineering Zoomcamp** — a project-based program where we build an end-to-end data pipeline using modern data engineering tools and best practices.

My goal: **upskill into data engineering** by learning how to design, build, orchestrate, and ship production-style data workflows—from ingestion all the way to analytics and streaming.

> Official course repo (source of truth): https://github.com/DataTalksClub/data-engineering-zoomcamp

---

## What I’m covering each week (high-level plan)

### Week 1 — Containerization & Infrastructure as Code
- Intro to cloud concepts (GCP)
- Docker + Docker Compose
- Run PostgreSQL in containers
- Provision infrastructure with Terraform
- Homework

### Week 2 — Workflow Orchestration
- Data lakes & orchestration fundamentals
- Build orchestrated pipelines with **Kestra**
- Homework

### Week 3 — Data Warehousing
- Data warehouse concepts using **BigQuery**
- Partitioning, clustering, and performance best practices
- (Optional) ML features in BigQuery

### Week 4 — Workshop: Data Ingestion
- Ingestion patterns (APIs, incremental loads, scalability)
- Data normalization & incremental loading
- Workshop homework

### Week 5 — Analytics Engineering
- **dbt** with DuckDB & BigQuery
- Testing, documentation, and deployment workflows
- Basic data apps / visualization (Streamlit & Looker Studio)

### Week 6 — Batch Processing
- Apache Spark fundamentals
- DataFrames + SQL
- Internals of joins and groupBy
- Homework

### Week 7 — Streaming
- Kafka fundamentals
- Kafka Streams / KSQL
- Schema management with Avro
- Homework

### Weeks 8–9 — Final Project (Capstone)
- Design and build a real-world end-to-end pipeline
- Apply course concepts (infra → ingestion → orchestration → modeling → serving)
- Peer review + iteration

---

## Repository structure

- `week_01/` — Docker, SQL, Terraform notes + homework
- `week_02/` — Kestra workflows + notes
- `week_03/` — BigQuery exercises + notes
- `week_04/` — Ingestion workshop (pipelines + homework)
- `week_05/` — dbt models + docs/tests
- `week_06/` — Spark batch jobs + notebooks
- `week_07/` — Kafka streaming exercises
- `project/` — Capstone project (design, code, docs, dashboard)

*(Folder names may evolve as I progress.)*

---

## Tools & stack (course-driven)
- Docker, PostgreSQL
- Terraform + Cloud (GCP)
- Kestra (orchestration)
- BigQuery (warehouse)
- dbt (analytics engineering)
- Spark (batch)
- Kafka (streaming)

---

## Acknowledgements
Massive thanks to **DataTalks.Club** for maintaining this free, hands-on curriculum and community.