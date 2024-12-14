import pandas as pd

# membaca data csv ke dalam dataframe
file_path = 'disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv'
data = pd.read_csv(file_path)

# soal 1
print("\nsoal 1")
data_sampah = data[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']]
print(data_sampah.head())

# soal 2
print("\nsoal 2")
tahun_tertentu = 2015
data_tahun_tertentu = data_sampah[data_sampah['tahun'] == tahun_tertentu]
total_sampah_tahun_tertentu = data_tahun_tertentu['jumlah_produksi_sampah'].sum()
print(f"total produksi sampah di seluruh kabupaten/kota di jawa barat untuk tahun {tahun_tertentu}: {total_sampah_tahun_tertentu} ton")

# soal 3
print("\nsoal 3")
tahun_range = range(2015, 2024)
data_per_tahun = data_sampah[data_sampah['tahun'].isin(tahun_range)]
data_per_tahun_agregat = data_per_tahun.groupby('tahun')['jumlah_produksi_sampah'].sum().reset_index()

data_per_tahun_iterrows= []
for index, row in data_per_tahun_agregat.iterrows():
    data_per_tahun_iterrows.append({'tahun': row['tahun'], 'total_produksi_sampah': row['jumlah_produksi_sampah']})
data_per_tahun_iterrows_df = pd.DataFrame(data_per_tahun_iterrows)
print(data_per_tahun_iterrows_df)

# soal 4
print("\nsoal 4")
data_per_kabupaten_tahun = []
for (kabupaten, tahun), group in data_sampah.groupby(['nama_kabupaten_kota', 'tahun']):
    total_sampah = group['jumlah_produksi_sampah'].sum()
    data_per_kabupaten_tahun.append({'nama_kabupaten_kota': kabupaten, 'tahun': tahun, 'total_produksi_sampah': total_sampah})
data_per_kabupaten_tahun_df = pd.DataFrame(data_per_kabupaten_tahun)
print(data_per_kabupaten_tahun_df)

# ekspor hasil ke dalam csv dan excel
data_per_tahun_iterrows_df.to_csv('hasil_total_per_tahun_2015_2023.csv', index=False)
data_per_kabupaten_tahun_df.to_csv('hasil_per_kabupaten_tahun.csv', index=False)

# menyimpan ke file excel
data_per_tahun_iterrows_df.to_excel('hasil_total_produksi_sampah_2015_2023.xlsx', index=False)
data_per_kabupaten_tahun_df.to_excel('hasil_per_kabupaten_tahun.xlsx', index=False)

print("\nhasil telah diekspor ke file csv dan excel.")
