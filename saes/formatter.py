from .state import State


class Formatter:


    # Integer -> Binary

    @staticmethod
    def binary(value: int) -> str:
        """
        0x6F6B

        menjadi

        0110 1111 0110 1011
        """

        bits = format(value, "016b")

        return " ".join(

            bits[i:i + 4]

            for i in range(0, 16, 4)

        )

  
    # Integer -> Hex

    @staticmethod
    def hex(value: int) -> str:

        return format(value, "04X")


    # State -> Matrix
   
    @staticmethod
    def matrix(state: State):

        m = state.to_list()

        return [

            [f"{m[0][0]:X}", f"{m[0][1]:X}"],

            [f"{m[1][0]:X}", f"{m[1][1]:X}"]

        ]

 
    # Pretty Matrix


    @staticmethod
    def pretty_matrix(state: State):

        m = Formatter.matrix(state)

        return (
            "+-----+-----+\n"
            f"|  {m[0][0]}  |  {m[0][1]}  |\n"
            "+-----+-----+\n"
            f"|  {m[1][0]}  |  {m[1][1]}  |\n"
            "+-----+-----+"
        )


    # Logger Object


    @staticmethod
    def step(title: str, state: State):

        return {

            "title": title,

            "binary": Formatter.binary(
                state.to_int()
            ),

            "hex": Formatter.hex(
                state.to_int()
            ),

            "matrix": Formatter.matrix(
                state
            )

        }


    # Round Key Formatter

    @staticmethod
    def round_key(name, value):

        return {

            "name": name,

            "binary": Formatter.binary(value),

            "hex": Formatter.hex(value)

        }