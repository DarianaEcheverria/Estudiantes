import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("student_exam_scores.csv")

# Asegurar carpeta assets
os.makedirs("assets", exist_ok=True)

# Histograma de promedio (si no tienes la columna, crea una)
if "avg_score" not in df.columns:
    df["avg_score"] = df.select_dtypes(include=["number"]).mean(axis=1)

plt.figure()
plt.hist(df["avg_score"], bins=10)
plt.xlabel("Promedio")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("assets/avg_hist.png")
plt.close()

# Top 10 por promedio
top10 = df.sort_values("avg_score", ascending=False).head(10)

plt.figure()
plt.barh(top10["student_id"].astype(str), top10["avg_score"])
plt.gca().invert_yaxis()
plt.xlabel("Promedio")
plt.tight_layout()
plt.savefig("assets/top10.png")
plt.close()
