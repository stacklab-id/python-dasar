
print("==========================")
print("==========================")
print("Selamat datang di toko Stacklab")

produk = input("Masukkan produk : ")
harga = float(input("Masukan harga produk: "))
diskon = float(input("Masukan diskon produk: "))

potongan = harga * (diskon / 100)
harga_final = harga - potongan

print("========rincian pesanan=============")
print(f"Produk: {produk}")
print(f"Harga: {harga}")
print(f"Diskon: {diskon}")
print(f"TOTAL: {harga_final}")