import numpy as np
import matplotlib.pyplot as plt

def transient_response(R, C, Vin, t):
    # Menghitung parameter dalam model orde dua
    tau = R * C
    omega = 1 / tau
    alpha = 1 / (2 * tau)
    
    # Menghitung respon transient
    Vout = Vin * (1 - np.exp(-alpha * t) * np.cos(omega * t))
    
    return Vout

def plot_s_plane(R, C):
    # Menghitung parameter dalam model orde dua
    tau = R * C
    omega = 1 / tau
    alpha = 1 / (2 * tau)
    
    # Menggambar titik-titik pada S-Plane
    real_part = -alpha
    imag_part = omega
    
    plt.scatter(real_part, imag_part, color='red', marker='x')
    plt.annotate('(-α, ω)', (-alpha, omega), xytext=(-alpha+0.05, omega+0.1), arrowprops=dict(arrowstyle='->'))
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('S-Plane RC Pemasak Nasi')
    plt.grid(True)
    plt.show()

# Parameter komponen
R = 100  # Nilai resistor dalam ohm
C = 1e-3  # Nilai kapasitor dalam farad
Vin = 5  # Tegangan input dalam volt

# Waktu simulasi
t = np.linspace(0, 5 * R * C, 500)  # Rentang waktu dari 0 hingga 5RC

# Memanggil fungsi respon transient
Vout = transient_response(R, C, Vin, t)

# Plot hasil respon transient
plt.plot(t, Vout)
plt.xlabel('Waktu (s)')
plt.ylabel('Tegangan Output (V)')
plt.title('Respon Transient Model Orde Dua RC Pemasak Nasi')
plt.grid(True)
plt.show()

# Menggambar grafik S-Plane
plot_s_plane(R, C)
