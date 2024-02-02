import re
from corpus_loader import word_list, name_list


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                print(result)
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
                print(result)
        else:
            result += char
    return result


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def crack(encrypted_text):

    for shift in range(26):
        decrypted = encrypt(encrypted_text, -shift)
        if is_english(decrypted_text=decrypted):
            return decrypted

    return ""  # Return an empty string if no known phrase is matched

def is_english(decrypted_text):
    english_word_count = 0
    
    for candidate_words in decrypted_text.split(): #spilts on whitespace
        word = re.sub(r'[^\w\s]', '', candidate_words)
        if word.lower() in word_list or word in name_list:
            english_word_count += 1

    percentage = int(english_word_count / len(decrypted_text.split()) * 100)

    if percentage > 50:
        return decrypted_text
    
    return ""
