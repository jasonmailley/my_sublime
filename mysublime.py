#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
My_Sublime

A Helper to install Sublime Text 2 with some extras configurations.
This is my Sublime Text 2 configuration based on post of @kennethreitz, and my
goal is try to optimize the python experience and better support
to web2py and other frameworks.


Usage:
    mysublime.py [options] ...
    mysublime --version [--args]
    mysublime -h | --help [--args]


Options:
    -h --help  Show this screen.
    --version  Show version.
    --no_sublime  Ignore the installation of Sublime Text 2
    --no_env  Ignore the installation of enviroment packages
    (not recommended because maybe necessary for plugins)
    --no_extras  Ignore the instalattion of extra packages
    --no_user_settings  Ignore personal configurations

"""

import os
import json
from time import sleep
from docopt import docopt

config = {
    'system': os.name,  # Operational system
    'arch': os.uname()[4],  # architeture
    'sublime_url': '',  # url for Sublime Installation
}

if config['arch'] == 'x86_64':
    config['sublime_url'] = "wget http://c758482.r82.cf2.rackcdn.com/Sublime"\
    "%20Text%202.0.1%20x64.tar.bz2"
else:
    config['sublime_url'] = "wget http://c758482.r82.cf2.rackcdn.com/Sublime"\
    "%20Text%202.0.1.tar.bz2"


def install_distribution_packages(requirements):
    for requirement in requirements.values()[0]:
        run("sudo apt-get install " + requirement)


def install_sublime(commands):
    for command in commands:
        run(command)


def install_pipy_packages(packs):
    for pack in packs.values()[0]:
        run("sudo pip install " + pack)


sublime_commands = [
    config['sublime_url'],
    'tar -jxvf Sublime\ Text\ *',
    'rm Sublime\ Text\ *.tar.bz2',
    'sudo mv  Sublime\ Text\ 2 /opt/sublime/',
    'sudo ln -s /opt/sublime/sublime_text /usr/bin/subl',
]


class InvalidCommand(Exception):
    pass


def run(command):
    sys_return = os.system(command)
    if sys_return == 0:
        return 0
    else:
        raise InvalidCommand("Failure on command: %s" % command)


def main(arguments):
    if config['system'] != 'posix':
        print('Change your life.Use linux!')
        return -1

    if not arguments['--no_sublime']:
        install_sublime(sublime_commands)

    if not arguments['--no_env']:
            install_distribution_packages(json.load(open('enviroment.json')))
            install_pipy_packages(json.load(open('packages.json')))
            os.system(
                "echo 'source /usr/local/bin/virtualenvwrapper.sh' "
                ">> ~/.bashrc")

    if not arguments['--no_extras']:
                install_distribution_packages(json.load(open('extra_envs.json')))
                install_pipy_packages(json.load(open('extra_packs.json')))

    run('subl &')
    sleep(3)

    if not arguments['--no_user_settings']:
        run('cp Preferences.sublime-settings ~/.config/sublime-text-2'
            '/Packages/User')
        run('cp SublimeLinter.sublime-settings ~/.config/sublime-text-2/'
            'Packages/User/')
        run('cp Package\ Control.sublime-package ~/.config/sublime-text-2'
            '/Installed\ Packages')
        run('cp Package\ Control.sublime-settings ~/.config/sublime-text-2/'
            'Packages/User')

    return 0

#Start
if __name__ == '__main__':
    arguments = docopt(__doc__, version='mysublime 0.3')
    main(arguments)
