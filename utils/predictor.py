import numpy as np
import pandas as pd
import joblib
import os
from utils.data_loader import NAMA_KLASTER, REKOMENDASI_KLASTER

MODEL_PATH  = "models/kmeans_model.pkl"
SCALER_PATH = "models/scaler.pkl"

FITUR_ORDER = [
    'punya_smartphone', 'punya_medsos_bisnis', 'punya_marketplace',
    'jumlah_platform', 'frekuensi_posting_mgg', 'pakai_pembayaran_digital',
    'persen_omzet_online', 'ikut_pelatihan_digital', 'punya_website',
    'pakai_tools_manajemen'
]

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "Model belum ada !"
        )
    kmeans = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return kmeans, scaler

def hitung_score(data: dict) -> float:
    score = (
        data['punya_smartphone']          * 10 +
        data['punya_medsos_bisnis']        * 15 +
        data['punya_marketplace']          * 20 +
        (data['jumlah_platform'] / 3)      * 10 +
        (data['frekuensi_posting_mgg'] / 5)* 10 +
        data['pakai_pembayaran_digital']   * 10 +
        (data['persen_omzet_online'] / 100)* 10 +
        data['ikut_pelatihan_digital']     * 5  +
        data['punya_website']              * 5  +
        data['pakai_tools_manajemen']      * 5
    )
    return round(score, 2)

def prediksi_klaster(input_data: dict) -> dict:
    kmeans, scaler = load_model()

    X = np.array([[input_data[f] for f in FITUR_ORDER]])
    X_scaled = scaler.transform(X)
    klaster_id = int(kmeans.predict(X_scaled)[0])

    nama   = NAMA_KLASTER.get(klaster_id, f"Klaster {klaster_id}")
    score  = hitung_score(input_data)
    saran  = REKOMENDASI_KLASTER.get(nama, "Tingkatkan adopsi digital secara bertahap.")

    return {
        "klaster_id" : klaster_id,
        "nama"       : nama,
        "score"      : score,
        "rekomendasi": saran
    }