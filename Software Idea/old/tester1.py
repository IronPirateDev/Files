import tkinter as tk

class ParkingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Home")
        self.master.geometry("800x600")
        self.master.configure(bg="#05162c")

        self.label = tk.Label(master, text="Parking Management System", bg="#05162c", fg="#ffffff", font=("Lucida Sans", 30))
        self.label.pack(pady=(50, 0))

        self.image = tk.PhotoImage(file="ParkingIcon1.png")
        self.image_label = tk.Label(master, image=self.image, bg="#05162c")
        self.image_label.pack()

        self.buttons_frame = tk.Frame(master, bg="#05162c")
        self.buttons_frame.pack(pady=(10, 50))

        self.button1 = tk.Button(self.buttons_frame, text="Car List Control", command=self.car_list_control, bg="#104386", fg="#ffffff", font=("Lucida Sans", 30), padx=20, pady=10)
        self.button1.pack(side="left", padx=20)

        self.button2 = tk.Button(self.buttons_frame, text="User List Control", command=self.user_list_control, bg="#104386", fg="#ffffff", font=("Lucida Sans", 30), padx=20, pady=10)
        self.button2.pack(side="left", padx=20)

        self.button3 = tk.Button(self.buttons_frame, text="Report Control", command=self.report_control, bg="#104386", fg="#ffffff", font=("Lucida Sans", 30), padx=20, pady=10)
        self.button3.pack(side="left", padx=20)

    def car_list_control(self):
        print("Car List Control button clicked")
        # Add your logic here for the Car List Control functionality

    def user_list_control(self):
        print("User List Control button clicked")
        # Add your logic here for the User List Control functionality

    def report_control(self):
        print("Report Control button clicked")
        # Add your logic here for the Report Control functionality

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingApp(root)
    root.mainloop()
