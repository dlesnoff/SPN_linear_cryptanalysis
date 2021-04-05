import numpy as np

s_box_table = (
    0b1110, 0b0100, 0b1101, 0b0001, 0b0010, 0b1111, 0b1011, 0b1000,
    0b0011, 0b1010, 0b0110, 0b1100, 0b0101, 0b1001, 0b0000, 0b0111
)


class Sbox:

    def __init__(self, table: tuple, input_length: int, output_length: int):
        self.table = table[:]
        if input_length < 1 or output_length < 1:
            raise ValueError("There must be at least one output/input variable")
        self.input_length = input_length
        self.output_length = output_length
        self.length = input_length * output_length

    def relationship(self, mask_input: str, mask_output: str, n: int) -> int:
        """ Compute the values of specific input and output random variables """
        x = str(bin(n))[2:].zfill(4)
        # print(f'x = ', x)
        y = str(bin(self.table[n])[2:]).zfill(4)
        # print(f'y = ', y)
        value = 0
        for index in range(self.input_length):
            if mask_input[index] == "1":
                value += int(x[index])
                value %= 2
        for index in range(self.output_length):
            if mask_output[index] == "1":
                value += int(y[index])
                value %= 2
        return value

    def number_correct_output_relation(self, mask_input, mask_output) -> int:
        count_zeros = 0
        for n in range(self.length):
            if self.relationship(mask_input, mask_output, n) == 0:
                count_zeros += 1
        return count_zeros

    def bias(self, a, b) -> float:
        return (self.number_correct_output_relation(a, b) - (self.length/2)) / self.length

    def compute_linear_approximation_table(self) -> np.ndarray:
        table = np.empty((2**self.input_length, 2**self.output_length), dtype=int)
        for a in range(2**self.input_length):
            mask_input = str(bin(a))[2:].zfill(4)
            for b in range(2**self.output_length):
                mask_output = str(bin(b))[2:].zfill(4)
                table[a, b] = self.number_correct_output_relation(mask_input, mask_output)
        return table

    def print_linear_approximation_table(a, b):
        pass


if __name__ == '__main__':
    s_box = Sbox(s_box_table, 4, 4)
    for i in range(16):
        print(f"i : {s_box.relationship('1001', '0100', i)}")
    print(s_box.number_correct_output_relation("1001", "0100"))
    print(s_box.number_correct_output_relation("0011", "1001"))
    print(s_box.bias("0011", "1001"))
    linear_approximation_table = s_box.compute_linear_approximation_table()
    print(linear_approximation_table)
