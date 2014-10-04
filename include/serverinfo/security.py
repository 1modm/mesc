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
from common import execute_cmd


__all__ = [
    "checkShells",
    "checkSSH",
    "checkDisabledCtrlAltDel",
    "checkCrontab",
    "checkApache",
    "recomendations"
]

#------------------------------------------------------------------------------
CHECKRESULTOK = 'CHECKED'
CHECKRESULTWARNING = 'WARNING'
CHECKRESULTCRITICAL = 'CRITICAL'
CHECKRESULTERROR = 'ERROR'
#------------------------------------------------------------------------------

def checkShells(__host__, __user__, __passwd__, __port__):
    """
    :returns: Valid shells status
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Valid shells status"
    __cmd__= "/etc/shells"
    __cmdfile__ = "cat /etc/shells"
    badshell=os.linesep
    badshellhtml='<br>'
    check_count=0
    __command_check__ = CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)

    if (os.path.isfile(__cmd__)):
        __command_check__ = CHECKRESULTOK
        f = open(__cmd__,'r')
        out = f.readlines()
        for line in out:
            if not (line.startswith("#")):
                if not (os.path.isfile(line.strip())):
                    check_count += 1
                    badshell+=line
                    badshellhtml+=line+'<br>'
    if check_count > 0:
        __command_check__ = CHECKRESULTWARNING

    if __command_check__ == CHECKRESULTOK:
        __check_message__ = 'All shells accounts are being used'
        __check_html_message__ = 'All shells accounts are being used'
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __cmd__
        __check_html_message__ = 'Unable to load the configuration file: '  + __cmd__
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'The shell ' + badshell + os.linesep + 'Not exists in the system but is allowed their usage, it is included in /etc/shells !!!'
        __check_html_message__ = 'The shell <br>' + badshellhtml + '<br>Not exists in the system but is allowed their usage, it is included in /etc/shells !!!'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)
#------------------------------------------------------------------------------


def checkSSH(__host__, __user__, __passwd__, __port__):
    """
    :returns: Check ssh service
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Check ssh service"
    __cmd__= "/etc/ssh/sshd_config"
    __cmdfile__ = "cat /etc/ssh/sshd_config"
    bad=os.linesep
    badhtml='<br>'
    check_count=0
    check=['#PermitRootLogin no','PermitRootLogin yes','#PermitEmptyPasswords no','PermitEmptyPasswords yes']
    __command_check__ = CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)
    if (os.path.isfile(__cmd__)):
        __command_check__ = CHECKRESULTOK
        f = open(__cmd__,'r')
        out = f.readlines()
        for line in out:
            for c in check:
                if c in line:
                    check_count += 1
                    bad+=line
                    badhtml+=line+'<br>'
    if check_count > 0:
        __command_check__ = CHECKRESULTWARNING

    if __command_check__ == CHECKRESULTOK:
        __check_message__ = 'The next file ' + __cmd__ + ' does not contain any of the following chains:' + check
        __check_html_message__ = 'The next file ' + __cmd__ + ' does not contain any of the following chains:' + check
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __cmd__
        __check_html_message__ = 'Unable to load the configuration file: ' + __cmd__
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'ssh root login or null passwords are allowed: ' + bad + os.linesep
        __check_html_message__ = 'ssh root login or null passwords are allowed: ' + badhtml + '<br>'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------


def checkDisabledCtrlAltDel(__host__, __user__, __passwd__, __port__):
    """
    :returns: ctrl+alt+del reboot check.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "ctrl+alt+del reboot check"
    __cmd__= "/etc/inittab"
    __cmdfile__ = "cat /etc/inittab"
    okline=os.linesep
    oklinehtml='<br>'
    check_count=0
    # Check that exists one of this:
    # #ca::ctrlaltdel:/sbin/shutdown -t3 -r now, #ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now
    check=['#ca::ctrlaltdel:', '#ca:12345:ctrlaltdel:']
    __command_check__ = CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)
    if (os.path.isfile(__cmd__)):
        __command_check__ = CHECKRESULTWARNING
        f = open(__cmd__,'r')
        out = f.readlines()
        for line in out:
            for c in check:
                if c in line:
                    check_count += 1
                    okline+=line
                    oklinehtml+=line+'<br>'
    if check_count > 0:
        __command_check__ = CHECKRESULTOK

    if __command_check__ == CHECKRESULTOK:
        __check_message__ = 'The next file ' + __cmd__ + ' contains the chain that comment ctrl+alt+del. It is not allowed reboot the system with ctrl+alt+del'
        __check_html_message__ = 'The next file ' + __cmd__ + ' contains the chain that comment ctrl+alt+del. It is not allowed reboot the system with ctrl+alt+del'
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __cmd__
        __check_html_message__ = 'Unable to load the configuration file: ' + __cmd__
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'The next file ' + __cmd__ + ' does not containt: ' + okline + os.linesep
        __check_html_message__ = 'The next file ' + __cmd__ + ' does not containt: ' + oklinehtml + '<br>'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)


#------------------------------------------------------------------------------


def checkCrontab(__host__, __user__, __passwd__, __port__):
    """
    :returns: Users allowed to use the crontab
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Users allowed to use the crontab"
    __cmd__= "/etc/cron.allow"
    __cmdfile__ = "cat /etc/cron.allow"
    okline=os.linesep
    oklinehtml='<br>'
    check_count=0
    # Check that exists at least the root user:
    check=['root']
    __command_check__ = CHECKRESULTERROR
    __output__, __command_check__ = execute_cmd(__cmdfile__, __host__, __user__, __passwd__, __port__)
    if (os.path.isfile(__cmd__)):
        __command_check__ = CHECKRESULTWARNING
        f = open(__cmd__,'r')
        out = f.readlines()
        for line in out:
            for c in check:
                if c in line:
                    check_count += 1
                    okline+=line
                    oklinehtml+=line+'<br>'
    if check_count > 0:
        __command_check__ = CHECKRESULTOK

    if __command_check__ == CHECKRESULTOK:
        __check_message__ = 'The next file exists and contais the root user: ' + __cmd__ + ', so the crontab it is only allowed their use for root user'
        __check_html_message__ = 'The next file exists and contais the root user: ' + __cmd__ + ', so the crontab it is only allowed their use for root user'
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to load the configuration file: ' + __cmd__ + ' - It is allowed the crontab use for all users  !!!!'
        __check_html_message__ = 'Unable to load the configuration file: ' + __cmd__ + ' - It is allowed the crontab use for all users  !!!!'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'The next file ' + __cmd__ + ' does not containt: ' + okline + os.linesep + ' - It is allowed the crontab use for all users  !!!!'
        __check_html_message__ = 'The next file ' + __cmd__ + ' does not containt: ' + oklinehtml + '<br>' + 'It is allowed the crontab use for all users  !!!!'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)


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
    __command_check__ = CHECKRESULTERROR

    if (os.path.isfile(apache1)):
        __command_check__ = CHECKRESULTOK
        f = open(apache1,'r')
        out = f.read()
    elif (os.path.isfile(apache2)):
        __command_check__ = CHECKRESULTOK
        f = open(apache2,'r')
        out = f.read()
    elif (os.path.isfile(apache3)):
        __command_check__ = CHECKRESULTOK
        f = open(apache3,'r')
        out = f.read()
    else: __command_check__ = CHECKRESULTERROR

    if __command_check__ == CHECKRESULTOK:
        __check_message__ = 'Apache configuration loaded'
        __check_html_message__ = 'Apache configuration loaded'
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to load configuration, Apache web server is not installed'
        __check_html_message__ = 'Unable to load configuration, Apache web server is not installed'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (out, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)
