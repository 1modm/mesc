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
from datetime import date
from thirdparty.color.termcolor import colored
from include import show_banner, get_banner


__all__ = [
    "print_result_txt",
    "print_title_txt",
    "print_audit_txt",
    "create_txt_file"
]


CHECKRESULTOK = 'CHECKED'
CHECKRESULTWARNING = 'WARNING'
CHECKRESULTCRITICAL = 'CRITICAL'
CHECKRESULTERROR = 'ERROR'

#------------------------------------------------------------------------------

def create_txt_file(file_name, outputdirectory):
    __file__ = outputdirectory +'/'+file_name
    __create_file__ = open(__file__, 'w')
    __create_file__.write(get_banner())
    __create_file__.write(os.linesep)
    __create_file__.close()
    #print((colored('Report created in the file ' + __file__, 'yellow')))

def print_result_txt(helpresult, outputresult, checkresult, checkmessage, commandresult, cmdresults, file_name, outputdirectory):
    __file__ = outputdirectory +'/'+file_name
    __file__ = open(__file__, 'a')
    __file__.write('- ' +commandresult + ': ')
    __file__.write(helpresult)
    __file__.write('- # ' + cmdresults + os.linesep)
    if checkresult != CHECKRESULTOK: __file__.write(' * Issue: ' + checkmessage + os.linesep)
    if checkresult != CHECKRESULTOK: __file__.write(' * Evidence: '+ os.linesep + outputresult + os.linesep* 4)
    else: __file__.write(outputresult + os.linesep* 4)
    __file__.close()

def print_audit_txt(commandresult,line, outputresult, file_name, outputdirectory):
    __file__ = outputdirectory +'/'+file_name
    __file__ = open(__file__, 'a')
    __file__.write(commandresult+ os.linesep)
    __file__.write(line+ os.linesep)
    __file__.write(outputresult + os.linesep* 4)
    __file__.close()

def print_title_txt(title_name, hr_title, file_name, outputdirectory):
    __file__ = outputdirectory +'/'+file_name
    __file__ = open(__file__, 'a')
    __file__.write(title_name + os.linesep)
    __file__.write(hr_title + os.linesep * 2)
    __file__.close()
