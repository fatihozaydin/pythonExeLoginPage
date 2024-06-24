import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Entry Succefully",)
    else:
        messagebox.showerror("Entry Fault")

# Pencere oluşturma
root = tk.Tk()
root.title("Faceit Recoil Hack")
root.geometry("300x200")

# Kullanıcı adı etiketi ve giriş alanı
label_username = tk.Label(root, text="User Name")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Şifre etiketi ve giriş alanı
label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Giriş düğmesi
button_login = tk.Button(root, text="Entry", command=login)
button_login.pack(pady=20)

# Pencereyi çalıştırma
root.mainloop()
