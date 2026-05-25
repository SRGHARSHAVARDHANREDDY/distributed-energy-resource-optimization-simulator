import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from energy_logic import allocate_energy, reset_battery

st.set_page_config(page_title="DER Simulator", layout="wide")

st.title("Distributed Energy Resource Optimization Simulator")

battery_capacity = st.sidebar.slider("Battery Capacity (kWh)", 50, 500, 200)
initial_battery = st.sidebar.slider("Initial Battery Level (kWh)", 0, battery_capacity, 100)

reset_battery(initial_battery, battery_capacity)

df = pd.read_csv("sample_data.csv")

battery_levels = []
grid_usage = []
battery_usage = []
renewable_used = []

for _, row in df.iterrows():
    b, g, bl, r = allocate_energy(row["Solar"], row["Wind"], row["Demand"])
    battery_usage.append(b)
    grid_usage.append(g)
    battery_levels.append(bl)
    renewable_used.append(r)

df["Battery Used"] = battery_usage
df["Grid Used"] = grid_usage
df["Battery Level"] = battery_levels
df["Renewable Used"] = renewable_used

st.dataframe(df)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["Hour"], df["Demand"], label="Demand")
ax.plot(df["Hour"], df["Solar"], label="Solar")
ax.plot(df["Hour"], df["Wind"], label="Wind")
ax.plot(df["Grid Used"], label="Grid Backup")
ax.legend()
st.pyplot(fig)

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df["Battery Level"], label="Battery Level")
ax2.legend()
st.pyplot(fig2)