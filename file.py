#!/usr/bin/python3

class File():
    def __init__(self, element):
        self.element = element
        self.path = element.attrib['path']
        self.words = element.attrib['words']
        self.is_ref = element.attrib['is_ref']
        self.marked = element.attrib['marked']

    def getPath(self):
        return self.path

    def __str__(self, endOfObjectDelimiter='\n', memberDelimiter='\n\t'):
        endOfObjectDelimiter += '\n'
        memberDelimiter += '\t'
        return "File: attributes=" + self.element.attrib.__str__()
