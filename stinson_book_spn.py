master_key = [0b0011, 0b1010, 0b1001, 0b0100, 0b1101, 0b0110, 0b0011, 0b1111]
# master_key = "0b00111010100101001101011000111111"
# master_key = (
# 0x3, 0xA, 0x9, 0x4, 0xD, 0x6, 0x3, 0xF
#)

plaintext = [0b0010, 0b0110, 0b1011, 0b0111]


class SPN:
    def __init__(self, masterkey, s_box, perm, n_rounds):
        self.round_keys = derive_key(masterkey)
        self.sbox = s_box
        self.permutation = perm
        self.n_rounds = n_rounds

    def encrypt(self, plaintext):
        state = convert(plaintext)
        for i in range(self.n_rounds - 1):
            state = self.add_round_key(state, self.round_keys[i])
            self.apply_s_box(state)
            state = self.permute_blocks(state)
        state = self.add_round_key(state, self.round_keys[n_rounds])
        self.apply_s_box(state)
        state = self.add_round_key(state, self.round_keys[-1])
        return convert(state)

    @property
    def __derive_key(self, masterkey):
        NotImplementedError

    def add_round_key(self, state):
        NotImplementedError

    def apply_s_box(self, state):
        NotImplementedError

    def permute_blocks(self, state):
        NotImplementedError

    @staticmethod
    def convert():
        pass


class StinsonBookSPN(SPN):
    perm = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    s_box_table = (
        0b1110, 0b0100, 0b1101, 0b0001, 0b0010, 0b1111, 0b1011, 0b1000,
        0b0011, 0b1010, 0b0110, 0b1100, 0b0101, 0b1001, 0b0000, 0b0111
    )
    def __derive_key(self, masterkey):
        pass

    def add_round_key(self, state):
        pass

    def apply_s_box(self, state):
        pass

    def permute_blocks(self, state):
        print(self.perm)
        pass