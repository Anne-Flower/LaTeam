import subprocess
import keyboard

commands = [
    "make email",
    "make run",
    "make encrypt",
    "make decrypt"
]

def execute_command(command):
    print(f"\n>>> Exécution : {command}")
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode == 0:
        print(f"Commande '{command}' exécutée !\n")
    else:
        print(f"Erreur avec la commande : {command}\n")

def main():
    print("Simulation interactive du ransomware !")
    print("Appuyez sur [Espace] pour passer à la commande suivante (ou [Ctrl+C] pour quitter).\n")
    
    for command in commands:
        print(f"Prochaine étape : {command}")
        keyboard.wait('space')
        execute_command(command)
    
    print("Simulation terminée!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulation interrompue. See you !")