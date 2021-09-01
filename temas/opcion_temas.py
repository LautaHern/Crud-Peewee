import shelve
import os


with shelve.open("temas/opcion_temas") as db:
    db["tema1"] = "#222"
    db["tema2"] = "blue"
    db["tema3"] = "OrangeRed"


def eleccion_tema(variable):
    with shelve.open("temas/opcion_temas") as db:
        if variable == 0:
            variable = "tema1"
        elif variable == 1:
            variable = "tema2"
        elif variable == 2:
            variable = "tema3"
        tema_seleccionado = db[variable]
        return tema_seleccionado
