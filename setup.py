from setuptools import setup


setup(
    name='slack-webhooks',
    version='0.0.1',
    packages=['webhooks'],
    description='Slack Webhooks API client',
    author='Chris Gilmer',
    author_email='chris.gilmer@gmail.com',
    url='http://github.com/chrisgilmerproj/slack-webhooks/',
    install_requires=['requests >= 2.12.1'],
    license='http://www.apache.org/licenses/LICENSE-2.0',
    test_suite='tests',
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
    keywords='slack api'
)
