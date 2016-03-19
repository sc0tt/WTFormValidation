from setuptools import setup


setup(
    name='WTFormValidation',
    version='1.0.0',
    url='https://github.com/sc0tt/WTFormValidation',
    description='The missing link between WTForms and http://formvalidation.io',
    license='MIT',
    author='Scott Adie',
    author_email='scott.w@adie.io',
    packages=["wtformvalidation"],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'WTForms',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
