import subprocess
import sys
import termios
import tty

commands = [
    "make email",
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


def wait_for_key():
    print("Appuyez sur n'importe quelle touche pour continuer...")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def main():
    print("Simulation interactive du ransomware !")
    print("Appuyez sur n'importe quelle touche pour passer à la commande suivante (ou [Ctrl+C] pour quitter).\n")

    for command in commands:
        print(f"Prochaine étape : {command}")
        wait_for_key()
        execute_command(command)

    print("Simulation terminée!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulation interrompue. See you!")
