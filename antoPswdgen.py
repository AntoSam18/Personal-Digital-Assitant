import random
import string

def generate_password_for_site(site, complexity, keyword="", favorite_symbol="", favorite_number="", password_length=None):
    site = site.lower()
    if site == "google":
        characters = string.ascii_letters + string.digits
        rules = "Google: Include letters and digits, no special characters."
    elif site == "microsoft":
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "Microsoft: Include letters, digits, and special characters."
    elif site == "chatgpt":
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "ChatGPT: Include letters, digits, and special characters."
    elif site == "instagram":
        characters = string.ascii_letters + string.digits + "_"
        rules = "Instagram: Include letters, digits, and underscores."
    elif site == "facebook":
        characters = string.ascii_letters + string.digits + "#@"
        rules = "Facebook: Include letters, digits, and #/@ special characters."
    elif site == "github":
        characters = string.ascii_letters + string.digits + "-_."
        rules = "GitHub: Include letters, digits, and -/_. special characters."
    elif site == "skillrack":
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "SkillRack: Include letters, digits, and special characters."
    elif site == "internshala":
        characters = string.ascii_letters + string.digits
        rules = "Internshala: Include letters and digits."
    elif site == "default":
        characters = string.ascii_letters + string.digits + string.punctuation
        rules = "Default: Include letters, digits, and special characters."
    else:
        return "Invalid site name! Choose a valid option.", ""

    if password_length is None:
        try:
            password_length = int(input(f"Enter desired password length for {site.capitalize()}: ").strip())
        except ValueError:
            print("Invalid input. Using a default length of 12.")
            password_length = 12

    # Generate the random portion of the password
    password = ''.join(random.choice(characters) for _ in range(password_length - len(keyword) - len(favorite_symbol) - len(favorite_number)))

    # Customize password with the keyword, favorite symbol, and number
    customized_password = keyword + password + favorite_symbol + favorite_number

    # Ensure compliance with rules if applicable
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

# Enhanced user interface
print("=" * 40)
print("\tWelcome to the Password Generator!")
print("=" * 40)
print("Supported Sites: Google, Microsoft, ChatGPT, Instagram, Facebook, GitHub, SkillRack, Internshala, Default")
print("=" * 40)

# Prompt user for inputs
site_name = input("Enter the site for which password is required: ").strip()
try:
    password_length = int(input(f"Enter the desired password length for {site_name.capitalize()}: ").strip())
except ValueError:
    print("Invalid input. Using a default length of 12.")
    password_length = 12

complexity = input("Enter desired complexity (soft, medium, high): ").strip().lower()
favorite_keyword = input("Enter your favorite keyword (optional, press Enter to skip): ").strip()
favorite_symbol = input("Enter your favorite symbol (optional, press Enter to skip): ").strip()
favorite_number = input("Enter your favorite number (1 to 9, optional, press Enter to skip): ").strip()

if complexity == "medium":
    medium_passwords = [
        generate_password_for_site(site_name, "medium", favorite_keyword, favorite_symbol, favorite_number, password_length)[0]
        for _ in range(3)
    ]
    print("\nGenerated Medium Complexity Passwords:")
    for i, pwd in enumerate(medium_passwords, 1):
        print(f"Medium {i}: {pwd}")

elif complexity == "soft":
    soft_passwords = [
        generate_password_for_site(site_name, "soft", favorite_keyword, favorite_symbol, favorite_number, password_length)[0]
        for _ in range(3)
    ]
    print("\nGenerated Soft Complexity Passwords:")
    for i, pwd in enumerate(soft_passwords, 1):
        print(f"Soft {i}: {pwd}")

elif complexity == "high":
    high_passwords = [
        generate_password_for_site(site_name, "high", favorite_keyword, favorite_symbol, favorite_number, password_length)[0]
        for _ in range(3)
    ]
    print("\nGenerated High Complexity Passwords:")
    for i, pwd in enumerate(high_passwords, 1):
        print(f"High {i}: {pwd}")

else:
    print("Invalid complexity option selected. Please choose soft, medium, or high.")
