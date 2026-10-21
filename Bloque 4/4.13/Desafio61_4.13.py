class Administrador:
    nombre_rol = "Administrador"

    def ejecutar(self, nombre):
        print(f"{nombre} gestiona presupuesto y permisos de la biblioteca")


class Mantenimiento:
    nombre_rol = "Mantenimiento"

    def ejecutar(self, nombre):
        print(f"{nombre} revisa y repara las instalaciones")


class Empleado:
    def __init__(self, nombre, salario, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.salario = salario
        self.roles = []

    def agregar_rol(self, rol):
        self.roles.append(rol)
        print(f"{self.nombre} asume el rol de {rol.nombre_rol}")

    def ejecutar_roles(self):
        for rol in self.roles:
            rol.ejecutar(self.nombre)

    def mostrar_info(self):
        roles = ", ".join(r.nombre_rol for r in self.roles) or "ninguno"
        print(f"{self.nombre} | {type(self).__name__} | Salario: ${self.salario} | Roles adicionales: {roles}")


class Gerente(Empleado):
    def __init__(self, equipo, **kwargs):
        super().__init__(**kwargs)
        self.equipo = equipo

    def dirigir(self):
        print(f"{self.nombre} dirige a: {', '.join(self.equipo)}")


class Tecnico(Empleado):
    def __init__(self, especialidad, **kwargs):
        super().__init__(**kwargs)
        self.especialidad = especialidad

    def reparar(self):
        print(f"{self.nombre} repara equipos de {self.especialidad}")


class GerenteTecnico(Gerente, Tecnico):
    def __init__(self, nombre, salario, equipo, especialidad):
        super().__init__(nombre=nombre, salario=salario, equipo=equipo, especialidad=especialidad)


class Voluntario(Empleado):
    def __init__(self, nombre, horas):
        super().__init__(nombre=nombre, salario=0)
        self.horas = horas

    def ayudar(self):
        print(f"{self.nombre} colabora {self.horas} horas por semana")


gerente = Gerente(nombre="Carlos", salario=3000, equipo=["Lucía", "Martín"])
tecnico = Tecnico(nombre="Lucía", salario=2000, especialidad="computadoras")
voluntario = Voluntario("Sofía", 6)
jefe = GerenteTecnico("Marta", 3500, ["Pedro"], "redes")

gerente.agregar_rol(Administrador())
tecnico.agregar_rol(Mantenimiento())
jefe.agregar_rol(Administrador())
jefe.agregar_rol(Mantenimiento())

for persona in [gerente, tecnico, voluntario, jefe]:
    persona.mostrar_info()

gerente.dirigir()
gerente.ejecutar_roles()
tecnico.reparar()
tecnico.ejecutar_roles()
voluntario.ayudar()
jefe.dirigir()
jefe.reparar()
jefe.ejecutar_roles()
print([clase.__name__ for clase in GerenteTecnico.__mro__])