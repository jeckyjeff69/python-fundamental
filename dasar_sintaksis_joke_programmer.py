"""
Semua sintaksis dasar bahasa pemograman terdiri dari:
1. Sequential   : langkah berurutan
2. Percabangan  : langkah melompat jika kondisi terpenuhi
3. Perulangan   : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sequential
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu, dan jika ada telur beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

# Branching
jumlah_botol_susu = 0
jumlah_butir_telur = 1854

print(f'Jumlah botol susu {jumlah_botol_susu} botol')
print(f'Jumlah butir telur {jumlah_butir_telur} butir')

if jumlah_botol_susu > 0:
    print('Budi mengecek harganya, dan ternyata uangnya cukup')
    if jumlah_butir_telur > 0:
        print('Budi membeli 1 botol susu dan 6 telur')
    else:
        print('Budi membeli 1 botol susu')
else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah')
print('Menyampaikan hasilnya pada Ibu')


