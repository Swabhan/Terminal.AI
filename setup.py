import setuptools

setuptools.setup(
    name="swibin",
    version="1.0.6",
    author="Swibin Team",
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
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'swibin=swibin.cli:main',
        ],
    },
)
