from saes.state import State
from saes.transforms import Transform

state = State(0xD728)

print("="*50)
print("ORIGINAL")
print("="*50)
print(state.pretty())

print()

sub = Transform.sub_nibbles(state)

print("="*50)
print("SUB NIBBLES")
print("="*50)
print(sub.pretty())

print()

shift = Transform.shift_rows(sub)

print("="*50)
print("SHIFT ROWS")
print("="*50)
print(shift.pretty())

print()

back = Transform.inv_shift_rows(shift)

print("="*50)
print("INV SHIFT")
print("="*50)
print(back.pretty())

print()

key = State(0xFFFF)

xor = Transform.add_round_key(state,key)

print("="*50)
print("ADD ROUND KEY")
print("="*50)
print(xor.pretty())