import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title = 'Analisis Prospek Demand Kendaraan Listrik di Indonesia',
    layout = 'wide'
)

# Fungsi untuk membuat sebuah paragraf rata kanan kiri dan ditambah 1 baris kosong dibawahnya
def justify_text(text):
    st.markdown(f"<div style='text-align: justify'>{text}</div><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.11,0.9,0.1])

with col1:
    st.write("")
with col2:
    st.title("Analisis Prospek Demand Kendaraan Listrik di Indonesia")
with col3:
    st.write("")

st.header("Kenapa diperlukan Kendaraan Listrik?")
justify_text("Menurut Institute for Essential Services Reform (IESR) pada publikasinya yang berjudul Indonesia Electric Vehicle Outlook 2023, terdapat 2 hal yang mendorong kebutuhan kendaraan listrik di indonesia, yang pertama dekarbonisasi yang bertujuan menekan peningkatan suhu global dibawah 1.5 derajat celsius pada 2050, dan yang kedua mengurangi impor bahan bakar. Dimana Sektor transportasi adalah sumber kedua terbesar emisi CO2 yaitu sebanyak 23.14%.")
justify_text("Peningkatan emisi Gas Rumah Kaca dari sektor transportasi utamanya disebabkan oleh peningkatan konsumsi bahan bakar fosil. Konsumsi bahan bakar meningkat sebesar 1,2 juta KL (Kilo Liter) per tahun antara tahun 2015-2020, kecuali pada tahun 2020 ketika pandemi melanda dan menekan konsumsi bahan bakar fosil.Disamping itu, Produksi dalam negeri Indonesia tidak dapat menutupi peningkatan permintaan bensin dan Indonesia telah menjadi importir minyak sejak tahun 2004 dan dengan nilai impor yang terus meningkat.")
justify_text("Sejak tahun 2015 hingga 2020, bensin impor telah memasok sekitar 52% dari total konsumsi bensin setiap tahunnya.Keputusan pemerintah menaikkan harga eceran bensin bersubsidi pada pertengahan tahun 2022 berdampak pada inflasi sehingga menyebabkan indeks harga konsumen meningkat sebesar 5,95% pada September 2022 dan 5,71% pada Oktober 2022 YoY. Peralihan dari bahan bakar minyak ke sumber energi yang tidak terlalu berfluktuasi seperti listrik pada transportasi dapat membantu mengurangi masalah ini di masa depan.")

# BAGIAN PERTAMA, GRAFIK PERTAMA

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
df_melted = df.melt(id_vars=['Year'], value_vars=['Car', 'Motorcycle'], var_name='Vehicle', value_name='Unit Sales')

# Create grouped bar chart
fig = px.bar(df_melted, x='Year', y='Unit Sales', color='Vehicle',
             labels={'Year': 'Tahun', 'Unit Sales': 'Konsumsi Bahan Bakar (Million KL)'},
             title='Konsumsi Bahan Bakar Mobil dan Motor (2015-2020)',
             text='Unit Sales',
            )

# Update Traces
fig.update_traces(texttemplate='%{text:.3s}', textfont_size=18)

# Set x-axis to display only integer values
fig.update_xaxes(type='category', tickfont=dict(size=20), title_font=dict(size=20), title_standoff=10)

# Pengaturan sumbu Y
fig.update_yaxes(tickfont=dict(size=20), title_font=dict(size=20), range=[0,35])

# Update layout untuk judul berada di tengah
fig.update_layout(title={
                        'text': 'Konsumsi Bahan Bakar Mobil dan Motor (2015-2020)',
                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top',
                        'font': dict(size=30)
                        },
                annotations=[
                    dict(x=0.5,
                         y=-0.32,
                         showarrow=False,
                         text="Sumber Data: IESR",
                         xref="paper",
                         yref="paper",
                         font=dict(size=15)
                         )
                    ]
                )

# Show the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

justify_text("Kita juga bisa melihat seberapa besar konsumsi BBM RON 90 yaitu Pertalite pada setiap tahunnya. Menurut data Kementerian ESDM, sepanjang 2023 konsumsi bahan bakar minyak (BBM) RON 90 di Indonesia mencapai 29,77 juta kiloliter dari kuota 32,56 juta kiloliter, atau sekitar 91,43%. Pada Juni 2023, harga Pertalite dipatok Rp10.000 per liter, harga tersebut disebabkan adanya subsidi dari pemerintah. Adapun menurut Abra Talattov, Kepala Pusat Pangan, Energi, dan Pembangunan Berkelanjutan INDEF, murahnya harga Pertalite ini menjadi salah satu faktor penghambat adopsi kendaraan listrik")
justify_text("\"Sepanjang subsidi Pertalite sifatnya terbuka dan belum tertutup, ini tantangan bagi penjualan kendaraan listrik, khususnya sepeda motor, Karena semua golongan bisa mengakses BBM Pertalite, maka penggunaan mobil dan motor konvensional masih terjangkau secara operasional\", Kata Abra")

# BAGIAN PERTAMA, GRAFIK KEDUA

# Data (source: katadata dan ESDM)
tahun_bbm = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
kiloliter = [0.38, 5.81, 14.49, 17.71, 19.41, 18.14, 23.3, 29.68, 29.77] # dalam jutaan (million)

df = pd.DataFrame({
    'Tahun': tahun_bbm,
    'Konsumsi BBM (Jutaan KL)': kiloliter
})

# Membuat Plot
fig = px.bar(df, x='Tahun', y='Konsumsi BBM (Jutaan KL)',
             color='Konsumsi BBM (Jutaan KL)',
             color_continuous_scale='bluered',
             )

# Menambahkan judul dan labels
fig.update_layout(title={'text': 'Konsumsi BBM RON 90 (Pertalite) Kendaraan Indonesia Pada Tahun 2015 - 2023', 'x':0.5, 'y':1, 'xanchor':'center', 'yanchor':'top'},
                  title_font=dict(size=30),
                  xaxis_title="Tahun",
                  xaxis_title_font=dict(size=20),
                  xaxis=dict(tickfont=dict(size=20)),
                  yaxis_title="Konsumsi BBM (Jutaan KL)",
                  yaxis_title_font=dict(size=20),
                  yaxis=dict(tickfont=dict(size=20)),
                  annotations=[dict(text="Sumber Data : databoks.katadata.co.id dan www.esdm.go.id", showarrow=False, x=0.5, y=-0.26, xref='paper', yref='paper', font=dict(size=15))],
                  coloraxis_colorbar=dict(title="Jutaan KiloLiter")
                  )

# Update Sumbu X
fig.update_xaxes(title_standoff=10)

# Update Sumbu Y
fig.update_yaxes(range=[0, 35])

# Update Traces
fig.update_traces(text=kiloliter, textposition='outside', textfont_size=20)

# Menampilkan Grafik
st.plotly_chart(fig, use_container_width=True)

st.header("Penjualan Mobil Listrik di Indonesia")
justify_text("Menurut data penjualan wholesales alias pengiriman dari pabrik ke dealer yang dirilis oleh Gabungan Industri Kendaraan Bermotor Indonesia (Gaikindo), mobil listrik berbasis baterai (battery electric vehicle/BEV) mencatatkan penjualan sebanyak 17.062 unit atau melonjak sekitar 65,2% (yoy) dibandingkan tahun 2022. Capaian tersebut sekaligus menjadi rekor tertinggi baru.")
justify_text("Namun secara kumulatif, penjualan mobil BEV di Indonesia masih belum mampu menyaingi penjualan mobil konvensional. Bahkan, angka penjualannya juga masih jauh dari mobil hybrid, yang mencatatkan capaian penjualan sebanyak 54.656 unit dan ekspornya mencapai 27.710 unit pada 2023.")

# BAGIAN KEDUA, GRAFIK PERTAMA

# Data
tahun = [2020, 2021, 2022, 2023]
unit_penjualan = [125, 687, 10327, 17062]

# Create bar chart
fig = px.bar(x=tahun, y=unit_penjualan, labels={'x': 'Tahun', 'y': 'Unit Penjualan'},
             title='Unit Penjualan Mobil Listrik (2020-2023)',
             color=unit_penjualan,
             color_continuous_scale='tealgrn')

# Set x-axis to display only integer values
fig.update_xaxes(type='category', title_font=dict(size=20), tickfont=dict(size=20), title_standoff=10)

# Modifikasi Sumbu Y
fig.update_yaxes(title_font=dict(size=20), tickfont=dict(size=20), range=[0,20000])

# Ubah Posisi dan Ukuran Judul
fig.update_layout(title={'text': "Unit Penjualan Mobil Listrik (2020-2023)", 
                         'x': 0.5,
                         'y': 0.9,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                  title_font_size=30,
                  coloraxis_colorbar=dict(title='Unit Penjualan')
                  )

# Update Traces
fig.update_traces(text=unit_penjualan, textposition='outside', textfont_size=18)

# Menambahkan Anotasi dibawah grafik berupa sumber data
fig.add_annotation(xref= 'paper', yref='paper', x=0.5, y=-0.3,
                   text='Sumber Data: goodstats.id',
                   showarrow=False,
                   font=dict(size=15))

# Show the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.header("Jenis Mobil Yang Terjual")
justify_text("Mengutip data Gabungan Industri Kendaraan Bermotor Indonesia (Gaikindo), terdapat 10 model mobil listrik yang terdistribusi bervariasi dari merek China, Eropa hingga Jepang. Hyundai Ioniq 5 menjadi mobil listrik terlaris pada tahun 2023 dengan penjualan mencapai 7.176 unit, diikuti oleh Wuling Air EV sebanyak 5.575 unit.")
justify_text("Hal tersebut bisa terjadi karena Dua mobil listrik paling laris merupakan produksi dalam negeri, yakni Hyundai Ioniq 5 dan Wuling Air ev. Keduanya mendapatkan subsidi Pajak Pertambahan Nilai (PPN) dari 11% menjadi hanya 1%.Karena subsidi itu, maka potongan diskonnya tergolong lumayan. Setelah dihitung-hitung berkat 'subsidi' pemerintah, harga Wuling Air ev paling banyak dipotong Rp 26 jutaan untuk unit di harga Rp 300 jutaan.Sementara Hyundai Ioniq 5 mendapat subsidi Rp 60-75 juta bergantung tipenya. Tipe standard range dengan banderol Rp 681,9 juta mendapat subsidi lebih kecil, sementara long range dengan harga Rp 783,1 juta mendapat subsidi lebih besar.")

tab1, tab2, tab3, tab4 = st.tabs(["Penjualan Mobil Listrik 2020", "Penjualan Mobil Listrik 2021", "Penjualan Mobil Listrik 2022", "Penjualan Mobil Listrik 2023"])

with tab1:
    # BAGIAN KETIGA, GRAFIK PERTAMA (2020)
    merek_mobil_20 = ['Hyundai Ioniq Electric', 'Hyundai Kona Electric',
                      'BMW i3s', 'Lexus UX 300e']
    
    unit_terjual_20 = [81, 38, 5, 1]

    df = pd.DataFrame({
        'Merek Mobil': merek_mobil_20,
        'Unit Terjual': unit_terjual_20
    })

    fig = px.bar(df, x='Unit Terjual', y='Merek Mobil', orientation='h',
                 text='Unit Terjual', title='Penjualan 4 Mobil Listrik Terlaris 2020',
                 color_discrete_sequence=['#E74C3C'])
    
    fig.update_traces(texttemplate='%{text}', textposition='outside', textfont_size=20)

    fig.update_layout(title={'text': 'Penjualan 4 Mobil Listrik Terlaris 2020', 'x': 0.5, 'y': 0.9,'xanchor': 'center', 'yanchor': 'top'},
                    title_font_size=30,
                    xaxis_title="Unit Terjual",
                    yaxis_title="Merek Mobil",
                    xaxis_tickformat=',d',
                    yaxis_categoryorder="total ascending",
                    xaxis=dict(tickfont=dict(size=15)),
                    yaxis=dict(tickfont=dict(size=15)),
                    annotations=[dict(x=0.5, y=-0.31, showarrow=False, text='Sumber Data: cnnindonesia.com dan databoks.katadata.co.id', xref='paper', yref='paper', font=dict(size=15))]
                    )
    
    fig.update_xaxes(title_font=dict(size=20))

    fig.update_yaxes(title_font=dict(size=20))

    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # BAGIAN KETIGA, GRAFIK KEDUA (2021)
    merek_mobil_21 = ['Hyundai Kona EV', 'Hyundai Ioniq EV', 'All New Nissan Leaf',
                      'Lexus UX 300e', 'Toyota Coms EV', 'Toyota C+Pod EV',
                      'DFSK Gelora E']
    
    unit_terjual_21 = [360, 228, 42, 26, 20, 7, 2]

    df = pd.DataFrame({
        'Merek Mobil': merek_mobil_21,
        'Unit Terjual': unit_terjual_21
    })

    fig = px.bar(df, x='Unit Terjual', y='Merek Mobil', orientation='h',
                 text='Unit Terjual', title='Penjualan 7 Mobil Listrik Terlaris 2021',
                 color_discrete_sequence=['#F39C12'])
    
    fig.update_traces(texttemplate='%{text}', textposition='outside', textfont_size=20)

    fig.update_layout(title={'text': 'Penjualan 7 Mobil Listrik Terlaris 2021', 'x': 0.5, 'y': 0.9,'xanchor': 'center', 'yanchor': 'top'},
                    title_font_size=30,
                    xaxis_title="Unit Terjual",
                    yaxis_title="Merek Mobil",
                    xaxis_tickformat=',d',
                    yaxis_categoryorder="total ascending",
                    xaxis=dict(tickfont=dict(size=15)),
                    yaxis=dict(tickfont=dict(size=15)),
                    annotations=[dict(x=0.5, y=-0.31, showarrow=False, text='Sumber Data: otomotif.kompas.com', xref='paper', yref='paper', font=dict(size=15))]
                    )
    
    fig.update_xaxes(title_font=dict(size=20))

    fig.update_yaxes(title_font=dict(size=20))

    st.plotly_chart(fig, use_container_width=True)

with tab3:
    # BAGIAN KETIGA, GRAFIK KETIGA (2022)
    merek_mobil_22 = ['Wuling Air EV', 'Hyundai Ioniq 5', 'Nissan Leaf',
                      'Hyundai Ioniq EV', 'Lexus UX300e', 'Mini Cooper Electric',
                      'Hyundai Kona EV', 'Hyundai Genesis G80 EV', 'DFSK Gelora']
    
    unit_terjual_22 = [5921, 1786, 52, 45, 42, 26, 20, 10, 9]

    df = pd.DataFrame({
        'Merek Mobil': merek_mobil_22,
        'Unit Terjual': unit_terjual_22
    })

    fig = px.bar(df, x='Unit Terjual', y='Merek Mobil', orientation='h',
                 text='Unit Terjual', title='Penjualan 9 Mobil Listrik Terlaris 2022',
                 color_discrete_sequence=['#2E86C1'])
    
    fig.update_traces(texttemplate='%{text}', textposition='outside', textfont_size=20)

    fig.update_layout(title={'text': 'Penjualan 9 Mobil Listrik Terlaris 2022', 'x': 0.5, 'y': 0.9,'xanchor': 'center', 'yanchor': 'top'},
                    title_font_size=30,
                    xaxis_title="Unit Terjual",
                    yaxis_title="Merek Mobil",
                    xaxis_tickformat=',d',
                    yaxis_categoryorder="total ascending",
                    xaxis=dict(tickfont=dict(size=15)),
                    yaxis=dict(tickfont=dict(size=15)),
                    annotations=[dict(x=0.5, y=-0.31, showarrow=False, text='Sumber Data: oto.detik.com', xref='paper', yref='paper', font=dict(size=15))]
                    )
    
    fig.update_xaxes(title_font=dict(size=20))

    fig.update_yaxes(title_font=dict(size=20))

    st.plotly_chart(fig, use_container_width=True)

with tab4:
    # BAGIAN KETIGA, GRAFIK KEEMPAT (2023)

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
                text="Unit Terjual", title="Penjualan 10 Mobil Listrik Terlaris 2023",
                color_discrete_sequence=['#27AE60'])

    # Customize the chart
    fig.update_traces(texttemplate='%{text}', textposition='outside', textfont_size=20)

    fig.update_layout(title={'text': 'Penjualan 10 Mobil Listrik Terlaris 2023', 'x': 0.5, 'y': 0.9,'xanchor': 'center', 'yanchor': 'top'},
                    title_font_size=30,
                    xaxis_title="Unit Terjual",
                    yaxis_title="Merek Mobil",
                    xaxis_tickformat=',d',
                    yaxis_categoryorder="total ascending",
                    xaxis=dict(tickfont=dict(size=15)),
                    yaxis=dict(tickfont=dict(size=15)),
                    annotations=[dict(x=0.5, y=-0.31, showarrow=False, text='Sumber Data: cnnindonesia.com', xref='paper', yref='paper', font=dict(size=15))]
                    )

    fig.update_xaxes(title_font=dict(size=20))

    fig.update_yaxes(title_font=dict(size=20))

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

css = '''
<style>
.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.77rem;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

justify_text("Berdasarkan data untuk penjualan mobil listrik tahun 2020, 2021, 2022, dan 2023. Kita dapat melihat bahwa untuk mobil listrik yang populer pada tahun 2020 adalah Hyundai Ioniq Electric, lalu pada 2021 adalah Hyundai Kona,  lalu pada 2022 adalah Wuling Air EV, dan pada 2023 adalah Hyundai Ioniq 5.")
justify_text("Dari data tersebut terlihat bahwa kebanyakan dari tahun ke tahun merek mobil listrik yang laris di indonesia adalah dari Hyundai dan dari Wuling. Hal tersebut bisa terjadi karena harganya yang sudah disubsidi oleh pemerintah. Namun perlu diketahui bahwa harga tersebut masih terbilang tinggi karena jika dibandingkan dengan mobil konvensional harganya bisa mencapai 2 kali lipatnya. Contohnya untuk Hyundai Ioniq yang berharga 600 jutaan dimana pada mobil konvensional masyarakat bisa membeli mobil berbahan bakar BBM di harga 300 jutaan.")

st.header("Faktor Untuk Percepatan Adopsi Kendaraan Listrik di Indonesia")
justify_text("Walaupun penjualan kendaraan listrik di indonesia terus meningkat setiap tahunnya, namun ternyata angka tersebut masih belum mencapai target yang ditetapkan pemerintah. Diperlukan langkah-langkah agar meningkatkan minat beli masyarakat terhadap kendaraan listrik, berdasarkan survey yang dilakukan oleh PwC indonesia, terdapat beberapa halangan yang membuat masyarakat indonesia belum mau membeli kendaran listrik.")
justify_text("Pertanyaan yang diajukan adalah sebagai berikut : Anda sebelumnya menyatakan bahwa Anda tidak mempertimbangkan untuk membeli mobil listrik atau sepeda motor. Apa beberapa hambatan yang menghalangi Anda untuk melakukannya?")

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
             labels={"value": "Persentase"},
             color_discrete_map={"Motor Listrik": "#FF9B00", "Mobil Listrik": "#D30000"})  

# Customize the layout
fig.update_layout(barmode="group", yaxis_title="", xaxis_title="Persentase",
                  title={'text': '5 Halangan dalam Membeli Kendaraan Listrik di Indonesia', 'x':0.5, 'y':0.9, 'xanchor': 'center', 'yanchor': 'top'},
                  title_font_size=30,
                  xaxis=dict(title='Persentase', tickfont=dict(size=20), title_font=dict(size=20), title_standoff=10),
                  yaxis=dict(tickfont=dict(size=18)),
                  annotations=[dict(x=0.5, y=-0.31, showarrow=False, text='Sumber Data: PWC Indonesia', xref='paper', yref='paper', font=dict(size=15))]
                  )

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

justify_text("kekhawatiran konsumen dapat berdampak signifikan terhadap angka ini. Mengatasi kekhawatiran ini bukan hanya tanggung jawab pelaku industri tetapi juga pembuat kebijakan, dan pengembang infrastruktur. Hasil survei menunjukkan angka yang sangat mirip antar responden baik untuk mobil listrik maupun sepeda motor. Paragraf ini akan menggunakan persentase mobil listrik sebagai representasi dari hasil survei. Salah satu kekhawatiran utama di antara 63% responden adalah kesulitan dalam menemukan stasiun pengisian daya dan menyoroti perlunya infrastruktur pengisian daya yang kuat, terutama di daerah terpencil (54%). Waktu yang dibutuhkan untuk mengisi daya kendaraan juga merupakan faktor penting (39%); konsumen sudah terbiasa dengan proses pengisian bahan bakar yang cepat pada mobil tradisional, dan terdapat persepsi bahwa pengisian bahan bakar kendaraan listrik memerlukan waktu yang lama sehingga dapat membuat calon pembeli enggan.")

st.header("Kesimpulan dan Saran")
st.write("Pemerintah harus memprioritaskan insentif kendaraan listrik untuk transportasi umum, E2W (pembangunan baru atau retrofit), dan infrastruktur pengisian daya. Insentif transportasi umum dimaksudkan untuk lebih mendukung strategi dekarbonisasi dengan membuat strategi peralihan menjadi lebih menarik dan terjangkau. Insentif untuk E2W mungkin akan memberikan manfaat yang signifikan bagi mereka yang menggunakannya untuk mencari nafkah, seperti pengemudi transportasi online atau pengemudi logistik, karena pengemudi dapat menghemat lebih banyak uang bagi pengguna dan periode pengembalian modal yang lebih cepat dari pemerintah. Memberikan insentif untuk investasi pada infrastruktur pengisian daya telah terbukti 4–7 kali lebih efektif dibandingkan program insentif kendaraan listrik langsung.")

# GRAFIK KELIMA

# Data
labels = ['Jawa & Bali', 'Sumatera', 'Sulawesi', 'Kalimantan', 'Lainnya']
values = [88.1, 5.6, 2.6, 2.3, 1.4]

# Membuat Donut Chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,textfont=dict(size=23))],
                layout=go.Layout(title=dict(text="Distribusi SPKLU Nasional", x=0.33, y=1, font=dict(size=20)), legend=dict(font=dict(size=30)))
               )

# Menampilkan di Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write("Beberapa poin penting untuk menjadi perhatian pemerintah dan pelaku industri adalah :")
justify_text("1. Insentif Kendaraan Listrik diperlukan terutama untuk motor listrik sehingga lebih terjangkau oleh masyarakat, selain itu terdapat juga potensi salah sasaran dari subsidi pemerintah dimana yang dapat membeli mobil listrik berharga 600 jutaan keatas adalah dari kalangan Ekonomi atas")
justify_text("2. Distribusi lokasi dan jumlah SPKLU dan juga SPBKLU perlu ditingkatkan sehingga masyarakat lebih percaya untuk menggunakan kendaraan listrik di berbagai daerah, bukan hanya pada daerah kota besar yang notabenenya memiliki SPKLU dan SPBKLU lebih banyak dibandingkan daerah lain seperti pada jalan tol maupun kota kecil")
justify_text("3. Indonesia dapat menjadi salah satu pemain penting dalam produksi kendaraan listrik di dunia karena indonesia memiliki cadangan nikel yang cukup banyak dimana nikel menjadi salah satu bahan mineral tambang yang merupakan bahan untuk membuat baterai kendaraan listrik")
justify_text("4. Riset kendaraan listrik perlu ditingkatkan karena kita sudah ketinggalan oleh tiongkok, amerika serikat, dan eropa. Risetnya dapat mencakup ketahanan dan keamanan dari baterai kendaraan listrik, riset port charging pada stasiun pengisian daya, maupun efisiensi kendaraan sehingga meningkatakan kecepatan dan jarak tempuh.")

