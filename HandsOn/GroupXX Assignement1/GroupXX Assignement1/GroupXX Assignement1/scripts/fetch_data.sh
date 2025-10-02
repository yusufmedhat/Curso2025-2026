#!/usr/bin/env bash
set -euo pipefail
mkdir -p "$(dirname "$0")/../csv"

echo "Downloading datasets from Open Data BCN…"
echo ">> Air quality (station-level, monthly CSV)"
# Replace UUID and file name with the month you need from the resource page if necessary
curl -L -o "$(dirname "$0")/../csv/2024_11_qualitat_aire_BCN.csv" "https://opendata-ajuntament.barcelona.cat/data/dataset/qualitat-aire-detall-bcn/resource/8b71b498-6171-4d7f-a9bf-75251e69794b/download/2024_11_Novembre_qualitat_aire_BCN.csv"

echo ">> Traffic by segments (TRAMS, monthly CSV)"
curl -L -o "$(dirname "$0")/../csv/2025_04_TRAMS_TRAMS.csv" "https://opendata-ajuntament.barcelona.cat/data/dataset/trams/resource/d18a6f9e-cd22-4a21-af28-99aa23af1fb2/download/2025_04_Abril_TRAMS_TRAMS.csv"

echo ">> Bicing stations (historical 2019 example)"
curl -L -o "$(dirname "$0")/../csv/2019_01_BICING_ESTACIONS.csv" "https://opendata-ajuntament.barcelona.cat/data/dataset/bicing/resource/f59e276c-1a1e-4fa5-8c89-8a8a56e56b34/download/2019_01_Gener_BICING_ESTACIONS.csv"

echo "Done. Files in csv/"
