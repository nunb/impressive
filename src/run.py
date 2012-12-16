#!/usr/bin/env python

from impressive import *
from json import loads
from glob import glob
import codecs
import sys

generated_HTML = None

def ask():
    """ Returns generated HTML output [@see: generateHTML] and asks for the requiered fields
    author, description, language, title, stylesheet
    """
    author_ = unicode(raw_input("Author: "), "utf-8")
    description_ = unicode(raw_input("Description: "), "utf-8")
    language_ = unicode(raw_input("Language: "), "utf-8")
    title_ = unicode(raw_input("Title: "), "utf-8")
    stylesheet_ = unicode(raw_input("Stylesheet: "), "utf-8")

    return generateHTML(content_list, language=language_, title=title_, description=description_, author=author_, stylesheet=stylesheet_)


content_list = containerGenerator(sys.argv[1])

for fileName in glob("%s/*" % (sys.argv[1])):
        fobj = codecs.open("%s" % (fileName), "r", encoding="utf-8")
        jsonObj = loads(fobj.read().encode("utf8"))
        mhm = updateContent(jsonObj)
        fobj.close()
        print "Updated content of %s = %s" % (fileName, str(mhm))


try:
    config = sys.argv[2]
    if config.split("/")[0] == "config":
        jsonFobj = codecs.open("%s" % (config), "r", encoding="utf-8")
        jsonObj = loads(jsonFobj.read().encode("utf8"))
        generated_HTML = generateHTML(
                content_list,
                language=jsonObj["presentation"]["language"],
                title=jsonObj["presentation"]["title"],
                description=jsonObj["presentation"]["description"],
                author=jsonObj["presentation"]["author"],
                stylesheet=jsonObj["presentation"]["stylesheet"])

except IndexError:
    generated_HTML = ask()

print "Generation was %s" % ( "-Successfull-" if generated_HTML == True else "#NOT SUCCESSFULL!#" )

