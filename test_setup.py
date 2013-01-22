#coding: utf-8
import unittest
import os
from setup import (InvalidCommand, run, install)


def mock_link(link):
    correct = "wget http://c758482.r82.cf2.rackcdn.com/Sublime%20Text"\
              "%202.0.1%20x64.tar.bz2"
    if link == correct:
        return "echo 'link correto'"
    return "invalid link"


class SetupTestCase(unittest.TestCase):
    '''Test class for setup'''
    def test_system_command_invalid(self):
        self.assertRaises(InvalidCommand, run, 'invalid comand')

    def test_system_valid_command(self):
        self.assertEquals(run('echo "teste"'), 0)

    def test_for_a_valid_system_call(self):
        self.assertEquals(run('ls -a'), 0)

    def test_for_a_invalid_system_call(self):
        self.assertRaises(InvalidCommand, run, 'git add ')

    def test_for_retrieve_error_code(self):
        try:
            run('git add')
        except InvalidCommand, e:
            self.assertEquals(e.message, "Failure on command: git add")


class InstallTestCase(unittest.TestCase):
    '''Test class for client install'''
    def test_sudo(self):
        self.assertEquals(run('sudo -v'), 0)

    def test_wget_ok(self):
        self.assertEquals(run(mock_link("wget http://c758482.r82.cf2.rackcdn."
                              "com/Sublime%20Text%202.0.1%20x64.tar.bz2")), 0)

    def test_wget_failure(self):
        url = "wget http://c58482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.1"
        "%20x64.tar.bz2"
        self.assertRaises(InvalidCommand, run, mock_link(url))

    def test_extract_failure(self):
        self.assertRaises(InvalidCommand, run, 'tar -jxvf Sublime\ Text\ *')

    def test_remove_failure(self):
        self.assertRaises(InvalidCommand, run, 'rm Sublime\ Text\ *.tar.bz2')

    def test_move_failure(self):
        self.assertRaises(InvalidCommand, run, 'mv  Sublime\ Text\ 2 "\
                          "/ opt / sublime /')

    def test_simbolic_link(self):
        ln = 'ln -s /opt/sublime/sublime_text /usr/bin/subl'
        self.assertRaises(InvalidCommand, run, ln)

    def test_wrong_sustem(self):
        os.name = 'windows'
        self.assertEquals(install(), -1)


if __name__ == '__main__':
    unittest.main()
