def fahr_to_kelvin(temp):
    "Convert temperature, temp, from F to K"
    return ((temp - 32) * (5.0/9.0)) + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def fahr_to_celsius(temp):
    temp_k = fahr_to_kelvin(temp)
    result = kelvin_to_celsius(temp_k)
    return result

