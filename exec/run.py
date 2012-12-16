#!/usr/bin/env python

from impressive import *
import sys

print sys.argv[1]
content_list = containerGenerator(sys.argv[1])

author_ = unicode(raw_input("Author: "), "utf-8")
description_ = unicode(raw_input("Description: "), "utf-8")
language_ = unicode(raw_input("Language: "), "utf-8")
title_ = unicode(raw_input("Title: "), "utf-8")
stylesheet_ = unicode(raw_input("Stylesheet: "), "utf-8")

generated_HTML = generateHTML(content_list, language=language_, title=title_, description=description_, author=author_, stylesheet=stylesheet_)

print "Generation was %s" % ( "-Successfull-" if generated_HTML == True else "#ERROR#" )
