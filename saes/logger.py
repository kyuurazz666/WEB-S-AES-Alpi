from copy import deepcopy
from .formatter import Formatter


class Logger:

    def __init__(self):

        self.logs = []

    def clear(self):

        self.logs.clear()

    def add(self, title, state):

        self.logs.append({

            "step": len(self.logs) + 1,

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

        })

    def get_logs(self):

        return deepcopy(self.logs)