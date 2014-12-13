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

import shutil
import include.serverinfo.config as config

__all__ = [
    "create_html_file",
    "create_blank_html_file",
    "htmlinfo",
    "htmldatadashboard",
    "htmldatadashboardjs",
    "htmlend",
    "htmldashboardend",
    "htmllast"
]

#------------------------------------------------------------------------------


def create_html_file(file_name, outputdir, outputdate):

    # Copy css and js
    cssoutput = outputdir + '/css'
    csspluginoutput = outputdir + '/css/plugins'
    csspluginoutputmestis = outputdir + '/css/plugins/metisMenu'
    jsoutput = outputdir + '/js'
    jsoutputflot = outputdir + '/js/plugins/flot'
    jsoutputdataTables = outputdir + '/js/plugins/dataTables'
    jsoutputmetisMenu = outputdir + '/js/plugins/metisMenu'
    jsoutputmorris = outputdir + '/js/plugins/morris'
    fontawesomesoutputcss = outputdir + '/font-awesome-4.1.0/css'
    fontawesomesoutputfonts = outputdir + '/font-awesome-4.1.0/fonts'
    fontawesomesoutputless = outputdir + '/font-awesome-4.1.0/less'
    fontawesomesoutputscss = outputdir + '/font-awesome-4.1.0/scss'
    fontsoutput = outputdir + '/fonts'
    lesssoutput = outputdir + '/less'
    sbadmin = 'lib/html/startbootstrap-sb-admin-2-1.0.1'

    shutil.copy2(sbadmin + '/css/bootstrap.css', cssoutput)
    shutil.copy2(sbadmin + '/css/bootstrap.min.css', cssoutput)
    shutil.copy2(sbadmin + '/css/sb-admin-2.css', cssoutput)
    shutil.copy2(sbadmin + '/css/plugins/morris.css', csspluginoutput)
    shutil.copy2(sbadmin + '/css/plugins/dataTables.bootstrap.css',
                 csspluginoutput)
    shutil.copy2(sbadmin + '/css/plugins/social-buttons.css', csspluginoutput)
    shutil.copy2(sbadmin + '/css/plugins/timeline.css', csspluginoutput)
    shutil.copy2(sbadmin + '/css/plugins/metisMenu/metisMenu.css',
                 csspluginoutputmestis)
    shutil.copy2(sbadmin + '/css/plugins/metisMenu/metisMenu.min.css',
                 csspluginoutputmestis)

    shutil.copy2(sbadmin + '/font-awesome-4.1.0/css/font-awesome.css',
                 fontawesomesoutputcss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/css/font-awesome.min.css',
                 fontawesomesoutputcss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/fonts/FontAwesome.otf',
                 fontawesomesoutputfonts)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/fonts/fontawesome-webfont.eot',
                 fontawesomesoutputfonts)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/fonts/fontawesome-webfont.svg',
                 fontawesomesoutputfonts)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/fonts/fontawesome-webfont.ttf',
                 fontawesomesoutputfonts)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/fonts/fontawesome-webfont.woff',
                 fontawesomesoutputfonts)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/bordered-pulled.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/fixed-width.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/icons.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/list.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/path.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/spinning.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/variables.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/core.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/font-awesome.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/larger.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/mixins.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/rotated-flipped.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/less/stacked.less',
                 fontawesomesoutputless)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_bordered-pulled.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_fixed-width.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_icons.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_list.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_path.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_spinning.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_variables.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_core.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/font-awesome.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_larger.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_mixins.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_rotated-flipped.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/font-awesome-4.1.0/scss/_stacked.scss',
                 fontawesomesoutputscss)
    shutil.copy2(sbadmin + '/fonts/glyphicons-halflings-regular.eot',
                 fontsoutput)
    shutil.copy2(sbadmin + '/fonts/glyphicons-halflings-regular.svg',
                 fontsoutput)
    shutil.copy2(sbadmin + '/fonts/glyphicons-halflings-regular.ttf',
                 fontsoutput)
    shutil.copy2(sbadmin + '/fonts/glyphicons-halflings-regular.woff',
                 fontsoutput)
    shutil.copy2(sbadmin + '/js/bootstrap.js', jsoutput)
    shutil.copy2(sbadmin + '/js/bootstrap.min.js', jsoutput)
    shutil.copy2(sbadmin + '/js/jquery.js', jsoutput)
    shutil.copy2(sbadmin + '/js/sb-admin-2.js', jsoutput)
    shutil.copy2(sbadmin + '/js/plugins/dataTables/dataTables.bootstrap.js',
                 jsoutputdataTables)
    shutil.copy2(sbadmin + '/js/plugins/dataTables/jquery.dataTables.js',
                 jsoutputdataTables)
    shutil.copy2(sbadmin + '/js/plugins/flot/excanvas.min.js', jsoutputflot)
    shutil.copy2(sbadmin + '/js/plugins/flot/flot-data.js', jsoutputflot)
    shutil.copy2(sbadmin + '/js/plugins/flot/jquery.flot.js', jsoutputflot)
    shutil.copy2(sbadmin + '/js/plugins/flot/jquery.flot.pie.js', jsoutputflot)
    shutil.copy2(sbadmin + '/js/plugins/flot/jquery.flot.resize.js',
                 jsoutputflot)
    shutil.copy2(sbadmin + '/js/plugins/flot/jquery.flot.tooltip.min.js',
                 jsoutputflot)
    shutil.copy2(sbadmin + '/js/plugins/morris/morris-data.js', jsoutputmorris)
    shutil.copy2(sbadmin + '/js/plugins/morris/morris.js', jsoutputmorris)
    shutil.copy2(sbadmin + '/js/plugins/morris/morris.min.js', jsoutputmorris)
    shutil.copy2(sbadmin + '/js/plugins/morris/raphael.min.js', jsoutputmorris)
    shutil.copy2(sbadmin + '/js/plugins/metisMenu/metisMenu.js',
                 jsoutputmetisMenu)
    shutil.copy2(sbadmin + '/js/plugins/metisMenu/metisMenu.min.js',
                 jsoutputmetisMenu)
    shutil.copy2(sbadmin + '/less/mixins.less', lesssoutput)
    shutil.copy2(sbadmin + '/less/sb-admin-2.less', lesssoutput)
    shutil.copy2(sbadmin + '/less/variables.less', lesssoutput)

    __title__ = outputdate
    __file__ = outputdir + '/' + file_name
    __htmFile__ = open(__file__, 'w')
    __htmFile__.write(head(__title__))
    __htmFile__.close


#------------------------------------------------------------------------------


def create_blank_html_file(file_name, outputdir, outputdate, menu_html):
    __title__ = outputdate
    __file__ = outputdir + '/reports/' + file_name
    __htmFile__ = open(__file__, 'w')
    __htmFile__.write(headreports(__title__))
    __htmFile__.write(navbarreports(menu_html))
    __htmFile__.write(bodyblank())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlaudit(file_name, html_report, outputdir, menu_html):
    __file__ = outputdir + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(navbar(menu_html))
    __htmFile__.write(bodydashboard(html_report))
    __htmFile__.close


#------------------------------------------------------------------------------

def htmltitle(file_name, outputdirectory, title, href):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodytitle(title, href))
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlinfo(file_name, outputdirectory, helpcommand, commandoutput,
     commandcheck, checkmessage, command, cmdresults):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyinfo(helpcommand, commandoutput, commandcheck,
                      checkmessage, command, cmdresults))
    __htmFile__.close


#------------------------------------------------------------------------------

def htmllast(file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyend())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmldashboardend(file_name, outputdirectory):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyendhtml())
    __htmFile__.close


#------------------------------------------------------------------------------

def htmlend(file_name, outputdirectory):
    __file__ = outputdirectory + '/reports/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(bodyendhtml())
    __htmFile__.close


#------------------------------------------------------------------------------


def htmldatadashboard(file_name, outputdirectory, htmlstat):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(datadashboard(htmlstat))
    __htmFile__.write(datadashboardtimeline(htmlstat))
    __htmFile__.close

#------------------------------------------------------------------------------


def htmldatadashboardjs(file_name, outputdirectory, htmlstat):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    a = htmlstat['system']
    b = htmlstat['boot']
    c = htmlstat['file']
    d = htmlstat['net']
    e = htmlstat['proc']
    f = htmlstat['sec']
    __htmFile__.write(bodyjsend(a, b, c, d, e, f))
    __htmFile__.close


#------------------------------------------------------------------------------

def head(title):
    __head__ = ("""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>%s</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="css/plugins/metisMenu/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="css/plugins/timeline.css" rel="stylesheet">

    <!-- Social Buttons CSS -->
    <link href="css/plugins/social-buttons.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/sb-admin-2.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="css/plugins/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>
    """) % title

    return (__head__)


#------------------------------------------------------------------------------

def headreports(title):
    __head__ = ("""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>%s</title>

    <!-- Bootstrap Core CSS -->
    <link href="../css/bootstrap.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../css/plugins/metisMenu/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="../css/plugins/timeline.css" rel="stylesheet">

    <!-- Social Buttons CSS -->
    <link href="../css/plugins/social-buttons.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../css/sb-admin-2.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="../css/plugins/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>
    """) % title

    return (__head__)


#------------------------------------------------------------------------------


def navbar(menuhtml):
    __navbar__ = ("""<body>

    <div id="wrapper">

        <!-- Navigation -->
        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
            <div class="navbar-default sidebar" role="navigation">
                <div class="sidebar-nav navbar-collapse">
                    <ul class="nav" id="side-menu">

                        <li>
                            <a class="active" href="%s"><i class="fa fa-dashboard fa-fw"></i> Dashboard</a>
                        </li>
                        <li>
                            <a href="reports/%s"><i class="fa fa-bar-chart-o fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="reports/%s"><i class="fa fa-flash fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="reports/%s"><i class="fa fa-hdd-o fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="reports/%s"><i class="fa fa-cloud fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="reports/%s"><i class="fa fa-sitemap fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="reports/%s"><i class="fa fa-shield fa-fw"></i> %s</a>
                        </li>
                    </ul>
                </div>
                <!-- /.sidebar-collapse -->
            </div>
            <!-- /.navbar-static-side -->
        </nav>
    """)
    return (__navbar__) % (menuhtml['fileout'], menuhtml['fileoutgen'],
                           menuhtml['general'], menuhtml['fileoutboot'],
                           menuhtml['boot'], menuhtml['fileoutfile'],
                           menuhtml['filesystem'], menuhtml['fileoutnet'],
                           menuhtml['tcpip'], menuhtml['fileoutproc'],
                           menuhtml['processes'], menuhtml['fileoutsec'],
                           menuhtml['security'])


#------------------------------------------------------------------------------


def navbarreports(menuhtml):
    __navbar__ = ("""<body>

    <div id="wrapper">

        <!-- Navigation -->
        <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
            <div class="navbar-default sidebar" role="navigation">
                <div class="sidebar-nav navbar-collapse">
                    <ul class="nav" id="side-menu">

                        <li>
                            <a class="active" href="../%s"><i class="fa fa-dashboard fa-fw"></i> Dashboard</a>
                        </li>
                        <li>
                            <a href="%s"><i class="fa fa-bar-chart-o fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="%s"><i class="fa fa-flash fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="%s"><i class="fa fa-hdd-o fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="%s"><i class="fa fa-cloud fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="%s"><i class="fa fa-sitemap fa-fw"></i> %s</a>
                        </li>
                        <li>
                            <a href="%s"><i class="fa fa-shield fa-fw"></i> %s</a>
                        </li>
                    </ul>
                </div>
                <!-- /.sidebar-collapse -->
            </div>
            <!-- /.navbar-static-side -->
        </nav>
    """)
    return (__navbar__) % (menuhtml['fileout'], menuhtml['fileoutgen'],
                           menuhtml['general'], menuhtml['fileoutboot'],
                           menuhtml['boot'], menuhtml['fileoutfile'],
                           menuhtml['filesystem'], menuhtml['fileoutnet'],
                           menuhtml['tcpip'], menuhtml['fileoutproc'],
                           menuhtml['processes'], menuhtml['fileoutsec'],
                           menuhtml['security'])


#------------------------------------------------------------------------------


def bodydashboard(htmldatareport):
    __body__ = ("""

<div id="page-wrapper">
            <div class="row">
                <div class="col-lg-12">
                    <div class="text-center">
                        <br>
                        <a class="btn btn-social-icon btn-github" href="https://github.com/1modm/mesc"><i class="fa fa-github"></i></a>
                        <a class="btn btn-social-icon btn-twitter" href="https://twitter.com/1_mod_m"><i class="fa fa-twitter"></i></a>
                        <h3 class="page-header">Minimun Essential Security Checks</h3>
                        <br>
                    </div>
                </div>

                <!-- /.col-lg-5 -->
                <div class="col-lg-5">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Auditor information
                        </div>
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <!-- Nav tabs -->
                            <ul class="nav nav-pills">
                                <li class="active"><a href="#System" data-toggle="tab">System Information</a>
                                </li>
                                <li><a href="#Auditor" data-toggle="tab">Auditor</a>
                                </li>
                            </ul>

                            <!-- Tab panes -->
                            <div class="tab-content">
                                <div class="tab-pane fade in active" id="System">
                                    <h4> </h4>
                                    <p><b>Distribution:</b> %s</p>
                                    <p><b>System:</b> %s</p>
                                    <p><b>Architecture:</b> %s</p>
                                    <p><b>Processor:</b> %s</p>
                                    <p><b>Platform:</b> %s</p>
                                    <p><b>Release:</b> %s</p>
                                    <p><b>Hostname:</b> %s</p>
                                    <p><b>Python version:</b> %s</p>
                                </div>
                                <div class="tab-pane fade" id="Auditor">
                                    <h4> </h4>
                                    <p>%s at %s</p>
                                </div>
                            </div>
                        </div>
                        <!-- /.panel-body -->
                    </div>
                    <!-- /.panel -->
                </div>
                <!-- /.col-lg-5 -->

                <div class="col-lg-7">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            Percentages
                        </div>
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <div class="flot-chart">
                                <div class="flot-chart-content" id="flot-pie-chart"></div>
                            </div>
                        </div>
                        <!-- /.panel-body -->
                    </div>
                    <!-- /.panel -->
                </div>

        </div>
        <!-- /.row -->
    """) % (htmldatareport['Distribution'], htmldatareport['System'],
            htmldatareport['Architecture'], htmldatareport['Processor'],
            htmldatareport['Platform'], htmldatareport['Release'],
            htmldatareport['Hostname'], htmldatareport['Python version'],
            htmldatareport['Auditor'], htmldatareport['Date'])

    return (__body__)

#------------------------------------------------------------------------------


def datadashboard(stat):
    __data__ = ("""
        <div class="row">
                <div class="col-lg-12 col-md-24">
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-database fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">%s</div>
                                    <div>Total</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
        <!-- /.row -->

        <div class="row">
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-green">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-check-square fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">%s</div>
                                    <div>OK</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-yellow">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-tasks fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">%s</div>
                                    <div>Warning</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-red">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-support fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">%s</div>
                                    <div>Critical</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-3">
                                    <i class="fa fa-times fa-5x"></i>
                                </div>
                                <div class="col-xs-9 text-right">
                                    <div class="huge">%s</div>
                                    <div>Error</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        <!-- /.row -->


    """) % (stat['total'], stat['ok'], stat['warn'], stat['critical'],
            stat['error'])
    return (__data__)


#------------------------------------------------------------------------------


def datadashboardtimeline(stat):
    __data__ = ("""

            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <i class="fa fa-clock-o fa-fw"></i> Timeline
                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> Date: %s</small></p>
                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> Duration: %s</small></p>
                        </div>
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <ul class="timeline">
                                <li>
                                    <div class="timeline-badge primary"><i class="fa fa-bar-chart-o"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title">System information</h4>
                                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> %s</small>
                                            </p>
                                        </div>
                                        <div class="timeline-body">
                                            <p>Operating System Information, architecture, kernel memory, shells, commands and users information.</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="timeline-inverted">
                                    <div class="timeline-badge warning"><i class="fa fa-flash"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title">Boot information</h4>
                                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> %s</small>
                                            </p>
                                        </div>
                                        <div class="timeline-body">
                                            <p>Boot process, configuration and runlevels.</p>
                                        </div>
                                    </div>
                                </li>
                                <li>
                                    <div class="timeline-badge success"><i class="fa fa-cloud"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title">File system information</h4>
                                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> %s</small>
                                            </p>
                                        </div>
                                        <div class="timeline-body">
                                            <p>Diskspace, inodes, file permissions and all related with how data is stored and retrieved.</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="timeline-inverted">
                                    <div class="timeline-badge default"><i class="fa fa-sitemap"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title">Network Information</h4>
                                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> %s</small>
                                            </p>
                                        </div>
                                        <div class="timeline-body">
                                            <p>Opened ports, routes, active connections and interfaces configuration.</p>
                                        </div>
                                    </div>
                                </li>
                                <li>
                                    <div class="timeline-badge info"><i class="fa fa-save"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title">Processes running in the system</h4>
                                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> %s</small>
                                            </p>
                                        </div>
                                        <div class="timeline-body">
                                            <p>Processes and memory consumed.</p>
                                        </div>
                                    </div>
                                </li>
                                <li class="timeline-inverted">
                                    <div class="timeline-badge danger"><i class="fa fa-shield"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title">Security information</h4>
                                            <p><small class="text-muted"><i class="fa fa-clock-o"></i> %s</small>
                                            </p>
                                        </div>
                                        <div class="timeline-body">
                                            <p>Configuration problems, vulnerabilities, and security checks.</p>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                        <!-- /.panel-body -->
                    </div>
                    <!-- /.panel -->

            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
    """) % (stat['starttime'], stat['endtime'], stat['stime'], stat['btime'], stat['ftime'],
            stat['ntime'], stat['ptime'], stat['endtime'])

    return (__data__)

#------------------------------------------------------------------------------


def bodyblank():
    __body__ = ("""

<div id="page-wrapper">
            <div class="row">

    """)

    return (__body__)

#------------------------------------------------------------------------------


def bodytitle(title, href):
    __title__ = ("""<a name="%s"></a><br><br>
    <div class="col-lg-12">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <center><h4 class="panel-title">%s</h4></center>
            </div>
        </div>
    </div>
    <br>
    """) % (href, title)

    return (__title__)

#------------------------------------------------------------------------------


def bodyinfo(helpcommand, commandoutput, commandcheck, checkmessage,
     command, cmdresults):

    if commandcheck == config.CHECKRESULTOK:
        __bodyinfo__ = ("""

              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      %s: %s
                    </div>
                    <div class="panel panel-success">
                        <div class="panel-heading">
                          %s: # %s
                          <br>
                          %s
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>

        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage,
         commandoutput)

    elif commandcheck == config.CHECKRESULTERROR:
        __bodyinfo__ = ("""

              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      %s: %s
                    </div>
                    <div class="panel panel-danger">
                        <div class="panel-heading">
                          %s: # %s
                          <br>
                          Issue: %s
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>

        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage,
         commandoutput)

    elif commandcheck == config.CHECKRESULTWARNING:
        __bodyinfo__ = ("""

              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      %s: %s
                    </div>
                    <div class="panel panel-warning">
                        <div class="panel-heading">
                          %s: # %s
                          <br>
                          Issue: %s
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>

        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage,
         commandoutput)

    elif commandcheck == config.CHECKRESULTCRITICAL:
        __bodyinfo__ = ("""

              <div class="col-lg-12">
                  <div class="panel panel-info">
                    <div class="panel-heading">
                      %s: %s
                    </div>
                    <div class="panel panel-danger">
                        <div class="panel-heading">
                          %s: # %s
                          <br>
                          Issue: %s
                        </div>
                    </div>
                    <div class="panel-body">
                        <pre>%s</pre>
                    </div>
                  </div>
            </div>

        """) % (command, helpcommand, commandcheck, cmdresults, checkmessage,
                commandoutput)

    return (__bodyinfo__)


#------------------------------------------------------------------------------

def bodyend():
    __bodyend__ = ("""
            </div>
            <!-- /.container-fluid -->

        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->
    """)

    return (__bodyend__)


#------------------------------------------------------------------------------

def bodyjsend(a, b, c, d, e, f):
    __bodyjsend__ = ("""
    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="js/plugins/metisMenu/metisMenu.min.js"></script>

    <!-- Flot Charts JavaScript -->
    <script src="js/plugins/flot/excanvas.min.js"></script>
    <script src="js/plugins/flot/jquery.flot.js"></script>
    <script src="js/plugins/flot/jquery.flot.pie.js"></script>
    <script src="js/plugins/flot/jquery.flot.resize.js"></script>
    <script src="js/plugins/flot/jquery.flot.tooltip.min.js"></script>

    <!-- Morris Charts JavaScript -->
    <script src="js/plugins/morris/raphael.min.js"></script>
    <script src="js/plugins/morris/morris.min.js"></script>

<script>
//Flot Pie Chart
$(function() {
    var data = [{
        label: "System",
        data: """ + str(a) + """
    }, {
        label: "Boot",
        data: """ + str(b) + """
    }, {
        label: "Filesystem",
        data: """ + str(c) + """
    }, {
        label: "Network",
        data: """ + str(d) + """
    }, {
        label: "Processes",
        data: """ + str(e) + """
    }, {
        label: "Security",
        data: """ + str(f) + """
    }];

    var plotObj = $.plot($("#flot-pie-chart"), data, {
        series: {
            pie: {
                show: true
            }
        },
        grid: {
            hoverable: true
        },
        tooltip: true,
        tooltipOpts: {
            content: "%p.0%, %s", // show percentages, rounding to 2 decimal places
            shifts: {
                x: 20,
                y: 0
            },
            defaultTheme: false
        }
    });

});


</script>

    <!-- Custom Theme JavaScript -->
    <script src="js/sb-admin-2.js"></script>

    """)
    return (__bodyjsend__)


#------------------------------------------------------------------------------


def bodyendhtml():
    __bodyendhtml__ = ("""
</body>

</html>
    """)

    return (__bodyendhtml__)


