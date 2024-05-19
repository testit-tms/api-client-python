from setuptools import setup, find_packages  # noqa: H301

NAME = "testit-api-client"

VERSION = "4.0.0"

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
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
    python_requires=">=3.6",
    install_requires=REQUIRES,
    py_modules=['testit_api_client'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True
)
