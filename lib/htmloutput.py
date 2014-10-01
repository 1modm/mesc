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
from datetime import date
import shutil
from thirdparty.color.termcolor import colored

__all__ = [
    "create_html_file",
    "htmlreport",
    "htmlinfo",
    "htmlend",
    "htmltile"
]


CHECKRESULTOK = 'CHECKED'
CHECKRESULTWARNING = 'WARNING'
CHECKRESULTCRITICAL = 'CRITICAL'
CHECKRESULTERROR = 'ERROR'

#------------------------------------------------------------------------------
def create_html_file(file_name, outputdir):

    # Copy css and js
    cssoutput = outputdir+'/css'
    jsoutput = outputdir+'/js'

    shutil.copy2('lib/html/bootstrap.css', cssoutput)
    shutil.copy2('lib/html/bootstrap.min.css', cssoutput)
    shutil.copy2('lib/html/bootswatch.less', cssoutput)
    shutil.copy2('lib/html/html5shiv.js', jsoutput)
    shutil.copy2('lib/html/respond.min.js', jsoutput)
    shutil.copy2('lib/html/variables.less', cssoutput)
    shutil.copy2('lib/html/jquery-1.10.2.min.js', jsoutput)
    shutil.copy2('lib/html/bootswatch.js', jsoutput)
    shutil.copy2('lib/html/bootstrap.min.js', jsoutput)


    __title__ = date.today()
    __file__ = outputdir +'/'+file_name
    __htmFile__ = open(__file__, 'w')
    __htmFile__.write(head(__title__))
    __htmFile__.close
    #print((colored('Report created in the file ' + __file__ + os.linesep, 'yellow')))


#------------------------------------------------------------------------------
def htmlaudit(file_name, html_report, outputdir):
    __title__ = date.today()
    __file__ = outputdir +'/'+file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(body(html_report))
    __htmFile__.close

def htmltitle(file_name, outputdirectory, title, href):
    __file__ = outputdirectory +'/'+file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodytitle(title, href))
    __htmFile__.close

def htmlinfo(file_name, outputdirectory, helpcommand, commandoutput, commandcheck, checkmessage, command, cmdresults):
    __file__ = outputdirectory +'/'+file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfo(helpcommand, commandoutput, commandcheck, checkmessage, command, cmdresults))
    __htmFile__.close

def htmlend(file_name, outputdirectory):
    __file__ = outputdirectory +'/'+file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyend())
    __htmFile__.close


#------------------------------------------------------------------------------


def bodytitle(title, href):
    __title__=("""<a name="%s"></a><br><br>
    <div class="row">
        <div class="col-lg-12">
              <h3>%s</h3>
        </div>
    </div>
    <br>
    """) % (href, title)

    return (__title__)


#------------------------------------------------------------------------------

def bodyinfo(helpcommand, commandoutput, commandcheck, checkmessage, command, cmdresults):

    if commandcheck == CHECKRESULTOK:
        __bodyinfo__=("""
            <div class="row">
              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      <h4 class="panel-title">%s: %s</h4>
                    </div>
                    <div class="panel panel-success">
                        <div class="panel-heading">
                          <h4 class="panel-title">%s: # %s</h4>
                          <br>
                          <h4 class="panel-title">%s</h4>
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>
          </div>
        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage, commandoutput)

    elif commandcheck == CHECKRESULTERROR :
        __bodyinfo__=("""
            <div class="row">
              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      <h4 class="panel-title">%s: %s</h4>
                    </div>
                    <div class="panel panel-danger">
                        <div class="panel-heading">
                          <h4 class="panel-title">%s: # %s</h4>
                          <br>
                          <h4 class="panel-title">Issue: %s</h4>
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>
          </div>
        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage, commandoutput)

    elif commandcheck == CHECKRESULTWARNING :
        __bodyinfo__=("""
            <div class="row">
              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      <h4 class="panel-title">%s: %s</h4>
                    </div>
                    <div class="panel panel-warning">
                        <div class="panel-heading">
                          <h4 class="panel-title">%s: # %s</h4>
                          <br>
                          <h4 class="panel-title">Issue: %s</h4>
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>
          </div>
        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage, commandoutput)


    elif commandcheck == CHECKRESULTCRITICAL :
        __bodyinfo__=("""
            <div class="row">
              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      <h4 class="panel-title">%s: %s</h4>
                    </div>
                    <div class="panel panel-danger">
                        <div class="panel-heading">
                          <h4 class="panel-title">%s: # %s</h4>
                          <br>
                          <h4 class="panel-title">Issue: %s</h4>
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>
          </div>
        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage, commandoutput)

    return (__bodyinfo__)



#------------------------------------------------------------------------------


def head(title):

    __head__=("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>%s</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="./css/bootstrap.css" media="screen">
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="./js/html5shiv.js"></script>
      <script src="./js/respond.min.js"></script>
    <![endif]-->
  </head>
    """) % title

    return (__head__)


def body(htmldatareport):

    __body__=("""<body>
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a href="www.educawol.com" class="navbar-brand">MICCCC</a> <!-- CAMBIAR -->
          <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar-main">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="navbar-collapse collapse" id="navbar-main">
          <ul class="nav navbar-nav">
            <li >
              <a href="#general">General System Information</a>
            </li>
            <li>
              <a href="#boot">Boot</a>
            </li>
            <li>
              <a href="#filesystem">File system</a>
            </li>
            <li>
              <a href="#tcpip">TCP/IP</a>
            </li>
            <li>
              <a href="#processes">Processes</a>
            </li>
            <li>
              <a href="#security">Security</a>
            </li>
          </ul>

          <ul class="nav navbar-nav navbar-right">
            <li><a href="http://builtwithbootstrap.com/" target="_blank">Enlace repositorio!!!!!</a></li>

          </ul>

        </div>
      </div>
    </div>


    <div class="container">

      <div class="page-header" id="banner">
        <div class="row">
          <div class="col-lg-12 col-md-7 col-sm-6">
            <h1>Auditor device: %s</h1> <!-- Hostname -->
            <p class="lead">%s</p>

            <table class="table table-striped table-hover ">
              <tbody>
                <tr>
                  <td>Python version</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>System</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Distribution</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Architecture</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Processor</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Platform</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Release</td>
                  <td>%s</td>
                </tr>
                <tr>
                  <td>Hostname</td>
                  <td>%s</td>
                </tr>
              </tbody>
            </table>

          </div>
        </div>
      </div>

    """) % (htmldatareport['Hostname'], htmldatareport['Distribution'], htmldatareport['Python version'], htmldatareport['System'], htmldatareport['Distribution'], htmldatareport['Architecture'], htmldatareport['Processor'], htmldatareport['Platform'], htmldatareport['Release'], htmldatareport['Hostname'])

    return (__body__)



def bodyend():

    __bodyend__=("""
      <footer>
        <div class="row">
          <div class="col-lg-12">

            <ul class="list-unstyled">
              <li class="pull-right"><a href="#top">Back to top</a></li>
              <li><a href="https://github.com/thomaspark/bootswatch/">GitHub</a></li>
              <li><a href="../help/#api">API</a></li>
              <li><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=F22JEM3Q78JC2">Donate</a></li>
            </ul>
            <p>Made by <a href="http://thomaspark.me" rel="nofollow">Thomas Park</a>. Contact him at <a href="mailto:thomas@bootswatch.com">thomas@bootswatch.com</a>.</p>
            <p>Code released under the <a href="https://github.com/thomaspark/bootswatch/blob/gh-pages/LICENSE">MIT License</a>.</p>
            <p>Based on <a href="http://getbootstrap.com" rel="nofollow">Bootstrap</a>. Icons from <a href="http://fortawesome.github.io/Font-Awesome/" rel="nofollow">Font Awesome</a>. Web fonts from <a href="http://www.google.com/webfonts" rel="nofollow">Google</a>.</p>

          </div>
        </div>

      </footer>


    </div>


    <script src="./js/jquery-1.10.2.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    <script src="./js/bootswatch.js"></script>
  </body>
</html>
    """)

    return (__bodyend__)


