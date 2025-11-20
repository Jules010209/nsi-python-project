import customtkinter


def button_callback():
    print("button clicked")


app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(
    app,
    values=["option 1", "option 2"],
    command=optionmenu_callback,
    variable=optionmenu_var,
)


optionmenu.pack(padx=20, pady=20)
app.mainloop()


