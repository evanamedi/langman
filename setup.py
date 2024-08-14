from setuptools import setup, find_packages

setup(
    name="langman",  # This is the name of the package
    version="1.0.0",  # Package version
    packages=find_packages(where='src'),  # This specifies where to find the packages
    package_dir={'': 'src'},  # This tells setuptools that packages are under 'src'
    entry_points={
        'console_scripts': [
            'langman=langman:main',  # The command `langman` will execute `main` in `langman.py`
        ],
    },
    install_requires=[],  # List your dependencies here or in requirements.txt
    include_package_data=True,  # This includes non-Python files specified in MANIFEST.in
    zip_safe=False,  # This prevents setuptools from zipping the package, which can cause issues
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)