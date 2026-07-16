from .state import State
from .logger import Logger
from .transforms import Transform
from .key_expansion import KeyExpansion

class SAES:

    def __init__(self, key: int):

        self.key = key
        self.logger = Logger()

        ks = KeyExpansion(key)
        result = ks.generate()

        self.key_schedule = result

        self.k0 = State(result["round_keys"]["K0"])
        self.k1 = State(result["round_keys"]["K1"])
        self.k2 = State(result["round_keys"]["K2"])

    
    def get_logs(self):

        return self.logger.get_logs()
    

    def encrypt(self, plaintext: int):

        self.logger.clear()

        state = State(plaintext)

        self.logger.add("Plaintext", state)

        # Initial Round

        state = Transform.add_round_key(state, self.k0)

        self.logger.add("AddRoundKey K0", state)

        # Round 1

        state = Transform.sub_nibbles(state)

        self.logger.add("SubNibbles", state)

        state = Transform.shift_rows(state)

        self.logger.add("ShiftRows", state)

        state = Transform.mix_columns(state)

        self.logger.add("MixColumns", state)

        state = Transform.add_round_key(state, self.k1)

        self.logger.add("AddRoundKey K1", state)

        # Round 2

        state = Transform.sub_nibbles(state)

        self.logger.add("SubNibbles", state)

        state = Transform.shift_rows(state)

        self.logger.add("ShiftRows", state)

        state = Transform.add_round_key(state, self.k2)

        self.logger.add("AddRoundKey K2", state)

        return state.to_int()
    
    def _initial_round(self, state):

        state = Transform.add_round_key(
            state,
            self.k0
        )

        self.logger.add(
            "Initial AddRoundKey",
            state
        )

        return state
    
    def _round1(self, state):

        state = Transform.sub_nibbles(state)
        self.logger.add("SubNib", state)

        state = Transform.shift_rows(state)
        self.logger.add("ShiftRows", state)

        state = Transform.mix_columns(state)
        self.logger.add("MixColumns", state)

        state = Transform.add_round_key(
            state,
            self.k1
        )

        self.logger.add("AddRoundKey K1", state)

        return state
    
    def _round2(self, state):

        state = Transform.sub_nibbles(state)
        self.logger.add("SubNib", state)

        state = Transform.shift_rows(state)
        self.logger.add("ShiftRows", state)

        state = Transform.add_round_key(
            state,
            self.k2
        )

        self.logger.add("AddRoundKey K2", state)

        return state
    
