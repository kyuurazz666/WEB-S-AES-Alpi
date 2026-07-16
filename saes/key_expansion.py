"""
=========================================================
key_expansion.py

Key Expansion (Key Schedule)
Simplified AES (S-AES)

Menghasilkan:
- w0
- w1
- w2
- w3
- w4
- w5
- K0
- K1
- K2

Sekaligus menyimpan seluruh proses perhitungan
untuk ditampilkan pada halaman Step-by-Step.
=========================================================
"""


from .constants import (
    SBOX,
    RCON1,
    RCON2
)


class KeyExpansion:

    def __init__(self, master_key: int):

        if not (0 <= master_key <= 0xFFFF):
            raise ValueError("Master key harus 16-bit.")

        self.master_key = master_key
        self.steps = []

    # =====================================================
    # Utility
    # =====================================================

    @staticmethod
    def to_binary(value: int, bits: int = 8) -> str:
        return format(value, f"0{bits}b")

    @staticmethod
    def to_hex(value: int, digits: int = 2) -> str:
        return format(value, f"0{digits}X")

    # =====================================================
    # RotWord
    # =====================================================

    def rot_word(self, word: int) -> int:
        """
        Contoh

        AB

        menjadi

        BA
        """

        return ((word << 4) | (word >> 4)) & 0xFF

    # =====================================================
    # SubWord
    # =====================================================

    def sub_word(self, word: int) -> int:

        left = (word >> 4) & 0xF
        right = word & 0xF

        sub_left = SBOX[left]
        sub_right = SBOX[right]

        return (sub_left << 4) | sub_right

    # =====================================================
    # Logger
    # =====================================================

    def add_step(
        self,
        title,
        operation,
        formula,
        inputs,
        result
    ):

        self.steps.append({

            "title": title,

            "operation": operation,

            "formula": formula,

            "inputs": inputs,

            "result": result

        })

    # =====================================================
    # Generate Key Schedule
    # =====================================================

    def generate(self):

        self.steps.clear()

        # ---------------------------------------------

        w0 = (self.master_key >> 8) & 0xFF
        w1 = self.master_key & 0xFF

        self.add_step(

            title="Split Master Key",

            operation="Split",

            formula="MasterKey -> w0 || w1",

            inputs={

                "Master Key": self.to_binary(self.master_key, 16)

            },

            result={

                "w0": self.to_binary(w0),

                "w1": self.to_binary(w1)

            }

        )

        # ---------------------------------------------

        rot1 = self.rot_word(w1)

        self.add_step(

            title="RotWord 1",

            operation="RotWord",

            formula="RotWord(w1)",

            inputs={

                "w1": self.to_binary(w1)

            },

            result={

                "RotWord": self.to_binary(rot1)

            }

        )

        # ---------------------------------------------

        sub1 = self.sub_word(rot1)

        self.add_step(

            title="SubWord 1",

            operation="Substitution",

            formula="SubWord(RotWord(w1))",

            inputs={

                "RotWord": self.to_binary(rot1)

            },

            result={

                "SubWord": self.to_binary(sub1)

            }

        )

        # ---------------------------------------------

        w2 = w0 ^ sub1 ^ RCON1

        self.add_step(

            title="Generate w2",

            operation="XOR",

            formula="w2 = w0 XOR SubWord XOR RCON1",

            inputs={

                "w0": self.to_binary(w0),

                "SubWord": self.to_binary(sub1),

                "RCON1": self.to_binary(RCON1)

            },

            result={

                "w2": self.to_binary(w2)

            }

        )

        # ---------------------------------------------

        w3 = w2 ^ w1

        self.add_step(

            title="Generate w3",

            operation="XOR",

            formula="w3 = w2 XOR w1",

            inputs={

                "w2": self.to_binary(w2),

                "w1": self.to_binary(w1)

            },

            result={

                "w3": self.to_binary(w3)

            }

        )

        # ---------------------------------------------

        rot2 = self.rot_word(w3)

        self.add_step(

            title="RotWord 2",

            operation="RotWord",

            formula="RotWord(w3)",

            inputs={

                "w3": self.to_binary(w3)

            },

            result={

                "RotWord": self.to_binary(rot2)

            }

        )

        # ---------------------------------------------

        sub2 = self.sub_word(rot2)

        self.add_step(

            title="SubWord 2",

            operation="Substitution",

            formula="SubWord(RotWord(w3))",

            inputs={

                "RotWord": self.to_binary(rot2)

            },

            result={

                "SubWord": self.to_binary(sub2)

            }

        )

        # ---------------------------------------------

        w4 = w2 ^ sub2 ^ RCON2

        self.add_step(

            title="Generate w4",

            operation="XOR",

            formula="w4 = w2 XOR SubWord XOR RCON2",

            inputs={

                "w2": self.to_binary(w2),

                "SubWord": self.to_binary(sub2),

                "RCON2": self.to_binary(RCON2)

            },

            result={

                "w4": self.to_binary(w4)

            }

        )

        # ---------------------------------------------

        w5 = w4 ^ w3

        self.add_step(

            title="Generate w5",

            operation="XOR",

            formula="w5 = w4 XOR w3",

            inputs={

                "w4": self.to_binary(w4),

                "w3": self.to_binary(w3)

            },

            result={

                "w5": self.to_binary(w5)

            }

        )

        # ---------------------------------------------

        K0 = (w0 << 8) | w1
        K1 = (w2 << 8) | w3
        K2 = (w4 << 8) | w5

        self.add_step(

            title="Round Keys",

            operation="Combine",

            formula="K0=w0||w1, K1=w2||w3, K2=w4||w5",

            inputs={

                "w0": self.to_binary(w0),

                "w1": self.to_binary(w1),

                "w2": self.to_binary(w2),

                "w3": self.to_binary(w3),

                "w4": self.to_binary(w4),

                "w5": self.to_binary(w5)

            },

            result={

                "K0": self.to_binary(K0, 16),

                "K1": self.to_binary(K1, 16),

                "K2": self.to_binary(K2, 16)

            }

        )

        # ---------------------------------------------
        self.words = {

            "w0": w0,
            "w1": w1,
            "w2": w2,
            "w3": w3,
            "w4": w4,
            "w5": w5

        }
        self.round_keys = {

            "K0": K0,
            "K1": K1,
            "K2": K2

        }

        return {

            "master_key": self.master_key,

            "words": {

                "w0": w0,
                "w1": w1,
                "w2": w2,
                "w3": w3,
                "w4": w4,
                "w5": w5

            },

            "round_keys": {

                "K0": K0,
                "K1": K1,
                "K2": K2

            },

            "steps": self.steps

        }