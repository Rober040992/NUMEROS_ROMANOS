from roman_funcs import to_roman, dividir_en_digitos, arabigo_a_romano,separa_unidad_del_orden #divide_en_miles


def test_romanos_simples():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(500) == "D"
    assert to_roman(1000) == "M"


def test_romanos_del_1_al_9():
    assert to_roman(1) == "I"
    assert to_roman(2) == "II"
    assert to_roman(3) == "III"
    assert to_roman(4) == "IV"
    assert to_roman(5) == "V"
    assert to_roman(6) == "VI"
    assert to_roman(7) == "VII"
    assert to_roman(8) == "VIII"
    assert to_roman(9) == "IX"
    
def test_romanos_10_al_90():
    assert to_roman(10) == "X"
    assert to_roman(20) == "XX"
    assert to_roman(30) == "XXX"
    assert to_roman(40) == "XL"
    assert to_roman(70) == "LXX"
    assert to_roman(90) == "XC"
    #pooner todos los casos
 

def test_dividir_en_digitos():
    assert dividir_en_digitos(2024) == [2000,0,20,4]


def test_cualquier_romano():
    assert arabigo_a_romano(1999) == "MCMXCIX"


def test_separa():
    assert separa_unidad_del_orden(20) == (2,10)

def xtest_divide_en_miles():
    assert divide_en_miles(4127) == [127, 4]  #lo vamos a recorer del reves por que es mayor de 3999
    assert divide_en_miles(3127) == [3127] 

def xtest_divide_en_millones():
    assert divide_en_millones(4127123) == [123,127, 4]
    
