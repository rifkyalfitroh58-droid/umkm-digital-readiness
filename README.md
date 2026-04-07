# DigiMap UMKM — Digital Readiness Clustering Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![Azure](https://img.shields.io/badge/Microsoft_Azure-App_Service-0078D4)
![License](https://img.shields.io/badge/License-MIT-green)

> Submission untuk **AI Impact Challenge 2026**
> Microsoft Elevate Training Center x Dicoding
> Tema: UMKM Go-Online

---

## Deskripsi

**DigiMap UMKM** adalah dashboard analitik berbasis AI yang
memetakan tingkat kesiapan digital (digital readiness) pelaku
UMKM Indonesia menggunakan algoritma K-Means Clustering.

Sistem ini mengelompokkan UMKM ke dalam 4 klaster:
- Digital Laggard — belum memanfaatkan teknologi digital
- Digital Beginner — baru memulai perjalanan digital
- Digital Adopter — aktif digital tapi belum optimal
- Digital Champion — sudah sangat siap digital

Setiap klaster dilengkapi rekomendasi aksi konkret yang
tepat sasaran untuk mendorong digitalisasi UMKM Indonesia.

---

## Demo & Links

| | Link |
|--|------|
| Live Demo | https://umkm-digital-readiness-4gv3rszqfebjgbvtm9uazz.streamlit.app/ |
| Google Colab | https://colab.research.google.com/drive/1kVF2R0lwc5BNEEYjzJGCsq8-viqiNQZ0?usp=sharing |
| Proposal | https://github.com/rifkyalfitroh58-droid/umkm-digital-readiness |

---

## Arsitektur Sistem

```
[Synthetic Dataset]
        ↓
[Google Colab — EDA + K-Means Clustering]
        ↓
[Model .pkl + Dataset .csv]
        ↓
[Streamlit Dashboard]
        ↓
[Microsoft Azure App Service]
        ↓
[User — Browser]
```

---

## Fitur Utama

- Kalkulasi Digital Readiness Score (0-100) otomatis
  berdasarkan 10 indikator adopsi digital UMKM
- K-Means Clustering menghasilkan 4 klaster UMKM
- Dashboard eksplorasi data interaktif dengan filter
  sektor dan skala usaha
- Visualisasi: distribusi score, score per sektor,
  score per provinsi, radar chart, PCA 2D
- Prediksi klaster real-time dengan rekomendasi aksi
- Dark mode profesional berbasis Streamlit
- Arsitektur modular (clean code)

---

## Teknologi

| Kategori | Teknologi |
|----------|-----------|
| Language | Python 3.10 |
| ML/AI | Scikit-learn (K-Means, PCA, StandardScaler) |
| Data | Pandas, NumPy |
| Visualisasi | Plotly, Seaborn, Matplotlib |
| Dashboard | Streamlit |
| Model Storage | Joblib |
| Cloud Deploy | Microsoft Azure App Service |
| Version Control | GitHub |
| Development | Google Colab, VS Code |

---

## Struktur Folder

```
umkm-digital-readiness/
├── app.py                  # Entry point dashboard
├── requirements.txt        # Dependencies
├── startup.sh              # Azure startup config
├── .gitignore
├── README.md
│
├── data/
│   └── dataset_umkm_final_dengan_klaster.csv
│
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
└── utils/                  # Modular code
    ├── __init__.py
    ├── data_loader.py      # Load & cache data
    ├── visualizations.py   # Semua fungsi grafik
    ├── predictor.py        # Prediksi klaster
    └── templates.py        # HTML card templates
```

---

## Cara Menjalankan Lokal

### 1. Clone repository
```bash
git clone https://github.com/rifkyalfitroh58-droid/umkm-digital-readiness.git
cd umkm-digital-readiness
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan dashboard
```bash
streamlit run app.py
```

### 4. Buka di browser
```
http://localhost:8501
```

---

## Cara Menjalankan Model di Colab

1. Buka [Google Colab Notebook](https://colab.research.google.com/drive/1kVF2R0lwc5BNEEYjzJGCsq8-viqiNQZ0?usp=sharing)
2. Klik **Runtime → Run all**
3. Semua sel akan berjalan otomatis:
   - Generate synthetic dataset
   - EDA & visualisasi
   - K-Means clustering
   - Evaluasi model
   - Export model .pkl

---

## Hasil Model

| Metrik | Nilai |
|--------|-------|
| Algoritma | K-Means Clustering |
| Jumlah data | 1.000 UMKM |
| Jumlah fitur | 10 indikator |
| Jumlah klaster | 4 |
| Silhouette Score | 0.2324 |
| Davies-Bouldin Score | 1.6684 |

### Distribusi Klaster

| Klaster | Jumlah | Persentase |
|---------|--------|------------|
| Digital Laggard | 330 | 33.0% |
| Digital Beginner | 373 | 37.3% |
| Digital Adopter | 86 | 8.6% |
| Digital Champion | 211 | 21.1% |

---

## Dataset

Dataset yang digunakan adalah **synthetic dataset** yang
dibuat berdasarkan distribusi statistik riil dari:

- Laporan PL-KUMKM 2023 — BPS & Kemenkop UKM
- Laporan INDEF 2024 tentang Platform Digital & UMKM
- Data adopsi digital UMKM — Kementerian Kominfo 2024

Penggunaan synthetic dataset dipilih karena data riil
PL-KUMKM 2023 belum dipublikasikan secara terbuka.

---

## Microsoft Azure

Proyek ini menggunakan 2 layanan Microsoft Azure:

| Layanan | Fungsi |
|---------|--------|
| Azure App Service | Deploy & hosting dashboard |
| Azure Blob Storage | Penyimpanan dataset & model |

---

## Kriteria Penilaian

| Kriteria | Bobot | Implementasi |
|----------|-------|-------------|
| Metodologi & EDA | 25% | EDA lengkap di Colab |
| Performa Model & Kode | 25% | K-Means + modular code |
| Pemanfaatan Azure | 30% | App Service + Blob Storage |
| Insight Strategis | 20% | 4 klaster + rekomendasi aksi |

---

## Author

**Rifky Alfitroh**
Solo Developer — AI Impact Challenge 2026
[GitHub](https://github.com/rifkyalfitroh58-droid)
