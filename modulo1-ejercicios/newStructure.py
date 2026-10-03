letter=input("ingrese una letra").upper()

"""
 if letter.upper() == 'A':
    print("es la vocal a")
elif letter.upper() == 'E':
    print("es la vocal E")
elif letter.upper() == 'I' or letter.upper() == 'O' or letter.upper() == 'U':
    print(" es un vocal")
else:
    print("no es una vocal") """

match letter:
    case 'A' :
        print("es la vocal A")
    case 'E':
        print("es la vocal E")
#    " ..... los otros casos"
    case _:
        print("No es una vocal")