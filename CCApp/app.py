import tkinter as tk
import matplotlib
from tkinter import filedialog
import model
from PIL import Image, ImageTk

matplotlib.use("TkAgg")

def run_program():
    parameter = parameter_entry.get()
    fileExt = parameter.split(".")[-1].lower()
    num = model.run(parameter)
    show_results(fileExt, num)

def show_results(fileExt, num):
    if fileExt in ['mp4', 'avi', 'mov']:
        image = Image.open("result.png")
        image = image.resize((500, 500), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        result_window = tk.Toplevel(root)
        result_window.title("Results")
        result_window.image = image

        label = tk.Label(result_window, image=image)
        label.pack(fill=tk.BOTH, expand=True)

    else:
        result_window = tk.Toplevel(root)
        result_window.title("Results")

        label = tk.Label(result_window, text="Number of People: " + str(num))
        label.pack(fill=tk.BOTH, expand=True)

    back_button = tk.Button(result_window, text="Close", font=("Helvetica", 14), command=result_window.destroy)
    back_button.pack(pady=10)

def upload_file():
    file_path = filedialog.askopenfilename()
    parameter_entry.delete(0, "end")
    parameter_entry.insert(0, file_path)

def webcam():
    parameter_entry.delete(0, "end")
    parameter_entry.insert(0, "0")
    run_program()

root = tk.Tk()
root.title("Model Output")

parameter_label = tk.Label(root, text="Parameter:", font=("Helvetica", 14))
parameter_label.pack(pady=10)

parameter_entry = tk.Entry(root, font=("Helvetica", 14))
parameter_entry.pack(pady=10)

upload_button = tk.Button(root, text="Upload File", font=("Helvetica", 14), command=upload_file)
upload_button.pack(pady=10)

run_button = tk.Button(root, text="Run", font=("Helvetica", 14), command=run_program)
run_button.pack(pady=10)

web_button = tk.Button(root, text="Webcam", font=("Helvetica", 14), command=webcam)
web_button.pack(pady=10)

root.mainloop()
