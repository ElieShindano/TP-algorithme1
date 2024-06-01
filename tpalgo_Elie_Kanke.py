import numpy as np
import matplotlib.pyplot as plt

# Définition des paramètres du système
m = 10.0  # Masse (kg)
k = 4000.0  # Constante de raideur du ressort (N/m)
alpha = 20.0  # Coefficient de frottement (Nc/m)
F0 = 100.0  # Amplitude de la force extérieure (N)
omega = 10.0  # Fréquence angulaire de la force extérieure (rad/s)
x0 = 0.01  # Position initiale (m)
v0 = 0.0  # Vitesse initiale (m/s)

# Définition de la fonction pour résoudre l'équation différentielle du système
def f(t, y):
    x, v = y
    return np.array([v, -k/m * x - alpha/m * v + F0/m * np.cos(omega * t)])

# Résolution de l'équation différentielle avec la méthode de Runge-Kutta de quatrième ordre
t = np.linspace(0, 10, 1000)
y = np.zeros((len(t), 2))
y[0] = [x0, v0]

for i in range(1, len(t)):
    h = t[i] - t[i-1]
    k1 = f(t[i-1], y[i-1])
    k2 = f(t[i-1] + h/2, y[i-1] + h/2 * k1)
    k3 = f(t[i-1] + h/2, y[i-1] + h/2 * k2)
    k4 = f(t[i], y[i-1] + h * k3)
    y[i] = y[i-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)

# Extraction des positions et vitesses
x = y[:, 0]
v = y[:, 1]

# Calcul de l'énergie cinétique et de l'énergie potentielle
Ec = 0.5 * m * v**2
Ep = 0.5 * k * x**2
Em = Ec + Ep

# Traçage des graphiques
plt.plot(t, x, label="Position")
plt.plot(t, v, label="Vitesse")
plt.plot(t, Ec, label="Energie cinétique")
plt.plot(t, Ep, label="Energie potentielle")
plt.plot(t, Em, label="Energie mécanique")
plt.xlabel("Temps (s)")
plt.ylabel("Valeur")
plt.legend()
plt.show()







