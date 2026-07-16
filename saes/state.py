from copy import deepcopy


class State:

    def __init__(self, value: int):

        if not (0 <= value <= 0xFFFF):
            raise ValueError("State harus 16-bit.")

        self.matrix = self.from_int(value)

 
    # Integer -> Matrix

    @staticmethod
    def from_int(value: int):

        n0 = (value >> 12) & 0xF
        n1 = (value >> 8) & 0xF
        n2 = (value >> 4) & 0xF
        n3 = value & 0xF

        return [
            [n0, n2],
            [n1, n3]
        ]

   
    # Matrix -> Integer

    def to_int(self):

        return (
            (self.matrix[0][0] << 12)
            | (self.matrix[1][0] << 8)
            | (self.matrix[0][1] << 4)
            | self.matrix[1][1]
        )


    # Copy

    def copy(self):

        s = State(0)
        s.matrix = deepcopy(self.matrix)
        return s

  
    # Getter

    def get(self, row, col):

        return self.matrix[row][col]

    # Setter

    def set(self, row, col, value):

        self.matrix[row][col] = value & 0xF


    # XOR

    def xor(self, other):

        result = self.copy()

        for r in range(2):
            for c in range(2):
                result.matrix[r][c] ^= other.matrix[r][c]

        return result

 
    # Formatter

    def to_binary(self):

        return format(self.to_int(), "016b")

    def to_hex(self):

        return format(self.to_int(), "04X")

    def to_list(self):

        return deepcopy(self.matrix)

    def pretty(self):

        rows = []

        rows.append("+-----+-----+")

        for row in self.matrix:

            rows.append(f"| {row[0]:X} | {row[1]:X} |")
            rows.append("+-----+-----+")

        return "\n".join(rows)