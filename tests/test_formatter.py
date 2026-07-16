from saes.state import State
from saes.formatter import Formatter

print("=" * 60)
print("TEST FORMATTER")
print("=" * 60)

state = State(0x6F6B)

print()

print("Binary")

print(Formatter.binary(state.to_int()))

print()

print("Hex")

print(Formatter.hex(state.to_int()))

print()

print("Matrix")

print(Formatter.matrix(state))

print()

print("Pretty Matrix")

print(Formatter.pretty_matrix(state))

print()

print("Step")

print(Formatter.step("Plaintext", state))

print()

print("Round Key")

print(Formatter.round_key("K0", 0xA73B))