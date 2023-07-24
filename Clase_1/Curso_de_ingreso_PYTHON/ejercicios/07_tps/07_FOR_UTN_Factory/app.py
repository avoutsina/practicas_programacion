'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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

        contador_a = 0
        nombre_jr_joven = None
        edad_jr_joven = 0
        sum_edades_m = 0
        sum_edades_f = 0
        sum_edades_nb = 0
        cant_edades_m = 0
        cant_edades_f = 0
        cant_edades_nb = 0
        postulantes_py=0
        postulantes_js=0
        postulantes_asp=0
        postulantes_m = 0
        postulantes_f = 0
        postulantes_nb = 0


        for i in range (10):
            nombre = prompt("Por favor","Ingrese su nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("Por favor","Ingrese su nombre")

            edad = prompt("Por favor","Ingrese su edad")
            while (edad == None or not edad.isdigit()) or int(edad) < 18 :
                edad = prompt("Por favor","Ingrese su edad")
            edad = int(edad)

            genero = prompt("Por favor","Ingrese su genero: F - M - NB")
            while genero == None or not genero.isalpha() or (genero != "F" and genero != "M" and genero != "NB"):
                genero = prompt("Por favor","Ingrese su genero: F - M - NB")

            tecnologia = prompt("Por favor","Ingrese que tecnologia utiliza: PYTHON - JS - ASP.NET")
            while tecnologia == None or (tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET"):
                tecnologia = prompt ("Por favor","Ingrese que tecnologia utiliza: PYTHON - JS - ASP.NET")

            puesto = prompt("Por favor","Ingrese a que puesto se postula: Jr - Ssr - Sr")
            while puesto == None or not puesto.isalpha() or (puesto != "Jr" and puesto != "Ssr" and puesto != "Sr"):
                puesto = prompt("Por favor","Ingrese a que puesto se postula: Jr - Ssr - Sr")
            
            #Consigna A
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 and edad <= 40) and puesto == "Ssr":
                contador_a += 1
            
            #Consigna B

            if (edad_jr_joven == 0 or edad_jr_joven > edad) and puesto == 'Jr':
                nombre_jr_joven = nombre
                edad_jr_joven = edad
            
            #Consigna C
            if genero == "M":
                sum_edades_m += edad
                cant_edades_m += 1
            elif genero == "F":
                sum_edades_f += edad
                cant_edades_f += 1
            elif genero == "NB":
                sum_edades_nb += edad
                cant_edades_nb += 1
            
            #Consigna D
            if tecnologia == "PYTHON":
                postulantes_py += 1
            elif tecnologia == "JS":
                postulantes_js += 1
            elif tecnologia == "ASP.NET":
                postulantes_asp += 1

            #Consigna E
            if genero == "M":
                postulantes_m += 1
            elif genero == "F":
                postulantes_f += 1
            elif genero == "NB":
                postulantes_nb += 1

        prom_m = (sum_edades_m/cant_edades_m)
        prom_f = (sum_edades_f/cant_edades_f)
        prom_nb= (sum_edades_nb/cant_edades_nb)
        tecnologia_mas_usada = None

        porcentaje_m = (postulantes_m*100)/10
        porcentaje_f = (postulantes_f*100)/10
        porcentaje_nb = (postulantes_nb*100)/10

        if postulantes_py > postulantes_js and postulantes_py > postulantes_asp:
            tecnologia_mas_usada = "PYTHON"
        elif postulantes_js > postulantes_asp and postulantes_js > postulantes_py:
            tecnologia_mas_usada = "JS"
        elif postulantes_asp > postulantes_py and postulantes_asp > postulantes_js:
            tecnologia_mas_usada = "ASP.NET"

        print(f'La cantidad de postulantes NB que programan en ASP.NET o JS cuya edadeste entre 25 y 40, que se hayan postulado para un puesto Ssr es de {contador_a}')
        print(f'Nombre del postulante Jr con menor edad: {nombre_jr_joven}')
        print(f'Promedio de edades por género:\nM:{prom_m}\nF:{prom_f}\nNB:{prom_nb}')
        print(f'Tecnologia con mas postulantes (solo hay una): {tecnologia_mas_usada}')
        print(f'Porcentaje de postulantes de cada genero:\nM:{porcentaje_m}%\nF:{porcentaje_f}%\nNB:{porcentaje_nb}%')



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
