import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# parameters
population = 120
infection_radius = 0.03
infection_probability = 0.3
recovery_time = 200

# random positions
x = np.random.rand(population)
y = np.random.rand(population)

# movement speed
vx = (np.random.rand(population) - 0.5) * 0.01
vy = (np.random.rand(population) - 0.5) * 0.01

# states
state = np.zeros(population)  # all susceptible
state[0] = 1  # patient zero

infection_timer = np.zeros(population)

fig, ax = plt.subplots()
scatter = ax.scatter(x, y)

ax.set_xlim(0,1)
ax.set_ylim(0,1)

def update(frame):

    global x, y, vx, vy, state

    # move people
    x += vx
    y += vy

    # bounce off walls
    vx[x<0] *= -1
    vx[x>1] *= -1
    vy[y<0] *= -1
    vy[y>1] *= -1

    # infection process
    for i in range(population):
        if state[i] == 1:

            for j in range(population):
                if state[j] == 0:

                    distance = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)

                    if distance < infection_radius:
                        if np.random.rand() < infection_probability:
                            state[j] = 1

            infection_timer[i] += 1

            if infection_timer[i] > recovery_time:
                state[i] = 2

    colors = ["blue" if s==0 else "red" if s==1 else "green" for s in state]

    scatter.set_offsets(np.c_[x,y])
    scatter.set_color(colors)

    return scatter,

ani = FuncAnimation(fig, update, frames=500, interval=50)

plt.title("Disease Spread Simulation")

anim = FuncAnimation(fig, update, frames=500, interval=50)
anim.save("disease_simulation.gif", writer="pillow", fps=20)

plt.show()


