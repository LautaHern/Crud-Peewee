from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
from temas.opcion_temas import eleccion_tema


class Producto:
    def __init__(self, control):
        self.control = control

    def crear_ventana_ppal(self, window):
        # Ventana principal
        self.root = window
        self.root.title("Tarea POO")

        self.titulo = Label(
            self.root,
            text="Ingrese sus datos",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=60,
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=1,
            pady=1,
            sticky=W + E,
            )

        Label(self.root, text="Título").grid(row=1, column=0, sticky=W)
        Label(self.root, text="Descripción").grid(row=2, column=0, sticky=W)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val = StringVar(), StringVar()
        w_ancho = 20

        self.entrada_nombre = Entry(
            self.root,
            textvariable=self.a_val,
            width=w_ancho,
            )
        self.entrada_nombre.grid(row=1, column=1)
        self.entrada_descripcion = Entry(
            self.root, textvariable=self.b_val, width=w_ancho
        )
        self.entrada_descripcion.grid(row=2, column=1)

        self.tree = Treeview(self.root, height=10, columns=3)
        self.tree["columns"] = ("one", "three")
        self.tree.grid(row=7, column=0, columnspan=3)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("one", text="Título", anchor=CENTER)
        self.tree.heading("three", text="Descripción", anchor=CENTER)
        Button(
            self.root,
            text="Mostrar registros existentes",
            command=self.control.mostrar_base,
        ).grid(row=5, columnspan=3, sticky=W + E)

        Button(self.root, text="Alta", command=self.alta).grid(
            row=3, column=1,
        )
        Button(
            self.root,
            text="Registros",
            command=self.popup_registros,
        ).grid(row=3, column=2)
        Button(
            self.root,
            text="Eliminar",
            command=self.popup_eliminar,
        ).grid(row=11, column=0)
        Button(
            self.root,
            text="Modificar",
            command=self.popup_modificar,
        ).grid(row=11, column=2)

        # #####################################################
        # ################ TEMAS #############3#################
        # #####################################################3
        self.temas_opciones = Frame(
            self.root,
            bg="red",
            borderwidth=2,
            relief=RAISED,
            )
        self.temas_opciones.grid(
            row=12, column=0, columnspan=4, padx=1, pady=1, sticky=W + E
        )

        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        # Agrego variables de control para elección de tema.
        self.tema_option = IntVar(value=0)

        Label(
            self.temas_opciones,
            borderwidth=4,
            relief=RAISED,
            text="Temas",
            bg="#222",
            fg="OrangeRed",
        ).pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(
                self.temas_opciones,
                text=str(opcion),
                indicatoron=1,
                value=int(opcion[-1]) - 1,
                variable=self.tema_option,
                bg="#222",
                fg="OrangeRed",
                command=self.bg_fg_option,
            )
            boton["width"] = ancho_boton
            boton.pack(side=TOP)
        window.mainloop()

    def bg_fg_option(self):
        self.temas_opciones["bg"] = eleccion_tema(self.tema_option.get())
        self.root["bg"] = eleccion_tema(self.tema_option.get())

    def mostrar(self, objeto):
        self.tree.insert(
            "",
            0,
            text=objeto.id,
            values=(
                objeto.titulo,
                objeto.descripcion,
            ),
        )

    def popup_modificar(self):
        popup_modificar = Toplevel()
        formulario = Frame(popup_modificar)
        div1 = Frame(formulario, width=100)
        div2 = Frame(formulario, padx=7, pady=2)
        formulario.pack(fill=X)
        div1.pack(side=LEFT)
        div2.pack(side=RIGHT, expand=YES, fill=X)
        var_titulo = StringVar()
        var_descripcion = StringVar()
        lab_tit = Label(div1, width=10, text="Tíulo:")
        lab_tit.pack(side=TOP)
        ent_tit = Entry(div2, textvariable=var_titulo, width=30, relief=SUNKEN)
        ent_tit.pack(side=TOP, fill=X)
        lab_desc = Label(div1, width=10, text="Descripción:")
        lab_desc.pack(side=TOP)
        ent_desc = Entry(
            div2,
            textvariable=var_descripcion,
            width=30,
            relief=SUNKEN,
            )
        ent_desc.pack(side=TOP, fill=X)
        variables = [var_titulo, var_descripcion]
        Button(
            popup_modificar,
            text="Modificar",
            command=lambda: self.control.modificar(variables, popup_modificar),
        ).pack()
        popup_modificar.mainloop()

    def alta(self):
        titulo = self.a_val.get()
        descripcion = self.b_val.get()
        datos = [titulo, descripcion]
        resultado = self.control.alta(datos)
        if resultado:
            showinfo("Validado", "El registro se ha agregado correctamente")
        else:
            showinfo(
                'No Validado',
                """El campo de título no cumple los requisitos,
                 ingrese datos alfabéticos
                """
                )

    def popup_eliminar(self):
        var_id = StringVar()
        popup_eliminar = Toplevel()
        formulario = Frame(popup_eliminar)
        div1 = Frame(formulario, width=100)
        div2 = Frame(formulario, padx=7, pady=2)
        formulario.pack(fill=X)
        div1.pack(side=LEFT)
        div2.pack(side=RIGHT, expand=YES, fill=X)
        lab = Label(div1, width=10, text="ID")
        ent = Entry(div2, textvariable=var_id, width=30, relief=SUNKEN)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        Button(
            popup_eliminar,
            text="Eliminar",
            command=lambda: self.control.eliminar(var_id),
        ).pack()
        popup_eliminar.mainloop()

    def popup_registros(self):
        popup_reg = Toplevel()
        popup_reg.tree = Treeview(popup_reg, height=10, columns=3)
        popup_reg.tree["columns"] = ("one", "two", "three")
        popup_reg.tree.grid(row=7, column=0, columnspan=3)
        popup_reg.tree.heading("#0", text="Fecha", anchor=CENTER)
        popup_reg.tree.heading("one", text="ID", anchor=CENTER)
        popup_reg.tree.heading("two", text="Título", anchor=CENTER)
        popup_reg.tree.heading("three", text="Descripción", anchor=CENTER)
        popup_reg.tree.column("one", width=50, anchor=CENTER)

        objetos = self.control.registros()

        for i in objetos:
            popup_reg.tree.insert(
                "",
                0,
                text=i.fecha,
                values=(
                    i.id_prod,
                    i.titulo,
                    i.descripcion,
                ),
            )

        popup_reg.mainloop()
