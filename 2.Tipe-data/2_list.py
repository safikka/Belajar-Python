# NOTE List
# karena di python gaada Array (harus import lib Array)
# Jadi ada namanya tipe-data List yang mirip array tapi bisa diisi
# berbagai tipe-data didalamnya
# C-ways            --> int x = [1,2,3];            (gaboleh diisi selain int)
# Python-ways       --> x = [1,2.0,"mantap",True]   (boleh dicampur)

# ====================================================== #
# TODO ini tipe-data list (List)
ini_list=[1,2.0,"mantap",True]

print('\nContoh print List:')
print(ini_list[3])
print(ini_list)

# Coba ditambah sesuatu didalam list pakai .append() tapi diakhir index
ini_list.append('nais')
print('setelah ditambah dengan append():')
print(ini_list)

# Coba ditambah sesuatu didalam list pakai .insert() bisa set letaknya
# .insert(index,isi)
ini_list.insert(3,'pancing')
print('setelah ditambah dengan insert():')
print(ini_list)

# Perbedaan pakai .append() dengan .extend()
list_baru = [1,2,3]
ini_list.append(list_baru)
print('setelah ditambah dengan append():')
print(ini_list)
ini_list.extend(list_baru)
print('setelah ditambah dengan extend():')
print(ini_list)
# ====================================================== #