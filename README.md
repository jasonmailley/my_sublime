MySublime
=========

This is my Sublime Text 2 configuration based on post of [@kennethreitz][kenneth] ,and my
goal is try to optimize the python experience and better support
to [web2py][web2py].

It's a compilation of better plugins thats include:

    - git support(commands and diff view)
    - pep8 autoformat
    - html helper(awesome!)
    - markdown preview
    - inline notation for syntax errors in many languages
    - nice snippets...very nice
    - json auto-formatter

Instalation
-----------

##### 1 - Run the script:

    `python setup.py` or `python setup.py --<commands> ... `

Commands:

     --no_sublime - ignore the installation of Sublime Text 2

     --no_enviroment - ignore the installation of enviroment packages(not recommended because maybe necessary for plugins)

     --no_extras - ignore the instalattion of extra packages

     --no_user_settings - ignore personal configurations

##### 2 - Reset the opened Sublime Text.

    Just close and open.

##### 3 - Wait appear a V8 successful message in the status bar.

    Wait the installation of the plguins.(This can take some minutes)

##### 4(extra) - Theme Soda

* Open your User Settings Preferences file Sublime Text 2 ->
Preferences -> Settings - User

* Add (or update) your theme entry to be "theme": "Soda Light.sublime-theme" or "theme": "Soda Dark.sublime-theme"

* Reset Sublime Text 2


Requirements
--------------
- Python 2.7
- Ubuntu (only support yet)


TODO:

    [] integration with other OS(include other distros).

    [] many snippets for web2py

    [] Test script in earlier versions of python

    [] Better setup interface with docopt

    [] Screenshots

[web2py]: http://www.web2py.com
[kenneth]: http://github.com/kennethreitz