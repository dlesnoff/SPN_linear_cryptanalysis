This programe aims at implementing simple linear cryptanalysis.

As a personal learning project, the code does not aim efficiency, but rather modularity and ease to use.


To use it, clone repo. Setup venv with numpy.

Add the table of your SPN into the python file into the form of a tuple list.


To instantiate an object :

AES_sbox = sbox(AES_sbox_table, 16, 16)

To print the linear approximation table (Warning: don’t do this with more than 10x10 big tables):

print(AES_sbox.compute_linear_approximation_table())