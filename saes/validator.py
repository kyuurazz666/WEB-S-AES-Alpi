class Validator:

    @staticmethod
    def is_binary(text: str) -> bool:
        """
        Memeriksa apakah string merupakan biner 16-bit.
        """
        text = text.strip().replace(" ", "")

        return (
            len(text) == 16
            and all(ch in "01" for ch in text)
        )

    @staticmethod
    def is_hex(text: str) -> bool:
        """
        Memeriksa apakah string merupakan hexadecimal 4 digit.
        """
        text = text.strip().upper()

        if len(text) != 4:
            return False

        allowed = "0123456789ABCDEF"

        return all(ch in allowed for ch in text)

    @staticmethod
    def detect_type(text: str):
        """
        Mengembalikan tipe input.
        """

        if Validator.is_binary(text):
            return "binary"

        if Validator.is_hex(text):
            return "hex"

        return None

    @staticmethod
    def parse(text: str) -> int:
        """
        Mengubah input menjadi integer.
        """

        text = text.strip().replace(" ", "").upper()

        t = Validator.detect_type(text)

        if t == "binary":
            return int(text, 2)

        if t == "hex":
            return int(text, 16)

        raise ValueError(
            "Input harus berupa Binary 16-bit atau Hexadecimal 4 digit."
        )