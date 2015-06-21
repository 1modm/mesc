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
from thirdparty.color.termcolor import colored
from include import get_banner

__all__ = [
    "create_log"
]


def create_log(report, reportline, hashhtmlreport, hashtxtreport,
               outputdirectory, html_file, txt_file, log_file_name,
               outputdate, host):
    __file__ = log_file_name
    if (os.path.isfile(__file__)):
        __create_file__ = open(__file__, 'a')
    else:
        __create_file__ = open(__file__, 'w')
        __create_file__.write(get_banner())
        __create_file__.write(os.linesep)
    __create_file__.write('# Audit date: %s' % outputdate)
    __create_file__.write(os.linesep)
    __create_file__.write('# Audit target: %s' % host)
    __create_file__.write(os.linesep)
    __create_file__.write('- HTML report (%s): ./' % hashhtmlreport +
                          outputdirectory + '/' + html_file)
    __create_file__.write(os.linesep)
    __create_file__.write('- Text report (%s): ./' % hashtxtreport +
                          outputdirectory + '/' + txt_file)
    __create_file__.write(os.linesep * 3)
    __create_file__.close()

    print((os.linesep * 2 + (colored(report, 'white'))))
    print((colored(reportline + os.linesep, 'white')))
    print((colored(' - HTML report (%s): ./' % hashhtmlreport + outputdirectory
                    + '/html/' + html_file, 'yellow')))
    print((colored(' - Text report (%s): ./' % hashtxtreport + outputdirectory
                   + '/txt/' + txt_file, 'yellow')))
    print((os.linesep))
