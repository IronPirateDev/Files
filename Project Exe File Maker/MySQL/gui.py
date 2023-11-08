import customtkinter as ctk
def submit_entry():
    entry_text = entry.get()
    print(entry_text)
    root.destroy()  # Terminate the program after submitting
root = ctk.CTk()
root.geometry("300x200")
root.title("Entry Box Example")
label = ctk.CTkLabel(root, text="Enter your name:")
label.pack(pady=20)
entry = ctk.CTkEntry(root)
entry.pack()
button = ctk.CTkButton(root, text="Submit", command=submit_entry)
button.pack(pady=20)
root.bind("<Return>", lambda event: submit_entry())  # Only bind Enter key to submit
root.mainloop()
