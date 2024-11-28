import scipy.stats as st
from math import sqrt

parameters = [["H0(μ)", 0], ["α", 0], ["x̄", 0], ["s", 0], ["pop", 0]]

for i in range(len(parameters)):
    print("Qu'elle est la valeur de ", parameters[i][0])
    parameters[i][1] = float(input())

if parameters[4][1] >= 30:
    zt = st.norm.ppf(1- parameters[1][1])
else:
    zt = st.t.ppf(1 - parameters[1][1], parameters[4][1] - 1)

z = ((parameters[2][1] - parameters[0][1]) * sqrt(parameters[4][1])) / (parameters[3][1])

if abs(round(z, 2)) > abs(round(zt, 2)):
    print("Rejet de H0")
elif abs(round(z, 2)) <= abs(round(zt, 2)):
    print("Non rejet de H0")
else:
    print("ERREUR")