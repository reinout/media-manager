from setuptools import setup

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Jinja2',
    'readline',
    'setuptools',
    ],

tests_require = [
    'nose',
    'coverage',
    ]

setup(name='media-manager',
      version=version,
      description="Sync/add library for my photos and videos",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='Reinout van Rees',
      author_email='reinout@vanrees.org',
      url='',
      license='GPL',
      packages=['media_manager'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
            'add_video = media_manager.runner:add_video',
            'generate_website = media_manager.runner:generate_website',
            'videos_that_can_be_removed = media_manager.runner:videos_that_can_be_removed',
          ]},
      )
