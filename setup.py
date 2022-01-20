import setuptools

setuptools.setup(
    name="norteamericano_form",
    version="0.0.1",
    author="Luis Santana",
    author_email="luis.santana@uchile.cl",
    description="Norteamericano Custom Form",
    url="https://norteamericano.virtual-labx.cl/",
    packages=setuptools.find_packages(),
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
)
