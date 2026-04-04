def card_hasil_prediksi(nama, score, saran, warna, em):

    URUTAN = [
        'Digital Laggard',
        'Digital Beginner',
        'Digital Adopter',
        'Digital Champion',
    ]

    WARNA_SCORE = {
        'Digital Champion': '#378ADD',
        'Digital Adopter' : '#378ADD',
        'Digital Beginner': '#BA7517',
        'Digital Laggard' : '#E24B4A',
    }

    idx = URUTAN.index(nama) if nama in URUTAN else 0
    ws  = WARNA_SCORE.get(nama, '#378ADD')
    sc  = int(score)

    # Buat step bar dan label
    bars = ''
    lbls = ''
    for i, lab in enumerate(URUTAN):
        bg    = warna if i <= idx else '#E0E0E0'
        short = lab.replace('Digital ', '')
        fw    = '600' if i == idx else '400'
        fc    = warna if i == idx else '#9E9E9E'

        bars += '''
'''.format(bg=bg)

        lbls += '''{short}'''.format(
            fw=fw, fc=fc, short=short
        )

    html = '''



    

            {em} {nama}
        

            Score: {sc}
        


    

        {bars}
    


    

        {lbls}
    


    

        

            REKOMENDASI
        

        

            {saran}
        

    




'''.format(
        warna=warna,
        em=em,
        nama=nama,
        ws=ws,
        sc=sc,
        bars=bars,
        lbls=lbls,
        saran=saran,
    )

    return html