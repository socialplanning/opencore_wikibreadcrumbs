from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='opencore_wikibreadcrumbs',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[

      ],
      entry_points="""
      [opencore.versions]
      wikibcrumbs = opencore_wikibreadcrumbs
      [topp.zcmlloader]
      opencore = opencore_wikibreadcrumbs
      """,
      )
