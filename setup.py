from setuptools import setup, find_packages

setup(
    name='youview',
    version='0.1',
    packages=find_packages(),
    install_requirements=[],
    author='Karl Kevin Domingo',
    author_email='karlkdomingo@gmail.com',
    description='Logger',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kbnskee/youview',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: Tested with Sindows'
    ],
)