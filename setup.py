from setuptools import find_packages, setup

setup(
    name="linearCryptanalysis",
    author="Dimitri Lesnoff",
    author_email="dimitri.lesnoff@gmail.com",
    url="https://github.com/dlesnoff/SPN_linear_cryptanalysis",
    # FIXME(Dimitri): understand the following line
    # packages=find_packages('linearCryptanalysis'),
    version='0.0.1',
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.20.2',  # probably lower versions work though
        'pycryptodome ~= 3.10.1'
    ],
    # extras_require={'test': ['pytest']},
    include_package_data=True
)
