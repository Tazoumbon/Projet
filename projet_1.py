# -*- coding: utf-8 -*-
"""projet_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g9-MUcd6q6ro_AdvJukFR_Q_j4hx6wWK
"""

import matplotlib.pyplot as plt

"""# Introduction

Un circuit RC compose d'une résistance R et d'un condensateur C connectés en serie ou en parallele est l'un des dispositif les fondamentaux en electronique. Il joue un role crucial dans le traitement des signaux, le filtrage et le stcokage d'energie.En raison de sa capacité a créer des delais dans les signaux électronique, le circuit RC est largement utilisé dans les applications telles que les oscillateurs, les filtres passe-bas et passe-haut, ainsi que dans les circuits de temporisation. Sa Simplicité son efficacité en font un élément essentiel dans la conception de circuit électroniques variés, allant des appareils grand publics aux systèmes de commutation avancés.

## **1- Charge du condensateur**
"""

circuit=plt.imread('circuit.jpg')
plt.imshow(circuit)
plt.show()

"""On cherche à prévoir l'évolution de la tension U aux bornes du
condensateur, sachant que le générateur est à tension
constante égale à E (c'est une source idéale de tension).
Appliquons la loi des mailles au circuit, et la loi d'Ohm à la
résistance R :
$$
E = U_C  + U_R  = U_C  + R × i
$$
Le courant i étant identique dans tout le circuit (loi d'unicité
des intensités), on a
$$
i=C\frac{dU}{dt}
$$
soit
$$
\textit{E}=\textit{u}_{c}(t)+RC\frac{du_{c}(t)}
{\textit{dt}}
$$
On définit la constante de temps τ associée à cette équation,
telle que $τ = RC$. Son unité est la seconde (s).
On suppose qu'au début de la charge du condensateur, la
tension à ses bornes vaut u (t = 0) = 0.
La résolution de cette équation différentielle donne la tension
en fonction du temps :
$$
u_{c}(t)= E\left ( 1-\textrm{e}^{\frac{-t}{\tau }} \right )
$$

**Implémentation en Python :**


script python de la charge du condensateur
"""

import numpy as np

# Demande des valeurs a l'utilisateur
R=float(input('Entrez la valeur de la resistance'))  # en ohms
C=float(input('Entrez la valeur du condensateur'))   # en farads
E=float(input('Entrez la valeur de la source'))  # en volts
duree=float(input('Entrez la duree de la simulation'))  # en seconde

pas=0.001

t=np.arange(0,duree,pas)

Uc=E*(1-np.exp(-t/(R*C)))

plt.plot(t,Uc)
plt.xlabel('Temps(s)')
plt.ylabel('Tension aux bornes du condensateur')
plt.title('charge du condensateur')
plt.grid(True)
plt.savefig('fig1')
plt.show()

"""nous observons que le condensateur se charge très rapidement et atteint un état de saturation à partir t>=0.2

## **2- Decharge du condensateur**
"""

circuit=plt.imread('circuit.jpg')
plt.imshow(circuit)
plt.show()

"""La seule différence avec le circuit précédent est l'absence de
générateur. En effet, en phase de décharge, c'est le
condensateur qui fournit du courant au circuit électrique.
Comme précédemment, on applique la loi des mailles sur le
circuit :
$$
0=u_{\textrm{C}}+u_{\textrm{R}}=u_{\textrm{C}}+R\times
i=u_{C}+RC\frac{du_{\textrm{C}}}{dt}
$$
soit
$$u_{C}
(t)+\tau\frac{du_{C}(t)}{dt}
$$
On suppose ici qu'au début de la décharge, la tension aux
bornes du condensateur vaut u (t = 0) = U.
Ainsi, la résolution de l'équation différentielle ci-dessus donne
u en fonction du temps :
$$
u_{c}(t)=\textrm{U}\times e^{\frac{-t}{\tau }}
$$

**Implémentation en Python :**


script python de la charge du condensateur
"""

# Demande des valeurs a l'utilisateur
R=float(input('Entrez la valeur de la resistance'))  # en ohms
C=float(input('Entrez la valeur du condensateur'))   # en farads
E=float(input('Entrez la valeur de la source'))  # en volts
duree=float(input('Entrez la duree de la simulation'))  # en seconde

pas=0.001

t=np.arange(0,duree,pas)

Uc=E*np.exp(-t/(R*C))

plt.plot(t,Uc)
plt.xlabel('Temps(s)')
plt.ylabel('Tension aux bornes du condensateur')
plt.title('Decharge du condensateur')
plt.grid(True)
plt.savefig('fig2')
plt.show()

"""La décharge du condensateur est également très rapide et devient nulle lorsque t>0.2.

# Conclusion

Rendu au terme de notre travail pourtant sur la simulation de la charge et de la décharge du condensateur nous constatons que cette derniere ce charge et se décharge de facon exponentielle conséquence de la valeur de la constante de temps. ceci montre que la constante de temps est un paramètre important dans le processus de charge et de dcharge du condensateur.
"""