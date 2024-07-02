from roman_funcs import to_roman, dividir_en_digitos
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
#pooner todos los casos 
def test_dividir_en_digitos():
    assert dividir_en_digitos(2024) == [2000,0,20,4]

