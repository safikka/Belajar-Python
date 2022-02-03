# NOTE Python dasar
# di Python ada hal unik dalam penulisan statement
# khususnya dalam penggunaan "Indentation"
# dan juga dalam deklarasi variabel pada Python
# markicuy!


# ================================================= #
# TODO                                              #
# mari kita coba untuk deklarasi variabel di Python #
# ================================================= #
num_int = 10
num_float = 2.0
ini_string = 'Hello World'
ini_benar = True
ini_list = [1,2,'mantap']
ini_tuple = (1,2,'nais')
ini_set = {1,2,3}
ini_dictionary = {'nilai':100,'nama':'Anton',}



# ===================================================== #
# TODO                                                  #
# mari kita coba memahami penulisan statement di Python #
# ===================================================== #
stat_biasa = 1 + 2
print('nilai stat_biasa: ' + str(stat_biasa))
stat_multi = 1 + 2 + \
             3 + 4 + \
             5 + 6
print('nilai stat_multi: ' + str(stat_multi))



# NOTE Indentation
# Kebanyakan bahasa pemrograman lain pake curly braces {}
# untuk definisi blok dari kode / scope.
# Nah di python ini unik karena pake indentation (ibarat di tab)
# langsung aja ke contoh biar kebayang!

# ======================================================= #
# TODO                                                    #
# mari kita coba memahami penulisan indentation di Python #
# ======================================================= #

# Indentation itu yang spasi kek di tab buat nandain ini
# blok kode atau scope
print('\nContoh indentation di for-loop: ')
for x in range(0,5):
    for y in range(0,x+1):
        print("*", end="")
    print('\r')