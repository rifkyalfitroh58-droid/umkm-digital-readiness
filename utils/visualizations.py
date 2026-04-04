import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.data_loader import WARNA_KLASTER

def grafik_distribusi_score(df: pd.DataFrame):
    fig = px.histogram(
        df, x='digital_readiness_score',
        nbins=25,
        color_discrete_sequence=['#1D9E75'],
        labels={'digital_readiness_score': 'Digital Readiness Score',
                'count': 'Jumlah UMKM'},
        title='Distribusi Digital Readiness Score'
    )
    fig.add_vline(
        x=df['digital_readiness_score'].mean(),
        line_dash='dash', line_color='#D85A30',
        annotation_text=f"Rata-rata: {df['digital_readiness_score'].mean():.1f}",
        annotation_position='top right'
    )
    fig.update_layout(bargap=0.1, showlegend=False)
    return fig

def grafik_pie_klaster(df: pd.DataFrame):
    counts = df['nama_klaster'].value_counts().reset_index()
    counts.columns = ['Klaster', 'Jumlah']
    fig = px.pie(
        counts, names='Klaster', values='Jumlah',
        color='Klaster',
        color_discrete_map=WARNA_KLASTER,
        title='Proporsi UMKM per Klaster',
        hole=0.4
    )
    fig.update_traces(textposition='outside', textinfo='percent+label')
    return fig

def grafik_score_per_sektor(df: pd.DataFrame):
    data = df.groupby('sektor')['digital_readiness_score'].mean().reset_index()
    data = data.sort_values('digital_readiness_score', ascending=True)
    fig = px.bar(
        data, x='digital_readiness_score', y='sektor',
        orientation='h',
        color='digital_readiness_score',
        color_continuous_scale='Teal',
        labels={'digital_readiness_score': 'Rata-rata Score',
                'sektor': 'Sektor Usaha'},
        title='Rata-rata Score per Sektor'
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig

def grafik_score_per_provinsi(df: pd.DataFrame):
    data = df.groupby('provinsi')['digital_readiness_score'].mean().reset_index()
    data = data.sort_values('digital_readiness_score', ascending=True)
    fig = px.bar(
        data, x='digital_readiness_score', y='provinsi',
        orientation='h',
        color='digital_readiness_score',
        color_continuous_scale='Blues',
        labels={'digital_readiness_score': 'Rata-rata Score',
                'provinsi': 'Provinsi'},
        title='Rata-rata Score per Provinsi'
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig

def grafik_pca_klaster(df: pd.DataFrame):
    if 'pca_1' not in df.columns:
        return None
    fig = px.scatter(
        df, x='pca_1', y='pca_2',
        color='nama_klaster',
        color_discrete_map=WARNA_KLASTER,
        opacity=0.65,
        labels={'pca_1': 'PC1', 'pca_2': 'PC2',
                'nama_klaster': 'Klaster'},
        title='Visualisasi Klaster UMKM (PCA 2D)',
        hover_data=['sektor', 'skala_usaha',
                    'digital_readiness_score']
    )
    fig.update_traces(marker_size=5)
    return fig

def grafik_radar_klaster(df):
    fitur = [
        'punya_medsos_bisnis',
        'punya_marketplace',
        'pakai_pembayaran_digital',
        'punya_website',
        'ikut_pelatihan_digital',
        'pakai_tools_manajemen',
    ]
    label = [
        'Media Sosial',
        'Marketplace',
        'Bayar Digital',
        'Website',
        'Pelatihan',
        'Tools Mgmt',
    ]

    fig = go.Figure()

    for nama, color in WARNA_KLASTER.items():
        subset = df[df['nama_klaster'] == nama]
        if len(subset) == 0:
            continue
        nilai = subset[fitur].mean().tolist()
        nilai += [nilai[0]]

        fig.add_trace(go.Scatterpolar(
            r=nilai,
            theta=label + [label[0]],
            fill='toself',
            name=nama,
            line_color=color,
            opacity=0.7,
        ))

    fig.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                tickfont=dict(color='#AAAAAA', size=10),
                gridcolor='#444444',
                linecolor='#444444',
            ),
            angularaxis=dict(
                tickfont=dict(color='#CCCCCC', size=11),
                gridcolor='#444444',
                linecolor='#444444',
            ),
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title='Profil Digital per Klaster',
        title_font=dict(color='#CCCCCC'),
        legend=dict(
            font=dict(color='#CCCCCC'),
        ),
        showlegend=True,
    )

    return fig