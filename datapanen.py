data_panen = {
    'lokasi1': {
        'nama_lokasi' : 'Kebuan A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2': {
        'nama_lokasi' : 'Kebuan B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3': {
        'nama_lokasi' : 'Kebuan C',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 700,
            'kedelai' : 600
        }
    },
    'lokasi4': {
        'nama_lokasi' : 'Kebuan D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5': {
        'nama_lokasi' : 'Kebuan E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}


for x,y in data_panen.items():
    lokasi = y['nama_lokasi']
    padi = y['hasil_panen']['padi']
    jagung = y['hasil_panen']['jagung']
    kedelai = y['hasil_panen']['kedelai']

    print(f"\nData panen {x}")
    print(f"Nama lokasi: {lokasi}")
    print(f"Hasil panen padi: {padi}")
    print(f"Hasil panen jagung: {jagung}")
    print(f"Hasil panen kedelai: {kedelai}")

print(f"\nJumlah hasil panen jagung lokasi2 adalah {data_panen['lokasi2']['hasil_panen']['jagung']}")

print(f"\nNama lokasi dari lokasi3 adalah {data_panen['lokasi3']['nama_lokasi']}")

hasil_panen_padi = {}
hasil_panen_kedelai = {}

for x,y in data_panen.items():
    hasil_panen_padi[x] = y['hasil_panen']['padi']
    hasil_panen_kedelai[x] = y['hasil_panen']['kedelai']

print("\nPadi", {hasil_panen_padi})
print("Kedelai", {hasil_panen_kedelai})

for x,y in data_panen.items():
    padi = y['hasil_panen']['padi']
    jagung = y['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f"{x} memerlukan perhatian khusus")
    else:
        print(f"{x} dalam kondisi baik") 