from setuptools import find_packages, setup

setup(
    name="linearCryptanalysis",
    author="Dimitri Lesnoff",
    author_email="dimitri.lesnoff@gmail.com",
    # FIXME(Dimitri): add github url
    # url="https://",
    # packages=find_packages('linearCryptanalysis'),
    version='0.0.1',
    # FIXME(Dimitri, 28 avril 2020): enable git version
    # setup_requires=[
    #     'setuptools_scm',  # versions through git releases
    # ],
    # use_scm_version=True,
    python_requires='>=3.8',
    install_requires=[
        'numpy>=1.20.2',  # probably lower versions work though
    ],
    extras_require={'test': ['pytest']},
    # entry_points={
    #     'console_scripts': ['']
    # },
    include_package_data=True
)
