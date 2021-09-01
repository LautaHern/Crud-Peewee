from peewee import *
import datetime

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class Producto(BaseModel):
    titulo = CharField(128)
    descripcion = TextField()

    def __str__(self):
        return self.id + self.titulo + self.descripcion


class Registros(BaseModel):
    fecha = DateTimeField(default=datetime.datetime.now)
    id_prod = TextField()
    titulo = CharField(128)
    descripcion = TextField()


def decorador(funcion):
    def crea_registro(*args):
        nuevo_reg = Registros()
        objeto = funcion(*args)
        nuevo_reg.id_prod = objeto.id
        nuevo_reg.titulo = objeto.titulo
        nuevo_reg.descripcion = objeto.descripcion
        nuevo_reg.save()

        return objeto

    return crea_registro


@decorador
def alta(datos):
    inst_objeto = Producto()
    inst_objeto.titulo = datos[0]
    inst_objeto.descripcion = datos[1]
    inst_objeto.save()
    return inst_objeto


def modificar(lista, id):
    if lista[0] != "":
        if lista[1] != "":
            actualizar = Producto.update(
                titulo=lista[0], descripcion=lista[1],
                ).where(
                Producto.id == id
            )
            actualizar.execute()
        else:
            actualizar = Producto.update(
                titulo=lista[0]).where(
                    Producto.id == id)
            actualizar.execute()
    elif lista[1] != "":
        actualizar = Producto.update(descripcion=lista[1]).where(
            Producto.id == id)
        actualizar.execute()
    return True


db.connect()
db.create_tables([Producto, Registros])
