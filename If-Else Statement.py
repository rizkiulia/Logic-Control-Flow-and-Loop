#sebuah if-else statement yang dimana akan mem-print 'Besar' jika ruangan adalah 'Kamar' dan ukuran lebih dari 12, kemudian mem-print 'Sedang' jika ruangan adalah 'Kamar' dan ukuran lebih dari 6 dan memprint 'Kecil' jika ruangan adalah 'Kamar' dan ukuran ruangan lebih kecil dan sama dengan 6.

ruangan = 'Kamar'
size = 20

if ruangan == 'Kamar' and size > 12:
    print('Besar')
elif ruangan == 'Kamar' and (size <= 12 or size >= 6):
    print('Sedang')
elif ruangan == 'Kamar' and (size < 6):
    print('Kecil')
else:
    print('Bukan Kamar')
