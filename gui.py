import tkinter as tk
from tkinter import ttk, messagebox
import logic as logic
class AreaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Area Calculator")
        self.geometry("640x420")
        self.minsize(560, 380)
        self.entries = []
        self._build_ui()
        self.bind("<Return>", lambda e: self.calculate())
        self.listbox.selection_set(0)
        self.on_select()

    def _build_ui(self):
        left = ttk.Frame(self, padding=10)
        left.pack(side="left", fill="y")
        ttk.Label(left, text="Select Shape", font=("Tahoma", 12, "bold")).pack(anchor="w")
        self.listbox = tk.Listbox(left, font=("Tahoma", 11), height=10,
                                  exportselection=False, activestyle="none")
        for name in logic.shape_names():
            self.listbox.insert("end", name)
        self.listbox.pack(fill="y", expand=True, pady=6)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        right = ttk.Frame(self, padding=15)
        right.pack(side="left", fill="both", expand=True)

        self.title_lbl = ttk.Label(right, text="", font=("Tahoma", 15, "bold"))
        self.title_lbl.pack(anchor="w")
        self.formula_lbl = ttk.Label(right, text="", font=("Tahoma", 11), foreground="#555")
        self.formula_lbl.pack(anchor="w", pady=(0, 10))

        self.form = ttk.Frame(right)
        self.form.pack(fill="x")

        btns = ttk.Frame(right)
        btns.pack(fill="x", pady=12)
        ttk.Button(btns, text="Calculate", command=self.calculate).pack(side="left")
        ttk.Button(btns, text="Clear", command=self.clear).pack(side="left", padx=8)

        self.result_lbl = ttk.Label(right, text="", font=("Tahoma", 14, "bold"),
                                    foreground="#0a7a2f")
        self.result_lbl.pack(anchor="w", pady=10)

    def selected_name(self):
        sel = self.listbox.curselection()
        return self.listbox.get(sel[0]) if sel else None

    def on_select(self, event=None):
        name = self.selected_name()
        if not name:
            return
        self.title_lbl.config(text=name)
        self.formula_lbl.config(text=logic.get_formula(name))
        self.result_lbl.config(text="")

        for w in self.form.winfo_children():
            w.destroy()
        self.entries = []
        for i, label in enumerate(logic.get_fields(name)):
            ttk.Label(self.form, text=label, font=("Tahoma", 11)).grid(
                row=i, column=0, sticky="w", pady=5)
            e = ttk.Entry(self.form, width=18, font=("Tahoma", 11))
            e.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(e)
        if self.entries:
            self.entries[0].focus()

    def calculate(self):
        name = self.selected_name()
        try:
            values = [float(e.get()) for e in self.entries]
        except ValueError:
            messagebox.showerror("Invalid Data", "Please fill in all fields with numbers")
            return
        try:
            area = logic.calculate_area(name, values)
        except ValueError as err:
            messagebox.showerror("Invalid Data", str(err))
            return
        self.result_lbl.config(text=f"Area = {area:,.4f} sq. units")

    def clear(self):
        for e in self.entries:
            e.delete(0, "end")
        self.result_lbl.config(text="")
        if self.entries:
            self.entries[0].focus()


if __name__ == "__main__":
    AreaApp().mainloop()