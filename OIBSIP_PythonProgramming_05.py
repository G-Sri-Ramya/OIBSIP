import secrets
import string

def generate_pass(length, letters, numbers, symbols):
    s = ""    #total characters included
    if letters:
        s += string.ascii_letters
    if numbers:
        s += string.digits
    if symbols:
        s += string.punctuation
    if not s:
        return "Error : You must select at least one character type."
    password = ''.join(secrets.choice(s) for _ in range(length) )
    return password





def main():
    print("=== Command - Line Password Generator ===")
    try:
        length_ip = input("Enter desired password length (e.g : 10) : ")
        length = int(length_ip)
        if length < 5:
            print("Length of password must be greater than 5.")
            length = 12
    except ValueError:
        print("Invalid number entered.")
        length = 12
    
    print("\nSelect character types : ")
    use_letters = input("Include letters (A-Z, a-z)? (y/n) : ").strip().lower() !='n'
    use_numbers = input("Include numbers (0-9)? (y/n) : ").strip().lower() != 'n'
    use_symbols = input("Include  symbols (!@#$)? (y/n) : ").strip().lower() !='n'
    password = generate_pass(length, use_letters, use_numbers, use_symbols)
    print("\n"+'='*20)
    print("Generated password : "+password)
    print("\n"+'='*20)
main()