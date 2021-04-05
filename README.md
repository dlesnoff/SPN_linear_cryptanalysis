This program aims at implementing simple linear cryptanalysis.

As a personal learning project, the code’s purpose is not efficiency, but rather modularity and ease to use. It is currently a WIP.


To use it, clone repo. Setup venv with numpy.

Add the table of your SPN into the python file into the form of a tuple list.


To instantiate an object :

AES_sbox = sbox(AES_sbox_table, 16, 16)

To print the linear approximation table (Warning: don’t do this with more than 10x10 big tables):

print(AES_sbox.compute_linear_approximation_table())

To do:

- implement SPN as described in Douglas R. Stinson’s book « Applied Cryptography : Theory and Practice ».

- implement the attack itself.

- write simple test cases.