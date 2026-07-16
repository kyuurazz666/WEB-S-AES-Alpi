from saes.cipher import SAES
from saes.inv_cipher import InvSAES

KEY = 0b1010011100111011
PLAINTEXT = 0b0110111101101011

enc = SAES(KEY)

cipher = enc.encrypt(PLAINTEXT)

print("Cipher :", format(cipher, "04X"))

dec = InvSAES(KEY)

plain = dec.decrypt(cipher)

print("Plain  :", format(plain, "04X"))

assert plain == PLAINTEXT

print("\nSUCCESS")