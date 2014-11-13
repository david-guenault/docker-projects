#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
shinkenctl.py
This script is intended to control shinken in docker container
Copyright (C) 2014 - David GUENAULT <david.guenault@gmail.com>
License: http://www.gnu.org/licenses/gpl.html GPL version 2 or higher
"""
import sys
import supervisor.xmlrpc
import xmlrpclib
from optparse import OptionParser

if __name__ == '__main__':
    major = sys.version_info.major
    minor = sys.version_info.minor
    if major != 2 or minor not in [6,7]:
        print sys.version_info
        print "You need python 2.6 or 2.7"
        sys.exit(0)

    """ parse command line options """

    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-c", "--container", dest="container", action="store_true", help="container ip address and port (host:port) with default port on 9001",default=False)
    parser.add_option("-u", "--user", dest="user", action="store_true", help="supervisor user",default=False)
    parser.add_option("-p", "--password", dest="password", action="store_true", help="process hostgroups",default=False)
    parser.add_option("--action", dest="action", action="store_true", help="Action to do [start,stop,restart]",default=False)
    parser.add_option("--target", dest="target", action="store_true", help="program or group to apply action",default=False)
    parser.add_option("--proto", dest = "proto", action="store_true", help="[http|https] default to http",default="http")

    (options, args) = parser.parse_args()

    groupactions = {
        "start" : ["supervisor.startProcessGroup"],
        "stop" : ["supervisor.stopProcessGroup"],
        "restart" : ["supervisor.startProcessGroup", "supervisor.stopProcessGroup"]
    }

    processaction = {
        "start" : ["supervisor.startProcess"],
        "stop" : ["supervisor.stopProcess"],
        "restart" : ["supervisor.startProcess", "supervisor.stopProcess"]
    }

    if options.container and options.user and options.password and options.action and options.target:
        uri = "%s://%s:%s@%s" % (proto,user,password,container)
        server=xmlrpclib.Server(uri)
        if action in ["start","stop","restart"]:
            if ":" in target:
                """ group action """
                for act in groupactions[action]:
                    result = getattr(server,act)()
            else:
                """ process action """

    else:
        usage

"""
supervisor.addProcessGroup
supervisor.clearAllProcessLogs
supervisor.clearLog
supervisor.clearProcessLog
supervisor.clearProcessLogs
supervisor.getAPIVersion
supervisor.getAllConfigInfo
supervisor.getAllProcessInfo
supervisor.getIdentification
supervisor.getPID
supervisor.getProcessInfo
supervisor.getState
supervisor.getSupervisorVersion
supervisor.getVersion
supervisor.readLog
supervisor.readMainLog
supervisor.readProcessLog
supervisor.readProcessStderrLog
supervisor.readProcessStdoutLog
supervisor.reloadConfig
supervisor.removeProcessGroup
supervisor.restart
supervisor.sendProcessStdin
supervisor.sendRemoteCommEvent
supervisor.shutdown
supervisor.startAllProcesses
supervisor.startProcess
supervisor.startProcessGroup
supervisor.stopAllProcesses
supervisor.stopProcess
supervisor.stopProcessGroup
supervisor.tailProcessLog
supervisor.tailProcessStderrLog
supervisor.tailProcessStdoutLog
system.listMethods
system.methodHelp
system.methodSignature
system.multicall
"""