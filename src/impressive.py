# -*- coding: iso-8859-1 -*-
#!/usr/bin/env python

# Kai Oliver Quambusch 2012

from json import dumps, loads
from glob import glob
from hashlib import sha256
import codecs

def updateContent(jsonObj):
    cntFobj = codecs.open(jsonObj["content"], "r", encoding="utf-8")
    cntFobj_str = cntFobj.read().encode("utf8")
    cntFobj.close()
    cntFobj = codecs.open(jsonObj["content"], "w", encoding="utf-8")

    if jsonObj.has_key("content-sum") == False:
        if jsonObj.has_key("content-parsed") == False:
            # parse content
            jsonObj["content-parsed"] = parseMarkup(cntFobj_str)
        else:
            jsonObj["content-sum"] = sha256(jsonObj["content-parsed"].encode("utf8")).hexdigest()
            jsonObj["content-parsed"] = parseMarkup(cntFobj_str)

    elif jsonObj["content-sum"] != sha256(jsonObj["content-parsed"].encode("utf8")).hexdigest():
        jsonObj["content-parsed"] = parseMarkup(cntFobj_str)

    cntFobj.write(jsonObj["content-parsed"])
    cntFobj.close()
    return True

def idMaker(jsonDirectoryPath):
    ids = []
    for item in glob("json/*"):
        ids.append(item.split(".")[0].split("/")[1])
    return ids


"""
This function will parse the impressiveMarkupLanguage iML into HTML code.
Available tags are:
    :-lst: List (optional css/class elements: :-lst:class'foo bar':)
        :-bp: (bullet point)
    :-img:/path/to/image: inserts an image
    :: linebreak
"""
def parseMarkup(content):
    return content.decode("utf8").replace("::", "<br>")

def containerGenerator(jsonDirectoryPath):
    '''This function scans the JSON directory, opens the JSON Files and generates the slide div-Tags'''
    divTags_raw = '<div id="%s" class="%s" data-x="%s" data-y="%s" data-rotate-x="%s" data-rotate-y="%s" data-scale="%s">\n%s\n</div>\n'
    divSlides_filled = []
    # iterate over id's
    for slideId in idMaker(jsonDirectoryPath):
        # open file and load as dictionary object
        jsonFobj = open("%s/%s.json" % (jsonDirectoryPath, slideId),"r")
        jsonDict = loads(jsonFobj.read())
        # TODO: parse content path from jsonDict["content"] into it's marked up content
        # manipulate HTML div-raw-Tag
        if jsonDict.has_key("content-parsed") == False:
            print "Error, JSON contains no parsed content."
            # TODO: Trigger auto parsing if possible
            # TODO: Remove exit function when autoparsing worked.
            exit()

        divSlides_filled.append((jsonDict["page-number"], divTags_raw % (
                slideId,
                jsonDict["class"],
                jsonDict["positions"]["data-x"],
                jsonDict["positions"]["data-y"],
                jsonDict["positions"]["x-rotate"],
                jsonDict["positions"]["y-rotate"],
                jsonDict["positions"]["scale"],
                jsonDict["content-parsed"])))

    return divSlides_filled

title_def = "My impressive presentation"
def generateHTML(divSlides_filled, language="de", charset="utf-8", viewport_width=1024, title="", description="No description", author="John Doe", stylesheet="css/style.css"):
    if title == "":
        title = title_def

    output_fobj = codecs.open("../presentation/index.html", "w", encoding="utf-8")
    output_str = ""
    rawOutput_fobj = open("raw.html", "r")
    rawOutput_str = rawOutput_fobj.read()

    slide_count = len(divSlides_filled)
    i = 0

    tmp_out = []
    while i != slide_count:
        tmp_out.append(None)
        i += 1

    i = 0

    for item in divSlides_filled:
        pnum, divcnt = item
        tmp_out[pnum - 1] = divcnt

    for item in tmp_out:
        output_str += item
        output_str += "\n"

    output_fobj.write(
        rawOutput_str % (
            language,
            charset,
            viewport_width,
            title,
            description,
            author,
            stylesheet,
            output_str))

    output_fobj.close()
    return True
