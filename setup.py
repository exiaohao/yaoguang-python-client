from setuptools import setup, find_packages

setup(
    name = 'yaoguang-python-client',
    version = '0.0.1',
    author = 'onesuper',
    author_email = 'onesuperclark@gmail.com',
    url = 'https://github.com/baixing/yaoguang',
    description = 'baixing data service python client',
    long_description = __doc__,
    packages = find_packages(),
    include_package_data = True,
    license = 'MIT',
    install_requires = ['thrift'],
    platforms = 'any',
    zip_safe = False,
)
