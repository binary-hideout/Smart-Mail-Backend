from setuptools import find_packages, setup

setup(
    name="smartmail",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Flask",
        "Flask-JWT-Extended",
        "flask-marshmallow",
        "Flask-RESTful",
        "Flask-SQLAlchemy",
        "marshmallow-sqlalchemy",
        "psycopg2",
        "pytest",
    ],
)
