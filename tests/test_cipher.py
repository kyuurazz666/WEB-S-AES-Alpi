from saes.cipher import SAES

KEY = 0b1010011100111011

PLAINTEXT = 0b0110111101101011

cipher = SAES(KEY)

ciphertext = cipher.encrypt(PLAINTEXT)

print("=" * 60)

print("Ciphertext")

print(format(ciphertext, "016b"))

print(hex(ciphertext))

print()

print("=" * 60)

print("LOG")

print("=" * 60)

for step in cipher.get_logs():

    print()

    print(step["title"])

    print(step["binary"])

    print(step["hex"])


EXPECTED = 0x0738

assert ciphertext == EXPECTED