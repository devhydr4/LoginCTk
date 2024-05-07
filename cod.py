import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Login feito com sucesso!")


texto = customtkinter.CTkLabel(janela, text="Fazer Login na rede")
texto.pack(padx=10, pady=10)


email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=15, pady=15)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=15, pady=15)

checkbox = customtkinter.CTkCheckBox(janela, text="Lembrar login?")
checkbox.pack(padx=15, pady=15)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=15, pady=15)

janela.mainloop()
