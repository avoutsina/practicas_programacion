'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        mayor_cantidad_de_votos = 0
        menor_cantidad_de_votos = 0
        candidato_mas_votado = None
        candidato_menos_votado = None
        edad_menos_votado = None
        sumatoria_edades = 0
        cantidad_edades = 0
        votos_emitidos = 0
        bandera = True
    
        while True:

            nombre = prompt("Por favor","Ingrese su nombre")
            while nombre == None or nombre.isalpha() == False:
                nombre = prompt("Por favor","Ingrese su nombre")

            edad = prompt("Por favor","Ingrese su edad")
            while (edad == None or not edad.isdigit()) or int(edad) < 25 :
                edad = prompt("Por favor","Ingrese su edad")
            edad = int(edad)

            votos = prompt("Por favor","Ingrese su cantidad de votos")
            while votos == None or not votos.isdigit():
                votos = prompt("Por favor","Ingrese su cantidad de votos")
            votos = int(votos)

            if bandera == True:
                candidato_mas_votado = nombre
                candidato_menos_votado = nombre
                menor_cantidad_de_votos = votos
                mayor_cantidad_de_votos = votos
                edad_menos_votado = edad
                bandera = False

            elif votos < menor_cantidad_de_votos:
                candidato_menos_votado = nombre
                menor_cantidad_de_votos = votos
                edad_menos_votado = edad

            elif votos > mayor_cantidad_de_votos:
                candidato_mas_votado = nombre
                mayor_cantidad_de_votos = votos


            sumatoria_edades += edad
            cantidad_edades += 1
            votos_emitidos += votos
            continuar = question("",'Desea continuar?')
            if continuar == True:
                continue
            else:
                break
        promedio = sumatoria_edades/cantidad_edades
        alert(message=f"El candidato mas votado es: {candidato_mas_votado}\nEl candidato menos votado es {candidato_menos_votado} y tiene {edad_menos_votado} años\nEl candidato menos votado tiene {menor_cantidad_de_votos} votos\nEl promedio de edades es de: {promedio}\nEl total de votos emitidos es de: {votos_emitidos}")

            

            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
