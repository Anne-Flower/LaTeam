import tkinter as tk
from PIL import Image, ImageTk

def resize_image(event):
    """Redimensionne l'image selon la taille de la fenêtre."""
    # Obtenir les dimensions actuelles de la fenêtre
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Redimensionner l'image en fonction des nouvelles dimensions
    resized_image = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
    new_photo = ImageTk.PhotoImage(resized_image)

    # Mettre à jour l'image dans le label
    bg_label.config(image=new_photo)
    bg_label.image = new_photo  # Conserver une référence pour éviter le garbage collection

def exit_fullscreen(event=True):
    """Ferme la fenêtre en appuyant sur la touche Échap."""
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.attributes("-fullscreen", True)  # Active le mode plein écran

# Charger l'image
image_path = "rancon.png"  # Chemin vers l'image
bg_image = Image.open(image_path)  # Charge l'image avec Pillow
bg_photo = ImageTk.PhotoImage(bg_image)  # Convertit l'image pour tkinter

# Ajouter l'image dans un Label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Étire le Label pour remplir la fenêtre

# Lier l'événement de redimensionnement
root.bind("<Configure>", resize_image)

# Lier la touche Échap pour quitter
root.bind("<Escape>", exit_fullscreen)

# Lancer la boucle principale
root.mainloop()
