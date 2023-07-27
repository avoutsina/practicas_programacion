import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            numero_solicitado=prompt("Por favor","ingrese un numero")
            if numero_solicitado == None:
                break
            elif numero_solicitado.isdigit():
                numero_solicitado=int(numero_solicitado)
                self.lista.append(numero_solicitado)
            elif numero_solicitado.isalpha() or numero_solicitado == '' or numero_solicitado.isalnum():
                continue
            elif int(numero_solicitado) < 0:
                numero_solicitado = int(numero_solicitado)
                self.lista.append(numero_solicitado)
            else:
                continue 

    def btn_mostrar_estadisticas_on_click(self):
        positivos = 0
        negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        minimo_negativos = 0
        maximo_positivos = 0
        bandera_positivos = True
        bandera_negativos = True
        for numero in self.lista:
            if numero > 0:
                positivos += numero
                contador_positivos += 1
                if bandera_positivos == True or numero > maximo_positivos:
                    bandera_positivos = False
                    maximo_positivos = numero
            elif numero < 0:
                negativos += numero
                contador_negativos += 1
                if bandera_negativos == True or numero < minimo_negativos:
                    bandera_negativos = False
                    minimo_negativos = numero
            else:
                contador_ceros += 1

        promedio_negativos = negativos / contador_negativos

        alert("Titulo", f"La suma acumulada de los positivos es: {positivos} y la cantidad es: {contador_positivos}\nLa suma acumulada de los negativos es: {negativos} y la cantidad es: {contador_negativos}\nLa cantidad de ceros es: {contador_ceros}\nEl máximo de los positivos es: {maximo_positivos} y el minimo de los negativos es: {minimo_negativos}\nEl promedio de los negativos es: {promedio_negativos}")
        
        
        
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
