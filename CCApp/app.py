import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import model

def run_program():
    parameter = parameter_entry.get()
    if not parameter:
        text.delete("1.0", "end")
        text.insert("end", "Please select a file" + "\n")
        return
    fileExt = parameter.split(".")[-1].lower()
    num = model.run(parameter)
    show_results(fileExt, num, parameter)

def show_results(fileExt, num, parameter):
    if fileExt in ['mp4', 'avi', 'mov']:
        image = Image.open("result.png")
        image = image.resize((500, 500), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        label = ctk.CTkLabel(root,text= "", image=image)
        label.pack(fill=ctk.BOTH, expand=True)
    else:
        label2 = ctk.CTkLabel(root, text= "Number of People in image " + parameter.split("/")[-1] + ": " + str(num),font=("Helvetica", 14))
        label2.pack(pady=1)

def upload_file():
    file_path = filedialog.askopenfilename()
    parameter_entry.delete(0, "end")
    parameter_entry.insert(0, file_path)

def webcam():
    parameter_entry.delete(0, "end")
    parameter_entry.insert(0, "0")
    run_program()


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.title("Crowd Counting App")

parameter_label = ctk.CTkLabel(root, text="file:", font=("Helvetica", 14))
parameter_label.pack(pady=1)

parameter_entry = ctk.CTkEntry(root, font=("Helvetica", 14))
parameter_entry.pack(pady=1)

upload_button = ctk.CTkButton(root, text="Select file", font=("Helvetica", 14), command=upload_file)
upload_button.pack(pady=10)

run_button = ctk.CTkButton(root, text="Run", font=("Helvetica", 14), command=run_program)
run_button.pack(pady=10)

web_button = ctk.CTkButton(root, text="Webcam", font=("Helvetica", 14), command=webcam)
web_button.pack(pady=10)

text = ctk.CTkTextbox(root, font=("Helvetica", 20), height=5)
text.pack(padx=10, pady=10)


root.mainloop()
