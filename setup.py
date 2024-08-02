from setuptools import setup, find_packages

setup(
    name='my-python-app',  # Replace with your application's name
    version='0.1.0',       # Replace with your application's version
    description='A sample Python project',  # Replace with a description of your project
    author='Your Name',    # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    url='https://github.com/Sanketcloud25/python-ci',  # Replace with your project's URL
    packages=find_packages(where='src'),  # Includes all packages under 'src'
    package_dir={'': 'src'},  # Tells setuptools that packages are under 'src'
    install_requires=[
        # List your project’s dependencies here
        # e.g., 'numpy', 'requests', etc.
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Replace with the minimum Python version required
)
