import random
import string

def generate_password_for_site(site, complexity, keyword="", favorite_symbol="", favorite_number=""):
    site = site.lower()
    if site == "google":
        length = 8 if complexity == "soft" else 10 if complexity == "medium" else 12
        characters = string.ascii_letters + string.digits
        rules = "Google: Include letters and digits, no special characters."
    elif site == "microsoft":
        length = 10 if complexity == "soft" else 12 if complexity == "medium" else 15
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "Microsoft: Include letters, digits, and special characters."
    elif site == "chatgpt":
        length = 12 if complexity == "soft" else 14 if complexity == "medium" else 16
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "ChatGPT: Include letters, digits, and special characters."
    elif site == "instagram":
        length = 8 if complexity == "soft" else 10 if complexity == "medium" else 12
        characters = string.ascii_letters + string.digits + "_"
        rules = "Instagram: Include letters, digits, and underscores."
    elif site == "facebook":
        length = 10 if complexity == "soft" else 12 if complexity == "medium" else 14
        characters = string.ascii_letters + string.digits + "#@"
        rules = "Facebook: Include letters, digits, and #/@ special characters."
    elif site == "github":
        length = 12 if complexity == "soft" else 14 if complexity == "medium" else 16
        characters = string.ascii_letters + string.digits + "-_."
        rules = "GitHub: Include letters, digits, and -/_. special characters."
    elif site == "skillrack":
        length = 9 if complexity == "soft" else 11 if complexity == "medium" else 13
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "SkillRack: Include letters, digits, and special characters."
    elif site == "internshala":
        length = 8 if complexity == "soft" else 10 if complexity == "medium" else 12
        characters = string.ascii_letters + string.digits
        rules = "Internshala: Include letters and digits."
    elif site == "default":
        length = 8 if complexity == "soft" else 10 if complexity == "medium" else 12
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "Default: Include letters, digits, and special characters."
    else:
        return "Invalid site name! Choose a valid option.", ""

    
    password = ''.join(random.choice(characters) for _ in range(length - len(keyword)))

    
    customized_password = keyword + password + favorite_symbol + favorite_number

    
    if not any(char.islower() for char in customized_password):
        customized_password += random.choice(string.ascii_lowercase)
    if not any(char.isupper() for char in customized_password):
        customized_password += random.choice(string.ascii_uppercase)
    if not any(char.isdigit() for char in customized_password):
        customized_password += random.choice(string.digits)

    if "_" in characters and "_" not in customized_password:
        customized_password += "_"
    if "-" in characters and "-" not in customized_password:
        customized_password += "-"
    if "#" in characters and "#" not in customized_password:
        customized_password += "#"

    return customized_password, rules


print("=" * 40)
print("\tWelcome to the Password Generator!")
print("=" * 40)
print("Supported Sites: Google, Microsoft, ChatGPT, Instagram, Facebook, GitHub, SkillRack, Internshala, Default")
print("=" * 40)


site_name = input("Enter the site for which password is required: ").strip()
complexity = input("Enter desired complexity (soft, medium, high): ").strip().lower()
favorite_keyword = input("Enter your favorite keyword (optional, press Enter to skip): ").strip()
favorite_symbol = input("Enter your favorite symbol (optional, press Enter to skip): ").strip()
favorite_number = input("Enter your favorite number (1 to 9, optional, press Enter to skip): ").strip()

 
passwords = []
for _ in range(3):
    password, rules = generate_password_for_site(site_name, complexity, favorite_keyword, favorite_symbol, favorite_number)
    passwords.append(password)

if passwords[0] != "Invalid site name! Choose a valid option.":
    print("\nPassword Rules:", rules)
    print("\nGenerated Passwords:")
    for i, pw in enumerate(passwords, 1):
        print(f"Password {i}: {pw}")
else:
    print(passwords[0])
