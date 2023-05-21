# Dibangun oleh Tengku Arya Saputra
# Tugas UTS Struktur data

import requests
import re
import matplotlib.pyplot as plt

# Masukkan kunci API Serpstack
api_key = "API_KEY"

# Fungsi untuk melakukan pencarian Google
def google_search(query, num_results):
    try:
        url = f"http://api.serpstack.com/search?access_key={api_key}&query={query}&num={num_results}"
        response = requests.get(url)
        response.raise_for_status()  # Menangani kesalahan HTTP

        data = response.json()
        if "error" in data:
            raise Exception(f"API Error: {data['error']['info']}")

        return data

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    return None

# Memasukkan query pencarian
search_query = "KEYWORD"

# Jumlah hasil pencarian yang ingin ditampilkan
num_results = 10000

# Melakukan pencarian Google
search_results = google_search(search_query, num_results)

data = {}  # Variabel untuk menyimpan data dari hasil pencarian berdasarkan tahun

if search_results:
    # Menyimpan data dari hasil pencarian berdasarkan tahun postingan
    for result in search_results["organic_results"]:
        title = result['title']
        url = result['url']
        snippet = result['snippet']

        # Mendapatkan tahun postingan dari URL jika tersedia
        year = None
        if 'http://' in url or 'https://' in url:
            parts = url.split('/')
            for part in parts:
                if re.match(r"\b(19[7-9]\d|20[0-2]\d)\b", part):  # Mencocokkan tahun pada bagian URL
                    year = part
                    break

        if year is not None:
            if year not in data:
                data[year] = 0
            data[year] += 1

# Mengurutkan data berdasarkan tahun
sorted_data = sorted(data.items())

# Memisahkan tahun dan jumlah data
years, data_count = zip(*sorted_data)

# Mengatur rentang tahun
start_year = int(min(years))
end_year = int(max(years))

# Mengumpulkan data dan jumlah data berdasarkan rentang tahun
years_range = [str(year) for year in range(start_year, end_year+1)]
data_count_range = [data.get(year, 0) for year in years_range]

print(f"Nama: Tengku Arya Saputra")
print(f"NIM: 20220801***")
print(f"Prodi: Teknik Informatika")
print(f"Data Science - Crawling data - UTS Structure Data")

# Membuat grafik garis
plt.figure(figsize=(8, 4))
plt.plot(years_range, data_count_range, marker='o', label='Jumlah Data {}'.format(search_query))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Data')
plt.title('Grafik Garis: Jumlah Data Tahunan')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Membuat grafik batang
plt.figure(figsize=(8, 4))
plt.bar(years_range, data_count_range, align='center', alpha=0.8, label='Jumlah Data {}'.format(search_query))
plt.xlabel('Tahun')
plt.ylabel('Jumlah Data')
plt.title('Grafik Batang: Jumlah Data Tahunan')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Membuat diagram lingkaran
plt.figure(figsize=(6, 6))
plt.pie(data_count_range, labels=years_range, autopct='%1.1f%%', startangle=90)
plt.title('Diagram Lingkaran: Jumlah Data Tahunan {}'.format(search_query))
plt.show()
