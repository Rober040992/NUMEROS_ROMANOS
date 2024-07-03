valors = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}



def separa_unidad_del_orden(cifra):  # cifra 200 devielve 2 , 100
    """procesa la cifra y devuelve separado el numero de las decenas, centenas , millares"""
    
    cifra_str = str(cifra)     #hay que transformar la cifra en una str para poder seleccionar 

    unidad = int(cifra_str[0]) #crea una var que tome el primer valor de cifra_str
    
    orden = 10 ** (len(cifra_str) - 1)   #ahora crea otra var que saque el orden 

    return unidad , orden



def to_roman_refact(n):          


    unidad = separa_unidad_del_orden(n)
    orden = separa_unidad_del_orden(n)
 
    if unidad <= 3:
        result = unidad * valors[orden]
    elif unidad == 4:
        result = valors[orden] + valors [5 * orden]
    elif n < 9:
        result = valors[5 * orden] + (unidad - 5) * valors[orden]
    elif n == 9:
        result = valors[orden] + valors[10 * orden]


    else:
        result = valors[unidad]
    return result
