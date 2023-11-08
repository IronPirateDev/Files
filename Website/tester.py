import tkinter as tk
def print_button_number(button_number1):
    root.destroy() 
    if button_number1==1:
        print('run def1')
    elif button_number1==2:
        print('run def2') 
    elif button_number1==3:
        print('run def3')  
    elif button_number1=='Tester':
        print('hello') 
def create_button(button_number):
    button = tk.Button(root, text=f'Button {button_number}', command=lambda: print_button_number(button_number))
    button.pack(pady=5)
root = tk.Tk()
root.title("Tester1")
root.geometry("200x200")
create_button(1)
create_button(2)
create_button(3)
create_button('Tester')
root.mainloop()