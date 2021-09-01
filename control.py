from tkinter import Tk, messagebox
import model
import view
import val


class Control:
    def __init__(self):
        self.activar_vista()

    def activar_vista(self):
        window = Tk()
        self.ventana = view.Producto(self)
        self.ventana.crear_ventana_ppal(window)

    def alta(self, datos):
        validacion = val.validar(datos[0])
        if validacion:
            objeto = model.alta(datos)
            self.ventana.mostrar(objeto)
            return True
        else:
            return False

    def mostrar_base(self):
        records = self.ventana.tree.get_children()
        for element in records:
            self.ventana.tree.delete(element)
        objetos = model.Producto.select()
        for i in objetos:
            self.ventana.mostrar(i)

    def eliminar(self, var_id):
        id = var_id.get()
        borrar = model.Producto.get(model.Producto.id == id)
        borrar.delete_instance()
        self.mostrar_base()

    def modificar(self, variables, popup):
        lista = []
        for variable in variables:
            lista.append(variable.get())
        focus = self.ventana.tree.focus()
        id_seleccionado = self.ventana.tree.item(focus, "text")
        resultado = model.modificar(lista, id_seleccionado)
        popup.destroy()
        if resultado:
            messagebox.showinfo(
                "Modificación", "El registro ha sido modificado correctamente"
            )
        self.mostrar_base()

    def registros(self):
        objetos = model.Registros.select()
        return objetos


if __name__ == "__main__":
    aplicacion = Control()
