# ETL Pipeline Overview

1. ADF copies raw CSVs from on-prem file shares to ADLS (Bronze)
2. Databricks performs cleaning, enrichment and joins (Silver)
3. Gold layer is modeled using star schema for business use
4. Power BI connects to curated model for reporting

This approach allows reusability across multiple client datasets.
