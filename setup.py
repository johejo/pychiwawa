from setuptools import setup, find_packages


def read(fname):
    with open(fname, 'rt', encoding='utf8') as f:
        return f.read()


setup(
    name='pychiwawa',
    version='0.1.0',
    author='Mitsuo Heijo',
    author_email='mitsuo_h@outlook.com',
    description='Chiwawa Python SDK',
    long_description=read('README.md'),
    packages=find_packages(),
    license='MIT',
    url='https://github.com/johejo/pychiwawa',
    py_modules=['pychiwawa'],
    keywords=['Chiwawa'],
    python_requires='>=3.5.3',
    install_requires=read('requirements.txt').split('\n'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)