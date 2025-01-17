valors = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

def to_roman(n):

    unidad, orden = separa_unidad_del_orden(n)
    
    if unidad <= 3:
        result = unidad * valors[orden]
    elif unidad == 4:
        result = valors[orden] + valors [5 * orden]
    elif unidad < 9:
        result = valors[5 * orden] + (unidad - 5) * valors[orden]
    elif unidad == 9:
        result = valors[orden] + valors[10 * orden]


    else:
        result = valors[n]

    return result


def dividir_en_digitos(n:int):
    """no entran numeros mayores de 3999"""
    cad = f"{n:04d}" #esto le mete ceros hasta 4 ejm 0034, 0002, 0123.
    millares = centenas = decenas = unidades = 0 

    millares = int(cad[0]) * 1000
    centenas = int(cad[1]) *100
    decenas = int(cad[2]) * 10
    unidades = int(cad[3]) * 1

    return [millares, centenas,decenas, unidades]

def digitos_a_roman(lista):
    result = ""
    for numero in lista:
        result += to_roman(numero)
    return result

def arabigo_a_romano(n: int):  

    miles = divide_en_miles(n)
    resultado = ""
    for num_asteriscos, cifra in enumerate(miles):
        lista = dividir_en_digitos(cifra)
        romano = digitos_a_roman(lista)
        if romano != "":   # esto es para que meta asteriscos 
            romano += "*" * num_asteriscos
        resultado = romano + resultado
    
    return resultado


def separa_unidad_del_orden(cifra):  # cifra 200 devuelve 2 , 100
    """procesa la cifra y devuelve separado el numero de las decenas, centenas , millares"""
    
    cifra_str = str(cifra)     #hay que transformar la cifra en una str para poder seleccionar 

    unidad = int(cifra_str[0]) #crea una var que tome el primer valor de cifra_str
    
    orden = 10 ** (len(cifra_str) - 1)   #ahora crea otra var que saque el orden 

    return unidad , orden


def divide_en_miles(n:int):
    """funcion que recibe un numero entero mayor de 4000 y devuelve una lista con el entero separado en y al reves # ejm (4127123) == [123,127, 4]"""
    lista = []
    modulo = n % 1000
    paluego = n // 1000
    while paluego >= 1000:
        lista.append(modulo)
        n = paluego
        modulo = n % 1000
        paluego = n // 1000 
    
    if paluego <= 3:
        lista.append(n)
    else:
        lista.append(modulo)
        lista.append(paluego)
    return lista
