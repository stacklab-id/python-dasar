
username = input("Masukan username: ")
password = input("Masukan password: ")

hasil = username == "admin" and len(password) >= 10
print("Status login anda adalah: ", hasil)
