from ceaser import logo
print(logo)
print("Welcome to Ceaser Cipher")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Enter the shift amount :\n"))


def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
    # new_letter = alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

# encrypt(plain_text= text , shift_amount= shift)

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
    # new_letter = alphabet[new_position]

  print(f"The decoded text is {plain_text}")



if direction == "encode":
  encrypt(plain_text = text , shift_amount = shift)
else:
  decrypt(cipher_text = text , shift_amount = shift)
    



