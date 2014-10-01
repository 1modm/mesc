Minimun Essential Security Checks
==================================

What's MESC?
------------

MESC is an open source tool for security testing and auditing systems.
Performing simple checks and tests into the localhost or remote host through ssh.


License
=======

```
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
```

Installation
============
MESC doesn't require installation, only are needed the dependencies mentioned below.

Dependencies
------------

* 2.7 < Python < 3.0
* python tabulate module # pip install tabulate
* python datetime module
* python argparse module
* python sys module
* python platform module
* python socket module
* python os module
* python struct module
* python fcntl module
* python re module
* python commands module
* python fabric module


Usage
=====
For localhost
-------------

```
python mesc.py -a -txt output.txt -html output.html localhost
```

For remote host
----------------
```
python mesc.py -a -txt output.txt -html output.html -u root -P 22 www.remoteserver.com
```

Help
----

```
# python mesc.py -h

#-----------------------------------------------#
| MESC 0.1 - Minimun Essential Security Checks. |
| Contact: https://twitter.com/1_mod_m/         |
|                                               |
| https://github.com/1modm/mesc                 |
#-----------------------------------------------#

usage: python mesc.py [OPTIONS] HOST

Example: python mesc.py -a -txt output.txt -html output.html localhost

positional arguments:
  host

optional arguments:
  -h, --help          show this help message and exit
  -v, --version       show program's version number and exit
  -a, --all           Set all options to true
  -txt TXT_FILE       txt file name where is writen the results
  -html HTML_FILE     html file name where is writen the results
  -u USER             Remote user
  -p PASSWD           Remote user password
  -P PORT             Remote port

Check Sections:
  -g, --general       General system information
  -b, --boot          Boot Information
  -f, --filesystem    File System Information
  -t, --tcpip         TCP/IP Information
  -proc, --processes  Processes running in the system
  -s, --security      Security Information
```


Output
======
- Text report
- HTML report

![MESC](https://dl.dropboxusercontent.com/u/5741635/mesc.png "MESC Output")