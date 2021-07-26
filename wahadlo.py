from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


def go(G, L1, L2, M1, M2, th1, th2, t):
    def derivs(state, t):
        dydx = np.zeros_like(state)
        dydx[0] = state[1]

        delta = state[2] - state[0]
        den1 = (M1 + M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
        dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                    + M2 * G * sin(state[2]) * cos(delta)
                    + M2 * L2 * state[3] * state[3] * sin(delta)
                    - (M1 + M2) * G * sin(state[0]))
                   / den1)

        dydx[2] = state[3]

        den2 = (L2 / L1) * den1
        dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                    + (M1 + M2) * G * sin(state[0]) * cos(delta)
                    - (M1 + M2) * L1 * state[1] * state[1] * sin(delta)
                    - (M1 + M2) * G * sin(state[2]))
                   / den2)

        return dydx

    w1 = 0.0
    w2 = 0.0

    state = np.radians([th1, w1, th2, w2])

    dt = 0.05
    t = np.arange(0, t, dt)

    y = integrate.odeint(derivs, state, t)

    x1 = L1 * sin(y[:, 0])
    y1 = -L1 * cos(y[:, 0])

    x2 = L2 * sin(y[:, 2]) + x1
    y2 = -L2 * cos(y[:, 2]) + y1

    fig = plt.figure()

    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-(L1 + L2 + ((L1 + L2) / 4)), (L1 + L2 + ((L1 + L2) / 4))),
                         ylim=(-(L1 + L2 + ((L1 + L2) / 4)), (L1 + L2 + ((L1 + L2) / 4))))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    inner_trail, = ax.plot([], [], c = "#B80000", lw = 1)
    outer_trail, = ax.plot([], [], c = "#6600FF", lw = 1)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        line.set_data([], [])
        inner_trail.set_data([], [])
        outer_trail.set_data([], [])
        time_text.set_text('')
        return line, time_text, inner_trail, outer_trail

    def animate(i):
        thisx = [0, x1[i], x2[i]]
        thisy = [0, y1[i], y2[i]]

        line.set_data(thisx, thisy)
        inner_trail.set_data(x1[:i + 1], y1[:i + 1])
        outer_trail.set_data(x2[:i + 1], y2[:i + 1])
        time_text.set_text(time_template % (i * dt))
        return line, time_text, inner_trail, outer_trail

    ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                                  interval=dt * 1000, blit=True, init_func=init)
    plt.show()


if __name__ == "__main__":
    G = 9.8
    L1 = 1.0
    L2 = 1.0
    M1 = 1.0
    M2 = 1.0
    th1 = 90
    th2 = 90
    t = 10
    go(G, L1, L2, M1, M2, th1, th2, t)
