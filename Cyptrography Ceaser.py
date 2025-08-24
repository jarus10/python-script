import string

def ceasar_encrypt(message,key):

    shift = key % 26
    cipher =str.maketrans(string.ascii_lowercase,string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift])

    encrypted_meassage = message.lower().translate(cipher)

    return encrypted_meassage

def ceasar_decrypt(encypted_message,key):

    shift = 26 - (key % 26)
    cipher =str.maketrans(string.ascii_lowercase,string.ascii_lowercase[shift:]+string.ascii_lowercase[:shift])

    message = encrypted_message .translate(cipher)
    return message

message = "fsocitey"
key = 5  
encrypted_message = ceasar_encrypt(message,key)
print("Encrypted Message: ",{encrypted_message})

decrypted_message = ceasar_decrypt(encrypted_message,key)
print("Decrypted Message: ",{decrypted_message})
