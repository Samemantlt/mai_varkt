import math

F = 168000
h = 78
GM = 3.5316000 * (10 ** 12)
r = 600000
Vy = 0
dt = 0.05
t = 0
time_stage = 0

m1 = 5810 + 3490
m1_b = 5810
m2 = 1510 + 3720
m2_b = 1510
m3 = 550 + 1260
m3_b = 550
m4 = 720
m4_b = 420
m0 = 17060

k = 80
p0 = 1
H = 5000
e = 2.71828
n = 0.3
times = []
velocity = []
height = []
mass = []
current_stage = 1


def minus_stage():
    global m0, m, m1_b, k, F, current_stage, time_stage
    if m < m0 - (m1 - m1_b) and current_stage == 1:
        m0 = m - m1_b
        F = 138000
        time_stage = 0
        k = 60
        current_stage += 1


while h < 30000:
    m = m0 - k * time_stage
    minus_stage()
    mass.append(m)
    times.append(t)
    p = p0 * e ** ((-1) * (h / H))
    ro = p * 1.2230948554874
    Fd = n * ro * ((Vy) ** 2)
    dVy = ((F / (m0 - k * time_stage)) - GM / (r + h) ** 2 - Fd * 1 / (m0 - k * time_stage)) * dt
    velocity.append(Vy)
    Vy = Vy + dVy
    dh = Vy * dt
    h = h + dh
    height.append(h)
    if m < m3 + m4 + m2_b:
        print(f"{t}, {m - m2_b}, {Vy}, {h}")
        mass.append(m)
        times.append(t)
        velocity.append(Vy)
        height.append(h)
        break
    else:
        print(f"{t}, {m}, {Vy}, {h}")
    t += 0.05
    time_stage += 0.05
