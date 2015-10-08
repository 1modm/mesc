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
import commands
import sys
import socket
import struct
import fcntl
import re
from .import config
from thirdparty.color.termcolor import colored
from netifaces import interfaces
from fabric.api import settings
from fabric.operations import run
from fabric.contrib.files import exists, contains


__all__ = [
    "execute_cmd",
    "check_file",
    "check_file_exact",
    "exists_file",
    "exists_read_file",
    "ip4_addresses",
    "OS_dist"
]

#------------------------------------------------------------------------------


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        #ifreq = ioctl(s, SIOCGIFADDR,struct.pack("16s16x",iff))
        ifreq = fcntl.ioctl(s.fileno(), config.SIOCGIFADDR, struct.pack('256s',
         ifname[:15]))
    except IOError:  # interface present in routing tables but doesn't have any assigned IP
        ifaddr = "0.0.0.0"
    else:
        addrfamily = struct.unpack("h", ifreq[16:18])[0]
        if addrfamily == socket.AF_INET:
            ifaddr = socket.inet_ntoa(fcntl.ioctl(s.fileno(),
            config.SIOCGIFADDR, struct.pack('256s', ifname[:15]))[20:24])
        else:
            warning("Interface %s: unkown address family (%i)" % (ifname, addrfamily))
            #continue
    return ifaddr

#------------------------------------------------------------------------------


def ip4_addresses():
    ip_list = []
    for interface in interfaces():
        #print interface
        #if interface == 'wlan0':
        #    print "ERROR Interface without IP"
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
        #print "%s local IP" % host
        __cmd_local__ = True
    elif host not in ip4_addresses():
        #print "%s NOT local IP --> SSH" % host
        #__status__, __output_cmd__ = execute(do_something(cmd), hosts=[host])
        __cmd_local__ = False
    else:
        #print "%s local IP" % host
        __cmd_local__ = True
    __output_cmd__ = cmd
    __command_check__ = config.CHECKRESULTERROR

    if __cmd_local__ is True:
        __status__, __output_cmd__ = commands.getstatusoutput(cmd)
        #__status__, __output_cmd__ = subprocess.getstatusoutput(cmd)
        __exit_code__ = __status__ >> 8
        __signal_num__ = __status__ % 256
        #print 'Status: x%04x' % __status__
        __status__ = 'x%04x' % __status__
        #print 'Signal: x%02x (%d)' % (__signal_num__, __signal_num__)
        #print 'Exit  : x%02x (%d)' % (__exit_code__, __exit_code__)
        #print __status__, __signal_num__, __exit_code__
        if __exit_code__ == 0 and __signal_num__ == 0 and __status__ == 'x0000':
            __command_check__ = config.CHECKRESULTOK
        elif __exit_code__ == 1 and __signal_num__ == 0 and __status__ == 'x0100':
            __command_check__ = config.CHECKRESULTWARNING
        else:
            __command_check__ = config.CHECKRESULTERROR
    elif __cmd_local__ is False:
        with settings(host_string=host, user=user_fabric,
                                            password=passwd_fabric,
                                            port=port_fabric):
            try:
                __output_cmd__ = run(cmd,shell=True,warn_only=True, quiet=True)
                if __output_cmd__.failed:
                    __command_check__ = config.CHECKRESULTERROR
                else:
                    __command_check__ = config.CHECKRESULTOK
            except:
                print((colored('*** Warning *** Host {host} on port {port} is down.', 'red')).format(host=host, port=port_fabric) + os.linesep*2)
                sys.exit(0)
    return (__output_cmd__, __command_check__)

#------------------------------------------------------------------------------


def check_file(filecheck, check, host, user_fabric, passwd_fabric, port_fabric):

    if host == 'localhost':
        __cmd_local__ = True
    elif host not in ip4_addresses():
        __cmd_local__ = False
    else:
        __cmd_local__ = True

    __file__ = filecheck
    __command_check__ = config.CHECKRESULTERROR
    __okline__ = os.linesep
    __oklinehtml__ = '<br>'
    __check_count__ = 0

    if __cmd_local__ is True:
        if (os.path.isfile(__file__)):
            __command_check__ = config.CHECKRESULTWARNING
            f = open(__file__, 'r')
            out = f.readlines()
            for line in out:
                if line.startswith('#'):
                    __command_check__ = config.CHECKRESULTWARNING
                else:
                    for c in check:
                        if c in line:
                            __check_count__ += 1
                            __okline__ += line
                            __oklinehtml__ += line + '<br>'
        if __check_count__ > 0:
            __command_check__ = config.CHECKRESULTOK
        else:
            __command_check__ = config.CHECKRESULTWARNING
    elif __cmd_local__ is False:
        with settings(host_string=host, user=user_fabric,
                      password=passwd_fabric, port=port_fabric):
            try:
                if (exists(__file__, use_sudo=False, verbose=False)):
                    for c in check:
                        __output_cmd__ = contains(__file__, c, exact=False,
                                                  use_sudo=False)
                        if __output_cmd__ is True:
                            __command_check__ = config.CHECKRESULTOK
                            __okline__ += c
                            __oklinehtml__ += c + '<br>'
                        else:
                            __command_check__ = config.CHECKRESULTWARNING
                else:
                    __command_check__ = config.CHECKRESULTERROR

            except:
                print((colored('*** Warning *** Host {host} on port {port} is down or file can not be read.', 'red')).format(host=host, port=port_fabric) + os.linesep*2)
                sys.exit(0)
    return (__command_check__, __okline__, __oklinehtml__, __check_count__)

#------------------------------------------------------------------------------


def exact_Match(phrase, word):
    b = r'(\s|^|$)'
    res = re.match(b + word + b, phrase, flags=re.IGNORECASE)
    return bool(res)


def check_file_exact(filecheck, check, host, user_fabric, passwd_fabric,
                     port_fabric):

    if host == 'localhost':
        __cmd_local__ = True
    elif host not in ip4_addresses():
        __cmd_local__ = False
    else:
        __cmd_local__ = True

    __file__ = filecheck
    __command_check__ = config.CHECKRESULTERROR
    __okline__ = os.linesep
    __oklinehtml__ = '<br>'
    __check_count__ = 0

    if __cmd_local__ is True:
        if (os.path.isfile(__file__)):
            __command_check__ = config.CHECKRESULTWARNING
            f = open(__file__, 'r')
            out = f.readlines()
            for line in out:
                if line.startswith('#'):
                    __command_check__ = config.CHECKRESULTWARNING
                else:
                    for c in check:
                        if (exact_Match(line, c)):
                            __check_count__ += 1
                            __okline__ += line
                            __oklinehtml__ += line + '<br>'
        if __check_count__ > 0:
            __command_check__ = config.CHECKRESULTOK
        else:
            __command_check__ = config.CHECKRESULTWARNING
    elif __cmd_local__ is False:
        with settings(host_string=host, user=user_fabric,
                      password=passwd_fabric, port=port_fabric):
            try:
                if (exists(__file__, use_sudo=False, verbose=False)):
                    for c in check:
                        __output_cmd__ = contains(__file__, c, exact=True,
                                                  use_sudo=False)
                        if __output_cmd__ is True:
                            __command_check__ = config.CHECKRESULTOK
                            __okline__ += c
                            __oklinehtml__ += c + '<br>'
                        else:
                            __command_check__ = config.CHECKRESULTWARNING
                else:
                    __command_check__ = config.CHECKRESULTERROR

            except:
                print((colored('*** Warning *** Host {host} on port {port} is down or file can not be read.', 'red')).format(host=host, port=port_fabric) + os.linesep*2)
                sys.exit(0)
    return (__command_check__, __okline__, __oklinehtml__, __check_count__)

#------------------------------------------------------------------------------


def exists_file(filecheck, host, user_fabric, passwd_fabric, port_fabric):
    if host == 'localhost':
        __cmd_local__ = True
    elif host not in ip4_addresses():
        __cmd_local__ = False
    else:
        __cmd_local__ = True

    __file__ = filecheck
    __command_check__ = False
    if __cmd_local__ is True:
        if (os.path.isfile(__file__)):
            __command_check__ = True
        else:
            __command_check__ = False
    elif __cmd_local__ is False:
        with settings(host_string=host, user=user_fabric,
             password=passwd_fabric, port=port_fabric):
            try:
                if (exists(__file__, use_sudo=False, verbose=False)):
                    __command_check__ = True
                else:
                    __command_check__ = False
            except:
                print((colored('*** Warning *** Host {host} on port {port} is down or file can not be read.', 'red')).format(host=host, port=port_fabric) + os.linesep*2)
                sys.exit(0)
    return (__command_check__)

#------------------------------------------------------------------------------


def exists_read_file(filecheck, host, user_fabric, passwd_fabric, port_fabric):
    if host == 'localhost':
        __cmd_local__ = True
    elif host not in ip4_addresses():
        __cmd_local__ = False
    else:
        __cmd_local__ = True
    __file__ = filecheck
    __command_check__ = False
    __out__ = ''

    if __cmd_local__ is True:
        if (os.path.isfile(__file__)):
            __command_check__ = True
            __f__ = open(__file__, 'r')
            __out__ = __f__.read()
        else:
            __command_check__ = False
    elif __cmd_local__ is False:
        with settings(host_string=host, user=user_fabric,
             password=passwd_fabric, port=port_fabric):
            try:
                if (exists(__file__, use_sudo=False, verbose=False)):
                    __cmd__ = 'cat ' + __file__
                    __out__ = run(__cmd__, shell=True, warn_only=True,
                         quiet=True)
                    __command_check__ = True
                else:
                    __command_check__ = False
            except:
                print((colored('*** Warning *** Host {host} on port {port} is down or file can not be read.', 'red')).format(host=host, port=port_fabric) + os.linesep*2)
                sys.exit(0)
    return (__command_check__, __out__)

#------------------------------------------------------------------------------


def OS_dist(host, user_fabric, passwd_fabric, port_fabric):
    RedHat = '/etc/redhat-release'
    SuSE = '/etc/SuSE-release'
    mandrake = '/etc/mandrake-release'
    debian = '/etc/debian_version'

    if (exists_file(RedHat, host, user_fabric, passwd_fabric, port_fabric)):
        __dist__ = "RedHat"
    elif (exists_file(SuSE, host, user_fabric, passwd_fabric, port_fabric)):
        __dist__ = "SuSE"
    elif (exists_file(debian, host, user_fabric, passwd_fabric, port_fabric)):
        __dist__ = "debian"
    elif (exists_file(mandrake, host, user_fabric, passwd_fabric, port_fabric)):
        __dist__ = "mandrake"
    else:
        __dist__ = "debian"

    return (__dist__)

#------------------------------------------------------------------------------