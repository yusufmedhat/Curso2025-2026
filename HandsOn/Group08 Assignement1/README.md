# Hands-on 1 — Smart City Datasets & App (Group01)

**Group**: GroupXX
**Members**:  
Hugo Núñez Búa (210199)

## Summary
We selected **three open datasets** from the Open Data BCN (Barcelona City Council) portal in *smart city* domains (mobility and environment). They will be used to convert to **RDF**, link to other sources, and publish on the Semantic Web. We also define an **application** built on top of these data.

Chosen datasets:
1. **Air quality (station-level detail, Barcelona)** — monthly CSVs, **CC BY 4.0** license.  
   See `requirements/datasetRequirements.html`.
2. **Traffic status by road segments (TRAMS), Barcelona** — monthly CSVs, **CC BY 4.0**.  
   See `requirements/datasetRequirements.html`.
3. **Bicing stations (public bike system), Barcelona** — CSV (historical / status), **CC BY 4.0**.  
   See `requirements/datasetRequirements.html`.

## Structure
```
GroupXX/
├─ README.md
├─ selfAssessmentHandsOn1.md
├─ csv/
│  ├─ barcelona_air_quality_sample.csv
│  ├─ barcelona_traffic_state_sample.csv
│  ├─ barcelona_bicing_stations_sample.csv
│  └─ README.md
├─ requirements/
│  ├─ datasetRequirements.html
│  └─ applicationRequirements.html
└─ scripts/
   └─ fetch_data.sh
```
> **Note**: `csv/` contains **samples** (≤20 rows) to keep the repo light. The script `scripts/fetch_data.sh` downloads the latest full CSVs.

## How to use
1. Read `requirements/datasetRequirements.html` and `requirements/applicationRequirements.html` for the requirement checks and mockups.
2. If you need full data, run:  
   ```bash
   bash scripts/fetch_data.sh
   ```
   This will download the full CSVs into `csv/` (requires `curl`).
3. Proceed with the RDF transformation and push to your GitHub repo.

## Licenses
All chosen datasets are published under **Creative Commons Attribution 4.0 (CC BY 4.0)**. See `requirements/datasetRequirements.html` and `LICENSES.md` (if you add it) for details.

## Last update
2025-10-02
