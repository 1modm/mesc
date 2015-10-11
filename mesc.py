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

Copyright (c) 2007-2015, Miguel Morillo
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
from tabulate import tabulate
from datetime import datetime
from thirdparty.color.termcolor import colored


#------------------------------------------------------------------------------
# Plugins
#------------------------------------------------------------------------------

from include import show_banner
from lib.htmloutput import htmlaudit, htmlend, htmllast, create_html_file,\
                           create_blank_html_file, htmldatadashboard,\
                           htmldatadashboardjs, htmldashboardend
from lib.txtoutput import create_txt_file, print_audit_txt
from lib.output import print_results, print_titles, print_title_console
import include.log as log
import include.serverinfo.common as common
import include.serverinfo.boot as boot
import include.serverinfo.filesystem as filesystem
import include.serverinfo.tcpip as tcpip
import include.serverinfo.proc as proc
import include.serverinfo.security as security
import include.serverinfo.psmem as ps_mem

#------------------------------------------------------------------------------
# Python version check.
#------------------------------------------------------------------------------

if __name__ == "__main__":
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0):
        show_banner()
        print ("[!] You must use Python version 2.7 or above")
        sys.exit(1)


#------------------------------------------------------------------------------
# Command line parser using argparse
#------------------------------------------------------------------------------

def cmdline_parser():
    parser = argparse.ArgumentParser(conflict_handler='resolve', add_help=True,
        description='Example: python %(prog)s -a -txt output.txt\
            -html output.html localhost', version='MESC 0.2',
             usage="python %(prog)s [OPTIONS] HOST")

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

    parser.add_argument('-html', action='store', default='results.html',
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
        help='Filesystem Information')

    group.add_argument('-t', '--tcpip', action='store_true', default=False,
        dest='tcpip',
        help='TCP/IP Information')

    group.add_argument('-proc', '--processes', action='store_true',
        default=False,
        dest='processes',
        help='Processes running in the system')

    group.add_argument('-s', '--security', action='store_true', default=False,
        dest='security',
        help='Security Information')

    return parser


#------------------------------------------------------------------------------
# Statistics
#------------------------------------------------------------------------------


def statistics(ccheck, section, title, totalchecks=[0], totalchecksok=[0],
               totalcheckswarning=[0], totalcheckscritical=[0],
               totalcheckserror=[0], totalchecksystem=[0], totalchecksboot=[0],
               totalchecksfile=[0], totalchecksnet=[0], totalchecksproc=[0],
               totalcheckssec=[0]):

    if (ccheck != "load"):
        totalchecks[0] += 1

        if (ccheck == 'CHECKED'):
            totalchecksok[0] += 1
        elif (ccheck == 'WARNING'):
            totalcheckswarning[0] += 1
        elif (ccheck == 'CRITICAL'):
            totalcheckscritical[0] += 1
        elif (ccheck == 'ERROR'):
            totalcheckserror[0] += 1

        if (section == 'general'):
            totalchecksystem[0] += 1
        if (section == 'boot'):
            totalchecksboot[0] += 1
        if (section == 'filesystem'):
            totalchecksfile[0] += 1
        if (section == 'tcpip'):
            totalchecksnet[0] += 1
        if (section == 'processes'):
            totalchecksproc[0] += 1
        if (section == 'security'):
            totalcheckssec[0] += 1

        consoleoutput.append([title, ccheck, section])

    return (totalchecks[0], totalchecksok[0], totalcheckswarning[0],
            totalcheckscritical[0], totalcheckserror[0], totalchecksystem[0],
            totalchecksboot[0], totalchecksfile[0], totalchecksnet[0],
            totalchecksproc[0], totalcheckssec[0], consoleoutput)


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
    # Start time
    #---------------------------------------------------------------------------
    start_time = datetime.now()

    #---------------------------------------------------------------------------
    # Sections
    #---------------------------------------------------------------------------

    AUDIT = 'Auditor information            '
    AUDIT_LINE = '-----------------------'
    GENERAL = 'System information             '
    GENERAL_LINE = '----------------------'
    BOOT = 'Boot information               '
    BOOT_LINE = '--------------------'
    FILESYSTEM = 'Filesystem information         '
    FILESYSTEM_LINE = '---------------------------'
    TCPIP = 'Network information            '
    TCPIP_LINE = '----------------------'
    PROCESSES = 'Processes running in the system'
    PROCESSES_LINE = '-----------------------------------'
    SECURITY = 'Security information           '
    SECURITY_LINE = '------------------------'
    REPORTS = 'Reports                        '
    REPORTS_LINE = '-----------'

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

    total = 0
    totalsok = 0
    totalwarning = 0
    totalcritical = 0
    totalserror = 0
    totalsystem = 0
    totalboot = 0
    totalfile = 0
    totalnet = 0
    totalproc = 0
    totalsec = 0
    processes_duration = 0
    network_duration = 0
    file_duration = 0
    boot_duration = 0
    sys_duration = 0

    global consoleoutput 
    consoleoutput = []


    # Fabric
    if results.port:
        fabric_port = results.port
    else:
        fabric_port = '22'

    if results.user:
        fabric_user = results.user
    else:
        fabric_user = 'root'

    if results.passwd:
        fabric_passwd = results.passwd
    else:
        fabric_passwd = None

    #---------------------------------------------------------------------------
    # Output
    #---------------------------------------------------------------------------

    # Create output directory for txt and html results
    outputdirectory = 'output'
    if not os.path.exists(outputdirectory):
        os.makedirs(outputdirectory)
    datenow = datetime.now()
    outputdate = datenow.strftime('%Y-%m-%d_%H_%M_%S')
    outputdirectory = 'output' + '/' + outputdate
    os.makedirs(outputdirectory)
    os.makedirs(outputdirectory + '/txt')
    os.makedirs(outputdirectory + '/html/reports')
    os.makedirs(outputdirectory + '/html/css')
    os.makedirs(outputdirectory + '/html/js')
    os.makedirs(outputdirectory + '/html/fonts')
    os.makedirs(outputdirectory + '/html/img')
    os.makedirs(outputdirectory + '/html/img/icons')
    outputdirectorytxt = (outputdirectory + '/txt')
    outputdirectoryhtml = (outputdirectory + '/html')

    # Create the txt results file
    if results.txt_file:
        create_txt_file(results.txt_file, outputdirectorytxt)
    else:
        results.txt_file = 'results.txt'
        create_txt_file(results.txt_file, outputdirectorytxt)

    # Create the html results file
    if results.html_file:
        create_html_file(results.html_file, outputdirectoryhtml, outputdate)
    else:
        results.html_file = 'results.html'
        create_html_file(results.html_file, outputdirectoryhtml, outputdate)

#------------------------------------------------------------------------------

    # Auditor Operating System Information
    os_output, htmlAuditreport = common.auditor_info(start_time,
                                                     results.auditorname)
    # Output txt
    print_audit_txt('[0] ' + AUDIT, AUDIT_LINE, os_output, results.txt_file,
                    outputdirectorytxt)

    # Output html
    gen_html_file = 'general_' + results.html_file
    boot_html_file = 'boot_' + results.html_file
    file_html_file = 'file_' + results.html_file
    net_html_file = 'net_' + results.html_file
    proc_html_file = 'proc_' + results.html_file
    sec_html_file = 'security_' + results.html_file

    cat_menu = {'fileout': results.html_file,
                'fileoutgen': gen_html_file, 'general': 'System information',
                'fileoutboot': boot_html_file, 'boot': 'Boot',
                'fileoutfile': file_html_file, 'filesystem': 'Filesystem',
                'fileoutnet': net_html_file, 'tcpip': 'Network',
                'fileoutproc': proc_html_file, 'processes': 'Processes',
                'fileoutsec': sec_html_file, 'security': 'Security'}

    htmlaudit(results.html_file, htmlAuditreport, outputdirectoryhtml, cat_menu)

    # Output console
    print_title_console('[0] ' + AUDIT, AUDIT_LINE, table0)
    print((tabulate(table0, tablefmt="plain")))  # print out the results
    print((colored(os_output + os.linesep, 'white')))

################################################################################

    if results.general or results.all:
        href = 'general'
        html_file = gen_html_file
        create_blank_html_file(html_file, outputdirectoryhtml, outputdate,
                               cat_menu)
        print_titles('[1] ' + GENERAL, GENERAL_LINE, href,
                     results.txt_file, html_file, outputdirectory,
                     table1)

        # System Information
        folder = "include/serverinfo/common/"
        for jsonfile in sorted(os.listdir(folder)):

            if jsonfile.endswith(".json"):
                command_output, help_command, command_check, check_message,\
                check_html_message, command, cmd = common.fire(results.host, fabric_user,
                                                               fabric_passwd, fabric_port, jsonfile, folder)
                print_results(help_command, command_output, command_check,
                              check_message, check_html_message, command, cmd, table1,
                              results.txt_file, html_file, outputdirectory)

                statistics(command_check, href, command)  # Statistics

        for rootfs, subFolders, files in os.walk(folder):
            for sf in subFolders:
                table1.append([(colored(' + ' + sf + '                                ', 'white')), '' + (colored('', 'blue')) + ''])
                folderjson = folder + sf
                for jsonfile in sorted(os.listdir(folderjson)):
                    if jsonfile.endswith(".json"):
                        command_output, help_command, command_check, check_message,\
                        check_html_message, command, cmd = common.fire(results.host, fabric_user,
                                                                       fabric_passwd, fabric_port, jsonfile, folderjson)
                        print_results(help_command, command_output, command_check,
                                      check_message, check_html_message, command, cmd, table1,
                                      results.txt_file, html_file, outputdirectory)

                        statistics(command_check, href, command)  # Statistics


        htmlend(html_file, outputdirectoryhtml)

        print((tabulate(table1, tablefmt="plain")))  # print out the results
        print((os.linesep))

    #---------------------------------------------------------------------------
    # system time
    #---------------------------------------------------------------------------
        sys_time = datetime.now()
        sys_duration = format(sys_time - start_time)

################################################################################

    if results.boot or results.all:
        href = 'boot'
        html_file = boot_html_file
        create_blank_html_file(html_file, outputdirectoryhtml, outputdate,
                               cat_menu)
        print_titles('[2] ' + BOOT, BOOT_LINE, href, results.txt_file,
                     html_file, outputdirectory, table2)

        # Boot Information
        folder = "include/serverinfo/boot/"
        for jsonfile in sorted(os.listdir(folder)):

            if jsonfile.endswith(".json"):
                command_output, help_command, command_check, check_message,\
                check_html_message, command, cmd = boot.fire(results.host, fabric_user,
                                                               fabric_passwd, fabric_port, jsonfile, folder)
                print_results(help_command, command_output, command_check,
                              check_message, check_html_message, command, cmd, table2,
                              results.txt_file, html_file, outputdirectory)

                statistics(command_check, href, command)  # Statistics

        for rootfs, subFolders, files in os.walk(folder):
            for sf in subFolders:
                table2.append([(colored(' + ' + sf + '                                ', 'white')), '' + (colored('', 'blue')) + ''])
                folderjson = folder + sf
                for jsonfile in sorted(os.listdir(folderjson)):
                    if jsonfile.endswith(".json"):
                        command_output, help_command, command_check, check_message,\
                        check_html_message, command, cmd = boot.fire(results.host, fabric_user,
                                                                       fabric_passwd, fabric_port, jsonfile, folderjson)
                        print_results(help_command, command_output, command_check,
                                      check_message, check_html_message, command, cmd, table2,
                                      results.txt_file, html_file, outputdirectory)

                        statistics(command_check, href, command)  # Statistics

        htmlend(html_file, outputdirectoryhtml)

        print((tabulate(table2, tablefmt="plain")))  # print out the results
        print((os.linesep))

    #---------------------------------------------------------------------------
    # boot time
    #---------------------------------------------------------------------------
        boot_time = datetime.now()
        boot_duration = format(boot_time - start_time)

################################################################################

    if results.filesystem or results.all:
        href = 'filesystem'
        html_file = file_html_file
        create_blank_html_file(html_file, outputdirectoryhtml, outputdate,
                               cat_menu)
        print_titles('[3] ' + FILESYSTEM, FILESYSTEM_LINE, href,
             results.txt_file, html_file, outputdirectory, table3)

        filesystem.defpath()
        # Filesystem
        folder = "include/serverinfo/filesystem/"
        for jsonfile in sorted(os.listdir(folder)):

            if jsonfile.endswith(".json"):
                command_output, help_command, command_check, check_message,\
                check_html_message, command, cmd = filesystem.fire(results.host, fabric_user,
                                                               fabric_passwd, fabric_port, jsonfile, folder)
                print_results(help_command, command_output, command_check,
                              check_message, check_html_message, command, cmd, table3,
                              results.txt_file, html_file, outputdirectory)

                statistics(command_check, href, command)  # Statistics

        for rootfs, subFolders, files in os.walk(folder):
            for sf in subFolders:
                table3.append([(colored(' + ' + sf + '                                ', 'white')), '' + (colored('', 'blue')) + ''])
                folderjson = folder + sf
                for jsonfile in sorted(os.listdir(folderjson)):
                    if jsonfile.endswith(".json"):
                        command_output, help_command, command_check, check_message,\
                        check_html_message, command, cmd = filesystem.fire(results.host, fabric_user,
                                                                       fabric_passwd, fabric_port, jsonfile, folderjson)
                        print_results(help_command, command_output, command_check,
                                      check_message, check_html_message, command, cmd, table3,
                                      results.txt_file, html_file, outputdirectory)

                        statistics(command_check, href, command)  # Statistics

        htmlend(html_file, outputdirectoryhtml)

        print((tabulate(table3, tablefmt="plain")))  # print out the results
        print((os.linesep))

    #---------------------------------------------------------------------------
    # file time
    #---------------------------------------------------------------------------
        file_time = datetime.now()
        file_duration = format(file_time - start_time)

################################################################################

    if results.tcpip or results.all:
        href = 'tcpip'
        html_file = net_html_file
        create_blank_html_file(html_file, outputdirectoryhtml, outputdate,
                               cat_menu)
        print_titles('[4] ' + TCPIP, TCPIP_LINE, href, results.txt_file,
                     html_file, outputdirectory, table4)

        # TCP/IP
        folder = "include/serverinfo/net/"
        for jsonfile in sorted(os.listdir(folder)):
            if jsonfile.endswith(".json"):
                command_output, help_command, command_check, check_message,\
                check_html_message, command, cmd = tcpip.fire(results.host, fabric_user,
                                                               fabric_passwd, fabric_port, jsonfile, folder)
                print_results(help_command, command_output, command_check,
                              check_message, check_html_message, command, cmd, table4,
                              results.txt_file, html_file, outputdirectory)

                statistics(command_check, href, command)  # Statistics

        for rootfs, subFolders, files in os.walk(folder):
            for sf in subFolders:
                table4.append([(colored(' + ' + sf + '                                ', 'white')), '' + (colored('', 'blue')) + ''])
                folderjson = folder + sf
                for jsonfile in sorted(os.listdir(folderjson)):
                    if jsonfile.endswith(".json"):
                        command_output, help_command, command_check, check_message,\
                        check_html_message, command, cmd = tcpip.fire(results.host, fabric_user,
                                                                       fabric_passwd, fabric_port, jsonfile, folderjson)
                        print_results(help_command, command_output, command_check,
                                      check_message, check_html_message, command, cmd, table4,
                                      results.txt_file, html_file, outputdirectory)

                        statistics(command_check, href, command)  # Statistics

        htmlend(html_file, outputdirectoryhtml)

        print((tabulate(table4, tablefmt="plain")))  # print out the results
        print((os.linesep))

    #---------------------------------------------------------------------------
    # network time
    #---------------------------------------------------------------------------
        network_time = datetime.now()
        network_duration = format(network_time - start_time)


################################################################################

    if results.processes or results.all:
        href = 'processes'
        html_file = proc_html_file
        create_blank_html_file(html_file, outputdirectoryhtml, outputdate,
                               cat_menu)
        print_titles('[5] ' + PROCESSES, PROCESSES_LINE, href,
             results.txt_file, html_file, outputdirectory, table5)



        # PROCESSES
        folder = "include/serverinfo/proc/"
        for jsonfile in sorted(os.listdir(folder)):
            if jsonfile.endswith(".json"):
                command_output, help_command, command_check, check_message,\
                check_html_message, command, cmd = proc.fire(results.host, fabric_user,
                                                            fabric_passwd, fabric_port, jsonfile, folder)
                print_results(help_command, command_output, command_check,
                              check_message, check_html_message, command, cmd, table5,
                              results.txt_file, html_file, outputdirectory)

                statistics(command_check, href, command)  # Statistics

        for rootfs, subFolders, files in os.walk(folder):
            for sf in subFolders:
                table5.append([(colored(' + ' + sf + '                                ', 'white')), '' + (colored('', 'blue')) + ''])
                folderjson = folder + sf
                for jsonfile in sorted(os.listdir(folderjson)):
                    if jsonfile.endswith(".json"):
                        command_output, help_command, command_check, check_message,\
                        check_html_message, command, cmd = proc.fire(results.host, fabric_user,
                                                                       fabric_passwd, fabric_port, jsonfile, folderjson)
                        print_results(help_command, command_output, command_check,
                                      check_message, check_html_message, command, cmd, table5,
                                      results.txt_file, html_file, outputdirectory)

                        statistics(command_check, href, command)  # Statistics

        # psmem Author: P@draigBrady.com
        command_output, help_command, command_check, check_message,\
        check_html_message, command, cmd = ps_mem.ps_mem(
                                         results.host, fabric_user,
                                         fabric_passwd, fabric_port)
        command_output_str = os.linesep
        for psm in command_output:
            command_output_str += psm + os.linesep
        print_results(help_command, command_output_str, command_check,
                      check_message, check_html_message, command, cmd, table5,
                      results.txt_file, html_file, outputdirectory)
        statistics(command_check, href, command)  # Statistics
        # psmem Author: P@draigBrady.com

        htmlend(html_file, outputdirectoryhtml)

        print((tabulate(table5, tablefmt="plain")))  # print out the results
        print((os.linesep))

    #---------------------------------------------------------------------------
    # processes time
    #---------------------------------------------------------------------------
        processes_time = datetime.now()
        processes_duration = format(processes_time - start_time)

################################################################################

    if results.security or results.all:
        href = 'security'
        html_file = sec_html_file
        create_blank_html_file(html_file, outputdirectoryhtml, outputdate,
                               cat_menu)
        print_titles('[6] ' + SECURITY, SECURITY_LINE, href,
                     results.txt_file, html_file, outputdirectory,
                     table6)

        # SECURITY
        folder = "include/serverinfo/security/"
        for jsonfile in sorted(os.listdir(folder)):
            if jsonfile.endswith(".json"):
                command_output, help_command, command_check, check_message,\
                check_html_message, command, cmd = security.fire(results.host, fabric_user,
                                                               fabric_passwd, fabric_port, jsonfile, folder)
                print_results(help_command, command_output, command_check,
                              check_message, check_html_message, command, cmd, table6,
                              results.txt_file, html_file, outputdirectory)

                statistics(command_check, href, command)  # Statistics

        for rootfs, subFolders, files in os.walk(folder):
            for sf in subFolders:
                table6.append([(colored(' + ' + sf + '                                ', 'white')), '' + (colored('', 'blue')) + ''])
                folderjson = folder + sf
                for jsonfile in sorted(os.listdir(folderjson)):
                    if jsonfile.endswith(".json"):
                        command_output, help_command, command_check, check_message,\
                        check_html_message, command, cmd = security.fire(results.host, fabric_user,
                                                                       fabric_passwd, fabric_port, jsonfile, folderjson)
                        print_results(help_command, command_output, command_check,
                                      check_message, check_html_message, command, cmd, table6,
                                      results.txt_file, html_file, outputdirectory)

                        statistics(command_check, href, command)  # Statistics

        print((tabulate(table6, tablefmt="plain")))  # print out the results


    #---------------------------------------------------------------------------
    # Last statistics
    #---------------------------------------------------------------------------


    total, totalsok, totalwarning, totalcritical, totalserror,\
    totalsystem, totalboot, totalfile, totalnet, totalproc,\
    totalsec, consoleoutputreport = statistics("load", "null", "null")
    htmlend(html_file, outputdirectoryhtml)

    #---------------------------------------------------------------------------
    # End time
    #---------------------------------------------------------------------------
    end_time = datetime.now()
    execute_duration = format(end_time - start_time)

################################################################################

    htmlreportstat = {'total': total, 'ok': totalsok, 'warn': totalwarning,
                      'critical': totalcritical, 'error': totalserror,
                      'system': totalsystem, 'boot': totalboot,
                      'file': totalfile, 'net': totalnet, 'proc': totalproc,
                      'sec': totalsec, 'starttime': start_time,
                      'endtime': execute_duration,
                      'ptime': processes_duration, 'ntime': network_duration,
                      'ftime': file_duration, 'btime': boot_duration,
                      'stime': sys_duration}
    #---------------------------------------------------------------------------
    htmldatadashboard(results.html_file, htmlAuditreport, outputdirectoryhtml, htmlreportstat, consoleoutputreport)
    htmllast(results.html_file, outputdirectoryhtml)
    htmldatadashboardjs(results.html_file, outputdirectoryhtml, htmlreportstat)
    #--------------------------------------------------------------------------
    htmldashboardend(results.html_file, outputdirectoryhtml)

    hash224html = outputdirectoryhtml + "/" + results.html_file
    with open(hash224html) as rfile:
        hashhtmlreport = "sha224sum: " + hashlib.sha224(rfile.read()).hexdigest()
    hash224txt = outputdirectorytxt + "/" + results.txt_file
    with open(hash224txt) as rfile:
        hashtxtreport = "sha224sum: " + hashlib.sha224(rfile.read()).hexdigest()

    log.create_log('[7] ' + REPORTS, REPORTS_LINE, hashhtmlreport,
                   hashtxtreport, outputdirectory, results.html_file,
                   results.txt_file, 'audit_mesc.log', outputdate, results.host)

    #---------------------------------------------------------------------------
    # The End
    #---------------------------------------------------------------------------

    sys.exit(0)


#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
