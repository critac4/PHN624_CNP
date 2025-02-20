import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

def plot_spherical_harmonic(l, m):
    theta = np.linspace(0, np.pi, 100)  
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    Y_lm = sph_harm(m, l, phi, theta)

    r = np.abs(Y_lm)
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)


    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, facecolors=plt.cm.viridis((r - r.min()) / (r.max() - r.min())), rstride=1, cstride=1)


    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Spherical Harmonic (l={l}, m={m})")

    plt.show()


l = 3
m = 2
plot_spherical_harmonic(l, m)
