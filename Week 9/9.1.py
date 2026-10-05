import matplotlib.pyplot as plt
import numpy as np

# Data IPU sahih dari MyEQMS / APIMS (eqms.doe.gov.my/APIMS/main)
matrix = np.array([
    [163, 163, 163, 163, 163],  # Limbang
    [190, 190, 189, 188, 187],  # ILP Miri
    [183, 183, 181, 180, 179],  # Miri
    [207, 207, 207, 205, 204],  # Samalaju
    [208, 206, 204, 203, 203],  # Bintulu
    [190, 189, 189, 189, 188],  # Mukah
    [152, 152, 151, 148, 142],  # Kapit
    [177, 178, 179, 180, 181],  # Sibu
    [181, 182, 183, 184, 185],  # Sarikei
    [232, 230, 227, 225, 224]   # Sri Aman
    [163, 163, 163, 163, 163]   # Limbang
])

kawasan = ['Limbang', 'ILP Miri', 'Miri', 'Samalaju', 'Bintulu', 'Mukah', 'Kapit', 'Sibu', 'Sarikei', 'Sri Aman']
kawasan = ['Miri', 'Bintulu', 'Mukah', 'Sibu', 'Limbang']
masa = ['19:00', '20:00', '21:00', '22:00', '23:00']

plt.imshow(matrix, cmap='YlOrRd', interpolation='nearest')
plt.colorbar(label='Indeks Pencemaran Udara (IPU)')

plt.xticks(range(len(masa)), masa)
plt.yticks(range(len(kawasan)), kawasan)

plt.title('Peta Haba IPU Sarawak (MyEQMS / APIMS)')
plt.show()