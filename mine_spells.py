#!/usr/bin/env python3

import http.client
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.myReset()
    
    def myReset(self):
        self.text = False
        self.spellName = False
        
        self.spelldetails = False
        self.rightTable = False
        self.schoolCell = False

        self.dataSpellName = False
        self.dataSpellSchool = False

        self.name = None
        self.school = None

    def handle_starttag(self, tag, attrs):
        if self.dataSpellName and self.dataSpellSchool:
            return
        if tag == 'div' and ('class', 'text') in attrs:
            self.text = True
        elif self.text and tag == 'h1':
            self.spellName = True
        elif tag == 'table':
            if self.rightTable:
                return
            if self.spelldetails:
                self.rightTable = True
            elif ('id', 'spelldetails') in attrs:
                self.spelldetails = True

    # def handle_endtag(self, tag):
    #     print("End tag  :", tag)

    def handle_data(self, data):
        if self.spellName and not self.dataSpellName:
            self.name = data
            self.dataSpellName = True
        if self.rightTable and not self.dataSpellSchool:
            if self.schoolCell and data[0:2] != r'\n':
                self.school = data
                self.dataSpellSchool = True
            elif data == 'School':
                self.schoolCell = True

    # def handle_comment(self, data):
    #     print("Comment  :", data)

    # def handle_entityref(self, name):
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #     print("Num ent  :", c)

    # def handle_decl(self, data):
    #     print("Decl     :", data)


file = open('spells.csv', 'bw')

parser = MyHTMLParser()
con = http.client.HTTPSConnection('classic.wowhead.com')
notFoundCount = 0
spellCount = 0
spellId = 0

while notFoundCount < 100:
    spellId += 1
    location = '/spell=%d/' % spellId

    retry = True
    while retry:
        retry = False
        try:
            con.request('GET', location)
            resp = con.getresponse()

            if resp.status == 404:
                notFoundCount += 1
                continue

            if resp.status == 301:
                resp.read()
                location = resp.getheader('Location')
                con.request('GET', location)
                resp = con.getresponse()

        except http.client.RemoteDisconnected:
            con = http.client.HTTPSConnection('classic.wowhead.com')
            retry = True

    parser.myReset()
    parser.feed(str(resp.read()))

    if parser.name == 'Spells':
        notFoundCount += 1
        continue

    print('%d;%s;%s' % (spellId, parser.name, parser.school))
    file.write(('%d;%s;%s\n' % (spellId, parser.name, parser.school)).encode(encoding='utf-8'))
    
    notFoundCount = 0
    spellCount += 1

print('Total spells found: %d' % spellCount)

file.close()