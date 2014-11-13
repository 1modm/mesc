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

Copyright (c) 2014, Miguel Morillo
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
from . import config
from .operations import execute_cmd


__all__ = [
    "nmap",
    "rpcinfo",
    "routes",
    "activeconections",
    "ifconfig"
]


def nmap(__host__, __user__, __passwd__, __port__):
    """
    :returns: Opened ports in the system.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Opened ports in the system"
    __cmd__ = "nmap localhost"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def rpcinfo(__host__, __user__, __passwd__, __port__):
    """
    :returns: Openned RPC services.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Openned RPC services"
    __cmd__ = "rpcinfo -p localhost"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def routes(__host__, __user__, __passwd__, __port__):
    """
    :returns: Routing tables
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Routing tables"
    __cmd__ = "netstat -nr"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def activeconections(__host__, __user__, __passwd__, __port__):
    """
    :returns: Active Internet connections (servers and established)
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Active Internet connections (servers and established)"
    __cmd__ = "netstat -ta"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def ifconfig(__host__, __user__, __passwd__, __port__):
    """
    :returns: Status of the currently active interfaces.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Status of the currently active interfaces"
    __cmd__ = "ifconfig -a"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)
