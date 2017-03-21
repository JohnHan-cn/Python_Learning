"""
实现一个HTTP Web服务器，他知道如何运行服务器脚本端CGI脚本；
从当前工作目录提供文件和脚本；Python脚本必须存储在webdir\cgi-bin 或webdir\htbin中；
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = 'D:\Python_Learning\Python_Learning'
port = 80

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
