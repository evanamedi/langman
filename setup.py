from setuptools import setup, find_packages

setup(
    name="langman",
    version="1.0.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # Ensure it points to the src directory
    entry_points={
        'console_scripts': [
            'langman=langman.langman:main',  # Update this to reflect the correct module path
        ],
    },
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)