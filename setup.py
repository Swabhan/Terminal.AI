import setuptools


version = {}
with open("src/swibin/version.py", "r") as f:
    exec(f.read(), version)

version = version["__version__"]

setuptools.setup(
    name="swibin",
    version=version,
    author="Terminal AI",
    author_email="your.email@example.com",
    description="Smart error insights for Python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'openai==1.3.3',
        'python-dotenv',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'swibin=swibin.cli:main',
        ],
    },
)
