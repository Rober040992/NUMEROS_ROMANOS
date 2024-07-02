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

    if n <= 3:
        result = n * valors[1]
    elif n == 4:
        result = valors[1] + valors[5]
    elif n < 9:
        result = valors[5] + (n - 5) * valors[1]
    elif n == 9:
        result = valors[1] + valors[10]
    else:
        result = valors[n]

    return result