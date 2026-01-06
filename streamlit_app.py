import streamlit as st

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="NanoSmart Packaging",
    page_icon="🧫🥩",
    layout="centered"
)

# =============================
# JUDUL
# =============================
st.title("🧫🥩 NanoSmart Packaging")
st.subheader("Simulasi Kemasan Pintar Berbasis Nanoteknologi")

st.write("""untuk mendeteksi **kesegaran pangan**  
berdasarkan **jenis kemasan nano, suhu, dan lama penyimpanan**.
""")

st.divider()

# =============================
# INPUT DATA
# =============================
st.header("🔍 Input Data Penyimpanan")

jenis_pangan = st.selectbox(
    "Jenis Pangan",
    ["Daging", "Ikan", "Buah", "Sayur", "Produk Olahan"]
)

jenis_nano = st.selectbox(
    "Jenis Nano Packaging",
    [
        "Nano-Perak (AgNP)",
        "Nano-ZnO",
        "Nano-Kitosan",
        "Nano-Clay"
    ]
)

suhu = st.slider("Suhu Penyimpanan (°C)", 0, 30, 4)
lama = st.slider("Lama Penyimpanan (hari)", 1, 30, 7)

st.divider()

# =============================
# PROSES ANALISIS
# =============================
if st.button("🔬 Analisis Kesegaran"):

    skor = 100

    # Pengaruh suhu
    if suhu > 10:
        skor -= 30

    # Pengaruh waktu
    if lama > 10:
        skor -= 40

    # Efektivitas nano material
    if "Perak" in jenis_nano:
        skor += 20
    elif "ZnO" in jenis_nano:
        skor += 15
    elif "Kitosan" in jenis_nano:
        skor += 10
    elif "Clay" in jenis_nano:
        skor += 5

    # Batas skor
    skor = max(0, min(skor, 100))

    st.header("📊 Hasil Analisis")

    if skor >= 80:
        st.success("🟢 Status Pangan: SEGAR")
        indikator = "Hijau"
    elif skor >= 50:
        st.warning("🟡 Status Pangan: MULAI MENURUN")
        indikator = "Kuning"
    else:
        st.error("🔴 Status Pangan: TIDAK LAYAK KONSUMSI")
        indikator = "Merah"

    st.write(f"**Warna indikator kemasan:** {indikator}")
    st.write(f"**Skor kesegaran:** {skor} / 100")

    st.info("""
    ⚠️ Catatan:
    Hasil ini merupakan simulasi berbasis literatur nanoteknologi pangan,
    bukan hasil pengukuran eksperimental langsung.
    """)

st.divider()

# =============================
# EDUKASI
# =============================
st.header("📚 Edukasi NanoSmart Packaging")

st.write("""
NanoSmart Packaging memanfaatkan material nano
untuk meningkatkan keamanan pangan,
memperlambat pertumbuhan mikroba,
dan memberikan **indikator visual kesegaran**
berdasarkan perubahan kondisi lingkungan.
""")
