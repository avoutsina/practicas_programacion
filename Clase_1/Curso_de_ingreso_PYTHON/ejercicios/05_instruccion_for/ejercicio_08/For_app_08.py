import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt(title='',prompt="Ingrese un número: ")
        while numero_ingresado == None or numero_ingresado.isdigit() == False:
            numero_ingresado = prompt("Hola",'ingrese un numero')
            
        numero_ingresado = int(numero_ingresado)
        rango_a_recorrer = range(1, numero_ingresado +1)
        bandera = True
        contador = 0
        for i in rango_a_recorrer:
                if numero_ingresado % i == 0:
                    contador+=1
                    if contador <= 2:
                        bandera = True
                    else:
                        bandera = False
                elif numero_ingresado % i != 0:
                    bandera = False
                    
        
        if bandera == True:
            alert("Titulo", f"El numero {numero_ingresado} ES PRIMO")
        else:
            alert("Titulo", f"El numero {numero_ingresado} NO es PRIMO")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()