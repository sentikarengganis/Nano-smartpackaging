import streamlit as st

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="Nano Smart Packaging",
    page_icon="🧫🥩",
    layout="centered"
)

# =============================
# BACKGROUND GRADIENT
# =============================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #FFFFFF 0%,
            #FFE0B2 50%,
            #FFB74D 100%
        );
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# SESSION STATE
# =============================
if "mulai" not in st.session_state:
    st.session_state.mulai = False

# =============================
# JUDUL
# =============================
st.title("🧫🥩 NanoSmart Packaging")
st.subheader("Simulasi Kemasan Pintar Berbasis Nanoteknologi")
st.divider()

# =============================
# TOMBOL MULAI
# =============================
if not st.session_state.mulai:
    st.button(
        "▶ Mulai Input Data",
        use_container_width=True,
        on_click=lambda: st.session_state.update({"mulai": True})
    )

# =============================
# INPUT DATA
# =============================
if st.session_state.mulai:

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
    if st.button("🔬 Analisis Kesegaran", use_container_width=True):

        skor = 100

        # ======================
        # Pengaruh Suhu (Literatur)
        # ======================
        if suhu <= 4:
            skor += 10          # cold storage memperpanjang shelf life
        elif suhu <= 10:
            skor -= 5           # masih relatif aman
        elif suhu <= 20:
            skor -= 20          # mulai berisiko
        else:
            skor -= 40          # suhu tinggi = cepat rusak

        # ======================
        # Pengaruh Waktu Simpan
        # ======================
        if lama <= 3:
            skor += 5
        elif lama <= 7:
            skor -= 5
        elif lama <= 14:
            skor -= 20
        else:
            skor -= 40

        # ======================
        # Efektivitas Nano Material
        # ======================
        if "Perak" in jenis_nano:
            skor += 20
        elif "ZnO" in jenis_nano:
            skor += 15
        elif "Kitosan" in jenis_nano:
            skor += 10
        elif "Clay" in jenis_nano:
            skor += 5

        # Batasi skor 0–100
        skor = max(0, min(skor, 100))

        # ======================
        # OUTPUT HASIL
        # ======================
        st.header("📊 Hasil Analisis")

        if skor >= 80:
            st.success("🟢 Status Pangan: AMAN BRO 🥂")
            st.balloons()
            indikator = "Hijau"
            keterangan = """
Pangan berada dalam kondisi aman untuk dikonsumsi.
Kemasan nano bekerja optimal dalam menjaga mutu produk.
"""
        elif skor >= 50:
            st.warning("🟡 Status Pangan: AGAK NGERI 😱")
            indikator = "Kuning"
            keterangan = """
Pangan mulai mengalami penurunan kualitas.
Masih dapat dikonsumsi dengan kehati-hatian.
"""
        else:
            st.error("🔴 Status Pangan: BAHAYA BRO ☠️")
            indikator = "Merah"
            keterangan = """
Pangan berada dalam kondisi tidak aman untuk dikonsumsi.
Disarankan untuk tidak mengonsumsi produk.
"""

        st.write(f"**Warna indikator kemasan:** {indikator}")
        st.write(f"**Skor kesegaran:** {skor} / 100")
        st.info(keterangan)

        st.error("""
⚠️ Catatan  
Hasil ini merupakan simulasi berbasis literatur nanoteknologi pangan,
bukan hasil pengukuran eksperimental langsung.
""")

    st.divider()

    # =============================
    # EDUKASI
    # =============================
    st.header("📖 NanoSmart Packaging")
    st.write("""
NanoSmart Packaging memanfaatkan material nano untuk meningkatkan
keamanan pangan, memperlambat pertumbuhan mikroba, serta memberikan
indikator visual kesegaran berdasarkan suhu, waktu penyimpanan,
dan jenis kemasan nano.
""")

    # =============================
    # TOMBOL KEMBALI
    # =============================
    if st.button("⬅ Kembali ke Awal"):
        st.session_state.mulai = False

