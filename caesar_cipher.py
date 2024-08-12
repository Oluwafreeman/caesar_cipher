# def prime_checker(number):
#     is_prime = True
#     if number == 1:
#         print("Not a prime number")
#         quit()
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime")
#     else:
#         print("Its not a prime number")
# num = int(input("enter a number"))
# prime_checker(num)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, cipher_direction):  
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter) 
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {cipher_direction}d text is: {cipher_text}")


from caesar_art import logo
print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift, cipher_direction = direction)
    user_response = input("Type 'yes' if you want to go again. Otherwise type 'no' ")
    if user_response == "no":
        should_continue = False