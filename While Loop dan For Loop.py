###Perbedaan While dan For Loop adalah
#Perulangan for disebut counted loop (perulangan yang terhitung), sementara perulangan while disebut uncounted loop (perulangan yang tak terhitung). Perbedaannya adalah perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya. Sementara while untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.


# Contoh Perulangan For

ulang = 10

for i in range(ulang):
  print("Perulangan Ke-" + str(i))

print(50*"=")




# Contoh Perulangan While
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
