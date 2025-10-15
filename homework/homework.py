
# %%
# Cargue los datos de las tabla "files/input/drivers.csv" a una variable llamada
# drivers, usando pandas 
import pandas as pd
drivers = pd.read_csv("../files/input/drivers.csv")


# %%
# Cargue los datos de las tabla "files/input/timesheet.csv" a una variable llamada
# timesheet, usando pandas
timesheet = pd.read_csv("../files/input/timesheet.csv")

# %%
# Calcule el promedio de las columnas "hours-logged" y "miles-logged" en la 
# tabla "timesheet", agrupando los resultados por cada conductor (driverId).
avg_timesheet = timesheet.groupby("driverId")[["hours-logged", "miles-logged"]].mean().reset_index()
avg_timesheet

# %%
# Cree una tabla llamada "timesheet_with_means" basada en la tabla "timesheet", 
# agregando una columna con el promedio de "hours-logged" para cada conductor (driverId).
timesheet_with_means = timesheet.merge(avg_timesheet[["driverId", "hours-logged"]], on="driverId", suffixes=("", "_mean"))

# %%
# Cree una tabla llamada "timesheet_below" a partir de "timesheet_with_means", filtrando los registros 
# donde "hours-logged" sea menor que "mean_hours-logged".
timesheet_below = timesheet_with_means[timesheet_with_means["hours-logged"] < timesheet_with_means["hours-logged_mean"]]
timesheet_below

# %%
# Genera un archivo CSV llamado "files/output/summary.csv" que contenga la tabla "timesheet_below".
# Crea la carpeta "files/output" si no existe.
import os
os.makedirs("../files/output", exist_ok=True)
timesheet_below.to_csv("../files/output/summary.csv", index=False)

# %%
# Cree un gráfico de barras que muestre los 10 conductores (driverId) con más
# registros en la tabla "timesheet_below". Guarde el gráfico como "files/plots/top10_drivers.png".

# Crea la carpeta "files/plots" si no existe.
os.makedirs("../files/plots", exist_ok=True)

import matplotlib.pyplot as plt
top10_drivers = timesheet_below["driverId"].value_counts().head(10)
plt.figure(figsize=(10, 6))
top10_drivers.plot(kind='bar')
plt.xlabel('Driver ID')
plt.ylabel('Number of Records')
plt.title('Top 10 Drivers with Most Records Below Average Hours Logged')
plt.savefig("../files/plots/top10_drivers.png")
plt.close()

# %%






