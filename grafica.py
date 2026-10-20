import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("resultados.csv")

antes = df[df["estado"] == "antes"]
despues = df[df["estado"] == "despues"]

plt.figure(figsize=(8,5))

plt.plot(
    antes["usuarios"],
    antes["tiempo_medio"],
    marker="o",
    label="Antes de optimizar"
)

plt.plot(
    despues["usuarios"],
    despues["tiempo_medio"],
    marker="o",
    label="Después de optimizar"
)

plt.title("Tiempo medio de respuesta")
plt.xlabel("Usuarios concurrentes")
plt.ylabel("Tiempo medio (s)")
plt.grid(True)
plt.legend()

plt.savefig("comparativa.png")

print("Gráfica creada: comparativa.png")
