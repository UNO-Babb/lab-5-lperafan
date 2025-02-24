#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

def decode(message, key):
    #We will want to decode the message here.
    return caesar_cipher(message, -key)

def caesar_cipher(message, key):
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                alpha = alpha_upper
            else:
                alpha = alpha_lower
            spot = (alpha.find(letter) + key) % 26
            result += alpha[spot]
        else:
            result += letter
    return result

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)
    plaintext = decode(secret, key)
    print ("Decrypted:", plaintext)


if __name__ == '__main__':
  main()
