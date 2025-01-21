import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
data = pd.read_csv('../data/datos.csv')

# Gráfico de barras: Ventas por mes
plt.figure(figsize=(10, 6))
plt.bar(data['Mes'], data['Ventas'], color='green')
plt.title('Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../outputs/grafico_ventas_barras.png')
