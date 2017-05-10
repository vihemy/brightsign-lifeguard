from setuptools import setup

setup(name='brightsign-lifeguard',
      version='0.1',
      description='tools for working with Brightsign show pools (shard/unshard)',
      url='http://github.com/riordan/brightsign-lifeguard',
      author='David Riordan',
      author_email='dr@daveriordan.com',
      license='Apache-2.0',
      packages=['brightsignlifeguard'],
      install_requires=["copyfile==0.1.1"],
      scripts=['bin/lifeguardIn', 'bin/lifeguardOut'],
      zip_safe=False)
