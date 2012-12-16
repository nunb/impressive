#!/usr/bin/env python

from impressive import parseMarkup
from json import dumps
import codecs

try:
    while True:
        jsonObj = {}
        jsonObj["name"] = unicode(raw_input("Slide name: "), "utf-8")
        jsonObj["class"] = unicode(raw_input("CSS classes: "), "utf-8")
        jsonObj["page-number"] = int(raw_input("Page no.: "))
        jsonObj["content"] = "cnt/%s.cnt" % (jsonObj["name"])
        jsonObj["positions"] = {}
        jsonObj["positions"]["data-x"] = int(raw_input("Data X: "))
        jsonObj["positions"]["data-y"] = int(raw_input("Data Y: "))
        jsonObj["positions"]["x-rotate"] = int(raw_input("Rotate X: "))
        jsonObj["positions"]["y-rotate"] = int(raw_input("Rotate Y: "))
        jsonObj["positions"]["scale"] = int(raw_input("Scale: "))

        # Open files we need and dump content to cnt_str
        out_fobj = codecs.open("json/%s.json" % (jsonObj["name"]), "w", "utf-8")
        cnt_fobj = codecs.open(jsonObj["content"], "r", "utf-8")
        jsonObj["content-parsed"] = parseMarkup(cnt_fobj.read().encode("utf8"))
        out_fobj.write(dumps(jsonObj))

        # NOTE: NOW we have to get the real file content from content-parse
        # TODO: Auto updater function which checks .cnt files for changes and if
        #       this is the case we should dump the new file content into the JSON

        cnt_fobj.close()
        out_fobj.close()
        print "Slide JSON for '%s' saved" % (jsonObj["name"])
        print "Content-length:\t\t%s" % (len(jsonObj["content-parsed"]))
        print "Data X * Y:\t\t%s * %s" % (jsonObj["positions"]["data-x"], jsonObj["positions"]["data-y"])
        print "Rotation X * Y:\t\t%s * %s" % (jsonObj["positions"]["x-rotate"], jsonObj["positions"]["y-rotate"])
        print "Scale:\t\t\t%s\n" % (jsonObj["positions"]["scale"])

except KeyboardInterrupt:
    print "\nClosing application, look into your json/ folder"
