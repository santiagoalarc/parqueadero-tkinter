import tkinter as tk
from tkinter import ttk, messagebox
from clases import Vehículo, Miembro, Parqueadero

class ParqueaderoGUI:
    def __init__(self, root, parqueadero, miembros_registrados):
        self.root = root
        self.parqueadero = parqueadero
        self.miembros_registrados = miembros_registrados

        # Configuración de la ventana
        self.root.title("Control de Parqueadero - Universidad Surcolombiana")
        self.root.geometry('400x300')

        # Labels y entradas para ingresar datos
        self.label_tipo = ttk.Label(self.root, text="Tipo de Vehículo (carro/moto/bicicleta):")
        self.label_tipo.pack()
        self.entry_tipo = ttk.Entry(self.root)
        self.entry_tipo.pack()

        self.label_placa = ttk.Label(self.root, text="Placa o ID (para bicicletas):")
        self.label_placa.pack()
        self.entry_placa = ttk.Entry(self.root)
        self.entry_placa.pack()

        self.label_identificacion = ttk.Label(self.root, text="ID de Miembro:")
        self.label_identificacion.pack()
        self.entry_identificacion = ttk.Entry(self.root)
        self.entry_identificacion.pack()

        # Botones para registrar entrada y salida
        self.button_entrada = ttk.Button(self.root, text="Registrar Entrada", command=self.registrar_entrada)
        self.button_entrada.pack()

        self.button_salida = ttk.Button(self.root, text="Registrar Salida", command=self.registrar_salida)
        self.button_salida.pack()

        # Botón para cerrar sesión
        self.button_logout = ttk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion)
        self.button_logout.pack()

        # Mostrar espacios disponibles
        self.label_disponibilidad = ttk.Label(self.root, text=self.actualizar_disponibilidad())
        self.label_disponibilidad.pack()

    def actualizar_disponibilidad(self):
        return f"Carros: {self.parqueadero.espacios_carro - self.parqueadero.ocupados_carro}, Motos: {self.parqueadero.espacios_moto - self.parqueadero.ocupados_moto}, Bicicletas: {self.parqueadero.espacios_bicicleta - self.parqueadero.ocupados_bicicleta}"

    def registrar_entrada(self):
        tipo = self.entry_tipo.get().lower()
        placa = self.entry_placa.get()
        identificacion = self.entry_identificacion.get()

        miembro = Miembro("", "", "", identificacion)

        if miembro.validar_miembro(self.miembros_registrados):
            vehiculo = Vehículo(tipo, placa, identificacion)

            if self.parqueadero.validar_entrada(vehiculo):
                if self.parqueadero.registrar_entrada(vehiculo):
                    messagebox.showinfo("Éxito", "Vehículo registrado con éxito")
                else:
                    messagebox.showwarning("Error", "No hay espacio disponible para este tipo de vehículo")
            else:
                messagebox.showwarning("Error", "Vehículo ya se encuentra registrado")
        else:
            messagebox.showwarning("Error", "Usuario no registrado")

        self.label_disponibilidad.config(text=self.actualizar_disponibilidad())

    def registrar_salida(self):
        placa = self.entry_placa.get()
        identificacion = self.entry_identificacion.get()

        if self.parqueadero.validar_salida(identificacion):
            if self.parqueadero.registrar_salida(placa):
                messagebox.showinfo("Éxito", "Salida registrada con éxito")
            else:
                messagebox.showwarning("Error", "Vehículo no encontrado")
        else:
            messagebox.showwarning("Error", "Usuario no es propietario del vehículo")

        self.label_disponibilidad.config(text=self.actualizar_disponibilidad())

    def cerrar_sesion(self):
        self.root.destroy()  # Cierra la ventana actual
        root_login = tk.Tk()  # Crea una nueva ventana para el login
        app_login = LoginRegistroGUI(root_login, self.miembros_registrados, self.parqueadero)
        root_login.mainloop()


# Interfaz gráfica de registro e inicio de sesión
class LoginRegistroGUI:
    def __init__(self, root, miembros_registrados, parqueadero):
        self.root = root
        self.miembros_registrados = miembros_registrados
        self.parqueadero = parqueadero
        self.root.title("Login y Registro")
        self.root.geometry('300x200')

        # Botones para registrar e iniciar sesión
        self.label_bienvenida = ttk.Label(self.root, text="Bienvenido")
        self.label_bienvenida.pack()

        self.button_registro = ttk.Button(self.root, text="Registrarse", command=self.mostrar_registro)
        self.button_registro.pack()

        self.button_login = ttk.Button(self.root, text="Parqueadero", command=self.mostrar_login)
        self.button_login.pack()

    def mostrar_registro(self):
        self.limpiar_ventana()
        self.label_nombre = ttk.Label(self.root, text="Nombre:")
        self.label_nombre.pack()
        self.entry_nombre = ttk.Entry(self.root)
        self.entry_nombre.pack()

        self.label_apellido = ttk.Label(self.root, text="Apellido:")
        self.label_apellido.pack()
        self.entry_apellido = ttk.Entry(self.root)
        self.entry_apellido.pack()

        self.label_identificacion = ttk.Label(self.root, text="ID de Miembro:")
        self.label_identificacion.pack()
        self.entry_identificacion = ttk.Entry(self.root)
        self.entry_identificacion.pack()

        self.label_tipo_miembro = ttk.Label(self.root, text="Tipo de Miembro (estudiante/profesor):")
        self.label_tipo_miembro.pack()
        self.entry_tipo_miembro = ttk.Entry(self.root)
        self.entry_tipo_miembro.pack()

        self.button_confirmar_registro = ttk.Button(self.root, text="Confirmar Registro", command=self.registrar_usuario)
        self.button_confirmar_registro.pack()

    def mostrar_login(self):
        self.limpiar_ventana()
        self.label_identificacion = ttk.Label(self.root, text="ID de Miembro:")
        self.label_identificacion.pack()
        self.entry_identificacion = ttk.Entry(self.root)
        self.entry_identificacion.pack()

        self.button_confirmar_login = ttk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.button_confirmar_login.pack()

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        identificacion = self.entry_identificacion.get()
        tipo_miembro = self.entry_tipo_miembro.get().lower()
        if nombre == "" or apellido == "" or identificacion == "" or tipo_miembro == "" or (tipo_miembro != "estudiante" and tipo_miembro != "profesor"):
            messagebox.showerror("Error", "Campos inválidos")
        else:
            nuevo_miembro = Miembro(nombre, apellido, tipo_miembro, identificacion)
            self.miembros_registrados.append(nuevo_miembro)
            messagebox.showinfo("Éxito", "Usuario registrado con éxito")
            self.mostrar_login()

    def iniciar_sesion(self):
        identificacion = self.entry_identificacion.get()

        miembro = Miembro("", "", "", identificacion)
        if miembro.validar_miembro(self.miembros_registrados):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.mostrar_parqueadero()
        else:
            messagebox.showwarning("Error", "ID no registrado")

    def mostrar_parqueadero(self):
        self.root.destroy()  # Cierra la ventana de login
        root_parqueadero = tk.Tk()  # Crea una nueva ventana para el parqueadero
        #parqueadero = Parqueadero(10, 20, 30) 
        app_parqueadero = ParqueaderoGUI(root_parqueadero, self.parqueadero, self.miembros_registrados)
        root_parqueadero.mainloop()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Crear la ventana principal de inicio
root = tk.Tk()
miembros_registrados = []
parqueadero = Parqueadero(10, 20, 30)
app_login = LoginRegistroGUI(root, miembros_registrados, parqueadero)

# Iniciar la aplicación
root.mainloop()