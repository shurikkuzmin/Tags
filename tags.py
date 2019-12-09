#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:19:37 2019

@author: shurik
"""
import os
import json

def splitPath(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:
            break
        elif parts[1] == path:
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

tagsFilesMap = {}
filesTagsMap = {}

allFiles = set()
allTags = set()

rootDir = "Files"
for dirName, subdirList, fileList in os.walk(rootDir):
    print("Found directory: %s Short Name: %s" % (dirName, os.path.basename(dirName)))
    tags = splitPath(dirName)
    
    for tag in tags:
        allTags.add(tag)
        if not tag in tagsFilesMap and len(fileList)!=0:
            tagsFilesMap[tag] = set()
        for fname in fileList:
            tagsFilesMap[tag].add(fname)
        
    for fname in fileList:
        allFiles.add(fname)
        #print("\t%s" % fname)
        #print("tags: ", splitPath(dirName))
        filesTagsMap[fname] = tags
        

for fname in filesTagsMap:
    print("File: ", fname, " has tags: ",filesTagsMap[fname])

for tag in tagsFilesMap:
    tagsFilesMap[tag]=list(tagsFilesMap[tag])
    print("Tag: ", tag, " is in files: ",tagsFilesMap[tag])

print("All tags = ", allTags)
overall = {"Files": filesTagsMap, "Tags": tagsFilesMap, "AllTags" : list(allTags), "AllFiles" : list(allFiles)}
with open("data.json", "w") as f:
    json.dump(overall, f)