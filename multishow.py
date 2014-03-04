#!/usr/bin/env python

from nxapi_utils import *
import textwrap
import sys

if len(sys.argv) != 6:
        print "Runs multiple commands on multiple devices. These devices and commands are obtained from txt files. "
        print "Usage: " + sys.argv[0] + " <username> <password> <ascii|xml> <host file> <command file>"
        quit()

username,password,out_type,host_file,cmd_file = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]

out_type = sys.argv[1]

hosts = open(host_file)

hostnames = []

for line in hosts:
   hostnames.append(line.strip())

commands = []
cmd = open(cmd_file)

for line in cmd:
   commands.append(line.strip())


for hostname in hostnames:
   api = NXAPI()
   api.set_target_url('https://' + hostname + '/ins')
   api.set_username(username)
   api.set_password(password)
   if out_type == "ascii":
      api.set_msg_type('cli_show_ascii')
   else:
      api.set_msg_type('cli_show')
   for command in commands:
      api.set_cmd(command)
      if out_type == 'json':
              api.set_out_format('json')
      apiData = api.get_out_format()
      apiData = api.send_req()

      for line in apiData:
         print line


