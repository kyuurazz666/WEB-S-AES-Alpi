# S-Box
SBOX = [
    0x9, 0x4, 0xA, 0xB,
    0xD, 0x1, 0x8, 0x5,
    0x6, 0x2, 0x0, 0x3,
    0xC, 0xE, 0xF, 0x7
]

# Inverse S-Box
INV_SBOX = [
    0xA, 0x5, 0x9, 0xB,
    0x1, 0x7, 0x8, 0xF,
    0x6, 0x0, 0x2, 0x3,
    0xC, 0x4, 0xD, 0xE
]

# GF(2^4) irreducible polynomial
IRREDUCIBLE_POLY = 0b10011

# RCON
RCON1 = 0b10000000
RCON2 = 0b00110000

# MixColumns Matrix
MIX_COLUMNS = [
    [1, 4],
    [4, 1]
]

# Inverse MixColumns Matrix
INV_MIX_COLUMNS = [
    [9, 2],
    [2, 9]
]


# MixColumns Matrix


# Matriks untuk enkripsi
MIX_COLUMNS_MATRIX = [
    [1, 4],
    [4, 1]
]

# Matriks untuk dekripsi
INV_MIX_COLUMNS_MATRIX = [
    [9, 2],
    [2, 9]
]