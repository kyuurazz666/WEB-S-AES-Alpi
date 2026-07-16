from saes.state import State

print("=" * 50)
print("TEST STATE")
print("=" * 50)

state = State(0xD728)

print("Binary :", state.to_binary())
print("Hex    :", state.to_hex())

print()
print(state.pretty())

copy_state = state.copy()

print()
print(copy_state.pretty())

xor_state = state.xor(State(0xFFFF))

print()
print(xor_state.pretty())