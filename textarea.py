#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import urllib
from urllib import urlopen
#from sample import calculateExperts
#import scipy
import os, cgi

LIB64_DIR = '/home/k/karpnv/lib64/python2.7/site-packages'
sys.path.insert(0, LIB64_DIR)
import nltk
import pymorphy2
#from pymorphy import get_morph
import urllib

CONTENT_HEADER = 'Content-Type: text/html; charset=utf-8'
PAGE_HEAD = u"""
<!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8">
  <title>Поиск экспертов</title>
<link type="text/css" rel="stylesheet" href="stylesheet.css"/>
 </head>
 <body>
 <p>
 
 <form action="textarea.py" method="post">
</p>
<table > 
<tr> <td><b>Введите ваш текст для обработки:</b>
</td> <td>
</td><td><b>Результат обработки:</b>
</td><td></td></tr>
<tr> 
<td>  
    <p><textarea rows="20" cols="55" name="text" >%s</textarea></p>
</td> 
<td> 
    <p><input type="submit" value="> Обработать >"></p>
</td> 
<td class='result'> 
    <div  class="divsprocr">"""

PAGE_FOOT = u"""
</div>

</td> <td></td>
</tr>
</table>
  
    </form>
 </body>
</html>"""

def process(text):
    out=''

    return out

def print_text(request,resp):
    print CONTENT_HEADER
    print (PAGE_HEAD  % (request)).encode('utf-8')
    print resp
    print (PAGE_FOOT).encode('utf-8')    
    return

def print_error(str):
    print CONTENT_HEADER
    print (PAGE_HEAD  % ('')).encode('utf-8')
    print str
    print (PAGE_FOOT).encode('utf-8') 
    return

def main():
    f = cgi.FieldStorage()
    #print_text('dddd')
    if f.has_key("text"):
        text=f["text"].value
        text = unicode(text, 'utf-8')
        print_text(text, text)
    else:
        print_error("No data to process")
      
if __name__ == '__main__':
    main()