import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
     numero_ingresado = prompt("hola","ingrese un numero")
     pares = 0
     numeros_pares = ''
     numero_ingresado = int(numero_ingresado)
     for numero in range(1,numero_ingresado+1):
        if numero % 2 == 0:
           pares += 1    
           numeros_pares += str(numero) + " "
    
     alert(title="Resultados", message=f"Los numeros pares son: {numeros_pares}\nLa Cantidad de numeros pares es de: {pares}")
    
     

            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()