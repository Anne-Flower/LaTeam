import tkinter as tk

def exit_fullscreen(event=None):
    root.destroy()  # Ferme la fenêtre en appuyant sur une touche

# Création de la fenêtre principale
root = tk.Tk()
root.attributes("-fullscreen", True)  # Active le mode plein écran
root.configure(bg="black")  # Change la couleur de fond en noir

# Ajout d'un label pour afficher un message
message = tk.Label(
    root,
    text="Vos fichiers ont été chiffrés. Pour les récupérer, envoyez 1 000 000 BTC à l'adresse suivante : \n Contactez-nous à anneviola@gmail.com après execution du paiement.",
    font=("Arial", 24),
    fg="green",
    bg="black"
)
message.pack(expand=True)

root.bind("<Escape>", exit_fullscreen)

root.mainloop()
