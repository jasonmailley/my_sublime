import os
import sys
import json

USER = os.getlogin()


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
    'wget http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.1%20x64.tar'
    '.bz2',
    'tar -jxvf Sublime\ Text\ *',
    'rm Sublime\ Text\ *.tar.bz2',
    'sudo mv  Sublime\ Text\ 2 /opt/sublime/',
    'sudo ln -s /opt/sublime/sublime_text /usr/bin/subl',
    'echo export EDITOR="subl" >> ~/.bashrc',
]


class InvalidCommand(Exception):
    pass


def run(command):
    sys_return = os.system(command)
    if sys_return == 0:
        return 0
    else:
        raise InvalidCommand("Failure on command: %s" % command)


def install():

    if os.name == 'posix':
        if not ('--no_sublime' in sys.argv):
            install_sublime(sublime_commands)

        if not('--no_enviroment' in sys.argv):
            install_distribution_packages(json.load(open('requirements.json')))
            install_pipy_packages(json.load(open('packs.json')))
            os.system(
                "echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc")

            if '--extras' in sys.argv:
                install_distribution_packages(json.load(open('extras.json')))
                install_pipy_packages(json.load(open('extra_packs.json')))

        run('subl &')
        if not('--no_user_settings' in sys.argv):
            run('cp Preferences.sublime-settings ~/.config/sublime-text-2/'
                '/Packages/Default/')
        run('cp SublimeLinter.sublime-settings ~/.config/sublime-text-2/'
            'Packages/User/')
        run('cp Package Control.sublime-package ~/.config/sublime-text-2'
            '/Installed Packages/')
        run('cp Package Control.sublime-settings ~/.config/sublime-text-2/'
            'Packages/User/')
    else:
        print "Change your life.Use Linux!"
        return -1
    return 0

if __name__ == '__main__':
    install()
