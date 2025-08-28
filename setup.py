from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="whatsappbot",
    version="0.1.0",
    author="YourName",
    author_email="phogway@gmail.com",
    description="Extensible library for WhatsApp bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/whatsappbot",
    packages=find_packages(where="."),
    install_requires=[
        "requests",
        "flask",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)