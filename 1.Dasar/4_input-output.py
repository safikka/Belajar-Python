# NOTE
# Pada python, fungsi print() biasa kita kenal buat ngeprint kan?
# lalu fungsi input() dikenal buat nerima inputan dari user
# Nah sebenernya mereka ini apasi?



# ========================================================== #
# TODO -->  OUTPUT                                           #
#                                                            #
# Kita biasa pake print() untuk nampilin sesuatu di terminal #
# atau bisa dibilang ini adalah bentuk dari Output           #
# ========================================================== #
print("___Contoh OUTPUT___")
print('Tampilin sesuatu')
a = 5
print('Tampilin nilai a :',a)

# NOTE
# Penasaran gasi sebenernya isi parameter print() itu?
# apa cuma sesuatu yang kita mau tampilin doang?
# 
# Ini parameternya:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 
# object --> sesuatu yang pengen kita tampilin
# sep --> separator/pembatas antar nilai, secara default dia diisi spasi
# end --> setelah object tampil, end akan tampil. Ibarat di C itu adalah '\n' secara manual
print("\n___Contoh daleman print()___")
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
print('')

# NOTE
# Selain itu, di python bisa lho nampilin 
# kek template literalnya Javacript
# pakai .format()
print("\n___Contoh Output Formatting___")
x = 5
y =10
print('Nilai dari x adalah {} dan y adalah {}'.format(x,y))

# Bisa juga berdasar index dari apa yang mau disummon
print('Aku sayang {0} tapi hanya bisa lihat dari {1}'.format('kamu','jauh'))
print('Lah kok {1} ? Mampus {0} haha'.format('lu','curhat'))

# Bisa juga berdasar dari argumen key-value macem json
print('Semua yang bernyawa pasti akan merasakan {kepastian}'.format(kepastian = 'mati'))

# Bisa juga kek sprintf() di C
Rumi = "What you seek is seeking you"
print('Jalaluddin Rumi bersabda bahwa %s' %Rumi)



# ========================================================== #
# TODO -->  INPUT                                            #
#                                                            #
# Kita biasa pake input() untuk nerima sesuatu dari user     #
# atau bisa dibilang ini adalah bentuk dari Input            #
# ========================================================== #
print("\n___Contoh INPUT___")
angka = input('Masukan angka: ')
print('Angka yang dimasukin', angka)
print('tipedata angka yang dimasukkin:', type(angka))
angka_ubah = int(angka)
print('tipedata angka udah diubah:', type(angka_ubah))