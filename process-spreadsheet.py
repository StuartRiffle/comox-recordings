import codecs
import os
from collections import defaultdict
d = defaultdict(list)


driveid = {}
with codecs.open('gdrive-list.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        fields = line.split()
        if len(fields) >= 2:
            driveid[fields[1]] = fields[0]
            #sharecommand = 'gdrive share ' + fields[0]
            #print(sharecommand)
            #os.system(sharecommand)

bytag = defaultdict(list)
with codecs.open('spreadsheet.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with codecs.open('playlinks.txt', 'w', encoding='utf-8-sig') as playfile:    
        for line in lines[1:]:
            fields = line.split('\t')
            playline = ''
            if len(fields) >= 6: 
                tape, starttime, endtime, english, translated, tags = fields[:6]
                if starttime and endtime:
                    mins, secs = starttime.split(':')[:2]
                    ident = tape + f'_{int(mins):02}{float(secs):02.0f}'

                    clipfile = f'clips/{ident}.wav'
                    clipcommand = f'ffmpeg -y -i audio/{tape}.wav -ss {starttime} -to {endtime} website/static/{clipfile}'
                    #print(clipcommand)
                    if not os.path.isfile(f'website/static/{clipfile}'):
                        print(clipcommand)
                        os.system(clipcommand)

                    with codecs.open('website/data/clips/' + ident + '.yaml', 'w', encoding='utf-8-sig') as y:
                        y.write('---\n')
                        y.write(f'title: "{ident}"\n')
                        y.write(f'tape: "{tape}"\n')
                        y.write(f'starttime: "{starttime}"\n')
                        y.write(f'endtime: "{endtime}"\n')
                        y.write(f'english: "{english}"\n')
                        y.write(f'translated: "{translated}"\n')
                        y.write(f'clipfile: "{clipfile}"\n')
                        y.write(f'tags: "{tags}"\n')
                        y.write('---\n')

                    # https://drive.google.com/open?id=1xFVVYh6SQljdLi-Xvtg-JpMPGp4iQUfU

                    rawfile = f'{ident}.wav'
                    if rawfile in driveid:
                        playline = f'=HYPERLINK("https://drive.google.com/open?id={driveid[rawfile]}","Play")'

                    linktext = translated
                    if linktext == '':
                        linktext = '(play)'

                         

                    mdline = f'{english} | <a href="{clipfile}">{linktext}</a>'

                    tagnames = [x.strip() for x in tags.split(',')]
                    for tagname in tagnames:
                        bytag[tagname].append(mdline)

            playfile.write(f'{playline}\n' )

with codecs.open('items.md', 'w', encoding='utf-8-sig') as itemfile:    
    for tagstr in bytag.keys():
        sectionname = tagstr
        if sectionname == '':
            sectionname = 'Uncategorized'
        itemfile.write(f'### {sectionname}\n')
        itemfile.write('English | ʔay̓aǰuθəm\n')
        itemfile.write('--- | ---\n')
        for mdline in bytag[tagstr]:
            itemfile.write(f'{mdline}\n')
        itemfile.write('\n')











