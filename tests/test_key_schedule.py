from saes.key_expansion import KeyExpansion

key = int("0100101011110101", 2)

ks = KeyExpansion(key)

result = ks.generate()

print("=" * 60)

print("ROUND KEYS")

print("=" * 60)

for name, value in result["round_keys"].items():
    print(name, format(value, "016b"))

print()

print("=" * 60)

print("STEP BY STEP")

print("=" * 60)

for step in result["steps"]:

    print(step["title"])

    print(step["formula"])

    print("Input :")

    for k, v in step["inputs"].items():
        print(f"   {k:10}: {v}")

    print("Output :")

    for k, v in step["result"].items():
        print(f"   {k:10}: {v}")

    print("-" * 60)