from setuptools import setup


def get_version(v):
    if v.count('.') > 2:
        v = ".Post".join(v.rsplit('.', 1))
    print("setup version = %s" % v)
    return v


setup(
    name='uda',
    version=get_version('@PROJECT_VERSION@'),
    description='Unified Data Access (UDA)',
    long_description='Unified Data Access (UDA)',
    author='Jonathan Hollocombe',
    author_email='jonathan.hollocombe@ukaea.uk',
    packages=['uda'],
)

