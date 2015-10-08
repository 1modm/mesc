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
VALUETOK = 3
VALUEWARNING = 5
VALUECRITICAL = 7
#------------------------------------------------------------------------------