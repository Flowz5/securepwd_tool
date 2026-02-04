import string
import secrets
import math
import hashlib
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def check_pwned_api(password):
    """Vérifie si le mot de passe a été exposé dans une fuite de données."""
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    try:
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None
        
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0
    except:
        return None

def calculate_entropy(password):
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in string.punctuation for c in password): pool_size += 32
    
    if pool_size == 0: return 0
    return len(password) * math.log2(pool_size)

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def display_results(pwd, entropy, pwned_count):
    # Détermination du niveau
    if entropy < 60:
        level, color = "Faible", "red"
    elif entropy < 80:
        level, color = "Moyen", "yellow"
    else:
        level, color = "Fort", "green"

    # Affichage des résultats
    console.print(f"\n[bold]Mot de passe analysé :[/bold] [white on blue] {pwd} [/white on blue]")
    
    table = Table(title="Analyse de sécurité")
    table.add_column("Critère", style="cyan")
    table.add_column("Résultat", style="white")

    table.add_row("Entropie", f"{entropy:.2f} bits")
    table.add_row("Niveau", f"[{color}]{level}[/{color}]")
    
    if pwned_count is None:
        table.add_row("Fuite de données", "[yellow]Indisponible (Hors-ligne)[/yellow]")
    elif pwned_count > 0:
        table.add_row("Fuite de données", f"[bold red]⚠️ Compromis {pwned_count} fois ![/bold red]")
    else:
        table.add_row("Fuite de données", "[bold green]✅ Aucune fuite détectée[/bold green]")

    console.print(table)

def generate_password_flow():
    length = console.input("[bold]Longueur du mot de passe (défaut 16) : [/bold]")
    length = int(length) if length.isdigit() else 16
    
    pwd = generate_password(length)
    entropy = calculate_entropy(pwd)
    pwned_count = check_pwned_api(pwd)
    display_results(pwd, entropy, pwned_count)

def analyze_password_flow():
    pwd = console.input("[bold]Entrez le mot de passe à analyser : [/bold]")
    entropy = calculate_entropy(pwd)
    pwned_count = check_pwned_api(pwd)
    display_results(pwd, entropy, pwned_count)

def run():
    console.print(Panel("[bold cyan]SecurePwd Pro - Générateur & Analyseur[/bold cyan]", expand=False))
    
    console.print("\n[bold]Choisissez une option :[/bold]")
    console.print("1. Générer un nouveau mot de passe")
    console.print("2. Analyser un mot de passe existant")
    
    choice = console.input("\n[bold]Votre choix (1 ou 2) : [/bold]")
    
    if choice == '1':
        generate_password_flow()
    elif choice == '2':
        analyze_password_flow()
    else:
        console.print("[bold red]Option invalide. Veuillez choisir 1 or 2.[/bold red]")

if __name__ == "__main__":
    run()