import numpy as np
import pandas as pd

# Dados fictícios para análise
# Substitua pelos valores reais
desmatamento = [628800, 817400, 627000]  # Hectares por ano
perda_biodiversidade = [503, 1200, 74]   # Espécies ameaçadas por ano

# Criar um DataFrame para melhor manipulação dos dados
dados = pd.DataFrame({
    "Desmatamento (ha)": desmatamento,
    "Perda de Biodiversidade (Espécies)": perda_biodiversidade
})

# Calcular a correlação de Pearson
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
plt.title("Correlação entre Desmatamento e Perda de Biodiversidade")
plt.xlabel("Desmatamento (ha)")
plt.ylabel("Perda de Biodiversidade (Espécies)")
plt.grid(True)
plt.show()
