alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_run=False
while not keep_run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def ceaser(start_text,shift_amount,cipher_direction):
        end_text=""
        if cipher_direction=="decode":
            shift_amount*=-1
        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_amount
                if new_position >= len(alphabet):
                    new_position= new_position -len(alphabet)
                end_text+= alphabet[new_position]
            else:
                end_text+=char
        print(f"The {direction}d text is {end_text}")
    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
    restart=input("Do you want to restart: Type 'yes' or 'no'\n")
    if restart=="no":
        keep_run=True
        print("thank you")
    
        
   

  