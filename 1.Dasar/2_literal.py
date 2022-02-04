# NOTE Literal
# Literal adalah data mentah (raw data) 
# yang ada di suatu variabel/konstanta



# ================================================= #
# TODO                                              #
# Numeric Literals                                  #
# ================================================= #
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal ---> Bilangan kompleks ada sb.real dan sb.imajiner
x = 3.14j

# Hasilnya --> 10 100 200 300
print(a, b, c, d)

# Hasilnya --> 10.5 150.0
print(float_1, float_2)

# Hasilnya --> 3.14j 3.14 0.0
print(x, x.imag, x.real)



# ================================================= #
# TODO                                              #
# String Literals                                   #
# ================================================= #
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline
                    string with more than
                   one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)