import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TurboMate:
    def __init__(self, root):
        self.root = root
        self.root.title("TurboMate - Windows GUI Customizer")
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="TurboMate", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.instructions_label = tk.Label(self.root, text="Select your customizable icon set:")
        self.instructions_label.pack(pady=5)

        self.select_icon_button = tk.Button(self.root, text="Browse Icon Set", command=self.browse_icon_set)
        self.select_icon_button.pack(pady=5)

        self.layout_label = tk.Label(self.root, text="Choose your preferred layout:")
        self.layout_label.pack(pady=5)

        self.layout_options = ["Grid", "List", "Custom"]
        self.selected_layout = tk.StringVar(value=self.layout_options[0])
        self.layout_menu = tk.OptionMenu(self.root, self.selected_layout, *self.layout_options)
        self.layout_menu.pack(pady=5)

        self.apply_button = tk.Button(self.root, text="Apply Customization", command=self.apply_customization)
        self.apply_button.pack(pady=20)

    def browse_icon_set(self):
        icon_path = filedialog.askopenfilename(title="Select Icon Set", filetypes=[("Icon files", "*.ico"), ("All files", "*.*")])
        if icon_path:
            self.icon_set = icon_path
            messagebox.showinfo("Icon Set Selected", f"Icon set selected: {icon_path}")

    def apply_customization(self):
        if hasattr(self, 'icon_set'):
            selected_layout = self.selected_layout.get()
            messagebox.showinfo("Customization Applied", f"Applied icon set: {self.icon_set} with {selected_layout} layout.")
        else:
            messagebox.showwarning("No Icon Set", "Please select an icon set before applying customization.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TurboMate(root)
    root.mainloop()