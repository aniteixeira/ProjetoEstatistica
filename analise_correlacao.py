import numpy as np
import pandas as pd

# Dados oficiais para análise
desmatamento = [25.000, 25.000, 25.000, 20.000, 20.000, 20.000, 38.000, 29.800, 31.200, 31.000, 25.000]  # Hectares por ano
perda_biodiversidade = [10, 11, 12, 10, 11, 12, 15, 14, 15, 15, 13]   # Espécies ameaçadas por ano

# DataFrame para melhor manipulação dos dados
dados = pd.DataFrame({
    "Desmatamento (ha)": desmatamento,
    "Perda de Biodiversidade (Espécies)": perda_biodiversidade
})

# Calcula a correlação de Pearson
correlacao = dados.corr().iloc[0, 1]  # Correlação entre as duas colunas

# Classificar o nível de correlação
if abs(correlacao) > 0.6:
    nivel = "moderada" if abs(correlacao) <= 0.8 else "forte"
    print(f"A correlação linear é {nivel} ({correlacao:.2f}).")
else:
    print(f"A correlação linear é fraca ({correlacao:.2f}).")

# Visualizar os dados
print("\nDados analisados:")
print(dados)

# Análise gráfica (opcional)
import matplotlib.pyplot as plt

plt.scatter(desmatamento, perda_biodiversidade, color='green', alpha=0.7)
plt.title("Correlação entre Desmatamento e Perda de Biodiversidade no Pantanal nos últimos 10 anos.")
plt.xlabel("Desmatamento (ha)")
plt.ylabel("Perda de Biodiversidade (Espécies)")
plt.grid(True)
plt.show()
