from setuptools import setup

setup(
    name="pytest-marker-bugzilla",
    version="0.01",
    description='py.test bugzilla integration plugin, using markers',
    author='Eric Sammons',
    author_email='elsammons@gmail.com' ,
    url='https://github.com/eanxgeek/pytest_marker_bugzilla',
    py_modules=['pytest_marker_bugzilla',],
    license='GPL',
    keywords='py.test pytest bugzilla',
    entry_points={'pytest11': ['pytest_marker_bugzilla = pytest_marker_bugzilla.pytest_marker_bugzilla']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'])
