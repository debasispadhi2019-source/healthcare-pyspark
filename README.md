# healthcare-pyspark

Step -1 from GIT HUB TO ADLS BRONZE (DIAGRAM)

              GITHUB
                 │
                 ▼
        ┌─────────────────┐
        │ ADF             │
        │ Web Activity    │
        │ Get GitHub Files│
        └────────┬────────┘
                 │
                 ▼
              ForEach
                 │
                 ▼
               Copy
                 │
                 ▼
        ┌─────────────────┐
        │ ADLS Gen2       │
        │ raw/_emr        │
        └────────┬────────┘
                 │
                 │ Get Metadata
                 ▼
              ForEach
                 │
                 ▼
               Copy
                 │
                 ▼
        ┌─────────────────┐
        │ ADLS Gen2       │
        │ bronze/_emr     │
        └─────────────────┘
