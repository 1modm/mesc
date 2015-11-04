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

    templateadmin = 'lib/html/NiceAdmin'

    # Copy css, img and js
    cssoutput = outputdir + '/css'
    shutil.copy2(templateadmin + '/css/timeline.css', cssoutput)
    shutil.copy2(templateadmin + '/css/social-buttons.css', cssoutput)
    shutil.copy2(templateadmin + '/css/bootstrap.min.css', cssoutput)
    shutil.copy2(templateadmin + '/css/bootstrap-theme.css', cssoutput)
    shutil.copy2(templateadmin + '/css/elegant-icons-style.css', cssoutput)
    shutil.copy2(templateadmin + '/css/font-awesome.css', cssoutput)
    shutil.copy2(templateadmin + '/css/font-awesome.min.css', cssoutput)
    shutil.copy2(templateadmin + '/css/fullcalendar.css', cssoutput)
    shutil.copy2(templateadmin + '/css/jquery-jvectormap-1.2.2.css', cssoutput)
    shutil.copy2(templateadmin + '/css/jquery-ui-1.10.4.min.css', cssoutput)
    shutil.copy2(templateadmin + '/css/line-icons.css', cssoutput)
    shutil.copy2(templateadmin + '/css/owl.carousel.css', cssoutput)
    shutil.copy2(templateadmin + '/css/style.css', cssoutput)
    shutil.copy2(templateadmin + '/css/style-responsive.css', cssoutput)
    shutil.copy2(templateadmin + '/css/widgets.css', cssoutput)
    shutil.copy2(templateadmin + '/css/xcharts.min.css', cssoutput)

    fontsoutput = outputdir + '/fonts'
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.eot', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.svg', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.ttf', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/ElegantIcons.woff', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/FontAwesome.otf', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.eot', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.svg', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.eot', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.woff', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.ttf', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.svg', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/fontawesome-webfont.woff', fontsoutput)
    shutil.copy2(templateadmin + '/fonts/glyphicons-halflings-regular.ttf', fontsoutput)

    jsoutput = outputdir + '/js'
    shutil.copy2(templateadmin + '/js/additional-methods.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap-switch.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap-wysiwyg-custom.js', jsoutput)
    shutil.copy2(templateadmin + '/js/bootstrap-wysiwyg.js', jsoutput)
    shutil.copy2(templateadmin + '/js/calendar-custom.js', jsoutput)
    shutil.copy2(templateadmin + '/js/chartjs-custom.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts-flot.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts-other.js', jsoutput)
    shutil.copy2(templateadmin + '/js/charts-xcharts.js', jsoutput)
    shutil.copy2(templateadmin + '/js/dynamic-table.js', jsoutput)
    shutil.copy2(templateadmin + '/js/easy-pie-chart.js', jsoutput)
    shutil.copy2(templateadmin + '/js/excanvas.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/form-component.js', jsoutput)
    shutil.copy2(templateadmin + '/js/form-validation-script.js', jsoutput)
    shutil.copy2(templateadmin + '/js/fullcalendar.js', jsoutput)
    shutil.copy2(templateadmin + '/js/fullcalendar.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/ga.js', jsoutput)
    shutil.copy2(templateadmin + '/js/gdp-data.js', jsoutput)
    shutil.copy2(templateadmin + '/js/gritter.js', jsoutput)
    shutil.copy2(templateadmin + '/js/html5shiv.js', jsoutput)
    shutil.copy2(templateadmin + '/js/index.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-1.8.3.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.autosize.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.customSelect.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.flot.pie.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.hotkeys.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-jvectormap-1.2.2.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-jvectormap-world-mill-en.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.localscroll.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.nicescroll.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.placeholder.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.rateit.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.scrollTo.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.slimscroll.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.smartWizard.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.sparkline-11.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.sparkline.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.stepy.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.tagsinput.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-ui-1.10.4.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery-ui-1.9.2.custom.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/jquery.validate.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/lte-ie7.js', jsoutput)
    shutil.copy2(templateadmin + '/js/morris.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/morris-script.js', jsoutput)
    shutil.copy2(templateadmin + '/js/owl.carousel.js', jsoutput)
    shutil.copy2(templateadmin + '/js/scripts.js', jsoutput)
    shutil.copy2(templateadmin + '/js/sliders.js', jsoutput)
    shutil.copy2(templateadmin + '/js/sparkline-chart.js', jsoutput)
    shutil.copy2(templateadmin + '/js/sparklines.js', jsoutput)
    shutil.copy2(templateadmin + '/js/xcharts.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/d3.min.js', jsoutput)
    shutil.copy2(templateadmin + '/js/d3pie.js', jsoutput)

    imgoutput = outputdir + '/img'
    shutil.copy2(templateadmin + '/img/avatar1_small.png', imgoutput)
    imgoutput = outputdir + '/img/icons'
    shutil.copy2(templateadmin + '/img/icons/line-icon-c.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/line-icon-hover.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/line-icon.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/search-line-icon.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/social.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/weather-hover.png', imgoutput)
    shutil.copy2(templateadmin + '/img/icons/weather.png', imgoutput)
            

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
    __htmFile__.write(bodydashboard(file_name))
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
    __htmFile__.write(bodyendhtmljs())
    __htmFile__.close


#------------------------------------------------------------------------------


def htmldatadashboard(file_name, html_report, outputdirectory, htmlstat, consolereport):
    __file__ = outputdirectory + '/' + file_name
    __htmFile__ = open(__file__, 'a')
    __htmFile__.write(datadashboard(htmlstat))
    __htmFile__.write(datadashboardtimeline(htmlstat))
    __htmFile__.write(datadashboardinfo(html_report))
    __htmFile__.write(datadashboardinfoconsole(consolereport, file_name))
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>%s</title>

    <!-- Bootstrap CSS -->    
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- bootstrap theme -->
    <link href="css/bootstrap-theme.css" rel="stylesheet">
    <!--external css-->
    <!-- font icon -->
    <link href="css/elegant-icons-style.css" rel="stylesheet" />
    <link href="css/font-awesome.min.css" rel="stylesheet" />    
    <!-- Custom styles -->
    <link href="css/style.css" rel="stylesheet">
    <link href="css/style-responsive.css" rel="stylesheet" />

    <link href="css/social-buttons.css" rel="stylesheet">
    <link href="css/timeline.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 -->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
      <script src="js/respond.min.js"></script>
      <script src="js/lte-ie7.js"></script>
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>%s</title>


    <!-- Bootstrap CSS -->    
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <!-- bootstrap theme -->
    <link href="../css/bootstrap-theme.css" rel="stylesheet">
    <!--external css-->
    <!-- font icon -->
    <link href="../css/elegant-icons-style.css" rel="stylesheet" />
    <link href="../css/font-awesome.min.css" rel="stylesheet" />    
    <!-- Custom styles -->
    <link href="../css/style.css" rel="stylesheet">
    <link href="../css/style-responsive.css" rel="stylesheet" />

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 -->
    <!--[if lt IE 9]>
      <script src="../js/html5shiv.js"></script>
      <script src="../js/respond.min.js"></script>
      <script src="../js/lte-ie7.js"></script>
    <![endif]-->
  </head>
    """) % title

    return (__head__)


#------------------------------------------------------------------------------


def navbar(menuhtml):
    __navbar__ = ("""
  <body>
  <!-- container section start -->
  <section id="container" class="">
     
      
      <header class="header dark-bg">
            <div class="toggle-nav">
                <div class="icon-reorder tooltips" data-original-title="Toggle Navigation" data-placement="bottom"></div>
            </div>

            <!--logo start-->
            <a href="" class="logo">MESC <span class="lite">Minimun Essential Security Checks</span></a>
            <!--logo end-->

            <div class="top-nav notification-row">                
                <!-- notificatoin dropdown start-->
                <ul class="nav pull-right top-menu">
                    
                    <!-- alert notification start-->
                    <li id="alert_notificatoin_bar" class="dropdown">
                        <a data-toggle="dropdown" class="dropdown-toggle" href="#">

                            <i class="icon-bell-l"></i>
                            <span class="badge bg-important">🔓</span>
                        </a>
                    </li>
                    <!-- alert notification end-->
                    
                </ul>
                <!-- notificatoin dropdown end-->
            </div>
      </header>      
      <!--header end-->


      <!--sidebar start-->
      <aside>
          <div id="sidebar"  class="nav-collapse ">
              <!-- sidebar menu start-->
              <ul class="sidebar-menu">                
                  <li class="active">
                      <a class="" href="%s">
                          <i class="icon_house_alt"></i>
                          <span>Dashboard</span>
                      </a>
                  </li>
                  <li>
                      <a class="" href="reports/%s">
                          <i class="icon_genius"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="reports/%s">
                          <i class="icon_cogs"></i>
                          <span>%s</span>
                      </a>
                  </li> 

                  <li>
                      <a class="" href="reports/%s">
                          <i class="icon_drive"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="reports/%s">
                          <i class="icon_cloud_alt"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="reports/%s">
                          <i class="icon_flowchart"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="reports/%s">
                          <i class="icon_shield_alt"></i>
                          <span>%s</span>
                      </a>
                  </li>
                  
              </ul>
              <!-- sidebar menu end-->
          </div>
      </aside>
      <!--sidebar end-->

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
    __navbar__ = ("""

  <body>
  <!-- container section start -->
  <section id="container" class="">
     
      
      <header class="header dark-bg">
            <div class="toggle-nav">
                <div class="icon-reorder tooltips" data-original-title="Toggle Navigation" data-placement="bottom"></div>
            </div>

            <!--logo start-->
            <a href="" class="logo">MESC <span class="lite">Minimun Essential Security Checks</span></a>
            <!--logo end-->
          
            <div class="top-nav notification-row">                
                <!-- notificatoin dropdown start-->
                <ul class="nav pull-right top-menu">
                    
                    <!-- alert notification start-->
                    <li id="alert_notificatoin_bar" class="dropdown">
                        <a data-toggle="dropdown" class="dropdown-toggle" href="#">

                            <i class="icon-bell-l"></i>
                            <span class="badge bg-important">🔓</span>
                        </a>
                    </li>
                    <!-- alert notification end-->
                    
                </ul>
                <!-- notificatoin dropdown end-->
            </div>
      </header>      
      <!--header end-->


      <!--sidebar start-->
      <aside>
          <div id="sidebar"  class="nav-collapse ">
              <!-- sidebar menu start-->
              <ul class="sidebar-menu">                
                  <li class="active">
                      <a class="" href="../%s">
                          <i class="icon_house_alt"></i>
                          <span>Dashboard</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="%s">
                          <i class="icon_genius"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="%s">
                          <i class="icon_cogs"></i>
                          <span>%s</span>
                      </a>
                  </li>

                   <li>
                      <a class="" href="%s">
                          <i class="icon_drive"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="%s">
                          <i class="icon_cloud_alt"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="%s">
                          <i class="icon_flowchart"></i>
                          <span>%s</span>
                      </a>
                  </li>

                  <li>
                      <a class="" href="%s">
                          <i class="icon_shield_alt"></i>
                          <span>%s</span>
                      </a>
                  </li>  
                  
              </ul>
              <!-- sidebar menu end-->
          </div>
      </aside>
      <!--sidebar end-->


    """)
    return (__navbar__) % (menuhtml['fileout'], menuhtml['fileoutgen'],
                           menuhtml['general'], menuhtml['fileoutboot'],
                           menuhtml['boot'], menuhtml['fileoutfile'],
                           menuhtml['filesystem'], menuhtml['fileoutnet'],
                           menuhtml['tcpip'], menuhtml['fileoutproc'],
                           menuhtml['processes'], menuhtml['fileoutsec'],
                           menuhtml['security'])


#------------------------------------------------------------------------------


def bodydashboard(htmlfile):
    __body__ = ("""


      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">
              
            <div class="row">
                <div class="col-lg-12">
                    <h3 class="page-header"><i class="fa fa-laptop"></i> Dashboard</h3>
                    <ol class="breadcrumb">
                        <li><i class="fa fa-home"></i><a href="%s">Home</a></li>
                        <li><i class="fa fa-laptop"></i>Dashboard</li>                          
                    </ol>
                </div>
            </div>

    """) % (htmlfile)

    return (__body__)


#------------------------------------------------------------------------------


def datadashboardinfo(htmldatareport):
    __body__ = ("""

            <div class="col-lg-12">
                      <!--Project Activity start-->
                      <section class="panel">
                          <div class="panel-body progress-panel">
                            <div class="row">
                              <div class="col-lg-8 task-progress pull-left">
                                  <h1>System Information</h1>                                  
                              </div>
                              <div class="col-lg-12">
                                <span class="profile-ava pull-right">
                                        <img alt="" class="simple" src="img/avatar1_small.png">
                                        Auditor
                                </span>                                
                              </div>
                            </div>
                          </div>
                          <table class="table table-hover personal-task">
                              <tbody>
                              <tr>
                                  <td>Auditor</td>
                                  <td>
                                      %s at %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Distribution</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>System</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Architecture</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Processor</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Platform</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Release</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Hostname</td>
                                  <td>
                                      %s
                                  </td>
                              </tr>
                              <tr>
                                  <td>Python version</td>
                                  <td>
                                      %s
                                  </td>
                            </tr>


                              </tbody>
                          </table>
                      </section>
                      <!--Project Activity end-->
                  </div>
              </div><br><br>




    """) % (htmldatareport['Auditor'], htmldatareport['Date'],
            htmldatareport['Distribution'], htmldatareport['System'],
            htmldatareport['Architecture'], htmldatareport['Processor'],
            htmldatareport['Platform'], htmldatareport['Release'],
            htmldatareport['Hostname'], htmldatareport['Python version'])

    return (__body__)

#------------------------------------------------------------------------------


def datadashboardinfoconsole(consolereport, filename):

    gen_html_file = 'reports/general_' + filename
    boot_html_file = 'reports/boot_' + filename
    file_html_file = 'reports/file_' + filename
    net_html_file = 'reports/net_' + filename
    proc_html_file = 'reports/proc_' + filename
    sec_html_file = 'reports/security_' + filename

    itemshtml = ['<table class=\"table\">']
    itemshtml.append('<tbody>')

    for key in consolereport:
        if key is not "load":
            if (key[1] == "CHECKED"):
                itemshtml.append('<tr class="success">')
            elif (key[1] == "WARNING"):
                itemshtml.append('<tr class="warning">')
            elif (key[1] == "CRITICAL"):
                itemshtml.append('<tr class="danger">')
            else:
                itemshtml.append('<tr>')
            if (key[2] == "general"):
                itemshtml.append('<td><a href="%s">%s</td></a>' % (gen_html_file,key[0]))
            if (key[2] == "boot"):
                itemshtml.append('<td><a href="%s">%s</a></td>' % (boot_html_file,key[0]))
            if (key[2] == "filesystem"):
                itemshtml.append('<td><a href="%s">%s</a></td>' % (file_html_file,key[0]))
            if (key[2] == "tcpip"):
                itemshtml.append('<td><a href="%s">%s</a></td>' % (net_html_file,key[0]))
            if (key[2] == "processes"):
                itemshtml.append('<td><a href="%s">%s</a></td>' % (proc_html_file,key[0]))
            if (key[2] == "security"):
                itemshtml.append('<td><a href="%s">%s</a></td>' % (sec_html_file,key[0]))

            #itemshtml.append('<td><a href="#">%s</a></td>' % key[0])
            itemshtml.append('<td>%s</td>' % key[1])
            #itemshtml.append('<td>%s</td>' % key[2])
            itemshtml.append('</tr>')

    itemshtml.append('</tbody>')
    itemshtml.append('</table>')

    htmllist = ''.join(itemshtml)

    __body__ = ("""
            <br>
                    <div class="col-lg-12">
                      <!--Project Activity start-->
                      <section class="panel">
                          <header class="panel-heading">
                              Checks
                          </header>
                            %s
                      </section>
                      <!--Project Activity end-->
                    </div>
            <br><br>

    """) % (htmllist)

    return (__body__)

#------------------------------------------------------------------------------


def datadashboard(stat):
    __data__ = ("""
        <div class="row">
            <div class="col-lg-12 col-md-3 col-sm-12 col-xs-12">
              <div class="info-box blue-bg">
                <i class="fa fa-database"></i>
                <div class="count text-right">%s</div>
                <div class="title text-right">Total</div>            
              </div><!--/.info-box-->     
            </div><!--/.col-->  
        </div>
        <!-- /.row -->

        <div class="row">

            <div class="col-lg-3 col-md-3">
              <div class="info-box green-bg">
                <i class="fa fa-check-square"></i>
                <div class="count text-right">%s</div>
                <div class="title text-right">OK</div>            
              </div><!--/.info-box-->     
            </div><!--/.col-->  

            <div class="col-lg-3 col-md-3">
              <div class="info-box yellow-bg">
                <i class="fa fa-tasks"></i>
                <div class="count text-right">%s</div>
                <div class="title text-right">Warning</div>            
              </div><!--/.info-box-->     
            </div><!--/.col-->  

            <div class="col-lg-3 col-md-3">
              <div class="info-box red-bg">
                <i class="fa fa-support"></i>
                <div class="count text-right">%s</div>
                <div class="title text-right">Critical</div>            
              </div><!--/.info-box-->     
            </div><!--/.col-->  

            <div class="col-lg-3 col-md-3">
              <div class="info-box dark-bg">
                <i class="fa fa-times"></i>
                <div class="count text-right">%s</div>
                <div class="title text-right">Error</div>            
              </div><!--/.info-box-->     
            </div><!--/.col-->  

        </div>
        <!-- /.row -->



    """) % (stat['total'], stat['ok'], stat['warn'], stat['critical'],
            stat['error'])
    return (__data__)


#------------------------------------------------------------------------------


def datadashboardtimeline(stat):
    __data__ = ("""

        <br>
            <center>
            <div class="col-lg-12">
                <div id="pie"></div>
            </div>
            </center>
        <br>

            <div class="row">
                <div class="col-lg-12">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <i class="fa fa-clock-o fa-fw"></i><b>Timeline</b>
                            <br><small><i class="fa fa-clock-o"></i> Date: %s</small>
                            <br><small><i class="fa fa-clock-o"></i> Duration: %s</small>
                        </div>
                        <!-- /.panel-heading -->
                        <div class="panel-body">
                            <ul class="timeline">
                                <li>
                                    <div class="timeline-badge primary"><i class="fa fa-bar-chart-o"></i>
                                    </div>
                                    <div class="timeline-panel">
                                        <div class="timeline-heading">
                                            <h4 class="timeline-title"><b>System information</b></h4>
                                            <p><small><i class="fa fa-clock-o"></i> %s</small>
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
                                            <h4 class="timeline-title"><b>Boot information</b></h4>
                                            <p><small><i class="fa fa-clock-o"></i> %s</small>
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
                                            <h4 class="timeline-title"><b>Filesystem information</b></h4>
                                            <p><small><i class="fa fa-clock-o"></i> %s</small>
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
                                            <h4 class="timeline-title"><b>Network Information</b></h4>
                                            <p><small><i class="fa fa-clock-o"></i> %s</small>
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
                                            <h4 class="timeline-title"><b>Processes running in the system</b></h4>
                                            <p><small><i class="fa fa-clock-o"></i> %s</small>
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
                                            <h4 class="timeline-title"><b>Security information</b></h4>
                                            <p><small><i class="fa fa-clock-o"></i> %s</small>
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


      <!--main content start-->
      <section id="main-content">
          <section class="wrapper">

    """)

    return (__body__)

#------------------------------------------------------------------------------


def bodytitle(title, href):
    __title__ = ("""<a name="%s"></a><br><br>

                <div class="col-lg-12">    
                    <div class="panel panel-default">
                        <div class="panel-heading">
                        <center>
                            <h2><strong>%s</strong></h2>
                        </center>
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
                  <div class="panel panel-info panel-default">
                    <div class="panel-heading">
                      <strong>%s: %s</strong>
                    </div>
                    <div class="panel panel-success panel-default">
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
                  <div class="panel panel-info panel-default">
                    <div class="panel-heading">
                      <strong>%s: %s</strong>
                    </div>
                    <div class="panel panel-danger panel-default">
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
                  <div class="panel panel-info panel-default">
                    <div class="panel-heading">
                      <strong>%s: %s</strong>
                    </div>
                    <div class="panel panel-warning panel-default">
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
                  <div class="panel panel-info panel-default">
                    <div class="panel-heading">
                      <strong>%s: %s</strong>
                    </div>
                    <div class="panel panel-danger panel-default">
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
                  <div class="col-lg-12">
            <div class="text-center">
                <br>
                <a class="btn btn-social-icon btn-github" href="https://github.com/1modm/mesc"><i class="fa fa-github"></i></a>
                <a class="btn btn-social-icon btn-twitter" href="https://twitter.com/1_mod_m"><i class="fa fa-twitter"></i></a>
                <br>
            </div>
          </div>

          </section>
      </section>
      <!--main content end-->
  </section>
  <!-- container section start -->
    """)

    return (__bodyend__)


#------------------------------------------------------------------------------

def bodyjsend(a, b, c, d, e, f):
    aa = str(a)

    __bodyjsend__ = ("""
    <script src="js/d3.min.js"></script>
    <script src="js/d3pie.js"></script>

    <!-- javascripts -->
    <script src="js/jquery.js"></script>
    <script src="js/jquery-ui-1.10.4.min.js"></script>
    <script src="js/jquery-1.8.3.min.js"></script>
    <script type="text/javascript" src="js/jquery-ui-1.9.2.custom.min.js"></script>
    <!-- bootstrap -->
    <script src="js/bootstrap.min.js"></script>
    <!-- nice scroll -->
    <script src="js/jquery.scrollTo.min.js"></script>
    <script src="js/jquery.nicescroll.js" type="text/javascript"></script>

    <!--script for this page only-->
    <script src="js/calendar-custom.js"></script>
    <script src="js/jquery.rateit.min.js"></script>
    <!-- custom select -->
    <script src="js/jquery.customSelect.min.js" ></script>
    <script src="assets/chart-master/Chart.js"></script>
   
    <!--custome script for all page-->
    <script src="js/scripts.js"></script>
  

<script>

var pie2 = new d3pie("pie", {
    header: {
          title: {
            text: "Percentages"
        }
    },
  data: {
    content: [
      { label: "System", value: """ + str(a) + """ },
      { label: "Boot", value: """ + str(b) + """ },
      { label: "Filesystem", value: """ + str(c) + """ },
      { label: "Network", value: """ + str(d) + """ },
      { label: "Processes", value: """ + str(e) + """ },
      { label: "Security", value: """ + str(f) + """ }
    ]
  },
      size: {
        "pieOuterRadius": "80%"
    },
  tooltips: {
    enabled: false,
    type: "placeholder",
    string: "{label}: {percentage}% ({value})",

    // data is an object with the three properties listed below. Just modify the properties
    // directly - there's no need to return anything
    placeholderParser: function(index, data) {
      data.label = data.label + "!";
      data.percentage = data.percentage.toFixed(2);
      data.value = data.value.toFixed(5);
    }
  }
});

var pie = new d3pie("pie", {
    header: {
        title: {
            text: "Number of checks"
        }
    },
    labels: {
        inner: {
            format: "value"
        },
        value: {
            color: "#ffffff"
        }
    },
      size: {
        "pieOuterRadius": "80%"
    },
    data: {
        content: [
            { label: "System", value: """ + str(a) + """ },
            { label: "Boot", value: """ + str(b) + """ },
            { label: "Filesystem", value: """ + str(c) + """ },
            { label: "Network", value: """ + str(d) + """ },
            { label: "Processes", value: """ + str(e) + """ },
            { label: "Security", value: """ + str(f) + """ }
        ]
    }
});

</script>


    """)

    return (__bodyjsend__)

#------------------------------------------------------------------------------


def bodyendhtmljs():
    __bodyendhtml__ = ("""

                          <div class="col-lg-12">
            <div class="text-center">
                <br>
                <a class="btn btn-social-icon btn-github" href="https://github.com/1modm/mesc"><i class="fa fa-github"></i></a>
                <a class="btn btn-social-icon btn-twitter" href="https://twitter.com/1_mod_m"><i class="fa fa-twitter"></i></a>
                <br>
            </div>
          </div>

          </section>
      </section>
      <!--main content end-->
  </section>
  <!-- container section start -->
  
    <script src="../js/d3.min.js"></script>
    <script src="../js/d3pie.js"></script>

    <!-- javascripts -->
    <script src="../js/jquery.js"></script>
    <script src="../js/jquery-ui-1.10.4.min.js"></script>
    <script src="../js/jquery-1.8.3.min.js"></script>
    <script type="text/javascript" src="../js/jquery-ui-1.9.2.custom.min.js"></script>
    <!-- bootstrap -->
    <script src="../js/bootstrap.min.js"></script>
    <!-- nice scroll -->
    <script src="../js/jquery.scrollTo.min.js"></script>
    <script src="../js/jquery.nicescroll.js" type="text/javascript"></script>

    <!--script for this page only-->
    <script src="../js/calendar-custom.js"></script>
    <script src="../js/jquery.rateit.min.js"></script>
    <!-- custom select -->
    <script src="../js/jquery.customSelect.min.js" ></script>
    <script src="../assets/chart-master/Chart.js"></script>
   
    <!--custome script for all page-->
    <script src="../js/scripts.js"></script>
  

  </body>
</html>
    """)

    return (__bodyendhtml__)

#------------------------------------------------------------------------------


def bodyendhtml():
    __bodyendhtml__ = ("""
  </body>
</html>
    """)

    return (__bodyendhtml__)




