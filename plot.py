import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Cargar CSV
df = pd.read_csv("student_exam_scores.csv")

# Asegurar carpeta de salida
assets = Path("assets")
assets.mkdir(exist_ok=True)

# 1) Histograma del promedio (simple: usa 'hours_studied' como ejemplo)
plt.figure()
df['hours_studied'].plot(kind='hist', bins=10, edgecolor='black')
plt.title("Distribución de horas de estudio")
plt.xlabel("Horas estudiadas")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig(assets / "avg_hist.png")
plt.close()

# 2) Top 10 por asistencia (o por horas, elige lo que quieras)
top10 = df.sort_values('attendance', ascending=False).head(10)

plt.figure()
plt.barh(top10['student_id'], top10['attendance'])
plt.gca().invert_yaxis()
plt.title("Top 10 por asistencia")
plt.xlabel("Asistencia (%)")
plt.tight_layout()
plt.savefig(assets / "top10.png")
plt.close()
