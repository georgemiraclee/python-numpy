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

def calculate_performance_metrics(Vout, t):
    # Nilai maksimum tegangan (overshoot)
    overshoot = np.max(Vout) - np.mean(Vout)
    
    # Waktu settling (0.02% dari nilai akhir)
    settling_threshold = 0.02 * np.max(Vout)
    settling_time = t[np.argmax(np.abs(Vout - np.max(Vout)) < settling_threshold)]
    
    # Konstanta waktu (time constant)
    time_constant = R * C
    
    return overshoot, settling_time, time_constant

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
plt.title('Respon Transient Model Orde Dua')
plt.grid(True)
plt.show()

# Menghitung performa
overshoot, settling_time, time_constant = calculate_performance_metrics(Vout, t)

print(f'Nilai Overshoot: {overshoot}')
print(f'Waktu Settling: {settling_time}')
print(f'Konstanta Waktu: {time_constant}')
