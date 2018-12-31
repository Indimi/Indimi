from setuptools import setup, find_packages

setup(
    install_requires=[
        "Flask==1.0.2",
        "Flask-SQLAlchemy==2.3.2",
        "Flask-Migrate==2.3.1",
        "pytest==4.0.2",
        "mysql-connector-python==8.0.13",
    ]
)