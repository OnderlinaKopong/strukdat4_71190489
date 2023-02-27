import json
n = int(input("Masukkan jumlah barang = "))
y = []
for item in range(n):
    nama_barang = input(f"Nama Barang{item+1}=")
    harga_barang = input(f"Harga Barang{item+1}=")
    list_barang = {'nama' : nama_barang, 'harga' : harga_barang} 
    y.append(list_barang)

total = sum(list_barang['harga'] for list_barang in y)

data = {'total' : total, 'barang' : list_barang}

with open("data_barang.json","w") as file:
    json.dump(data, file, indent=4)