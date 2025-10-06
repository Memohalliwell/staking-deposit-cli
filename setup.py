from setuptools import find_packages, setup
import warnings

"""
⚠️ DEPRECATED: This repository has been deprecated and is no longer maintained.
Please use the actively maintained fork at https://github.com/ethstaker/ethstaker-deposit-cli

THIS IS A STUB FOR RUNNING THE APP
"""

# Display deprecation warning when setup.py is run
warnings.warn(
    "\n" + "=" * 80 + "\n"
    "⚠️  DEPRECATION WARNING\n"
    "=" * 80 + "\n"
    "This repository (ethereum/staking-deposit-cli) has been DEPRECATED.\n"
    "It is no longer maintained and may contain security vulnerabilities.\n\n"
    "Please use the actively maintained fork instead:\n"
    "    https://github.com/ethstaker/ethstaker-deposit-cli\n"
    "=" * 80 + "\n",
    DeprecationWarning,
    stacklevel=2
)

setup(
    name="staking_deposit",
    version='2.8.0',
    py_modules=["staking_deposit"],
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.12,<4",
)
