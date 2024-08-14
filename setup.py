from setuptools import setup, find_packages

setup(
    name="langman",
    version="1.0.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'langman=langman.langman:main',  # Note the correct module path
        ],
    },
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)