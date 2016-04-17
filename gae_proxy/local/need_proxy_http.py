#!/usr/bin/env python

import os 
need_proxy_http_conf = 'need_proxy_http.conf'

def proxy(host):
    '''without config file,all request go with proxy'''
    if not os.path.isfile(need_proxy_http_conf):
        return True
    file = open(need_proxy_http_conf)
    line = file.readline()
    while line:
        line = line.strip()
        if line and line[0]!='#':
            #print(line in host)
            if line in host:
                return True
        line = file.readline()
    return False
    