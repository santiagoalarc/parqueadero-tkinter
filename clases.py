
import datetime

# Clases base (Vehículo, Miembro, Parqueadero)
class Vehículo:
    def __init__(self, tipo, placa, identificacion, hora_entrada=None, hora_salida=None):
        self.identificacion = identificacion
        self.tipo = tipo
        self.placa = placa
        self.hora_entrada = hora_entrada if hora_entrada else datetime.datetime.now()
        self.hora_salida = hora_salida

    def registrar_salida(self):
        self.hora_salida = datetime.datetime.now()

class Miembro:
    def __init__(self, nombre, apellido, tipo_miembro, identificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_miembro = tipo_miembro
        self.identificacion = identificacion

    def validar_miembro(self, miembros_registrados):
        return self.identificacion in [m.identificacion for m in miembros_registrados]

class Parqueadero:
    def __init__(self, espacios_carro, espacios_moto, espacios_bicicleta):
        self.espacios_carro = espacios_carro
        self.espacios_moto = espacios_moto
        self.espacios_bicicleta = espacios_bicicleta
        self.ocupados_carro = 0
        self.ocupados_moto = 0
        self.ocupados_bicicleta = 0
        self.vehiculos = []

    def verificar_disponibilidad(self, tipo):
        if tipo == 'carro':
            return self.ocupados_carro < self.espacios_carro
        elif tipo == 'moto':
            return self.ocupados_moto < self.espacios_moto
        elif tipo == 'bicicleta':
            return self.ocupados_bicicleta < self.espacios_bicicleta

    def registrar_entrada(self, vehiculo):
        if self.verificar_disponibilidad(vehiculo.tipo):
            self.vehiculos.append(vehiculo)
            if vehiculo.tipo == 'carro':
                self.ocupados_carro += 1
            elif vehiculo.tipo == 'moto':
                self.ocupados_moto += 1
            elif vehiculo.tipo == 'bicicleta':
                self.ocupados_bicicleta += 1
            return True
        return False

    def validar_entrada(self, vehiculo):
        if not any(v.placa == vehiculo.placa for v in self.vehiculos):
            return True
        return False

    def registrar_salida(self, placa):
        vehiculo = next((v for v in self.vehiculos if v.placa == placa), None)
        if vehiculo:
            vehiculo.registrar_salida()
            self.vehiculos.remove(vehiculo)
            if vehiculo.tipo == 'carro':
                self.ocupados_carro -= 1
            elif vehiculo.tipo == 'moto':
                self.ocupados_moto -= 1
            elif vehiculo.tipo == 'bicicleta':
                self.ocupados_bicicleta -= 1
            return True
        return False

    def validar_salida(self, identificacion):
        vehiculo = next((v for v in self.vehiculos if v.identificacion == identificacion), None)
        if vehiculo:
            return True
        return False
