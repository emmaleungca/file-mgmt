import tkinter as tk
from tkinter import ttk
from functions import function_registry
import inspect


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Function Runner")
        self.geometry("400x400")

        self.func_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.func_var, values=list(function_registry.keys()))
        self.dropdown.pack()

        self.input_frame = tk.Frame(self)
        self.input_frame.pack()

        self.run_button = tk.Button(self, text="Run", command=self.run_selected_function)
        self.run_button.pack()

        self.output = tk.Text(self, height=10)
        self.output.pack()

        self.dropdown.bind("<<ComboboxSelected>>", self.update_input_fields)

    def update_input_fields(self, event=None):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.inputs = {}
        func = function_registry[self.func_var.get()]
        sig = inspect.signature(func)
        for param in sig.parameters.values():
            lbl = tk.Label(self.input_frame, text=param.name)
            lbl.pack()
            entry = tk.Entry(self.input_frame)
            entry.pack()
            self.inputs[param.name] = entry

    def run_selected_function(self):
        func = function_registry[self.func_var.get()]
        kwargs = {k: self.inputs[k].get() for k in self.inputs}
        try:
            result = func(**kwargs)
            self.output.insert(tk.END, str(result) + "\n")
        except Exception as e:
            self.output.insert(tk.END, f"Error: {e}\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
