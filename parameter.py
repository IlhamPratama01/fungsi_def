def selamatDatang(nama, waktu):
    print('halo', nama, 'selamat', waktu)
    print('apakah', nama, 'sudah datang', waktu, 'ini?')


selamatDatang('hitam', 'siang')
selamatDatang('putih', 'sore')
selamatDatang('ujang', 'malam')

# selamatDatang(waktu='siang', nama='udin')
selamatDatang = ('siang', 'udin')


def penjumlahan(a, b):
    hasil = a+b
    return hasil


hasil_jumlah = penjumlahan(2, 5)
print(selamatDatang)
print(hasil_jumlah)