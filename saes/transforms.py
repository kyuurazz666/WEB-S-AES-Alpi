from copy import deepcopy

from .constants import (
    SBOX,
    INV_SBOX,
    MIX_COLUMNS_MATRIX,
    INV_MIX_COLUMNS_MATRIX
)

from .gf import GFArithmetic

from .state import State


class Transform:

    @staticmethod
    def sub_nibbles(state: State):

        result = state.copy()

        for r in range(2):
            for c in range(2):

                value = result.matrix[r][c]

                result.matrix[r][c] = SBOX[value]

        return result

    @staticmethod
    def inv_sub_nibbles(state: State):

        result = state.copy()

        for r in range(2):
            for c in range(2):

                value = result.matrix[r][c]

                result.matrix[r][c] = INV_SBOX[value]

        return result

    @staticmethod
    def shift_rows(state: State):

        result = state.copy()

        result.matrix[1][0], result.matrix[1][1] = \
            result.matrix[1][1], result.matrix[1][0]

        return result

    @staticmethod
    def inv_shift_rows(state: State):

        # karena hanya 2 kolom
        return Transform.shift_rows(state)

    @staticmethod
    def add_round_key(state: State, key: State):

        return state.xor(key)
    
    @staticmethod
    def mix_columns(state: State):

        result = state.copy()

        s00 = state.get(0, 0)
        s01 = state.get(0, 1)
        s10 = state.get(1, 0)
        s11 = state.get(1, 1)

        result.set(
            0,
            0,
            GFArithmetic.multiply(1, s00)
            ^ GFArithmetic.multiply(4, s10)
        )

        result.set(
            1,
            0,
            GFArithmetic.multiply(4, s00)
            ^ GFArithmetic.multiply(1, s10)
        )

        result.set(
            0,
            1,
            GFArithmetic.multiply(1, s01)
            ^ GFArithmetic.multiply(4, s11)
        )

        result.set(
            1,
            1,
            GFArithmetic.multiply(4, s01)
            ^ GFArithmetic.multiply(1, s11)
        )

        return result
        
    
    @staticmethod
    def inv_mix_columns(state: State):

        result = state.copy()

        s00 = state.get(0, 0)
        s01 = state.get(0, 1)
        s10 = state.get(1, 0)
        s11 = state.get(1, 1)

        result.set(
            0,
            0,
            GFArithmetic.multiply(9, s00)
            ^ GFArithmetic.multiply(2, s10)
        )

        result.set(
            1,
            0,
            GFArithmetic.multiply(2, s00)
            ^ GFArithmetic.multiply(9, s10)
        )

        result.set(
            0,
            1,
            GFArithmetic.multiply(9, s01)
            ^ GFArithmetic.multiply(2, s11)
        )

        result.set(
            1,
            1,
            GFArithmetic.multiply(2, s01)
            ^ GFArithmetic.multiply(9, s11)
        )

        return result
    