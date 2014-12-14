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

from thirdparty.color.termcolor import colored
import include.serverinfo.config as config


__all__ = [
    "print_result_console",
    "print_title_console"
]


#------------------------------------------------------------------------------

def print_result_console(helpresult, outputresult, checkresult, checkmessage,
     commandresult, cmdresults, tableresult):
    __color_font__ = ''
    if checkresult == config.CHECKRESULTOK:
        __color_font__ = 'green'
    elif checkresult == config.CHECKRESULTWARNING:
        __color_font__ = 'yellow'
    elif checkresult == config.CHECKRESULTCRITICAL:
        __color_font__ = 'red'
    elif checkresult == config.CHECKRESULTERROR:
        __color_font__ = 'white'
    else:
        __color_font__ = 'blue'
    tableresult.append([(colored(' - ' + commandresult + '', 'blue')), '[ '
        + (colored(checkresult, __color_font__)) + ' ]'])


def print_title_console(title_name, hr_title, tableresult):
    tableresult.append([(colored(title_name
        + '                                ', 'white')), ''
        + (colored('', 'blue')) + ''])
    tableresult.append([(colored(hr_title + '                                ',
         'white')), '' + (colored('', 'blue')) + ''])

