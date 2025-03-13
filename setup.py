from setuptools import setup, find_packages  # noqa: H301

NAME = "testit-api-client"

VERSION = "5.3.0"

PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]
setup(
    name=NAME,
    version=VERSION,
    description='API-client for Test IT',
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    author='Integration team',
    author_email='integrations@testit.software',
    url='https://pypi.org/project/testit-api-client/',
    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRES,
    py_modules=['testit_api_client'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True
)
