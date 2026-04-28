import matplotlib.pyplot as plt

dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]
vendas = [200, 300, 150, 400, 250]

plt.plot(dias, vendas)
plt.title("Vendas por dia")
plt.xlabel("Dias")
plt.ylabel("Vendas")
plt.show()