#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """

███╗   ███╗███████╗███████╗ ██████╗
████╗ ████║██╔════╝██╔════╝██╔════╝
██╔████╔██║█████╗  ███████╗██║
██║╚██╔╝██║██╔══╝  ╚════██║██║
██║ ╚═╝ ██║███████╗███████║╚██████╗
╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝

MESC: Minimun Essential Security Checks

Author: https://twitter.com/1_mod_m/

Project site: https://github.com/1modm/mesc

Copyright (c) 2014, Miguel Morillo.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

#------------------------------------------------------------------------------
# Modules
#------------------------------------------------------------------------------

import os
import StringIO
from . import config
from .operations import execute_cmd, check_file, exists_file, exists_read_file,\
                        check_file_exact, OS_dist


__all__ = [
    "checkShells",
    "LoadSSH",
    "checkSSH2",
    "checkDisabledCtrlAltDel",
    "checkCrontab",
    "LoadApache",
    "checkPassAging",
    "checkPassLength",
    "autologout",
    "MagicSysRq",
    "NumberTTYs"
]


def checkShells(__host__, __user__, __passwd__, __port__):
    """
    :returns: Valid shells status
    :param host: Target.
    """
    __help_result__ = 'Check shells status'
    __help_result__ += os.linesep
    __command__ = "Valid login shells"
    __file__ = "/etc/shells"
    __cmdfile__ = "cat /etc/shells"
    check_count = 0
    badshell = os.linesep
    badshellhtml = '<br>'
    __command_check__ = config.CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__,
         __passwd__, __port__)

    s = StringIO.StringIO(__output__)

    if __command_check__ == config.CHECKRESULTOK:
        for line in s:
            if not (line.startswith("#")):
                if not (exists_file(line.strip(), __host__, __user__,
                 __passwd__, __port__)):
                    check_count += 1
                    badshell += line
                    badshellhtml += line + '<br>'

    if check_count > 0:
        __command_check__ = config.CHECKRESULTWARNING

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'All shells accounts are being used'
        __check_html_message__ = 'All shells accounts are being used'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' +\
         __cmdfile__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __cmdfile__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'These shells '
        __check_message__ += badshell + os.linesep
        __check_message__ += 'does not exist in the system but is allowed their'
        __check_message__ += ' use, are included in /etc/shells !!!'
        __check_html_message__ = 'These shells <br>'
        __check_html_message__ += badshellhtml
        __check_html_message__ += '<br>does not exist in the system but is'
        __check_html_message__ += ' allowed their use, are included in'
        __check_html_message__ += ' /etc/shells !!!'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
            __check_html_message__, __command__, __file__)

#------------------------------------------------------------------------------


def LoadSSH(__host__, __user__, __passwd__, __port__):
    """
    :returns: Load SSH config file
    :param host: Target.
    """
    __help_result__ = 'OpenSSH SSH daemon configuration file'
    __help_result__ += os.linesep
    __command__ = "Load SSH config file"
    __file__ = "/etc/ssh/sshd_config"
    __command_check__ = config.CHECKRESULTERROR
    __check_message__ = os.linesep
    __check_html_message__ = '<br>'
    __output__ = ""

    __cmd_check__, __out__ = exists_read_file(__file__, __host__, __user__,
         __passwd__, __port__)
    if (__cmd_check__):
        __command_check__ = config.CHECKRESULTOK
        __output__ = __out__
        __cmd__ = __file__

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'SSH configuration loaded'
        __check_html_message__ = 'SSH configuration loaded'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration'
        __check_html_message__ = 'Unable to load configuration'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)


#------------------------------------------------------------------------------

def checkSSH(__host__, __user__, __passwd__, __port__):
    """
    :returns: Check ssh service
    :param host: Target.
    """
    __help_result__ = 'Check PermitRootLogin'
    __help_result__ += os.linesep
    __command__ = "Check PermitRootLogin in ssh service"
    __file__ = "/etc/ssh/sshd_config"
    __check__ = ['#PermitRootLogin yes', 'PermitRootLogin no',
                 'PermitRootLogin without-password']
    __output__ = ""

    __cmd_check__ = exists_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__ +\
         ' contains any of the following chains:' + __line__
        __check_html_message__ = 'The next file ' + __file__ +\
         ' contains any of the following chains:' + __line__
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'ssh service has an insecure configuration: ' + \
        'should have: ' + __check__[0] + ' or ' + __check__[1] + ' or ' + \
         __check__[2] + os.linesep
        __check_html_message__ = 'ssh service has an insecure configuration '\
         + 'should have: ' + __check__[0] + ' or ' + __check__[1] \
         + ' or ' + __check__[2] + '<br>'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)


#------------------------------------------------------------------------------


def checkSSH2(__host__, __user__, __passwd__, __port__):
    """
    :returns: Check ssh service
    :param host: Target.
    """
    __help_result__ = 'Check PermitEmptyPasswords'
    __help_result__ += os.linesep
    __command__ = "Check PermitEmptyPasswords in ssh service"
    __file__ = "/etc/ssh/sshd_config"
    __check__ = ['#PermitEmptyPasswords yes', 'PermitEmptyPasswords no']
    __output__ = ""

    __cmd_check__ = exists_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__ +\
         ' contains any of the following chains:' + __line__
        __check_html_message__ = 'The next file ' + __file__ +\
         ' contains any of the following chains:' + __line__
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'ssh service has an insecure configuration ' \
         + 'should have: ' + __check__[0] + ' or ' + __check__[1] + os.linesep
        __check_html_message__ = 'ssh service has an insecure configuration '\
         + 'should have: ' + __check__[0] + ' or ' + __check__[1] \
         + '<br>'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)

#------------------------------------------------------------------------------


def checkDisabledCtrlAltDel(__host__, __user__, __passwd__, __port__):
    """
    :returns: ctrl+alt+del reboot check.
    :param host: Target.
    """
    __help_result__ = 'Restrict the privilege to allow certain non-root users the right to shutdown or reboot the system from the console'
    __help_result__ += os.linesep
    __command__ = "ctrl+alt+del reboot check"
    # Check that exists one of this:
    # #ca::ctrlaltdel:/sbin/shutdown -t3 -r now
    # #ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now

    __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)

    if (__distribution__ == "RedHat"):
        __file__ = "/etc/inittab"
        __check__ = ['#ca::ctrlaltdel:', '#ca:12345:ctrlaltdel:']
    elif (__distribution__ == "SuSE"):
        __file__ = "/etc/inittab"
        __check__ = ['#ca::ctrlaltdel:', '#ca:12345:ctrlaltdel:']
    elif (__distribution__ == "debian"):
        __file__ = "/etc/init/control-alt-delete.conf"
        __check__ = ['#exec shutdown -r now']
    elif (__distribution__ == "mandrake"):
        __file__ = "/etc/inittab"
        __check__ = ['#ca::ctrlaltdel:', '#ca:12345:ctrlaltdel:']
    else:
        __file__ = "/etc/inittab"
        __check__ = ['#ca::ctrlaltdel:', '#ca:12345:ctrlaltdel:']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__ +\
         ' contains the chain that comment ctrl+alt+del. It is not allowed reboot the system with ctrl+alt+del' + __line__
        __check_html_message__ = 'The next file ' + __file__ +\
         ' contains the chain that comment ctrl+alt+del. It is not allowed reboot the system with ctrl+alt+del' + __linehtml__
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'It is allowed to reboot the system with ctrl+alt+del!' + os.linesep
        __check_html_message__ = 'It is allowed to reboot the system with ctrl+alt+del!' + '<br>'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)


#------------------------------------------------------------------------------


def checkCrontab(__host__, __user__, __passwd__, __port__):
    """
    :returns: Users allowed to use the crontab
    :param host: Target.
    """
    __help_result__ = 'Controlling access to Cron'
    __help_result__ += os.linesep
    __command__ = "Users allowed to use the crontab"
    __file__ = "/etc/cron.allow"
    # Check that exists at least the root user:
    __check__ = ['root']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTWARNING
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file exists and contains the root user: '\
         + __file__ +\
          ', so the crontab it is only allowed their use for root user'
        __check_html_message__ =\
         'The next file exists and contains the root user: ' + __file__ +\
          ', so the crontab it is only allowed their use for root user'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' +\
         __file__ + ' - It is allowed the crontab use for all users  !!!!'
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__ + ' - It is allowed the crontab use for all users  !!!!'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The next file ' + __file__ +\
         ' does not contain: ' + __check__[0] + os.linesep +\
          ' - It is allowed the crontab use for all users  !!!!'
        __check_html_message__ = 'The next file ' + __file__ +\
         ' does not contain: ' + __check__[0] + '<br>' +\
          'It is allowed the crontab use for all users  !!!!'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)


#------------------------------------------------------------------------------


def LoadApache(__host__, __user__, __passwd__, __port__):
    """
    :returns: Load Apache configuration.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Load Apache configuration"
    __cmd__ = "Apache conf"
    apache1 = "/etc/httpd/conf/httpd.conf"
    apache2 = "/etc/apache2/apache2.conf"
    apache3 = "/etc/apache/apache.conf"
    __command_check__ = config.CHECKRESULTERROR
    __check_message__ = os.linesep
    __check_html_message__ = '<br>'
    __output__ = ""

    __cmd_check__, __out__ = exists_read_file(apache1, __host__, __user__,
         __passwd__, __port__)
    if (__cmd_check__):
        __command_check__ = config.CHECKRESULTOK
        __output__ = __out__
        __cmd__ = apache1

    __cmd_check__, __out__ = exists_read_file(apache2, __host__, __user__,
         __passwd__, __port__)
    if (__cmd_check__):
        __command_check__ = config.CHECKRESULTOK
        __output__ = __out__
        __cmd__ = apache2

    __cmd_check__, __out__ = exists_read_file(apache3, __host__, __user__,
         __passwd__, __port__)
    if (__cmd_check__):
        __command_check__ = config.CHECKRESULTOK
        __output__ = __out__
        __cmd__ = apache3

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'Apache configuration loaded'
        __check_html_message__ = 'Apache configuration loaded'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration, Apache web server is not installed'
        __check_html_message__ = 'Unable to load configuration, Apache web server is not installed'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def checkPassAging(__host__, __user__, __passwd__, __port__):
    """
    :returns: Password aging controls check.
    :param host: Target.
    """
    __help_result__ = 'defines the site-specific configuration for '
    __help_result__ += 'the shadow password suite'
    __help_result__ += os.linesep
    __command__ = "Password aging controls check"
    __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)

    if (__distribution__ == "RedHat"):
        __file__ = "/etc/login.defs"
        __check__ = ['PASS_MAX_DAYS	99999', 'PASS_MIN_DAYS	0',
                     'PASS_WARN_AGE	7']
    elif (__distribution__ == "SuSE"):
        __file__ = "/etc/login.defs"
        __check__ = ['PASS_MAX_DAYS	99999', 'PASS_MIN_DAYS	0',
                     'PASS_WARN_AGE	7']
    elif (__distribution__ == "debian"):
        __file__ = "/etc/login.defs"
        __check__ = ['PASS_MAX_DAYS	99999', 'PASS_MIN_DAYS	0',
                     'PASS_WARN_AGE	7']
    elif (__distribution__ == "mandrake"):
        __file__ = "/etc/login.defs"
        __check__ = ['PASS_MAX_DAYS	99999', 'PASS_MIN_DAYS	0',
                     'PASS_WARN_AGE	7']
    else:
        __file__ = "/etc/login.defs"
        __check__ = ['PASS_MAX_DAYS	99999', 'PASS_MIN_DAYS	0',
                     'PASS_WARN_AGE	7']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __check_count__ > 1:
        __command_check__ = config.CHECKRESULTWARNING

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__
        __check_message__ += ' contains password aging controls: '
        __check_message__ += __line__ + os.linesep
        __check_message__ += 'Review the values'
        __check_html_message__ = 'The next file ' + __file__
        __check_html_message__ += ' contains password aging controls: '
        __check_html_message__ += __linehtml__ + '<br>'
        __check_html_message__ += 'Review the values'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The next file ' + __file__
        __check_message__ += ' contains default password aging controls: '
        __check_message__ += __line__ + os.linesep
        __check_message__ += 'Modify default values to more restrictive values'
        __check_html_message__ = 'The next file ' + __file__
        __check_html_message__ += ' contains default password aging controls: '
        __check_html_message__ += __linehtml__ + '<br>'
        __check_html_message__ += 'Modify default values to more restrictive values'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)

#------------------------------------------------------------------------------


def checkPassLength(__host__, __user__, __passwd__, __port__):
    """
    :returns: Minimum password length check.
    :param host: Target.
    """
    __help_result__ = 'In order to improve the security of standard reusable'
    __help_result__ += ' passwords, \"best practices\" tell us to require users'
    __help_result__ += ' to change their passwords on a regular basis, enforce'
    __help_result__ += ' minimum lengths and good \"rules\" for new passwords'
    __help_result__ += ' (such as requiring mixed case and non-alphanumeric'
    __help_result__ += ' characters), and even keep a \"history\" of previous'
    __help_result__ += ' user passwords so that users don\'t \"repeat\"'
    __help_result__ += ' \"minlen\" is actually the minimum required length for'
    __help_result__ += ' a password consisting of all lower-case letters.'
    __help_result__ += ' The four parameters \"lcredit\", \"ucredit\",'
    __help_result__ += ' \"dcredit\", and \"ocredit\" are used to set the'
    __help_result__ += ' maximum credit for lower-case, upper-case, numeric'
    __help_result__ += ' (digit), and non-alphanumeric (other) characters,'
    __help_result__ += ' respectively.'
    __help_result__ += os.linesep
    __command__ = "Minimum password length check"
    __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)

    if (__distribution__ == "RedHat"):
        __file__ = "/etc/pam.d/system-auth"
        __check__ = ['retry=', 'minlen=', 'difok=', 'lcredit=', 'ucredit=',
                     'dcredit=', 'ocredit=']
    elif (__distribution__ == "SuSE"):
        __file__ = "/etc/pam.d/system-auth"
        __check__ = ['retry=', 'minlen=', 'difok=', 'lcredit=', 'ucredit=',
                     'dcredit=', 'ocredit=']
    elif (__distribution__ == "debian"):
        __file__ = "/etc/pam.d/common-password"
        __check__ = ['retry=', 'minlen=', 'difok=', 'lcredit=', 'ucredit=',
                     'dcredit=', 'ocredit=']
    elif (__distribution__ == "mandrake"):
        __file__ = "/etc/pam.d/system-auth"
        __check__ = ['retry=', 'minlen=', 'difok=', 'lcredit=', 'ucredit=',
                     'dcredit=', 'ocredit=']
    else:
        __file__ = "/etc/pam.d/common-password"
        __check__ = ['retry=', 'minlen=', 'difok=', 'lcredit=', 'ucredit=',
                     'dcredit=', 'ocredit=']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file(__file__, __check__, __host__, __user__, __passwd__,
                         __port__)

    if __check_count__ < 7:
        __command_check__ = config.CHECKRESULTWARNING

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__
        __check_message__ += ' contains minimum password length controls: '
        __check_message__ += __line__ + os.linesep
        __check_message__ += 'Review the values'
        __check_html_message__ = 'The next file ' + __file__
        __check_html_message__ += ' contains minimum password length controls: '
        __check_html_message__ += __linehtml__ + '<br>'
        __check_html_message__ += 'Review the values'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The next file ' + __file__
        __check_message__ += ' doesn\'t contains minimum password length and'
        __check_message__ += ' password best practices'
        __check_message__ += ' controls like ' + __check__[1] + os.linesep
        __check_message__ += 'Set values to restrict password length and use'
        __check_html_message__ = 'The next file ' + __file__
        __check_html_message__ += ' doesn\'t contains minimum password length'
        __check_html_message__ += ' password best practices'
        __check_html_message__ += ' controls like ' + __check__[1] + '<br>'
        __check_html_message__ += 'Set values to restrict password length and use'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)

#------------------------------------------------------------------------------


def autologout(__host__, __user__, __passwd__, __port__):
    """
    :returns: Logout shell user after certain minutes of inactivity.
    :param host: Target.
    """
    __help_result__ = 'UNIX or Linux login shells can be configured to'
    __help_result__ += ' automatically log users out after a period of'
    __help_result__ += ' inactivity. The TMOUT (under bash ) and autologout'
    __help_result__ += ' (under tcsh) variables defines auto logout'
    __help_result__ += ' time in seconds.'
    __help_result__ += os.linesep
    __command__ = "Console auto Logout"
    __file__ = "/etc/profile"
    __check__ = ['TMOUT']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file(__file__, __check__, __host__, __user__, __passwd__,
                   __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The file ' + __file__
        __check_message__ += ' contains the TMOUT variable: '
        __check_message__ += __line__ + os.linesep
        __check_message__ += 'Review the values'
        __check_html_message__ = 'The file ' + __file__
        __check_html_message__ += ' contains the TMOUT variable: '
        __check_html_message__ += __linehtml__ + '<br>'
        __check_html_message__ += 'Review the values'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The file ' + __file__
        __check_message__ += ' doesn\'t contains the TMOUT variable'
        __check_message__ += __check__[0] + os.linesep
        __check_message__ += 'Set value to define a variable to auto logout'
        __check_html_message__ = 'The file ' + __file__
        __check_html_message__ += ' doesn\'t contains the TMOUT variable'
        __check_html_message__ += __check__[0] + '<br>'
        __check_html_message__ += 'Set value to define a variable to auto logout'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)


#------------------------------------------------------------------------------


def MagicSysRq(__host__, __user__, __passwd__, __port__):
    """
    :returns: The magic SysRq key.
    :param host: Target.
    """
    __help_result__ = 'The magic SysRq key is a key combination understood'
    __help_result__ += ' by the Linux kernel, which allows the user to'
    __help_result__ += ' perform various low-level commands regardless'
    __help_result__ += ' of the system\'s state. It is often used to recover'
    __help_result__ += ' from freezes, or to reboot a computer'
    __help_result__ += ' without corrupting the filesystem.'
    __help_result__ += os.linesep
    __command__ = "The magic SysRq key"
    __file__ = "/etc/sysctl.conf"
    __check__ = ['kernel.sysrq=1']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                   __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The file ' + __file__
        __check_message__ += ' contains the kernel.sysrq variable: '
        __check_message__ += __line__ + os.linesep
        __check_message__ += 'Review the values'
        __check_html_message__ = 'The file ' + __file__
        __check_html_message__ += ' contains the kernel.sysrq variable: '
        __check_html_message__ += __linehtml__ + '<br>'
        __check_html_message__ += 'Review the values'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The file ' + __file__
        __check_message__ += ' doesn\'t contains the kernel.sysrq variable'
        __check_message__ += __check__[0] + os.linesep
        __check_message__ += 'Set value to active the magic SysRq key'
        __check_html_message__ = 'The file ' + __file__
        __check_html_message__ += ' doesn\'t contains the kernel.sysrq variable'
        __check_html_message__ += __check__[0] + '<br>'
        __check_html_message__ += 'Set value to active the magic SysRq key'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)


#------------------------------------------------------------------------------


def NumberTTYs(__host__, __user__, __passwd__, __port__):
    """
    :returns: Check the number of TTYs.
    :param host: Target.
    """
    __help_result__ = 'In the [Login] section: NAutoVTs, takes a positive'
    __help_result__ += ' integer. Configures how many virtual terminals'
    __help_result__ += ' (VTs) to allocate.'
    __help_result__ += os.linesep
    __command__ = "Number of TTYs"
    __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)

    if (__distribution__ == "RedHat"):
        __file__ = "/etc/systemd/logind.conf"
        __check__ = ['#NAutoVTs=6']
    elif (__distribution__ == "SuSE"):
        __file__ = "/etc/systemd/logind.conf"
        __check__ = ['#NAutoVTs=6']
    elif (__distribution__ == "debian"):
        __file__ = "/etc/default/console-setup"
        __check__ = ['ACTIVE_CONSOLES=\"/dev/tty[1-6]\"']
    elif (__distribution__ == "mandrake"):
        __file__ = "/etc/systemd/logind.conf"
        __check__ = ['#NAutoVTs=6']
    else:
        __file__ = "/etc/default/console-setup"
        __check__ = ['ACTIVE_CONSOLES=\"/dev/tty[1-6]\"']

    __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__,
                                                 __passwd__, __port__)

    if not __cmd_check__:
        __command_check__ = config.CHECKRESULTERROR
    else:
        __command_check__, __line__, __linehtml__, __check_count__ =\
        check_file_exact(__file__, __check__, __host__, __user__, __passwd__,
                   __port__)

    if __check_count__ > 1:
        __command_check__ = config.CHECKRESULTWARNING

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The file ' + __file__
        __check_message__ += ' contains a variable to reduce the number of TTYs'
        __check_message__ += __line__ + os.linesep
        __check_message__ += 'Review the values'
        __check_html_message__ = 'The file ' + __file__
        __check_html_message__ += ' contains a variable to reduce the number of TTYs'
        __check_html_message__ += __linehtml__ + '<br>'
        __check_html_message__ += 'Review the values'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' +\
         __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The file ' + __file__
        __check_message__ += ' doesn\'t contains a variable to reduce the number of TTYs'
        __check_message__ += __check__[0] + os.linesep
        __check_message__ += 'Set value to reduce the number of TTYs'
        __check_html_message__ = 'The file ' + __file__
        __check_html_message__ += ' doesn\'t contains a variable to reduce the number of TTYs'
        __check_html_message__ += __check__[0] + '<br>'
        __check_html_message__ += 'Set value to reduce the number of TTYs'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __file__)

