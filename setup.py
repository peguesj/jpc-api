from setuptools import setup, find_packages

setup(
    name='JamfProClassicAPI (jpc-api)',
    version='0.1.0',
    author='Jeremiah Pegues',
    author_email='jeremiah@pegues.io',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A package to sync user information between macOS workstations, Jamf Connect, and Jamf Pro.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/peguesj/jpc-api',
)
