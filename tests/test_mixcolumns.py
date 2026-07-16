from saes.state import State
from saes.transforms import Transform

print("=" * 60)
print("TEST MIX COLUMNS")
print("=" * 60)

state = State(0xD728)

print("Original")
print(state.pretty())

mixed = Transform.mix_columns(state)

print("\nMixColumns")
print(mixed.pretty())

restored = Transform.inv_mix_columns(mixed)

print("\nInverse MixColumns")
print(restored.pretty())

assert restored.to_int() == state.to_int()

print("\n✓ MixColumns Test Passed")