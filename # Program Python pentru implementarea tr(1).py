import tkinter as tk
from tkinter import messagebox

# Dicționar pentru codul Morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..', 
                    '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

# Funcții pentru criptare și decriptare
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Caută în dicționar și adaugă codul Morse corespunzător
           # împreună cu un spațiu pentru a separa codurile morse pentru diferite caractere
            cipher += MORSE_CODE_DICT.get(letter, '') + ' '
        else:
            # 1 spațiu indică caractere diferite și 2 indică cuvinte diferite
            cipher += ' '
    return cipher

# Funcție pentru decriptare a șirului din morse în engleză
def decrypt(message):
 # Spațiu suplimentar adăugat la sfârșit pentru a accesa ultimul cod morse
    message += ' '
    decipher = ''
    citext = ''
    i = 0 # Contor pentru a ține evidența spațiilor
    for letter in message:
        if letter != ' ':
            # Resetăm contorul deoarece este găsit un caracter fără spațiu
            i = 0
            # Stocarea codului Morse al unui singur caracter
            citext += letter
        else:
             # Creștem contorul de spațiu pentru a indica un spațiu
            i += 1
            # Dacă i == 1, indică un caracter nou
            if i == 2:
            # Dacă i == 2, aceasta indică un cuvânt nou
                decipher += ' '
            elif i == 1 and citext != '':
            # Accesarea cheilor folosind valorile acestora (inversul criptării)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

# Funcții pentru interfața grafică
def encrypt_message():
    message = input_text.get("1.0", tk.END).strip().upper()
    if not message:
        messagebox.showerror("Eroare", "Introduceți un text pentru criptare!")
        return
    encrypted_message = encrypt(message)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_message)

def decrypt_message():
    message = input_text.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Eroare", "Introduceți un cod Morse pentru decriptare!")
        return
    try:
        decrypted_message = decrypt(message)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_message)
    except ValueError:
        messagebox.showerror("Eroare", "Cod Morse invalid!")

# Interfața utilizatorului cu Tkinter
root = tk.Tk()
root.title("Translator cod Morse")

# Intrare text
input_label = tk.Label(root, text="Introduceți textul (Engleză sau Morse):", font=("Arial", 12))
input_label.pack(pady=5)

input_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
input_text.pack(pady=5)

# Butoane pentru criptare și decriptare
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

encrypt_button = tk.Button(button_frame, text="Criptare", font=("Arial", 12), command=encrypt_message)
encrypt_button.grid(row=0, column=0, padx=5)

decrypt_button = tk.Button(button_frame, text="Decriptare", font=("Arial", 12), command=decrypt_message)
decrypt_button.grid(row=0, column=1, padx=5)

# Rezultatul afișat
output_label = tk.Label(root, text="Rezultatul:", font=("Arial", 12))
output_label.pack(pady=5)

output_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
output_text.pack(pady=5)

# Rulează aplicația
root.mainloop()
