def encrypt(plain, shift):
    
    encrypted_text = ""
        # ABCD -> BCDA with shift of 1
        # ABCD -> CDEF with shift of 2
    
        number_of_charachters = 4
        base_charachter = "A"
    
        for char in plain:
            base_code = ord(base_charachter)
            current_code = ord(char)
            current_position = current_code - base_code # "A" would be 0, "B" would be 1, etc.
            shifted_position = (current_position + shift) % number_of_charachters
            shifted_code = base_code + shifted_position
            shifted_char = chr(shifted_code)
    
        return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)
    

    
    for charachter in plain: # "1"

    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

if __name__ == "__main__":
    pins = [
        "AAAA", 
        "BBBB",
        "ABCD",
        "ABAB",
    ]

for i, pin in enumerate(pins):
    shift = i + 1
    print("plain pin:", pin)
    print("shift by", shift)
    encrypted_pin = encrypt(pin, shift)
    print("encrypted pin:", encrypted_pin)
    decrypted_pin = decrypt(encrypted_pin, shift)
    print("decrypted pin:", decrypted_pin)

   