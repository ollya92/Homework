"""
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
Repeats of letters in the word are removed, then the cipher alphabet is generated
with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters
are used in alphabetical order, excluding those already used in the key.

Encryption: Keyword is "Crypto"

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Example:

cipher = Cipher("crypto")
cipher.encode("Hello world")
"Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
"""

import string


class Cipher:
    def __init__(self, code_word):
        self._code_word = code_word.upper()
        print(string.ascii_uppercase)
        str = ""
        for letter in string.ascii_uppercase:
            if letter not in self._code_word:
                str = str + letter
        self._out = self._code_word + str
        print(self._out)

    def encode(self, word):
        self._word = word.upper()
        res = ""
        for letter in self._word:
            if letter == " ":
                res = res + letter
            else:
                index = string.ascii_uppercase.find(letter)
                res = res + self._out[index]
        print(f"{self._word.lower()} -> {res.capitalize()}")


    def decode(self, word):
        self._word = word.upper()
        res = ""
        for letter in self._word:
            if letter == " ":
                res = res + letter
            else:
                index = self._out.find(letter)
                res = res + string.ascii_uppercase[index]
        print(f"{self._word.lower()} -> {res.capitalize()}")


if __name__ == "__main__":
    cipher = Cipher("crypto")
    cipher.encode("Hello world")
    cipher.decode("Fjedhc dn atidsn")