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
import argparse
import hashlib
from tabulate import tabulate  # pip install tabulate
from datetime import datetime
from thirdparty.color.termcolor import colored


#------------------------------------------------------------------------------
# Python version check.
#------------------------------------------------------------------------------

if __name__ == "__main__":
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0):
        show_banner()
        print ("[!] You must use Python version 2.7 or above")
        sys.exit(1)


#------------------------------------------------------------------------------
# Plugins
#------------------------------------------------------------------------------

from include import show_banner, get_banner
from lib.htmloutput import htmlaudit, htmlend, create_html_file
from lib.txtoutput import create_txt_file, print_audit_txt
from lib.output import print_results, print_titles, print_title_console
import include.serverinfo.common as common
import include.serverinfo.boot as boot
import include.serverinfo.filesystem as filesystem
import include.serverinfo.tcpip as tcpip
import include.serverinfo.proc as proc
import include.serverinfo.security as security

#------------------------------------------------------------------------------
# Command line parser using argparse
#------------------------------------------------------------------------------

def cmdline_parser():
    parser = argparse.ArgumentParser(conflict_handler='resolve', add_help=True,
        description='Example: python %(prog)s -a -txt output.txt -html output.html localhost',
        version='MESC 0.1', usage="python %(prog)s [OPTIONS] HOST")

    # Mandatory
    parser.add_argument('host', action="store")

    # Optional
    parser.add_argument('-a', '--all', action='store_true', default=False,
        dest='all',
        help='Set all options to true')

    parser.add_argument('-n', '--name', action='store', default='Auditor',
        dest='auditorname',
        help='Auditor name')

    parser.add_argument('-txt', action='store', default='results.log',
        dest='txt_file',
        help='txt file name where is writen the results')

    parser.add_argument('-html', action='store',  default='results.html',
        dest='html_file',
        help='html file name where is writen the results')

    parser.add_argument('-u', action='store',
        dest='user',
        help='Remote user')

    parser.add_argument('-p', action='store',
        dest='passwd',
        help='Remote user password')

    parser.add_argument('-P', action='store',
        dest='port',
        help='Remote port')

    group = parser.add_argument_group("Check Sections")

    group.add_argument('-g', '--general', action='store_true', default=False,
        dest='general',
        help='General system information')

    group.add_argument('-b', '--boot', action='store_true', default=False,
        dest='boot',
        help='Boot Information')

    group.add_argument('-f', '--filesystem', action='store_true', default=False,
        dest='filesystem',
        help='File System Information')

    group.add_argument('-t', '--tcpip', action='store_true', default=False,
        dest='tcpip',
        help='TCP/IP Information')

    group.add_argument('-proc', '--processes', action='store_true', default=False,
        dest='processes',
        help='Processes running in the system')

    group.add_argument('-s', '--security', action='store_true', default=False,
        dest='security',
        help='Security Information')

    return parser


#------------------------------------------------------------------------------
# Start of program
#------------------------------------------------------------------------------

def main():

    # Show the program banner.
    show_banner()

    # Get the command line parser.
    parser = cmdline_parser()

    # Show help if no args
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    #---------------------------------------------------------------------------

    # Get results line parser.
    results = parser.parse_args()

    #---------------------------------------------------------------------------
    # Sections
    #---------------------------------------------------------------------------

    AUDIT='[0] Auditor information            '
    AUDIT_LINE = '-----------------------'
    GENERAL='[1] System information             '
    GENERAL_LINE = '----------------------'
    BOOT='[2] Boot information               '
    BOOT_LINE='--------------------'
    FILESYSTEM='[3] File system information        '
    FILESYSTEM_LINE='---------------------------'
    TCPIP='[4] Network Information            '
    TCPIP_LINE='----------------------'
    PROCESSES='[5] Processes running in the system'
    PROCESSES_LINE='-----------------------------------'
    SECURITY='[6] Security information           '
    SECURITY_LINE='------------------------'
    REPORTS='[7] Reports                        '
    REPORTS_LINE='-----------'

    #---------------------------------------------------------------------------
    # Global variables
    #---------------------------------------------------------------------------
    table0 = []
    table1 = []
    table2 = []
    table3 = []
    table4 = []
    table5 = []
    table6 = []

    # Fabric
    if results.port:
        fabric_port = results.port
    else: fabric_port = '22'

    if results.user:
        fabric_user = results.user
    else: fabric_user = 'root'

    if results.passwd:
        fabric_passwd = results.passwd
    else: fabric_passwd = None

    #---------------------------------------------------------------------------
    # Output
    #---------------------------------------------------------------------------

    # Create output directory for txt and html results
    outputdirectory = 'output'
    if not os.path.exists(outputdirectory):
        os.makedirs(outputdirectory)
    datenow = datetime.now()
    outputdate = datenow.strftime('%Y-%m-%d@%H_%M_%S')
    outputdirectory = 'output'+'/'+ outputdate
    os.makedirs(outputdirectory)
    os.makedirs(outputdirectory+'/css')
    os.makedirs(outputdirectory+'/js')

    # Create the txt results file
    if results.txt_file:
        create_txt_file (results.txt_file,outputdirectory)
    else:
        results.txt_file='results.log'
        create_txt_file (results.txt_file,outputdirectory)

    # Create the html results file
    if results.html_file:
        create_html_file (results.html_file,outputdirectory)
    else:
        results.html_file='results.html'
        create_html_file (results.html_file,outputdirectory)

    #---------------------------------------------------------------------------

    # Auditor Operating System Information
    os_output, htmlAuditreport = common.auditor_info(outputdate, results.auditorname)
    # Output
    print_audit_txt(AUDIT,AUDIT_LINE, os_output, results.txt_file, outputdirectory)
    htmlaudit(results.html_file, htmlAuditreport, outputdirectory)

    print_title_console(AUDIT, AUDIT_LINE, table0)
    print tabulate(table0, tablefmt="plain")# print out the results
    print((colored(os_output + os.linesep, 'white')))


    #---------------------------------------------------------------------------

    if results.general or results.all:
        print_titles(GENERAL, GENERAL_LINE, 'general', results.txt_file, results.html_file, outputdirectory, table1)

        # Operating System Information
        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.OS_ver(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.OS_kernel(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.OS_kernelver(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.OS_machine(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.OS_processor(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        # System Information
        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.uptime(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.free(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.who(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.tail_root(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.last(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = common.shells(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table1, results.txt_file, results.html_file, outputdirectory)

        print tabulate(table1, tablefmt="plain")# print out the results
        print os.linesep
    #---------------------------------------------------------------------------

    if results.boot or results.all:
        print_titles(BOOT, BOOT_LINE, 'boot', results.txt_file, results.html_file, outputdirectory, table2)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = boot.grub(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table2, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = boot.rc3(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table2, results.txt_file, results.html_file, outputdirectory)

        print tabulate(table2, tablefmt="plain") # print out the results
        print os.linesep
    #---------------------------------------------------------------------------

    if results.filesystem or results.all:
        print_titles(FILESYSTEM, FILESYSTEM_LINE, 'filesystem', results.txt_file, results.html_file, outputdirectory, table3)

        filesystem.defpath()

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.diskspace(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.inodespace(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.setuid(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.setgid(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.rhosts(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.allpermissionsdir(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.allpermissionsfiles(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.writefiles(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = filesystem.tmpcontent(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table3, results.txt_file, results.html_file, outputdirectory)

        print tabulate(table3, tablefmt="plain") # print out the results
        print os.linesep
    #---------------------------------------------------------------------------

    if results.tcpip or results.all:
        print_titles(TCPIP, TCPIP_LINE, 'tcpip', results.txt_file, results.html_file, outputdirectory, table4)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = tcpip.nmap(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table4, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = tcpip.rpcinfo(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table4, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = tcpip.routes(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table4, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = tcpip.activeconections(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table4, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = tcpip.ifconfig(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table4, results.txt_file, results.html_file, outputdirectory)

        print tabulate(table4, tablefmt="plain") # print out the results
        print os.linesep
    #---------------------------------------------------------------------------

    if results.processes or results.all:
        print_titles(PROCESSES, PROCESSES_LINE, 'processes', results.txt_file, results.html_file, outputdirectory, table5)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = proc.proc(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table5, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = proc.packages(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table5, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = proc.top(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table5, results.txt_file, results.html_file, outputdirectory)

        print tabulate(table5, tablefmt="plain") # print out the results
        print os.linesep
    #---------------------------------------------------------------------------

    if results.security or results.all:
        print_titles(SECURITY, SECURITY_LINE, 'security', results.txt_file, results.html_file, outputdirectory, table6)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = security.checkShells(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table6, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = security.checkSSH(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table6, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = security.checkDisabledCtrlAltDel(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table6, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = security.checkCrontab(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table6, results.txt_file, results.html_file, outputdirectory)

        command_output, help_command, command_check, check_message, check_html_message, command, cmd = security.checkApache(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table6, results.txt_file, results.html_file, outputdirectory)
        '''
        command_output, help_command, command_check, check_message, check_html_message, command, cmd = security.recomendations(results.host, fabric_user, fabric_passwd, fabric_port)
        print_results(help_command, command_output, command_check, check_message, check_html_message, command, cmd, table6, results.txt_file, results.html_file, outputdirectory)

        print "<FONT COLOR=$color_cabecera>- chkrootkit: shell script that checks system binaries for rootkit modification</FONT> http://www.chkrootkit.org/<br>";
        print "<FONT COLOR=$color_cabecera>- AIDE (Advanced Intrusion Detection Environment) </FONT>http://www.cs.tut.fi/~rammer/aide.html<br>";
        print "<FONT COLOR=$color_cabecera>- John the Ripper is a fast password cracker </FONT>http://www.openwall.com/john/ <br>";
        print "<FONT COLOR=$color_cabecera>- Logcheck is a simple utility which is designed to allow a system administrator to view the logfiles which are produced upon hosts under their control. </FONT>http://logcheck.org/ <br>";
        print "<FONT COLOR=$color_cabecera>- Portsentry is an attack detection tool </FONT>http://sourceforge.net/projects/sentrytools/<br>";
        print "<FONT COLOR=$color_cabecera>- HostSentry is a host based intrusion detection tool </FONT><br>";
        print "<FONT COLOR=$color_cabecera>- DenyHosts is a script intended to be run by Linux system administrators to help thwart SSH server attacks  </FONT>http://denyhosts.sourceforge.net/<br>";
        '''
        print tabulate(table6, tablefmt="plain") # print out the results

    #---------------------------------------------------------------------------

    htmlend(results.html_file, outputdirectory)

    print(os.linesep * 2  + (colored(REPORTS, 'white')))
    print((colored(REPORTS_LINE + os.linesep, 'white')))
    hashhtmlreport = hashlib.sha224(results.html_file).hexdigest()
    hashtxtreport = hashlib.sha224(results.txt_file).hexdigest()
    print((colored(' - HTML report (%s): ./' % hashhtmlreport + outputdirectory +'/' + results.html_file, 'yellow')))
    print((colored(' - Text report (%s): ./' % hashtxtreport + outputdirectory +'/' + results.txt_file, 'yellow')))
    print os.linesep

    #---------------------------------------------------------------------------
    # The End
    #---------------------------------------------------------------------------

    sys.exit(0)


#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()