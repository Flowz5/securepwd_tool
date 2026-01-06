import string
import secrets
import math

def calculate_entropy(password):
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(c in string.punctuation for c in password): pool_size += 32
    
    entropy = len(password) * math.log2(pool_size)
    return entropy

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def main():
    print("--- SecurePwd Generator ---")
    try:
        length = int(input("Longueur souhaitée (min 12 recommandé) : "))
    except ValueError:
        length = 12

    pwd = generate_password(length)
    entropy = calculate_entropy(pwd)

    print(f"\nMot de passe généré : {pwd}")
    print(f"Entropie : {entropy:.2f} bits")

    if entropy < 60:
        print("Niveau : 🔴 Faible")
    elif entropy < 80:
        print("Niveau : 🟠 Moyen")
    else:
        print("Niveau : 🟢 Fort (Recommandé)")

if __name__ == "__main__":
    main()