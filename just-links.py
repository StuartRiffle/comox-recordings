import codecs
import os

driveid = {}
with codecs.open('gdrive-list.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        fields = line.split()
        if len(fields) >= 2:
            driveid[fields[1]] = fields[0]

with codecs.open('spreadsheet.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with codecs.open('items.md', 'w', encoding='utf-8-sig') as itemfile:    
        for line in lines[1:]:
            fields = line.split('\t')
            playline = ''
            if len(fields) >= 6: 
                tape, starttime, endtime, english, translated, tags = fields[:6]
                if starttime and endtime:
                    mins, secs = starttime.split(':')[:2]
                    ident = tape + f'_{int(mins):02}{float(secs):02.0f}'

                    # https://drive.google.com/open?id=1xFVVYh6SQljdLi-Xvtg-JpMPGp4iQUfU

                    rawfile = f'{ident}.wav'
                    if rawfile in driveid:
                        playline = f'=HYPERLINK("https://drive.google.com/open?id={driveid[rawfile]}","Play")'



            itemfile.write(f'{playline}\n' )








