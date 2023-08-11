alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) 

def cipher(start_text,shift_text,direction_position):
    end_text=""
    if direction== "decode":
        shift_text *=-1
    for letter in start_text:
        position=alphabet.index(letter)
        new_position= position+shift_text
        if new_position>= len(alphabet):
            new_position=new_position-len(alphabet)
        end_text+= alphabet[new_position]
    print(f"The {direction}d message is {end_text}")

cipher(start_text=text,shift_text=shift,direction_position=direction)