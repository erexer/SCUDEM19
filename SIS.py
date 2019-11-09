"""
11/9/19
2019 SIMIODE Student Competition Using Differential Equations Modeling
Authors: Esteban Ramos, Emily Rexer, and Percy Xie
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# N = total population
N = 100

# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 10, 0

# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0

# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.05,  1./10

# Individual's decreasing immunity
xi = 0.2

# characteristic infectious period
taoI = 5

# characteristic immunity period
taoR = 2

# birth and death rate
birthRate = .0185
deathRate = .0185

# A grid of time points (in days)
t = np.linspace(0, 3000, 3000)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I = y

    dSdt = - beta * S / N + gamma * I / N
    dIdt = beta * S / N - gamma * I / N

    return dSdt, dIdt

# Initial conditions vector
y0 = S0, I0

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I = ret.T

# Plot the data on two separate curves for S(t) and I(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)

ax.plot(t, S/N, 'b', alpha=0.5, lw=2, label='Conformists')
ax.plot(t, I/N, 'r', alpha=0.5, lw=2, label='Nonconformists')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Number of People (10^3)')
ax.set_title('Figure 1: SIS Model')
ax.set_ylim(0,1.1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
