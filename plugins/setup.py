from setuptools import setup, find_packages

setup(
    name="custom-mkdocs-plugins",
    version="0.0.1",
    install_requires=[
        "mkdocs-material",
        "pillow",
    ],
    packages=find_packages(where="mkdocs_custom"),
    entry_points={
        "mkdocs.plugins": [
            "custom-cards = mkdocs_custom.social:CustomSocialPlugin",
        ]
    },
)
