import os
from setuptools import setup

PACKAGE_NAME = "wintools"

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open(os.path.join(PACKAGE_NAME, "VERSION"), encoding="utf-8") as f:
    version = f.read()

setup(
    # matadata
    name=PACKAGE_NAME,
    version=version,
    description="utilities for windows.",
    long_description=readme,
    author="Yutaka Kato",
    author_email="kato.yutaka@gmail.com",
    url="https://github.com/yukkun007/wintools",
    # liscence=
    # platform=
    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=["pyperclip", "boto3"],
    entry_points="""
        [console_scripts]
        {app} = {app}.cli:main
    """.format(
        app=PACKAGE_NAME
    ),
)
