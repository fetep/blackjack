import setuptools

setuptools.setup(name='blackjack',
                 packages=['blackjack', 'cards'],
                 install_requires=[],
                 extras_require={
                     'dev': [
                         'pycodestyle',
                         'pytest',
                         'pytest-cov',
                        ]
                 })
