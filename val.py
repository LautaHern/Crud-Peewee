import re


def validar(cad):
    patron = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
    try:
        print("------------------")
        print(cad)
        re.match(patron, cad)
        if re.match(patron, cad):
            return True
        else:
            return False
    except:
        return False
