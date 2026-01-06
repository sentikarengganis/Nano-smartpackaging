import streamlit as st

st.set_page_config(
    page_title="Jenis Nano Packaging",
    page_icon="🌬️",
    layout="centered"
)

# =============================
# BACKGROUND GRADIENT ORANGE - PUTIH
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

st.title("📘 Jenis Nano Packaging")
st.write(
    "Berikut adalah jenis-jenis *nano material* yang umum digunakan "
    "dalam *NanoSmart Packaging* untuk menjaga kualitas dan keamanan pangan."
)

st.divider()

# =====================
# NANO PERAK
# =====================
st.subheader("🧫 Nano-Perak (AgNP)")
st.write("""
Nano-Perak (Silver Nanoparticles) dikenal memiliki *sifat antimikroba yang sangat kuat*.
Material ini mampu:
- Menghambat pertumbuhan bakteri dan jamur
- Memperpanjang umur simpan pangan
- Banyak digunakan pada kemasan *daging, ikan, dan produk segar*

⚠️ Penggunaan harus terkontrol agar tetap aman bagi konsumen.
""")

# =====================
# NANO ZNO
# =====================
st.subheader("⚗️ Nano-Zinc Oxide (ZnO)")
st.write("""
Nano-ZnO memiliki kemampuan *antibakteri dan antioksidan*.
Keunggulannya:
- Stabil pada suhu tinggi
- Melindungi pangan dari sinar UV
- Aman digunakan dalam kemasan pangan

Sering digunakan pada kemasan plastik berbasis polimer.
""")

# =====================
# NANO KITOSAN
# =====================
st.subheader("🌿 Nano-Kitosan")
st.write("""
Nano-Kitosan berasal dari *kulit udang atau kepiting* sehingga bersifat alami.
Keunggulan utama:
- Biodegradable dan ramah lingkungan
- Menghambat bakteri gram positif
- Cocok untuk konsep *green packaging*

Banyak diteliti sebagai alternatif kemasan berkelanjutan.
""")

# =====================
# NANO CLAY
# =====================
st.subheader("🪨 Nano-Clay")
st.write("""
Nano-Clay digunakan untuk meningkatkan *kekuatan dan daya tahan kemasan*.
Fungsi utamanya:
- Menghambat masuknya oksigen dan uap air
- Menjaga kelembaban pangan
- Biasanya dikombinasikan dengan plastik atau biopolimer

Tidak bersifat antimikroba, tetapi sangat efektif sebagai *barrier protection*.
""")

st.divider()

st.info(
    "📌 Halaman ini bersifat *edukatif* dan disusun berdasarkan "
    "literatur nanoteknologi pangan."
)
