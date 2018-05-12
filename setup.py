from setuptools import setup, find_packages

setup(
    name="assert_types",
    version="0.1.4",
    description="Python decorator to add assertions for type hints",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    python_requires='>=3.5',
    install_requires=['numpy'],

    # metadata for upload to PyPI
    author="Matthew Sochor",
    author_email="matthew.sochor@gmail.com",
    license="MIT",
    keywords="decorators type hint assertion unit testing",
    url="http://github.com/matthew-sochor/assert_types",   # project home page, if any
    download_url="http://github.com/matthew-sochor/assert_types",   # project home page, if any
)
