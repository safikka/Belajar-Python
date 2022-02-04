# NOTE
# Terdapat dua tipe konversi pada Python
#   1.  Implicit
#   2.  Explicit



# ========================================================= #
# TODO -->  Konversi Implicit                               #
#                                                           #
# Python otomatis akan konversi tipe data ke tipe data lain #
# Contoh : Penjumlahan int + float --> hasilnya float       #
# ========================================================= #
print("___Contoh Konversi Implicit___")
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("tipedata num_int:",type(num_int))
print("tipedata num_flo:",type(num_flo))

print("Nilai num_new:",num_new)
print("tipedata num_new:",type(num_new))



# ========================================================= #
# TODO -->  Konversi Explicit (TypeCasting)                 #
#                                                           #
# Python akan konversi tipe data ke tipe data lain          #
# menggunakan fungsi tertentu seperti int(), float(), str() #
# ========================================================= #
print("\n___Contoh Konversi Explicit___")
num_int = 123
num_str = "456"

print("tipedata num_int:",type(num_int))
print("tipedata num_str sebelum di TypeCasting:",type(num_str))

num_str = int(num_str)
print("tipedata num_str setelah di TypeCasting:",type(num_str))

num_sum = num_int + num_str

print("Hasil dari num_int dan num_str:",num_sum)
print("tipedatanya:",type(num_sum))