from tkinter import Tk, ttk, font, messagebox, StringVar, HORIZONTAL, TOP, BOTH, X, LEFT, RIGHT, END
import encryptor_Decryptor

#Esta clase es la encargada de generar la interfaz de la aplicación.
class gui():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Encryptor/Decryptor")
        self.raiz.geometry('300x300')
        path = __file__.replace('gui.py', 'Encryptor_Decryptor.ico')
        self.raiz.iconbitmap(path)
		
        fuente = font.Font(weight='bold')

        self.etiq1 = ttk.Label(self.raiz, text="Select an option:", font=fuente)           
        self.etiq2 = ttk.Label(self.raiz, text="Input:", font=fuente)
        self.etiq3 = ttk.Label(self.raiz, text="Output:", font=fuente)
        
        self.input = StringVar()
        self.output = StringVar()
        
        self.option = ttk.Combobox(self.raiz, state="readonly")
        self.option["values"] = ["Encrypt", "Decrypt"]
        self.option.current(0)
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.input, width=30)
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.output, width=30, state="readonly")
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        #Esta función se encarga de comprobar que operación se va a realizar al pulsar el botón 'Encrypt/Decrypt'
        # dependiendo de la función seleccionada en el combobox.
        def encryptDecrypt_Button():
           inputText = self.ctext1.get()
           if self.option.get() == "Encrypt":
               self.output.set(encryptor_Decryptor.encrypt(inputText))
           elif self.option.get() == "Decrypt":
               self.output.set(encryptor_Decryptor.decrypt(inputText))

        #Esta función se encarga de asignar a input el texto escrito en output.
        def outputToInput_Button():
           outputText = self.ctext2.get()
           self.input.set(outputText)
           self.output.set("")

        self.button1 = ttk.Button(self.raiz, text="Encrypt/Decrypt", command=encryptDecrypt_Button)
        self.button2 = ttk.Button(self.raiz, text="Output to input", command=outputToInput_Button)

        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.option.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.etiq3.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.button1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.button2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
                
        self.ctext1.focus_set()
        
        self.raiz.mainloop()

        self.output.set("")

#Esta función se encarga de llamar a la clase 'gui' para iniciar la aplicación.
def main():
    gui()
    return 0

if __name__ == '__main__':
    main()

#Esta función crea una ventana que avisa al usuario de que los caracteres no validos han sido borrados.
def invalidCharMessage():
    messagebox.showinfo("Invalid characters", "Invalid characters deleted")

#Esta función crea una ventana que avisa al usuario de que al desencriptar solo se puede introducir hexadecimal.
def noHexDecrypt():
    messagebox.showinfo("Invalid input", "Decrypt accepts only hexadecimal")