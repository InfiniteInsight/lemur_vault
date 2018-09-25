"""Basic package information."""
from __future__ import absolute_import
from setuptools import setup, find_packages

install_requires = [
    'lemur',
    'Flask',
    'requests',
    'pyOpenSSL',
]

setup(
    name='lemur_vault',
    version='0.4',
    author='Ron Cohen',
    author_email='roncohen04@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'lemur.plugins': [
            'vault_issuer = lemur_vault.plugin:VaultIssuerPlugin',
        ]
    }
)
