import pandas as pd
import random
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Initialize empty lists to store data
data = []

# Class distribution
class_distribution = {
    'DS 50 01': 40,
    'DS 50 02': 44,
    'DS 50 03': 41,
    'DS 50 04': 45,
    'DS 50 05': 45,
    'DS 50 06': 43,
    'DS 50 07': 42
}

# Wali kelas mapping
wali_kelas_mapping = {
    'DS 50 01': 'AOK',
    'DS 50 02': 'AOK',
    'DS 50 03': 'VCA',
    'DS 50 04': 'DBA',
    'DS 50 05': 'DBA',
    'DS 50 06': 'NAA',
    'DS 50 07': 'NAA'
}

# Generate base NIM (will increment for each student)
base_nim = 130592490001

# Generate data for each class
for kelas, jumlah in class_distribution.items():
    for _ in range(jumlah):
        nim = str(base_nim)
        jenis_kelamin = random.choice(['L', 'P'])
        kode_wali = wali_kelas_mapping[kelas]
        nilai = random.randint(60, 100)  # Generate random nilai between 60-100
        
        # Add record to data list
        data.append({
            'NIM': nim,
            'Jenis_Kelamin': jenis_kelamin,
            'Kelas': kelas,
            'Kode_Wali_Kelas': kode_wali,
            'Kode_Mata_Kuliah': 'STD11',
            'Nilai_Mata_Kuliah': nilai
        })
        
        base_nim += 1

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data_mahasiswaa.csv', index=False)

# Display first few rows
print(df.head())
print("\nTotal records:", len(df))
print("\nDistribution of students per class:")
print(df['Kelas'].value_counts().sort_index())