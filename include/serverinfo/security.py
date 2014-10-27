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
import commands
import platform
import StringIO
import config
from operations import execute_cmd, check_file, exists_file, exists_read_file


__all__ = [
    "checkShells",
    "checkSSH",
    "checkDisabledCtrlAltDel",
    "checkCrontab",
    "checkApache",
    "recomendations"
]


def checkShells(__host__, __user__, __passwd__, __port__):
    """
    :returns: Valid shells status
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Valid shells status"
    __file__= "/etc/shells"
    __cmdfile__ = "cat /etc/shells"
    check_count = 0
    badshell = os.linesep
    badshellhtml = '<br>'
    __command_check__ = config.CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)

    s = StringIO.StringIO(__output__)

    if __command_check__ == config.CHECKRESULTOK:
        for line in s:
            if not (line.startswith("#")):
                if not (exists_file(line.strip(),__host__, __user__, __passwd__, __port__)):
                    check_count += 1
                    badshell+=line
                    badshellhtml+=line+'<br>'

    if check_count > 0:
        __command_check__ = config.CHECKRESULTWARNING

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'All shells accounts are being used'
        __check_html_message__ = 'All shells accounts are being used'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __cmd__
        __check_html_message__ = 'Unable to load the configuration file: '  + __cmd__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'These shells ' + badshell + os.linesep + 'does not exist in the system but is allowed their use, are included in /etc/shells !!!'
        __check_html_message__ = 'These shells <br>' + badshellhtml + '<br>does not exist in the system but is allowed their use, are included in /etc/shells !!!'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__file__)
#------------------------------------------------------------------------------


def checkSSH(__host__, __user__, __passwd__, __port__):
    """
    :returns: Check ssh service
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Check ssh service"
    __file__= "/etc/ssh/sshd_config"
    __cmdfile__ = "cat /etc/ssh/sshd_config"
    __check__=['#PermitRootLogin yes','PermitRootLogin no','#PermitEmptyPasswords yes','PermitEmptyPasswords no']
    __check_count__ = 0

    __command_check__ = config.CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)

    if (__command_check__ == config.CHECKRESULTOK):
        __command_check__, __line__, __linehtml__, __check_count__ = check_file(__file__, __check__, __host__, __user__, __passwd__, __port__)

    if (__check_count__ < 2 ):
        __command_check__ = config.CHECKRESULTWARNING

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__ + ' contains any of the following chains:' + __line__
        __check_html_message__ = 'The next file ' + __file__ + ' contains any of the following chains:' + __line__
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' + __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'ssh service has an insecure configuration: ' + os.linesep
        __check_html_message__ = 'ssh service has an insecure configuration: ' + '<br>'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__file__)

#------------------------------------------------------------------------------


def checkDisabledCtrlAltDel(__host__, __user__, __passwd__, __port__):
    """
    :returns: ctrl+alt+del reboot check.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "ctrl+alt+del reboot check"
    __file__= "/etc/inittab"
    __cmdfile__ = "cat /etc/inittab"

    # Check that exists one of this:
    # #ca::ctrlaltdel:/sbin/shutdown -t3 -r now, #ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now
    __check__=['#ca::ctrlaltdel:', '#ca:12345:ctrlaltdel:']
    __command_check__ = config.CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)

    if (__command_check__ == config.CHECKRESULTOK):
        __command_check__, __line__, __linehtml__, __check_count__ = check_file(__file__, __check__, __host__, __user__, __passwd__, __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file ' + __file__ + ' contains the chain that comment ctrl+alt+del. It is not allowed reboot the system with ctrl+alt+del' + __line__
        __check_html_message__ = 'The next file ' + __file__ + ' contains the chain that comment ctrl+alt+del. It is not allowed reboot the system with ctrl+alt+del' + __linehtml__
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__
        __check_html_message__ = 'Unable to load the configuration file: ' + __file__
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'It is allowed to reboot the system with ctrl+alt+del!' + os.linesep
        __check_html_message__ = 'It is allowed to reboot the system with ctrl+alt+del!' + '<br>'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__, __file__)


#------------------------------------------------------------------------------


def checkCrontab(__host__, __user__, __passwd__, __port__):
    """
    :returns: Users allowed to use the crontab
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Users allowed to use the crontab"
    __file__= "/etc/cron.allow"
    __cmdfile__ = "cat /etc/cron.allow"
    __line__ = ""
    __linehtml__ = ""
    # Check that exists at least the root user:
    __check__=['root']
    __command_check__ = config.CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)

    if (__command_check__ == config.CHECKRESULTOK):
        __command_check__, __line__, __linehtml__, __check_count__ = check_file(__file__, __check__, __host__, __user__, __passwd__, __port__)

    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = 'The next file exists and contais the root user: ' + __file__ + ', so the crontab it is only allowed their use for root user'
        __check_html_message__ = 'The next file exists and contais the root user: ' + __file__ + ', so the crontab it is only allowed their use for root user'
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __file__ + ' - It is allowed the crontab use for all users  !!!!'
        __check_html_message__ = 'Unable to load the configuration file: ' + __file__ + ' - It is allowed the crontab use for all users  !!!!'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'The next file ' + __file__ + ' does not containt: ' + __line__ + os.linesep + ' - It is allowed the crontab use for all users  !!!!'
        __check_html_message__ = 'The next file ' + __file__ + ' does not containt: ' + __linehtml__ + '<br>' + 'It is allowed the crontab use for all users  !!!!'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__file__)


#------------------------------------------------------------------------------


def checkApache(__host__, __user__, __passwd__, __port__):
    """
    :returns: Apache configuration.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Apache configuration"
    __cmd__= "Apache conf"
    apache1="/etc/httpd/conf/httpd.conf";
    apache2="/etc/apache2/apache2.conf";
    apache3="/etc/apache/apache.conf";
    __command_check__ = config.CHECKRESULTERROR
    __check_message__ = os.linesep
    __check_html_message__ = '<br>'
    __output__ = ""

    __cmd_check__, __out__= exists_read_file(apache1, __host__, __user__, __passwd__, __port__)
    if (__cmd_check__):
        __command_check__ = config.CHECKRESULTOK
        __output__ = __out__
        __cmd__ = apache1

    __cmd_check__, __out__= exists_read_file(apache2, __host__, __user__, __passwd__, __port__)
    if (__cmd_check__):
        __command_check__ = config.CHECKRESULTOK
        __output__ = __out__
        __cmd__ = apache2

    __cmd_check__, __out__= exists_read_file(apache3, __host__, __user__, __passwd__, __port__)
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
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__, __cmd__)
