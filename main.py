# named parameter
# adalah istilah untuk menyebut cara pengiriman
# sebuah nilai argument ke parameter dengan menulis nama parameter
# tidak hanya sekedar nilainya saja.
# named paramter juga sering disebut named argument atau keyword arguments

# tidak menggunakan teknik named parameter
def pangkat(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
        hasil = hasil * angka
    return hasil

print(pangkat(5))
print(pangkat(5,4))
print(pangkat(6,6))

# menggunakan named parameter
def pangkatt(angka, pangkat = 2):
    hasil = 1
    for i in range(0, pangkat):
        hasil = hasil * angka
    return hasil

print(pangkatt(angka= 4, pangkat=3))
print(pangkatt(pangkat=2, angka=9))
print(pangkatt(angka=10, pangkat=2))

# tidak menggunakan named parameter
def akses_database(addres, username, password):
    print("database connection")
    print("server",addres)
    print("username", username)
    print("password", password)
    print("....connection success....!")

akses_database("localhost", "root", "123456")

# tidak menggunakan named parameter
def akses_databases(addres, username, password):
    print("database connection")
    print("server :",addres)
    print("username :", username)
    print("password : ", password)
    print("....connection success....!")

akses_databases(username="admin", password="qwerty", addres="192.168.1.0")

# named parameter perkalian
def perkalian(angka1, angka2):
    hasil = angka1*angka2
    return hasil

print(perkalian(angka2=20, angka1=15))