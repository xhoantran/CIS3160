"""
/*=============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Vigenere cipher
|
| Author: Your name here
| Language: c, c++, Java, go, python
|
| To Compile: javac pa01.java
| gcc -o pa01 pa01.c
| g++ -o pa01 pa01.cpp
| go build pa01.go
| python pa01.py
|
| To Execute: java -> java pa01 kX.txt pX.txt
| or c++ -> ./pa01 kX.txt pX.txt
| or c -> ./pa01 kX.txt pX.txt
| or go -> ./pa01 kX.txt pX.txt
| or python -> python pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Fall 2022
| Instructor: McAlpin
| Due Date: per assignment
|
+=============================================================================*/
"""

class VigenereCipher:
    def __init__(self, key):
        # clean up the key
        key = "".join([c for c in key if c.isalpha()])
        self.key = key.lower()

    # Return alphabetically order of a character
    @staticmethod
    def getAlphabetOrd(char):
        return ord(char) - 97

    def encrypt(self, plaintext):
        # clean up the plaintext
        plaintext = "".join([c for c in plaintext if c.isalpha()])
        plaintext = plaintext.lower()
        if len(plaintext) < 512:
          plaintext += "x" * (512 - len(plaintext))
        else:
          plaintext = plaintext[:512]

        # encrypt the plaintext
        ciphertext = ""
        for i in range(len(plaintext)):
            c = plaintext[i]
            k = self.key[i % len(self.key)]
            ciphertext += chr((self.getAlphabetOrd(c) + self.getAlphabetOrd(k)) % 26 + 97)

        # ta da!
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i in range(len(ciphertext)):
            c = ciphertext[i]
            k = self.key[i % len(self.key)]
            plaintext += chr((self.getAlphabetOrd(c) - self.getAlphabetOrd(k)) % 26 + 97)
        return plaintext

def main(argv):
    # check for correct number of arguments
    if len(argv) != 3:
        print("Usage: python pa01.py keyfile plaintextfile")
        return

    # read in the key file
    keyfile = argv[1]
    plaintextfile = argv[2]


    # read in the plaintext file
    with open(keyfile, "r") as f:
        key = f.read()

    # read in the plaintext file
    with open(plaintextfile, "r") as f:
        plaintext = f.read()

    cipher = VigenereCipher(key)
    ciphertext = cipher.encrypt(plaintext)
    for i in range(0, len(ciphertext), 80):
        print(ciphertext[i:i+80])

if __name__ == "__main__":
    import sys
    main(sys.argv)

"""
/*=============================================================================
| I Hoan Tran (ho638953) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================*/
"""