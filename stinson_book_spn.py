from Crypto.Util import strxor
masterKey = [0b0011, 0b1010, 0b1001, 0b0100, 0b1101, 0b0110, 0b0011, 0b1111]
# master_key = "0b00111010100101001101011000111111"
# master_key = (
# 0x3, 0xA, 0x9, 0x4, 0xD, 0x6, 0x3, 0xF
#)

plaintext = [0b0010, 0b0110, 0b1011, 0b0111]


class SPN:
    def __init__(self, master_key, s_box, perm, n_rounds):
        self._round_keys = self.derive_key(master_key)
        self.sbox = s_box
        self.permutation = perm
        self.n_rounds = n_rounds

    def encrypt(self, plaintext):
        state = self.convert(plaintext)
        for i in range(self.n_rounds - 1):
            state = self.add_round_key(state, self._round_keys[i])
            self.apply_s_box(state)
            state = self.permute_blocks(state)
        state = self.add_round_key(state, self._round_keys[self.n_rounds])
        self.apply_s_box(state)
        state = self.add_round_key(state, self._round_keys[-1])
        return self.state_to_output(state)

    def derive_key(self, master_key):
        raise NotImplementedError

    def add_round_key(self, state, round_key):
        raise NotImplementedError

    def apply_s_box(self, state) -> None:
        raise NotImplementedError

    def permute_blocks(self, state):
        raise NotImplementedError

    @staticmethod
    def convert(input):
        state = [int(i) for i in input]
        return state

    @staticmethod
    def state_to_output(state):
        return ''.join([str(i) for i in state])


class StinsonBookSPN(SPN):
    perm_g = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
    s_box_table = (
        0b1110, 0b0100, 0b1101, 0b0001, 0b0010, 0b1111, 0b1011, 0b1000,
        0b0011, 0b1010, 0b0110, 0b1100, 0b0101, 0b1001, 0b0000, 0b0111
    )

    def __init__(self, master_key, s_box=s_box_table, perm=perm_g, n_rounds=4):
        super().__init__(master_key, s_box, perm, n_rounds)
        self._round_keys = self.derive_key(master_key)
        self.sbox = s_box
        self.permutation = perm
        self.n_rounds = n_rounds

    def derive_key(self, master_key: bytes) -> list:
        # assert len(master_key) >= 32
        return [master_key[4*r+1: 4*r+18] for r in range(0, 4)]

    def add_round_key(self, state, round_key):
        return strxor(state, round_key)

    def apply_s_box(self, state):
        state = [int(self.sbox[state[i]]) for i in range(len(state))]

    def permute_blocks(self, state):
        print(self.permutation)
        return [state[self.permutation[i]] for i in range(len(state))]


if __name__ == '__main__':
    sb = StinsonBookSPN(masterKey)
    ciphertext = sb.encrypt(plaintext)
    print(ciphertext)
