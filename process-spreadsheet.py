import codecs
import os

with codecs.open('spreadsheet.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with codecs.open('items.md', 'w', encoding='utf-8-sig') as itemfile:    
        for line in lines[1:]:
            fields = line.split('\t')
            if len(fields) >= 6: 
                tape, starttime, endtime, english, translated, tags = fields[:6]
                if starttime and endtime:
                    mins, secs = starttime.split(':')[:2]
                    ident = tape + f'_{int(mins):02}{float(secs):02.0f}'

                    clipfile = f'clips/{ident}.wav'
                    clipcommand = f'ffmpeg -y -i audio/{tape}.wav -ss {starttime} -to {endtime} website/static/{clipfile}'
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

                    itemfile.write(f'{english} | <a href="{clipfile}">{translated}</a>\n' )








