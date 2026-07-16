from .constants import IRREDUCIBLE_POLY


class GFArithmetic:

    @staticmethod
    def add(a: int, b: int) -> int:
        """
        Penjumlahan pada GF(2^4)
        Sama dengan XOR.
        """
        return a ^ b

    @staticmethod
    def mul(a: int, b: int) -> int:
        """
        Perkalian pada GF(2^4)
        menggunakan polinomial x⁴ + x + 1.
        """

        result = 0

        while b:

            if b & 1:
                result ^= a

            b >>= 1
            a <<= 1

            if a & 0b10000:
                a ^= IRREDUCIBLE_POLY

        return result & 0b1111

    @staticmethod
    def multiply(a: int, b: int) -> int:
        """
        Alias untuk mul()
        """
        return GFArithmetic.mul(a, b)