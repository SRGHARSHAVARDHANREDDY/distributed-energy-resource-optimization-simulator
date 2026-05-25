# Distributed Energy Resource Optimization Simulator

An interactive energy management simulator built using Python and Streamlit for modeling Distributed Energy Resource (DER) optimization.

This project simulates how electricity demand is intelligently managed using renewable energy sources such as solar and wind, battery storage, and conventional grid backup.

## Features

- Distributed Energy Resource (DER) simulation
- Solar and wind energy integration
- Battery storage management
- Grid backup utilization
- Renewable-first energy allocation logic
- Interactive dashboard visualization
- Real-time energy analytics and graphs

## Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib

## Project Overview

The simulator models hourly energy demand and allocates available energy resources in the following order:

1. Renewable energy (Solar + Wind)
2. Battery storage
3. Grid backup

This approach demonstrates smart energy scheduling strategies commonly used in modern distributed energy systems.

## Dashboard Features

The dashboard provides:

- Hourly solar generation visualization
- Wind energy trends
- Demand analysis
- Battery usage monitoring
- Grid dependency tracking
- Energy allocation analytics

## Project Structure

```bash
distributed-energy-resource-optimization-simulator/
│
├── app.py
├── energy_logic.py
├── sample_data.csv
├── requirements.txt
└── README.md
