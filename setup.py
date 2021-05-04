from distutils.core import setup

setup(
  name = 'lambdata-jason-young',         # How you named your package folder (MyLib)
  packages = ['lambdata-jason-young'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Helper functions for a project',   # Give a short description about your library
  author = 'Jason Young',                   # Type in your name
  author_email = 'yaobviously@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/yaobviously/lambdata-jason-young/tree/main',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/yaobviously/lambdata-jason-young/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['Lambda', 'Project', 'Stretch'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: Pre-Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Instructors',      # Define that your audience are developers
    'Topic :: Software Development :: Learning How',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support
    
  ],
)