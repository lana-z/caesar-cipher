def encrypt(plain, shift):
    
    encrypted_text = ""

    for charachter in plain: # "1" 

        num = int(charachter) # 1
        shifted_num = num + shift # integer 2
        shifted_charachter = str(shifted_num) # "2"

        encrypted_text += shifted_charachter # "2"

    return encrypted_text


def decrypt(encrypted, shift):
    return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
    plain_pin = "1234"
    encrypted_pin = encrypt(plain_pin, 1)
    assert encrypted_pin == "2345"
    assert decrypt(encrypted_pin, 1) == plain_pin
    print(encrypted_pin)

    plain_pin = "9999"
    encrypted_pin = encrypt(plain_pin, 1)
    assert encrypted_pin == "0000", encrypted_pin

    plain_pin = "5555"
