#sebuah fungsi yang menerima satu argument bertipe data numeric dan menghasilkan sebuah return sebagai berikut :
#- menghasilkan return 'Aneh' jika nilai dari argument tersebut adalah bilangan ganjil
#- menghasilkan return 'Tidak Aneh' jika nilai dari argument tersebut adalah bilangan genap dan diantara nilai 2 sampai 5 (2 dan 5 termasuk)
#- menghasilkan return 'Aneh' jika nilai dari argument tersebut adalah bilangan genap dan diantara nilai 6 sampai 20 (6 dan 20 termasuk)
#- menghasilkan return 'Tidak Aneh' jika nilai dari argument tersebut adalah bilangan genap dan lebih besari dari 20

# Cara 1
def inspect(angka):
    if ((angka % 2) == 0):
        if (angka >=2 and angka<=5):
            return 'Tidak Aneh'
        if (angka >=6 and angka<=20):
            return  'Aneh'
        else:            
            return 'Tidak Aneh'
    else:
       return 'Aneh'

print(inspect(1))
print(inspect(2))


# Cara 2

num = int(input("Masukan angka: "))

def inspect(x):
    if x %2 == 0:
        print('Tidak Aneh')
    elif (x >= 2) and  (x <= 5):
        print('Tidak Aneh')
    elif (x >= 6) and (x <= 20):
        print('Aneh')
    else:
        print('Aneh')

inspect(num)



# Cara 3
def inspect(x):
    if x %2 == 0:
        print('Tidak Aneh')
    elif (x >= 2) and  (x <= 5):
        print('Tidak Aneh')
    elif (x >= 6) and (x <= 20):
        print('Aneh')
    else:
        print('Aneh')

inspect(2)
inspect(21)
