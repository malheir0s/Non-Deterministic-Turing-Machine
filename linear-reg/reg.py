import pandas as pd

import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
from   sklearn.metrics import r2_score

dataFile = pd.read_csv('2.csv', decimal=',', error_bad_lines=False)

plt.figure(figsize = (16,8))
plt.scatter(
    dataFile['palavra'], 
    dataFile['time'], 
    c='red')
plt.xlabel("Tamanho da Palavra")
plt.ylabel("Tempo de Execução (s)")

plt.show()

x = dataFile['palavra'].values.reshape(-1,1)
y = dataFile['time'].values.reshape(-1,1)
reg = LinearRegression()
reg.fit(x, y)

f_previsoes = reg.predict(x)

plt.figure(figsize = (16,8))
plt.scatter(
    dataFile['palavra'], 
    dataFile['time'], 
    c='red')

plt.plot(
    dataFile['palavra'],
    f_previsoes,
    c='blue',
    linewidth=3,
    linestyle=':'
)

plt.xlabel("Tamanho da Palavra")
plt.ylabel("Tempo de Execução (s)")

plt.show()



