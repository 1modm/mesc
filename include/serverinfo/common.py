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
import platform
import sys
import socket
import struct
import fcntl
import re
from thirdparty.color.termcolor import colored
from platform import system
from netifaces import interfaces, ifaddresses, AF_INET
from fabric.api import settings
from fabric.operations import run


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


#------------------------------------------------------------------------------
# From bits/ioctls.h
SIOCGIFHWADDR  = 0x8927          # Get hardware address
SIOCGIFADDR    = 0x8915          # get PA address
SIOCGIFNETMASK = 0x891b          # get network PA mask
SIOCGIFNAME    = 0x8910          # get iface name
SIOCSIFLINK    = 0x8911          # set iface channel
SIOCGIFCONF    = 0x8912          # get iface list
SIOCGIFFLAGS   = 0x8913          # get flags
SIOCSIFFLAGS   = 0x8914          # set flags
SIOCGIFINDEX   = 0x8933          # name -> if_index mapping
SIOCGIFCOUNT   = 0x8938          # get number of devices
SIOCGSTAMP     = 0x8906          # get packet timestamp (as a timeval)
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

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        #ifreq = ioctl(s, SIOCGIFADDR,struct.pack("16s16x",iff))
        ifreq = fcntl.ioctl(s.fileno(), SIOCGIFADDR, struct.pack('256s', ifname[:15]))
    except IOError: # interface is present in routing tables but does not have any assigned IP
        ifaddr="0.0.0.0"
    else:
        addrfamily = struct.unpack("h",ifreq[16:18])[0]
        if addrfamily == socket.AF_INET:
            ifaddr = socket.inet_ntoa(fcntl.ioctl(s.fileno(),SIOCGIFADDR, struct.pack('256s', ifname[:15]))[20:24])
        else:
            warning("Interface %s: unkown address family (%i)"%(ifname, addrfamily))
            #continue
    return ifaddr

def ip4_addresses():
      ip_list = []
      for interface in interfaces():
        #print interface
        #if interface == 'wlan0':
        #    print "ERROR Interface sin IP"
        #else:
        #    for link in ifaddresses(interface)[AF_INET]:
        #        ip_list.append(link['addr'])
        addr = get_ip_address(interface)
        if addr is not None:
                ip_list.append(addr)
      return ip_list


#------------------------------------------------------------------------------
def execute_cmd(cmd, host, user_fabric, passwd_fabric, port_fabric):

    if host == 'localhost':
       #print "%s  es una ip local" % host
       __cmd_local__ = True
    elif host not in ip4_addresses():
       #print "%s no es una ip local --> SSH" % host
       #__status__, __output_cmd__ = execute(do_something(cmd), hosts=[host])
       __cmd_local__ = False
    else:
       #print "%s  es una ip local" % host
       __cmd_local__ = True
       #execute(do_something, hosts=[host])

    __output_cmd__ = cmd
    __command_check__ = CHECKRESULTERROR

    if __cmd_local__ == True:
        __status__, __output_cmd__ = commands.getstatusoutput(cmd)
        #__status__, __output_cmd__ = subprocess.getstatusoutput(cmd)
        __exit_code__ = __status__ >> 8
        __signal_num__ = __status__ % 256
        #print 'Status: x%04x' % __status__
        __status__ ='x%04x' % __status__
        #print 'Signal: x%02x (%d)' % (__signal_num__, __signal_num__)
        #print 'Exit  : x%02x (%d)' % (__exit_code__, __exit_code__)
        #print __status__, __signal_num__, __exit_code__
        if __exit_code__ == 0 and __signal_num__ == 0 and __status__ == 'x0000':
            __command_check__ = CHECKRESULTOK
        elif __exit_code__ == 1 and __signal_num__ == 0 and __status__ == 'x0100':
            __command_check__ = CHECKRESULTWARNING
        else:
            __command_check__ = CHECKRESULTERROR
    elif __cmd_local__ == False:
        #with settings(host_string=host,user="root",password="miguel"):
        with settings(host_string=host,user=user_fabric, password=passwd_fabric, port=port_fabric):
            #print run(cmd,shell=True,warn_only=True, quiet=True)
            try:
                __output_cmd__ = run(cmd,shell=True,warn_only=True, quiet=True)
                if __output_cmd__.failed:
                    __command_check__ = CHECKRESULTERROR
                else:
                    __command_check__ = CHECKRESULTOK
            except:
                print((colored('*** Warning *** Host {host} on port {port} is down.', 'red')).format(host=host, port=port_fabric) + os.linesep*2)
                sys.exit(0)
    return (__output_cmd__, __command_check__)

#------------------------------------------------------------------------------

def OS_ver(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Operating System Version"
    __cmd__= "uname -o"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__={'Operating System Version':__output__}
    __OSout__=__osreport__['Operating System Version']
    return (__OSout__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)


def OS_kernel(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Kernel Name"
    __cmd__= "uname -s"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__={'Kernel Name':__output__}
    __OSout__=__osreport__['Kernel Name']
    return (__OSout__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)


def OS_kernelver(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Kernel Version"
    __cmd__= "uname -r"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__={'Kernel Version':__output__}
    __OSout__=__osreport__['Kernel Version']
    return (__OSout__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)


def OS_machine(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Machine"
    __cmd__= "uname -m"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__={'Machine':__output__}
    __OSout__=__osreport__['Machine']
    return (__OSout__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)

def OS_processor(__host__, __user__, __passwd__, __port__):
    __osreport__ = {}
    __help_result__ = '' + os.linesep
    __command__ = "Processor"
    __cmd__= "uname -p"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    __osreport__={'Processor':__output__}
    __OSout__=__osreport__['Processor']
    return (__OSout__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)

#------------------------------------------------------------------------------

def auditor_info():
    __htmlreport__ = {}
    __dist__ ="%s %s %s" % (str(platform.linux_distribution()[0]), str(platform.linux_distribution()[1]), str(platform.linux_distribution()[2]))
    __htmlreport__={'System':platform.system(), 'Distribution':__dist__, 'Architecture':platform.machine(), 'Processor':platform.processor(), 'Platform':platform.platform(),'Release':platform.release(),'Hostname':os.uname()[1],'Python version':sys.version}

    if platform.system() == 'Linux':
        __output__ =' - ' + "System: %s" % platform.system() + os.linesep
        __output__ +=' - ' + "Distribution: %s %s %s" % (str(platform.linux_distribution()[0]), str(platform.linux_distribution()[1]), str(platform.linux_distribution()[2]))  + os.linesep
        __output__ +=' - ' + "Architecture: %s" % platform.machine() + os.linesep
        __output__ +=' - ' + "Processor: %s" % platform.processor() + os.linesep
        __output__ +=' - ' + "Platform: %s" % platform.platform() + os.linesep
        __output__ +=' - ' + "Release: %s" % platform.release() + os.linesep
        __output__ +=' - ' + "Hostname: %s" % os.uname()[1] + os.linesep
    elif platform.system() == 'Windows':
        __output__ +=' - ' + "System: %s" % platform.system() + os.linesep
    elif platform.system() == 'Darwin':
        __output__ +=' - ' + "Mac: %s" % platform.mac_ver() + os.linesep
    elif platform.system() == 'FreeBSD':
        __output__ +=' - ' + "System: %s" % platform.system() + os.linesep
    __output__ +=' - ' + "Python version: %s" % sys.version.split('\n') + os.linesep
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
    __cmd__= "uptime"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)

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
    __cmd__= "free -o"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)

    if __command_check__ == CHECKRESULTOK:
        pattern = re.compile(r'\s+')
        sentence = re.sub(pattern, ' ', __output__)
        sentence = sentence.lstrip(' ')
        split_text=sentence.split(' ')
        total=split_text[7]
        used=split_text[8]
        freemem=split_text[9]
        sharedmem=split_text[10]
        buffers=split_text[11]
        cached=split_text[12]
        swap_total=split_text[14]
        swap_used=split_text[15]
        swap_free=split_text[16]
        percentage_used = (int(used)*100)/(int(total));
        percentage_swap_used = (int(swap_used)*100)/(int(swap_total));
        __check_message__ = ''
        __check_html_message__ = ''
        if (percentage_used < RESULTOKTHRESHOLD):
            __check_message__ = 'RAM memory used: ' + str(percentage_used) + '%'+ os.linesep
        elif (percentage_used < RESULTWARNINGTHRESHOLD ):
            __command_check__= CHECKRESULTWARNING
            __check_message__ = os.linesep + '   - Release memory '
            __check_message__ += os.linesep + '   - RAM memory used: ' + str(percentage_used) + '%' + ' | Swap memory used: ' + str(percentage_swap_used) + '%'
            __check_message__ += os.linesep + '   - Total Memory: ' + str(total) + ' Kbytes ' + ' - ' + 'Free Memory: ' + str(freemem) + ' Kbytes'
            __check_html_message__ = 'Release memory'
            __check_html_message__ += '<br> RAM memory used: ' + str(percentage_used) + '%' + ' | Swap memory used: ' + str(percentage_swap_used) + '%'
            __check_html_message__ += '<br> Total Memory: ' + str(total) + ' Kbytes ' + ' - ' + 'Free Memory: ' + str(freemem) + ' Kbytes'
        else:
            __command_check__ = CHECKRESULTCRITICAL
            __check_message__ = os.linesep + '   - Release memory '
            __check_message__ += os.linesep + '   - RAM memory used: ' + str(percentage_used) + '%' + ' | Swap memory used: ' + str(percentage_swap_used) + '%'
            __check_message__ += os.linesep + '   - Total Memory: ' + str(total) + ' Kbytes ' + ' - ' + 'Free Memory: ' + str(freemem) + ' Kbytes'
            __check_html_message__ = 'Release memory'
            __check_html_message__ += '<br> RAM memory used: ' + str(percentage_used) + '%' + ' | Swap memory used: ' + str(percentage_swap_used) + '%'
            __check_html_message__ += '<br> Total Memory: ' + str(total) + ' Kbytes ' + ' - ' + 'Free Memory: ' + str(freemem) + ' Kbytes'

    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)

#------------------------------------------------------------------------------


def who(__host__, __user__, __passwd__, __port__):
    """
    :returns: w command.
    :param host: Target.
    """
    __help_result__ = 'Show who is logged on and what they are doing'
    __help_result__ += os.linesep
    __command__ = "Users logged"
    __cmd__= "w"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)

#------------------------------------------------------------------------------


def tail_root(__host__, __user__, __passwd__, __port__):
    """
    :returns: tail_root command.
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = "Last 100 root commands executed"
    __cmd__= "tail -100 /root/.bash_history"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command, you must be root'
        __check_html_message__ = 'Unable to execute the command, you must be root'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = 'Unable to execute the command, you must be root'
        __check_html_message__ = 'Unable to execute the command, you must be root'
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)

#------------------------------------------------------------------------------


def last(__host__, __user__, __passwd__, __port__):
    """
    :returns: last command.
    :param host: Target.
    """
    __help_result__ = 'Show listing of last logged in users'
    __help_result__ += os.linesep
    __command__ = 'Last logged in users'
    __cmd__= "last"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)


#------------------------------------------------------------------------------


def shells(__host__, __user__, __passwd__, __port__):
    """
    :returns: active shells
    :param host: Target.
    """
    __help_result__ = ''
    __help_result__ += os.linesep
    __command__ = 'Active users in the system with an active shell'
    __cmd__= "cat /etc/passwd | grep -v \/false | grep -v \/nologin | grep -v \/shutdown | grep -v \/halt | grep -v \/sync | grep -v \/news"
    __output__, __command_check__ = execute_cmd(__cmd__, __host__, __user__, __passwd__, __port__)
    if __command_check__ == CHECKRESULTOK:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTERROR:
        __check_message__ = 'Unable to execute the command'
        __check_html_message__ = 'Unable to execute the command'
    elif __command_check__ == CHECKRESULTWARNING:
        __check_message__ = ''
        __check_html_message__ = ''
    elif __command_check__ == CHECKRESULTCRITICAL:
        __check_message__ = ''
        __check_html_message__ = ''
    return (__output__, __help_result__, __command_check__, __check_message__, __check_html_message__ , __command__,__cmd__)