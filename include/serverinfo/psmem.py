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

# BASED ON THE P@draigBrady.com script:
"""
# Try to determine how much RAM is currently being used per program.
# Note the per program, not per process. So for example this script
# will report mem used by all httpd process together. In detail it reports:
# sum(all RSS for process instances) + max(shared mem for any process instance)
#
# The shared calculation below will factor out shared text and
# libs etc. within a program, but not between programs. So there
# will always be some overestimation. This will be the same for
# all processes that just use libc for e.g. but more for others
# that use larger shared libs like gnome, kde etc.


# Author: P@draigBrady.com

# V1.0      06 Jul 2005    Initial release
# V1.1      11 Aug 2006    root permission required for accuracy
# V1.2      08 Nov 2006    Add total to output
#                          Use KiB,MiB,... for units rather than K,M,...
# V1.3      22 Nov 2006    Ignore shared col from /proc/$pid/statm for
#                          2.6 kernels up to and including 2.6.9.
#                          There it represented the total file backed extent
# V1.4      23 Nov 2006    Remove total from output as it's meaningless
#                          (the shared values overlap with other programs).
#                          Display the shared column. This extra info is
#                          useful, especially as it overlaps between programs.
# V1.5      26 Mar 2007    Remove redundant recursion from human()
# V1.6      05 Jun 2007    Also report number of processes with a given name.
#                          Patch from riccardo.murri@gmail.com

# Notes:
#
# All interpreted programs where the interpreter is started
# by the shell or with env, will be merged to the interpreter
# (as that's what's given to exec). For e.g. all python programs
# starting with "#!/usr/bin/env python" will be grouped under python.
# You can change this by changing comm= to args= below but that will
# have the undesirable affect of splitting up programs started with
# differing parameters (for e.g. mingetty tty[1-6]).
#
# For 2.6 kernels up to and including 2.6.13 and later 2.4 redhat kernels
# (rmap vm without smaps) it can not be accurately determined how many pages
# are shared between processes in general or within a program in our case:
# http://lkml.org/lkml/2005/7/6/250
# A warning is printed if overestimation is possible.
# In addition for 2.6 kernels up to 2.6.9 inclusive, the shared
# value in /proc/$pid/statm is the total file-backed extent of a process.
# We ignore that, introducing more overestimation, again printing a warning.
#
# I don't take account of memory allocated for a program
# by other programs. For e.g. memory used in the X server for
# a program could be determined, but is not.
#
# This script assumes threads are already merged by ps

# TODO:
#
# use ps just to enumerate the pids and names
# so as to remove the race between reading rss and shared values
"""
#------------------------------------------------------------------------------
# Modules
#------------------------------------------------------------------------------
import os
import string
import sys

PAGESIZE=os.sysconf("SC_PAGE_SIZE")/1024 #KiB
our_pid=os.getpid()


def ps_mem():
    cmds={}
    shareds={}
    count={}
    for line in os.popen("ps -e -o rss=,pid=,comm=").readlines():
        size, pid, cmd = map(string.strip,line.strip().split(None,2))
        if int(pid) == our_pid:
            continue #no point counting this process
        try:
            shared=getShared(pid)
        except:
            continue #ps gone away
        if shareds.get(cmd):
            if shareds[cmd] < shared:
                shareds[cmd]=shared
        else:
            shareds[cmd]=shared
        #Note shared is always a subset of rss (trs is not always)
        cmds[cmd]=cmds.setdefault(cmd,0)+int(size)-shared
        if count.has_key(cmd):
          count[cmd] += 1
        else:
          count[cmd] = 1

    #Add max shared mem for each program
    for cmd in cmds.keys():
        cmds[cmd]=cmds[cmd]+shareds[cmd]

    sort_list = cmds.items()
    sort_list.sort(lambda x,y:cmp(x[1],y[1]))
    sort_list=filter(lambda x:x[1],sort_list) #get rid of zero sized processes (kernel threads)

    i=0
    output=[]
    output.append("Private   +  Shared   =  RAM used          Program")
    for cmd in sort_list:
        txtoutput = "%8sB + %8sB = %8sB\t%s" % (human(cmd[1]-shareds[cmd[0]]), human(shareds[cmd[0]]), human(cmd[1]),
                                          cmd_with_count(cmd[0], count[cmd[0]]))
        output.append(txtoutput)
        i=i+1
        #print "%8sB + %8sB = %8sB\t%s" % (human(cmd[1]-shareds[cmd[0]]), human(shareds[cmd[0]]), human(cmd[1]),
                                          #cmd_with_count(cmd[0], count[cmd[0]]))
    output.append("Private   +  Shared   =  RAM used          Program")
    return output


#The following matches "du -h" output
#see also human.py
def human(num, power="Ki"):
    powers=["Ki","Mi","Gi","Ti"]
    while num >= 1000: #4 digits
        num /= 1024.0
        power=powers[powers.index(power)+1]
    return "%.1f %s" % (num,power)

def cmd_with_count(cmd, count):
    if count>1:
      return "%s (%u)" % (cmd, count)
    else:
      return cmd


#(major,minor,release)
def kernel_ver():
    kv=open("/proc/sys/kernel/osrelease").readline().split(".")[:3]
    for char in "-_":
        kv[2]=kv[2].split(char)[0]
    return (int(kv[0]), int(kv[1]), int(kv[2]))


def getShared(pid):
    kv = kernel_ver()
    if os.path.exists("/proc/"+str(pid)+"/smaps"):
        shared_lines=[line
                      for line in open("/proc/"+str(pid)+"/smaps").readlines()
                      if line.find("Shared")!=-1]
        return sum([int(line.split()[1]) for line in shared_lines])
    elif (2,6,1) <= kv <= (2,6,9):
        return 0 #lots of overestimation, but what can we do?
    else:
        return int(open("/proc/"+str(pid)+"/statm").readline().split()[2])*PAGESIZE





