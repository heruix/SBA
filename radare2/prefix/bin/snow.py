#!/usr/bin/python
import r2pipe
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import Terminal256Formatter
from os import popen

r2 = r2pipe.open()
filepath = r2.cmdj("ij")['core']['file']
from_addr = r2.cmd("?v $FB")
to_addr = r2.cmd("?v $FE")

nocode = popen( "nocode --from=%s --to=%s %s" % (from_addr, to_addr, filepath) )

print highlight( nocode.read(), CppLexer(), Terminal256Formatter(style='monokai') )