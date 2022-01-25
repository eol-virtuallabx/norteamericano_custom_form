import os

from setuptools import setup

def package_data(pkg, roots):
    """Generic function to find package_data.
    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name="norteamericano_form",
    version="0.0.1",
    author="Luis Santana",
    author_email="luis.santana@uchile.cl",
    description="Norteamericano Custom Form",
    url="https://norteamericano.virtual-labx.cl/",
    packages=['norteamericano_form'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "lms.djangoapp": [
            "norteamericano_form = norteamericano_form.apps:NorteamericanoCustomFormConfig",
        ]
    },
    package_data=package_data("norteamericano_form", ["static", "public"]),
)
