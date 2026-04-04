import streamlit as st
from utils import (
    load_data, get_ringkasan,
    grafik_distribusi_score, grafik_pie_klaster,
    grafik_score_per_sektor, grafik_score_per_provinsi,
    grafik_pca_klaster, grafik_radar_klaster,
    prediksi_klaster
)
from utils.data_loader import WARNA_KLASTER

# ── Konfigurasi halaman ──────────────────────────────────────
st.set_page_config(
    page_title="UMKM Digital Readiness",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ── Custom CSS Dark Mode ─────────────────────────────────────
st.markdown("""

""", unsafe_allow_html=True)


# ── Load data ────────────────────────────────────────────────
df = load_data()

# ── Sidebar navigasi ─────────────────────────────────────────
st.sidebar.title("📊 UMKM Digital Readiness")
st.sidebar.markdown("AI Impact Challenge 2026")
st.sidebar.divider()

halaman = st.sidebar.radio(
    "Navigasi",
    ["🏠 Beranda", "🔍 Eksplorasi Data", "🤖 Prediksi Klaster"],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.caption("Dibuat dengan Python + Streamlit")
st.sidebar.caption("Dataset: 1.000 UMKM Indonesia")

# ════════════════════════════════════════════════════════════
# HALAMAN 1: BERANDA
# ════════════════════════════════════════════════════════════
if halaman == "🏠 Beranda":
    st.title("📊 UMKM Digital Readiness Dashboard")
    st.markdown(
        "Sistem klasterisasi UMKM Indonesia berdasarkan tingkat "
        "kesiapan digital menggunakan algoritma **K-Means Clustering**."
    )
    st.divider()

    # Metrik utama
    ringkasan = get_ringkasan(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total UMKM", f"{ringkasan['total_umkm']:,}")
    col2.metric("Rata-rata Score", f"{ringkasan['avg_score']}")
    col3.metric("Belum Siap Digital", f"{ringkasan['pct_belum_siap']}%")
    col4.metric("Sektor Terbaik", ringkasan['sektor_terbaik'])

    st.divider()

    # Dua grafik utama berdampingan
    col_a, col_b = st.columns(2)
    with col_a:
        st.plotly_chart(grafik_distribusi_score(df), use_container_width=True)
    with col_b:
        st.plotly_chart(grafik_pie_klaster(df), use_container_width=True)

    st.divider()

    # Ringkasan klaster
    st.subheader("Ringkasan 4 Klaster UMKM")
    cols = st.columns(4)
    urutan = ["Digital Champion", "Digital Adopter",
              "Digital Beginner", "Digital Laggard"]
    emoji  = ["🏆", "📈", "🌱", "⚠️"]

    for col, nama, em in zip(cols, urutan, emoji):
        subset = df[df['nama_klaster'] == nama]
        avg    = subset['digital_readiness_score'].mean()
        jumlah = len(subset)
        warna  = WARNA_KLASTER.get(nama, "#888")
        col.markdown(
            f"""

                
{em}

                
{nama}

                
{jumlah} UMKM

                
Avg Score: {avg:.1f}

            
""",
            unsafe_allow_html=True
        )

# ════════════════════════════════════════════════════════════
# HALAMAN 2: EKSPLORASI DATA
# ════════════════════════════════════════════════════════════
elif halaman == "🔍 Eksplorasi Data":
    st.title("🔍 Eksplorasi Data UMKM")
    st.markdown("Analisis distribusi dan pola digital readiness UMKM Indonesia.")
    st.divider()

    # Filter sidebar
    st.sidebar.subheader("Filter Data")
    sektor_pilihan = st.sidebar.multiselect(
        "Sektor Usaha",
        options=df['sektor'].unique().tolist(),
        default=df['sektor'].unique().tolist()
    )
    skala_pilihan = st.sidebar.multiselect(
        "Skala Usaha",
        options=df['skala_usaha'].unique().tolist(),
        default=df['skala_usaha'].unique().tolist()
    )

    # Terapkan filter
    df_filtered = df[
        (df['sektor'].isin(sektor_pilihan)) &
        (df['skala_usaha'].isin(skala_pilihan))
    ]

    st.caption(f"Menampilkan {len(df_filtered):,} dari {len(df):,} UMKM")
    st.divider()

    # Grafik per sektor dan provinsi
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            grafik_score_per_sektor(df_filtered),
            use_container_width=True
        )
    with col2:
        st.plotly_chart(
            grafik_score_per_provinsi(df_filtered),
            use_container_width=True
        )

    st.divider()

    # Visualisasi PCA dan Radar
    col3, col4 = st.columns(2)
    with col3:
        fig_pca = grafik_pca_klaster(df_filtered)
        if fig_pca:
            st.plotly_chart(fig_pca, use_container_width=True)
        else:
            st.info("Kolom PCA tidak ditemukan di dataset.")
    with col4:
        st.plotly_chart(
            grafik_radar_klaster(df_filtered),
            use_container_width=True
        )

    st.divider()

    # Tabel data mentah
    with st.expander("Lihat data mentah"):
        st.dataframe(
            df_filtered[[
                'id_umkm', 'provinsi', 'sektor', 'skala_usaha',
                'digital_readiness_score', 'nama_klaster'
            ]].reset_index(drop=True),
            use_container_width=True
        )
# ════════════════════════════════════════════════════════════
# HALAMAN 3: PREDIKSI KLASTER
# ════════════════════════════════════════════════════════════
elif halaman == "🤖 Prediksi Klaster":
    from utils.templates import card_hasil_prediksi

    st.title("🤖 Prediksi Klaster UMKM Kamu")
    st.markdown(
        "Masukkan data UMKM untuk mengetahui klaster digital readiness "
        "dan mendapatkan rekomendasi yang tepat sasaran."
    )
    st.divider()

    col_form, col_result = st.columns([1, 1], gap="large")

    with col_form:
        st.subheader("Input Data UMKM")

        punya_smartphone = st.selectbox(
            "Punya smartphone?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )
        punya_medsos = st.selectbox(
            "Punya akun media sosial bisnis?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )
        punya_marketplace = st.selectbox(
            "Sudah jualan di marketplace?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )
        jumlah_platform = st.slider(
            "Jumlah platform marketplace", 0, 3, 0
        )
        frekuensi_posting = st.slider(
            "Frekuensi posting per minggu", 0, 5, 0
        )
        pakai_pembayaran = st.selectbox(
            "Menerima pembayaran digital?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )
        persen_omzet = st.slider(
            "Persentase omzet dari online (%)", 0, 100, 0
        )
        ikut_pelatihan = st.selectbox(
            "Pernah ikut pelatihan digital?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )
        punya_website = st.selectbox(
            "Punya website/toko online?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )
        pakai_tools = st.selectbox(
            "Pakai tools manajemen digital?", [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )

        tombol = st.button(
            "🔍 Prediksi Sekarang",
            use_container_width=True
        )

    with col_result:
        st.subheader("Hasil Prediksi")

        if tombol:
            input_data = {
                'punya_smartphone'         : punya_smartphone,
                'punya_medsos_bisnis'      : punya_medsos,
                'punya_marketplace'        : punya_marketplace,
                'jumlah_platform'          : jumlah_platform,
                'frekuensi_posting_mgg'    : frekuensi_posting,
                'pakai_pembayaran_digital' : pakai_pembayaran,
                'persen_omzet_online'      : persen_omzet,
                'ikut_pelatihan_digital'   : ikut_pelatihan,
                'punya_website'            : punya_website,
                'pakai_tools_manajemen'    : pakai_tools
            }

            try:
                hasil = prediksi_klaster(input_data)

                EMOJI_MAP = {
                    "Digital Champion" : "🏆",
                    "Digital Adopter"  : "📈",
                    "Digital Beginner" : "🌱",
                    "Digital Laggard"  : "⚠️"
                }

                nama  = hasil['nama']
                score = hasil['score']
                saran = hasil['rekomendasi']
                warna = WARNA_KLASTER.get(nama, '#888')
                em    = EMOJI_MAP.get(nama, '📍')

                html = card_hasil_prediksi(
                    nama=nama,
                    score=score,
                    saran=saran,
                    warna=warna,
                    em=em
                )
                st.markdown(html, unsafe_allow_html=True)

            except FileNotFoundError as e:
                st.error(str(e))

        else:
            st.info("Isi form di sebelah kiri lalu klik Prediksi.")


