import pandas as pd
import streamlit as st

DATA_PATH = "data/dataset_umkm_final_dengan_klaster.csv"

NAMA_KLASTER = {
    0: "Digital Laggard",
    2: "Digital Beginner",
    3: "Digital Adopter",
    1: "Digital Champion"
}

WARNA_KLASTER = {
    "Digital Laggard"  : "#E24B4A",
    "Digital Beginner" : "#FAC775",
    "Digital Adopter"  : "#1D9E75",
    "Digital Champion" : "#378ADD"
}

REKOMENDASI_KLASTER = {
    "Digital Champion" : (
        "UMKM ini sudah sangat siap digital. "
        "Fokus selanjutnya: ekspansi ke pasar ekspor, "
        "optimalkan iklan berbayar, dan jadikan mentor UMKM lain."
    ),
    "Digital Adopter" : (
        "Sudah aktif digital tapi belum optimal. "
        "Tingkatkan frekuensi konten, coba multi-platform marketplace, "
        "dan mulai gunakan tools analitik penjualan."
    ),
    "Digital Beginner" : (
        "Baru memulai perjalanan digital. "
        "Prioritas: daftar ke 1-2 marketplace utama (Shopee/Tokopedia), "
        "aktifkan QRIS, dan ikuti pelatihan digital gratis Kemenkop."
    ),
    "Digital Laggard" : (
        "Belum memanfaatkan teknologi digital sama sekali. "
        "Langkah pertama: buat akun media sosial bisnis, "
        "aktifkan pembayaran digital, dan minta pendampingan dari dinas UMKM setempat."
    )
}

@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    if 'nama_klaster' not in df.columns:
        df['nama_klaster'] = df['klaster'].map(NAMA_KLASTER)
    return df

def get_ringkasan(df: pd.DataFrame) -> dict:
    return {
        "total_umkm"     : len(df),
        "avg_score"      : df['digital_readiness_score'].mean().round(1),
        "pct_belum_siap" : round((df['digital_readiness_score'] < 50).sum() / len(df) * 100, 1),
        "sektor_terbaik" : df.groupby('sektor')['digital_readiness_score'].mean().idxmax(),
        "prov_terbaik"   : df.groupby('provinsi')['digital_readiness_score'].mean().idxmax(),
    }