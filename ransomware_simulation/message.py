import tkinter as tk
from PIL import Image, ImageTk

def exit_fullscreen(root, event=None):
    """Ferme la fenêtre en appuyant sur la touche Échap."""
    root.destroy()

def message():
    root = tk.Tk()
    root.attributes("-fullscreen", True) 
    image_path = "rancon.png" 
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((1600, 900), Image.Resampling.LANCZOS)  # Redimension à 1600x900
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Calculer la position pour centrer l'image
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_offset = (screen_width - 1600) // 2
    y_offset = (screen_height - 900) // 2

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=x_offset, y=y_offset) 

    root.bind("<Escape>", lambda event: exit_fullscreen(root, event))

    root.mainloop()
