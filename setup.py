import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),
                                       os.pardir)))

requirements = [
    'django>=2.0.7',
    'channels>=2.1.2',
    'gevent>=1.3.4',
]

extras_require = {
    'test': [],
}

setup(
    name='django-eel',
    version='0.1',
    packages=find_packages(),
    package_data={
        'django_eel': ['static/eel/js/eel.js'],
    },
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    license='MIT License',
    description='A Django App for little HTML GUI applications, with easy Python/JS interoperation.',
    long_description=open('README.md', encoding='utf-8').readlines()[1],
    url='https://github.com/seLain/django-eel',
    author='Victor Hu',
    author_email='selain@nature.ee.ncku.edu.tw',
    zip_safe=False, # not being egg
)