import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    result = ""

    shift = shift % len(alphabet)
        
    if direction == "decode":
        # Negate the shift value to shift left
        shift = shift * (-1)
    
    for letter in text:
        if letter not in alphabet:
            result += letter
            
        else:
            alphabet_index = alphabet.index(letter)
            shifted_index = alphabet_index + shift
            
            if shifted_index >= len(alphabet):
                shifted_index = shifted_index - len(alphabet)
                
            result += alphabet[shifted_index]

    print(f"The {direction}d text is:\n {result}")



print(art.logo)

user_input = "yes"
while user_input == "yes":
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text=text, shift=shift, direction=direction)

    user_input = lower(input("Type 'yes' if you want to go again. Otherwise type 'no'."))


print("Goodbye!")