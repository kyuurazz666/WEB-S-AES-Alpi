from .state import State
from .transforms import Transform
from .key_expansion import KeyExpansion
from .logger import Logger

class InvSAES:

    def __init__(self, key):

        self.logger = Logger()

        ks = KeyExpansion(key)
        result = ks.generate()

        self.k0 = State(result["round_keys"]["K0"])
        self.k1 = State(result["round_keys"]["K1"])
        self.k2 = State(result["round_keys"]["K2"])

    
    def decrypt(self, ciphertext):

        self.logger.clear()

        state = State(ciphertext)

        self.logger.add("Ciphertext", state)

        # Initial Round
        state = Transform.add_round_key(state, self.k2)
        self.logger.add("AddRoundKey K2", state)

        # Round 2
        state = Transform.inv_shift_rows(state)
        self.logger.add("InvShiftRows", state)

        state = Transform.inv_sub_nibbles(state)
        self.logger.add("InvSubNib", state)

        # Round 1
        state = Transform.add_round_key(state, self.k1)
        self.logger.add("AddRoundKey K1", state)

        state = Transform.inv_mix_columns(state)
        self.logger.add("InvMixColumns", state)

        state = Transform.inv_shift_rows(state)
        self.logger.add("InvShiftRows", state)

        state = Transform.inv_sub_nibbles(state)
        self.logger.add("InvSubNib", state)

        # Final
        state = Transform.add_round_key(state, self.k0)
        self.logger.add("Recovered Plaintext", state)

        return state.to_int()