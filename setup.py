from distutils.core import setup
from distutils.command.install_data import install_data

setup(
    name="iiwaPy",
    version="0.1",
    description="Python library to control a IIWA LBR robot",
    packages=["iiwaPy"],
    provides=["iiwaPy"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Software Development :: Libraries :: Python Modules",
])
