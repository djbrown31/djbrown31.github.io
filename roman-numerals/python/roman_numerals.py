def to_roman(num):
    output = ''
    numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    for i in numerals:
        while num >= numerals[i]:
            output += i
            num -= numerals[i]

    print(output)

to_roman(999)



    