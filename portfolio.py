import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title = 'Analisis Prospek Demand Kendaraan Listrik di Indonesia',
    layout = 'wide'
)

st.title("Analisis Prospek Demand Kendaraan Listrik di Indonesia")
st.header("Kenapa diperlukan Kendaraan Listrik?")
st.write("Peningkatan emisi Gas Rumah Kaca dari sektor transportasi utamanya disebabkan oleh peningkatan konsumsi bahan bakar fosil. Konsumsi bahan bakar meningkat sebesar 1,2 juta KL (Kilo Liter) per tahun antara tahun 2015-2020, kecuali pada tahun 2020 ketika pandemi melanda dan menekan konsumsi bahan bakar fosil.Disamping itu, Produksi dalam negeri Indonesia tidak dapat menutupi peningkatan permintaan bensin dan Indonesia telah menjadi importir minyak sejak tahun 2004 dan dengan nilai impor yang terus meningkat.")
st.write("Sejak tahun 2015 hingga 2020, bensin impor telah memasok sekitar 52% dari total konsumsi bensin setiap tahunnya.Keputusan pemerintah menaikkan harga eceran bensin bersubsidi pada pertengahan tahun 2022 berdampak pada inflasi sehingga menyebabkan indeks harga konsumen meningkat sebesar 5,95% pada September 2022 dan 5,71% pada Oktober 2022 YoY. Peralihan dari bahan bakar minyak ke sumber energi yang tidak terlalu berfluktuasi seperti listrik pada transportasi dapat membantu mengurangi masalah ini di masa depan.")

# GRAFIK PERTAMA

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020]
motorcycle_values = [22.5, 23.4, 24.27, 25, 25.9, 22.62]
car_values = [7.91, 8.22, 8.53, 8.78, 9.10, 7.95]

# Create a DataFrame
df = pd.DataFrame({
    'Year': years,
    'Motorcycle': motorcycle_values,
    'Car': car_values
})

# Melt the DataFrame for grouped bar chart
df_melted = df.melt(id_vars=['Year'], value_vars=['Motorcycle', 'Car'], var_name='Vehicle', value_name='Unit Sales')

# Create grouped bar chart
fig = px.bar(df_melted, x='Year', y='Unit Sales', color='Vehicle',
             labels={'Year': 'Tahun', 'Unit Sales': 'Konsumsi Bahan Bakar (Million KL)'},
             title='Konsumsi Bahan Bakar Mobil dan Motor (2015-2020)')

# Set x-axis to display only integer values
fig.update_xaxes(type='category')

# Show the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)


st.header("Penjualan Mobil Listrik di Indonesia")
st.write("Menurut data penjualan wholesales alias pengiriman dari pabrik ke dealer yang dirilis oleh Gabungan Industri Kendaraan Bermotor Indonesia (Gaikindo), mobil listrik berbasis baterai (battery electric vehicle/BEV) mencatatkan penjualan sebanyak 17.062 unit atau melonjak sekitar 65,2% (yoy) dibandingkan tahun 2022. Capaian tersebut sekaligus menjadi rekor tertinggi baru.")
st.write("Namun secara kumulatif, penjualan mobil BEV di Indonesia masih belum mampu menyaingi penjualan mobil konvensional. Bahkan, angka penjualannya juga masih jauh dari mobil hybrid, yang mencatatkan capaian penjualan sebanyak 54.656 unit dan ekspornya mencapai 27.710 unit pada 2023.")

# GRAFIK KEDUA

# Data
tahun = [2020, 2021, 2022, 2023]
unit_penjualan = [125, 687, 10327, 17062]

# Create bar chart
fig = px.bar(x=tahun, y=unit_penjualan, labels={'x': 'Tahun', 'y': 'Unit Penjualan'},
             title='Unit Penjualan Mobil Listrik (2020-2023)')

# Set x-axis to display only integer values
fig.update_xaxes(type='category')

# Show the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.header("Jenis Mobil Yang Terjual")
st.write("Mengutip data Gabungan Industri Kendaraan Bermotor Indonesia (Gaikindo), terdapat 10 model mobil listrik yang terdistribusi bervariasi dari merek China, Eropa hingga Jepang. Hyundai Ioniq 5 menjadi mobil listrik terlaris pada tahun 2023 dengan penjualan mencapai 7.176 unit, diikuti oleh Wuling Air EV sebanyak 5.575 unit.")
st.write("Hal tersebut bisa terjadi karena Dua mobil listrik paling laris merupakan produksi dalam negeri, yakni Hyundai Ioniq 5 dan Wuling Air ev. Keduanya mendapatkan subsidi Pajak Pertambahan Nilai (PPN) dari 11% menjadi hanya 1%.Karena subsidi itu, maka potongan diskonnya tergolong lumayan. Setelah dihitung-hitung berkat 'subsidi' pemerintah, harga Wuling Air ev paling banyak dipotong Rp 26 jutaan untuk unit di harga Rp 300 jutaan.Sementara Hyundai Ioniq 5 mendapat subsidi Rp 60-75 juta bergantung tipenya. Tipe standard range dengan banderol Rp 681,9 juta mendapat subsidi lebih kecil, sementara long range dengan harga Rp 783,1 juta mendapat subsidi lebih besar.")

# GRAFIK KETIGA

# Data
merek_mobil = [
    "Hyundai Ioniq 5", "Wuling Air", "Wuling Bingou", "BMW iX",
    "Toyota BZ4X", "Hyundai Ioniq 6", "DFSK Gelora EV",
    "Lexus RZ450e", "Mini Cooper SE Hatch (Mini Electric)", "Neta V"
]
unit_terjual = [7176, 5575, 1393, 615, 479, 263, 260, 206, 185, 181]

# Create a DataFrame
df = pd.DataFrame({"Merek Mobil": merek_mobil, "Unit Terjual": unit_terjual})

# Create the Horizontal Bar Chart
fig = px.bar(df, x="Unit Terjual", y="Merek Mobil", orientation="h",
             text="Unit Terjual", title="Penjualan Mobil Listrik")

# Customize the chart
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(xaxis_title="Unit Terjual", yaxis_title="Merek Mobil",
                  xaxis_tickformat=',d', yaxis_categoryorder="total ascending")

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.header("Faktor Untuk Percepatan Adopsi Kendaraan Listrik di Indonesia")
st.write("Walaupun penjualan kendaraan listrik di indonesia terus meningkat setiap tahunnya, namun ternyata angka tersebut masih belum mencapai target yang ditetapkan pemerintah. Diperlukan langkah-langkah agar meningkatkan minat beli masyarakat terhadap kendaraan listrik, berdasarkan survey yang dilakukan oleh PwC indonesia, terdapat beberapa halangan yang membuat masyarakat indonesia belum mau membeli kendaran listrik.")
st.write("Pertanyaan yang diajukan adalah sebagai berikut : Anda sebelumnya menyatakan bahwa Anda tidak mempertimbangkan untuk membeli mobil listrik atau sepeda motor. Apa beberapa hambatan yang menghalangi Anda untuk melakukannya?")

# GRAFIK KEEMPAT

# Data
categories = [
    "Stasiun Pengisian Sulit Ditemukan",
    "Stasiun Pengisian Tidak Tersedia di Tempat Terpencil",
    "Pengisian Baterai yang Lama",
    "Jarak Tempuh yang Pendek",
    "Servis yang Mahal",
]
mobil_listrik = [63, 54, 39, 36, 30]
motor_listrik = [52, 47, 34, 37, 18]

# Create a DataFrame
df = pd.DataFrame({
    "Category": categories,
    "Mobil Listrik": mobil_listrik,
    "Motor Listrik": motor_listrik
})

# Sort the DataFrame by the "Mobil Listrik" column in descending order
df.sort_values(by="Mobil Listrik", ascending=True, inplace=True)

# Create the horizontal grouped bar chart
fig = px.bar(df, x=["Motor Listrik", "Mobil Listrik"], y="Category", orientation="h",
             title="Halangan dalam Membeli Kendaraan Listrik di Indonesia",
             labels={"value": "Persentase"})  

# Customize the layout
fig.update_layout(barmode="group", yaxis_title="", xaxis_title="Persentase")

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write("kekhawatiran konsumen dapat berdampak signifikan terhadap angka ini. Mengatasi kekhawatiran ini bukan hanya tanggung jawab pelaku industri tetapi juga pembuat kebijakan, dan pengembang infrastruktur. Hasil survei menunjukkan angka yang sangat mirip antar responden baik untuk mobil listrik maupun sepeda motor. Paragraf ini akan menggunakan persentase mobil listrik sebagai representasi dari hasil survei. Salah satu kekhawatiran utama di antara 63% responden adalah kesulitan dalam menemukan stasiun pengisian daya dan menyoroti perlunya infrastruktur pengisian daya yang kuat, terutama di daerah terpencil (54%). Waktu yang dibutuhkan untuk mengisi daya kendaraan juga merupakan faktor penting (39%); konsumen sudah terbiasa dengan proses pengisian bahan bakar yang cepat pada mobil tradisional, dan terdapat persepsi bahwa pengisian bahan bakar kendaraan listrik memerlukan waktu yang lama sehingga dapat membuat calon pembeli enggan.")

st.header("Kesimpulan dan Saran")
st.write("Pemerintah harus memprioritaskan insentif kendaraan listrik untuk transportasi umum, E2W (pembangunan baru atau retrofit), dan infrastruktur pengisian daya. Insentif transportasi umum dimaksudkan untuk lebih mendukung strategi dekarbonisasi dengan membuat strategi peralihan menjadi lebih menarik dan terjangkau. Insentif untuk E2W mungkin akan memberikan manfaat yang signifikan bagi mereka yang menggunakannya untuk mencari nafkah, seperti pengemudi transportasi online atau pengemudi logistik, karena pengemudi dapat menghemat lebih banyak uang bagi pengguna dan periode pengembalian modal yang lebih cepat dari pemerintah. Memberikan insentif untuk investasi pada infrastruktur pengisian daya telah terbukti 4–7 kali lebih efektif dibandingkan program insentif kendaraan listrik langsung.")

# GRAFIK KELIMA

# Data
labels = ['Java & Bali', 'Sumatera', 'Sulawesi', 'Kalimantan', 'Lainnya']
values = [88.1, 5.6, 2.6, 2.3, 1.4]

# Membuat Donut Chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

# Menampilkan di Streamlit
st.plotly_chart(fig, use_container_width=True)
