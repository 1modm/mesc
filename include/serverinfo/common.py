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

Copyright (c) 2015, Miguel Morillo
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
import json
from . import config
from .operations import execute_cmd, OS_dist, exists_read_file


__all__ = [
    "auditor_info",
    "fire"
]



#------------------------------------------------------------------------------
def fire(__host__, __user__, __passwd__, __port__, __jsonfile__, __subfolder__):
    """
    :returns: Output security check from json file
    :params: Target, User, Passwd, Port and Json file
    """
    
    if (__subfolder__ == "include/serverinfo/common/"):
        __file__ = __subfolder__+__jsonfile__
    else:
        __file__ = __subfolder__+"/"+__jsonfile__

    with open(__file__) as data_file:
        data = json.loads(data_file.read())
        __help_result__ = data["help_result"]
        __command__ = data["command"]
        __distribution__ = OS_dist(__host__, __user__, __passwd__, __port__)
        if (__distribution__ == "RedHat"):
            __cmd__ = data["distribution"]["RedHat"]["cmd"]
        elif (__distribution__ == "SuSE"):
            __cmd__ = data["distribution"]["SuSE"]["cmd"]
        elif (__distribution__ == "debian"):
            __cmd__ = data["distribution"]["debian"]["cmd"]
        elif (__distribution__ == "mandrake"):
            __cmd__ = data["distribution"]["mandrake"]["cmd"]
        else:
            __cmd__ = data["distribution"]["all"]["cmd"]

        __type__ = data["type"]

        if __type__ == "execute_cmd":
            __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)

        if __type__ == "exists_read_file":
            if (__distribution__ == "RedHat"):
                __file__ = data["distribution"]["RedHat"]["file"]
            elif (__distribution__ == "SuSE"):
                __file__ = data["distribution"]["SuSE"]["file"]
            elif (__distribution__ == "debian"):
                __file__ = data["distribution"]["debian"]["file"]
            elif (__distribution__ == "mandrake"):
                __file__ = data["distribution"]["mandrake"]["file"]
            else:
                __file__ = data["distribution"]["all"]["file"]

            __cmd_check__, __output__ = exists_read_file(__file__, __host__, __user__, __passwd__, __port__)
        
            if (__cmd_check__):
                __command_check__ = config.CHECKRESULTOK
                __cmd__ = __file__
            else:
                __command_check__ = config.CHECKRESULTERROR
                __cmd__ = __file__

        if __type__ == "os_information":
            __osreport__ = {}
            __output_os__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
            __information__ = data["information"]
            __osreport__ = {__information__: __output_os__}
            __output__ = __osreport__[__information__]

        if (data["check"] == "free"):
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
        else:
            if __command_check__ == config.CHECKRESULTOK:
                __check_message__ = data["result"]["checkresultok"]["check_message"]
                __check_html_message__ = data["result"]["checkresultok"]["check_html_message"]
            elif __command_check__ == config.CHECKRESULTWARNING:
                __check_message__ = data["result"]["checkresultwarning"]["check_message"]
                __check_html_message__ = data["result"]["checkresultwarning"]["check_html_message"]
            elif __command_check__ == config.CHECKRESULTCRITICAL:
                __check_message__ = data["result"]["checkresultcritical"]["check_message"]
                __check_html_message__ = data["result"]["checkresultcritical"]["check_html_message"]
            elif __command_check__ == config.CHECKRESULTERROR:
                __check_message__ = data["result"]["checkresulterror"]["check_message"]
                __check_html_message__ = data["result"]["checkresulterror"]["check_html_message"]

    return (__output__.decode("ascii", "ignore"), __help_result__, __command_check__, __check_message__,
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
