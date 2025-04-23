import numpy as np
import matplotlib.pyplot as plt

#1.
def make_sin_wave(x, A, w):
    return A*np.sin(w * x)

#2.
x = np.linspace(0, 2 * np.pi, 1000)

#3.
amplitudes = [0.5, 1, 1.5, 2, 2.5]
frequencies = [1, 2, 3, 4, 5]

#4.
plt.figure(figsize=(10, 6))

#5.
for A, w, in zip(amplitudes, frequencies):
    y = make_sin_wave(x, A, w)
    plt.plot(x, y,  label = f'A={A}, w={w}')

#6.
plt.title("Sin waves with different amplitudes and frequencies")
plt.xlabel("x")
plt.ylabel("y = A * sin(w * x)")
plt.legend()
plt.grid(True)

plt.show()