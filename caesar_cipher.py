print("Caesar Cipher")

def caesar(text, shift, direction):
    output_text = ""
    shift = shift % 26  # Normalize shifts larger than 26

    if direction == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Compute shifted character with modulo wrap-around
            shifted_pos = (ord(char) - start + shift) % 26
            shifted_char = chr(start + shifted_pos)
            output_text += shifted_char
        else:
            # Non-alphabetic characters are unchanged
            output_text += char

    print(f"Here is the {direction}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    while direction not in ("encode", "decode"):
        print("Invalid input. Please type 'encode' or 'decode'.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to continue, otherwise type 'no'.\n").strip().lower()
    if restart == "no":
        should_continue = False
        print("See you later!")
