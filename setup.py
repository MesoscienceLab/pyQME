from setuptools import setup, find_packages

setup(
    name="pyQME",
    version="0.0.1",
    url="https://molimen1.dcci.unipi.it/p.saraceno/pyQME",
    author="Piermarco Saraceno, Lorenzo Cupellini",
    author_email="piermarco.saraceno@phd.unipi.it",
    description=open("README.md").read(),
    packages=find_packages(),
    python_requires='>3.8',
    install_requires=[
        "numpy>=1.26",  # safe baseline for new Python
        "scipy>=1.13",
        "opt_einsum>=3.3",
        "tqdm>=4.60",
        "psutil>=5.8",
        "matplotlib>=3.8",
    ],
)
