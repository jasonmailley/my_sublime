import os

commands = [
    'sudo -v',
    'sudo apt-get install ipython ipython3 python-tk python3-tk '
    'python-pip git git-core',
    'sudo pip install docutils pygments pep8 pyflakes virtualenv '
    'virtualenvwrapper',
    'wget http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.1%'
    '20x64.tar.bz2',
    'tar -jxvf Sublime\ Text\ *',
    'rm Sublime\ Text\ *.tar.bz2',
    'sudo mv  Sublime\ Text\ 2 /opt/sublime/',
    'sudo ln -s /opt/sublime/sublime_text /usr/bin/subl',
    'echo export EDITOR="subl" >> ~/.bashrc',
    "echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc",
]

repositories = [
    'git clone https://github.com/buymeasoda/soda-theme/ "Theme - Soda" ',
    "git clone https://github.com/kemayo/sublime-text-2-git.git",
    "git clone https://github.com/sergeche/emmet-sublime.git",
    "git clone https://github.com/jisaacks/GitGutter.git",
    "git clone https://github.com/Kronuz/SublimeCodeIntel.git",
    "git clone https://github.com/SublimeLinter/SublimeLinter.git",
    "git clone https://github.com/revolunet/sublimetext-markdown-preview.git "
    "Markdown\ Preview",
    "git clone https://github.com/dzhibas/SublimePrettyJson.git",
    "git clone https://github.com/martinsam/sublime-unittest.git",
    "git clone https://github.com/wistful/SublimeAutoPEP8.git AutoPEP8",
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
    name = raw_input('Digite o nome de usuario do sistema ')
    dir_path = os.getcwdu()
    if os.name == 'posix':
        for command in commands:
            run(command)
        os.chdir('/home' + name + '/.config/sublime-text-2/Packages')
        for repository in repositories:
            run(repository)
        os.chdir(dir_path)
        run('subl &')
        run('cp Preferences.sublime-settings ~/.config/sublime-text-2/'
            '/Packages/Default/')
        run('cp SublimeLinter.sublime-settings ~/.config/sublime-text-2/'
            'Packages/User/')
    else:
        print "Change your life.Use Linux!"
        return -1
    return 0

if __name__ == '__main__':
    install()
