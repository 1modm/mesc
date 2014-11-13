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
import sys
import platform
import re
from . import config
from .operations import execute_cmd


__all__ = [
    "OS_ver",
    "OS_kernel",
    "OS_kernelver",
    "OS_machine",
    "OS_processor",
    "auditor_info",
    "uptime",
    "free",
    "who",
    "tail_root",
    "last"
]


def OS_ver(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Operating System Version"
    __cmd__ = "uname -o"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__ = {'Operating System Version': __output__}
    __OSout__ = __osreport__['Operating System Version']
    return (__OSout__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)


def OS_kernel(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Kernel Name"
    __cmd__ = "uname -s"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__,
         __user__, __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__ = {'Kernel Name': __output__}
    __OSout__ = __osreport__['Kernel Name']
    return (__OSout__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__,__cmd__)


def OS_kernelver(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Kernel Version"
    __cmd__ = "uname -r"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__ = {'Kernel Version': __output__}
    __OSout__ = __osreport__['Kernel Version']
    return (__OSout__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__,__cmd__)


def OS_machine(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Machine"
    __cmd__ = "uname -m"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__ = {'Machine': __output__}
    __OSout__ = __osreport__['Machine']
    return (__OSout__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)


def OS_processor(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Processor"
    __cmd__ = "uname -p"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__ = {'Processor': __output__}
    __OSout__ = __osreport__['Processor']
    return (__OSout__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def auditor_info(date, auditorname):
    __htmlreport__ = {}
    __dist__ = "%s %s %s" % (str(platform.linux_distribution()[0]),
         str(platform.linux_distribution()[1]),
          str(platform.linux_distribution()[2]))
    __htmlreport__ = {'Date': date, 'System': platform.system(),
         'Distribution': __dist__, 'Architecture': platform.machine(),
          'Processor': platform.processor(), 'Platform': platform.platform(),
          'Release': platform.release(), 'Hostname': os.uname()[1],
          'Python version': sys.version, 'Auditor': auditorname}
    __date__ = date

    __output__ = ' - ' + "Date: %s" % __date__ + os.linesep
    __output__ += ' - ' + "Auditor: %s" % auditorname + os.linesep

    if platform.system() == 'Linux':
        __output__ += ' - ' + "System: %s" % platform.system() + os.linesep
        __output__ += ' - ' + "Distribution: %s %s %s" %\
         (str(platform.linux_distribution()[0]),
         str(platform.linux_distribution()[1]),
         str(platform.linux_distribution()[2])) + os.linesep
        __output__ += ' - ' + "Architecture: %s" %\
             platform.machine() + os.linesep
        __output__ += ' - ' + "Processor: %s" %\
             platform.processor() + os.linesep
        __output__ += ' - ' + "Platform: %s" % platform.platform() + os.linesep
        __output__ += ' - ' + "Release: %s" % platform.release() + os.linesep
        __output__ += ' - ' + "Hostname: %s" % os.uname()[1] + os.linesep
    elif platform.system() == 'Windows':
        __output__ += ' - ' + "System: %s" % platform.system() + os.linesep
    elif platform.system() == 'Darwin':
        __output__ += ' - ' + "Mac: %s" % platform.mac_ver() + os.linesep
    elif platform.system() == 'FreeBSD':
        __output__ += ' - ' + "System: %s" % platform.system() + os.linesep
    __output__ += ' - ' + "Python version: %s" %\
         sys.version.split('\n') + os.linesep
    return (__output__, __htmlreport__)

#------------------------------------------------------------------------------


def uptime(__host__, __user__, __passwd__, __port__):
    """
    :returns: uptime command.
    :param host: Target.
    """
    __help_result__ = 'Gives a one line display of the following '
    __help_result__ += 'information, the current time, how long the system has '
    __help_result__ += 'been running, how many users are currently logged on, '
    __help_result__ += 'and the system load averages for the past 1, 5, and 15 '
    __help_result__ += 'minutes' + os.linesep
    __command__ = "System Uptime"
    __cmd__ = "uptime"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def free(__host__, __user__, __passwd__, __port__):
    """
    :returns: free command.
    :param host: Target.
    """
    __help_result__ = 'Displays the total amount of free and used '
    __help_result__ += 'physical and swap memory in the system, as well as the '
    __help_result__ += 'buffers used by the kernel' + os.linesep
    __command__ = "Free and used memory"
    __cmd__ = "free -o"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)

    if __command_check__ == config.CHECKRESULTOK:
        pattern = re.compile(r'\s+')
        sentence = re.sub(pattern, ' ', __output__)
        sentence = sentence.lstrip(' ')
        split_text = sentence.split(' ')
        total = split_text[7]
        used = split_text[8]
        freemem = split_text[9]
        sharedmem = split_text[10]
        buffers = split_text[11]
        cached = split_text[12]
        swap_total = split_text[14]
        swap_used = split_text[15]
        swap_free = split_text[16]
        percentage_used = (int(used) * 100) / (int(total))
        if (swap_used != "0"):
            percentage_swap_used = (int(swap_used) * 100) / (int(swap_total))
        else:
            percentage_swap_used = 0
        __check_message__ = ''
        __check_html_message__ = ''
        if (percentage_used < config.RESULTOKTHRESHOLD):
            __check_message__ = 'RAM memory used: ' + str(percentage_used) +\
             '%' + os.linesep
        elif (percentage_used < config.RESULTWARNINGTHRESHOLD):
            __command_check__ = config.CHECKRESULTWARNING
            __check_message__ = os.linesep + '   - Release memory '
            __check_message__ += os.linesep + '   - RAM memory used: ' +\
             str(percentage_used) + '%' + ' | Swap memory used: ' +\
             str(percentage_swap_used) + '%'
            __check_message__ += os.linesep + '   - Total Memory: ' +\
             str(total) + ' Kbytes ' + ' - ' + 'Free Memory: ' +\
             str(freemem) + ' Kbytes'
            __check_html_message__ = 'Release memory'
            __check_html_message__ += '<br> RAM memory used: ' +\
             str(percentage_used) + '%' + ' | Swap memory used: ' +\
             str(percentage_swap_used) + '%'
            __check_html_message__ += '<br> Total Memory: ' + str(total) +\
             ' Kbytes ' + ' - ' + 'Free Memory: ' + str(freemem) + ' Kbytes'
        else:
            __command_check__ = config.CHECKRESULTCRITICAL
            __check_message__ = os.linesep + '   - Release memory '
            __check_message__ += os.linesep + '   - RAM memory used: ' +\
             str(percentage_used) + '%' + ' | Swap memory used: ' +\
             str(percentage_swap_used) + '%'
            __check_message__ += os.linesep + '   - Total Memory: ' +\
             str(total) + ' Kbytes ' + ' - ' + 'Free Memory: ' +\
             str(freemem) + ' Kbytes'
            __check_html_message__ = 'Release memory'
            __check_html_message__ += '<br> RAM memory used: ' +\
             str(percentage_used) + '%' + ' | Swap memory used: ' +\
              str(percentage_swap_used) + '%'
            __check_html_message__ += '<br> Total Memory: ' + str(total) +\
             ' Kbytes ' + ' - ' + 'Free Memory: ' + str(freemem) + ' Kbytes'

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


def who(__host__, __user__, __passwd__, __port__):
    """
    :returns: w command.
    :param host: Target.
    """
    __help_result__ = 'Show who is logged on and what they are doing'
    __help_result__ += os.linesep
    __command__ = "Users logged"
    __cmd__ = "w"
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


def tail_root(__host__, __user__, __passwd__, __port__):
    """
    :returns: tail_root command.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Last 100 root commands executed"
    __cmd__ = "tail -100 /root/.bash_history"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__,
         __passwd__, __port__)
    if __command_check__ == config.CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == config.CHECKRESULTERROR:
        __check_message__ = 'Unable to execute, you must be root'
        __check_html_message__ = 'Unable to execute, you must be root'
    elif __command_check__ == config.CHECKRESULTWARNING:
        __check_message__ = 'Unable to execute, you must be root'
        __check_html_message__ = 'Unable to execute, you must be root'
    elif __command_check__ == config.CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__,
         __check_html_message__, __command__, __cmd__)

#------------------------------------------------------------------------------


def last(__host__, __user__, __passwd__, __port__):
    """
    :returns: last command.
    :param host: Target.
    """
    __help_result__ = 'Show listing of last logged in users'
    __help_result__ += os.linesep
    __command__ = 'Last logged in users'
    __cmd__ = "last"
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


def shells(__host__, __user__, __passwd__, __port__):
    """
    :returns: active shells
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = 'Active users in the system with an active shell'
    __cmd__ = "cat /etc/passwd | grep -v \/false | grep -v \/nologin" +\
     " | grep -v \/shutdown | grep -v \/halt | grep -v \/sync | grep -v \/news"
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