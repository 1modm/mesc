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

Author: 1_mod_m

Project site: https://github.com/1modm/mesc

Copyright (c) 2014, Miguel Morillo Iruela.
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
import re
from common import execute_cmd


__all__ = [
    "diskspace",
    "inodespace",
    "setuid",
    "setgid",
    "rhosts",
    "runFilesNoGroup",
    "allpermissionsdir",
    "allpermissionsfiles",
    "writefiles",
    "tmpcontent"
]

#------------------------------------------------------------------------------
CHECKRESULTOK = 'CHECKED'
CHECKRESULTWARNING = 'WARNING'
CHECKRESULTCRITICAL = 'CRITICAL'
CHECKRESULTERROR = 'ERROR'
#------------------------------------------------------------------------------
RESULTOKTHRESHOLD = 50
RESULTWARNINGTHRESHOLD = 90
RESULTCRITICALTHRESHOLD = 99
#------------------------------------------------------------------------------

def diskspace(__host__, __user__, __passwd__, __port__):
    """
    :returns: File system disk space usage.
    :param host: Target.
    """
    __help_result__ = 'df displays the amount of disk space available on the file system'
    __help_result__ += os.linesep
    __command__ = "File system disk space usage"
    __cmd__= "df -h"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
        pattern = re.compile(r'\s+')
        sentence = re.sub(pattern, ' ', __output__)
        split_text=sentence.split(' ')
        filesys=split_text[7]
        space=split_text[8]
        used=split_text[9]
        free=split_text[10]
        use=split_text[11]
        mounted=split_text[12]
        int_use = use[:-1]
        percentage_used = (int(int_use));
        if (percentage_used < RESULTOKTHRESHOLD):
            __check_message__ = 'Disk space usage: ' + str(percentage_used) + '%'+ os.linesep
            __check_html_message__ = ''
        elif (percentage_used < RESULTWARNINGTHRESHOLD ):
            __command_check__= CHECKRESULTWARNING
            __check_message__ = 'Disk space usage: ' + str(percentage_used) + '%' + os.linesep
            __check_message__ += 'Space: ' + str(space) + ' - ' + 'Free: ' + str(free)
            __check_html_message__ = 'Disk space usage: ' + str(percentage_used) + '%'
            __check_html_message__ += '<br>Space: ' + str(space) + ' - ' + 'Free: ' + str(free)
        else:
            __command_check__ = CHECKRESULTCRITICAL
            __check_message__ = 'Disk space usage: ' + str(percentage_used) + '%' + os.linesep
            __check_message__ += 'Space: ' + str(space) + ' - ' + 'Free: ' + str(free)
            __check_html_message__ = 'Disk space usage: ' + str(percentage_used) + '%'
            __check_html_message__ += '<br>Space: ' + str(space) + ' - ' + 'Free: ' + str(free)

    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------


def inodespace(__host__, __user__, __passwd__, __port__):
    """
    :returns: File system disk inode space usage.
    :param host: Target.
    """
    __help_result__ = 'df displays the amount of disk space available on the file system'
    __help_result__ += os.linesep
    __command__ = "File system disk inode space usage"
    __cmd__= "df -i"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
        pattern = re.compile(r'\s+')
        sentence = re.sub(pattern, ' ', __output__)
        split_text=sentence.split(' ')
        filesys=split_text[7]
        inode=split_text[8]
        used=split_text[9]
        free=split_text[10]
        use=split_text[11]
        mounted=split_text[12]
        int_use = use[:-1]
        percentage_used = (int(int_use));
        if (percentage_used < RESULTOKTHRESHOLD):
            __check_message__ = 'Disk space usage: ' + str(percentage_used) + '%'+ os.linesep
            __check_html_message__ = ''
        elif (percentage_used < RESULTWARNINGTHRESHOLD ):
            __command_check__= CHECKRESULTWARNING
            __check_message__ = 'Disk space usage: ' + str(percentage_used) + '%' + os.linesep
            __check_message__ += 'Space: ' + str(inode) + ' - ' + 'Free: ' + str(free)
            __check_html_message__ = 'Disk space usage: ' + str(percentage_used) + '%'
            __check_html_message__ += '<br>Space: ' + str(inode) + ' - ' + 'Free: ' + str(free)
        else:
            __command_check__ = CHECKRESULTCRITICAL
            __check_message__ = 'Disk space usage: ' + str(percentage_used) + '%' + os.linesep
            __check_message__ += 'Space: ' + str(inode) + ' - ' + 'Free: ' + str(free)
            __check_html_message__ = 'Disk space usage: ' + str(percentage_used) + '%'
            __check_html_message__ += '<br>Space: ' + str(inode) + ' - ' + 'Free: ' + str(free)

    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------

def setuid(__host__, __user__, __passwd__, __port__):
    """
    :returns: Files with setuid permissions.
    :param host: Target.
    """
    __help_result__ = 'setuid and setgid (short for "set user ID upon execution" and "set group ID upon execution",'
    __help_result__ += ' respectively) are Unix access rights flags that allow users to run an executable with the'
    __help_result__ += ' permissions of the executables owner or group respectively and to change behaviour in directories.'
    __help_result__ += os.linesep
    __command__ = "Files with setuid permissions"
    __cmd__= "find /tmp -type f -perm -4000 -print 2>/dev/null"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''

    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------

def setgid(__host__, __user__, __passwd__, __port__):
    """
    :returns: Files with setgid permissions.
    :param host: Target.
    """
    __help_result__ = 'setuid and setgid (short for "set user ID upon execution" and "set group ID upon execution",'
    __help_result__ += ' respectively) are Unix access rights flags that allow users to run an executable with the'
    __help_result__ += ' permissions of the executables owner or group respectively and to change behaviour in directories.'
    __help_result__ += os.linesep
    __command__ = "Files with setgid permissions"
    __cmd__= "find /tmp -type f -perm -2000 -print 2>/dev/null"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)


#------------------------------------------------------------------------------
def rhosts(__host__, __user__, __passwd__, __port__):
    """
    :returns: rhosts files.
    :param host: Target.
    """
    __help_result__ = 'The .rhosts file is the user equivalent of the /etc/hosts.equiv file. It contains a list of'
    __help_result__ += ' host-user combinations, rather than hosts in general. If a host-user combination is listed in this file,'
    __help_result__ += ' the specified user is granted permission to log in remotely from the specified host without having to supply a password.'
    __help_result__ += 'The machines and users writen in these files they will have allowed to access without password using some r-service, like rlogin'
    __help_result__ += os.linesep
    __command__ = ".rhosts files"
    __cmd__= "find /tmp -type f -name .rhosts -print 2>/dev/null"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)


#------------------------------------------------------------------------------


def writefiles(__host__, __user__, __passwd__, __port__):
    """
    :returns: Files with write access for all users.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Files with write access for all users"
    __cmd__= "find /tmp -type f -perm -2 -print 2>/dev/null"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------


def allpermissionsfiles(__host__, __user__, __passwd__, __port__):
    """
    :returns: Files with 777 permissions
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Files with 777 permissions"
    __cmd__= "find /tmp -type f -perm 777"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------


def allpermissionsdir(__host__, __user__, __passwd__, __port__):
    """
    :returns: Folders with 777 permissions
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Folders with 777 permissions"
    __cmd__= "find /tmp -type d -perm 777"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------


def runFilesNoGroup(__host__, __user__, __passwd__, __port__):
    """
    :returns: Files without group
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Files without group"
    __cmd__= "find /tmp  -nouser -o -nogroup"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)

#------------------------------------------------------------------------------


def tmpcontent(__host__, __user__, __passwd__, __port__):
    """
    :returns: /tmp content
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "/tmp content"
    __cmd__= "ls -ltr /tmp"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'You must be root'
        __check_html_message__ = 'You must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__, __command__,__cmd__)


#------------------------------------------------------------------------------
