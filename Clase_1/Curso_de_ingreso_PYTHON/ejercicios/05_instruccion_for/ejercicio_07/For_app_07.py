import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("Hola",'ingrese un numero')
        numeros_divisores = ''
        contador = 0
        while numero_ingresado == None or numero_ingresado.isdigit() == False:
            numero_ingresado = prompt("Hola",'ingrese un numero')
        numero_ingresado = int(numero_ingresado)
        for numero in range(1,numero_ingresado+1):
            if numero_ingresado % numero == 0:
                numeros_divisores += str(numero)+' '
                contador +=1 
            else:
                pass
        alert(title='',message=f'Los numeros divisores son: {numeros_divisores}\nLa cantidad de numeros divisores es de: {contador}')
                
                
                
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()