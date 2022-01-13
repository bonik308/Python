import re

ls = []
ls.append(re.compile("^\d{1,3}(?:[.-]\d{1,3}){3}|[0-9a-fA-F]{1,4}(?:[:-][0-9a-fA-F]{1,4}){7}"))
ls.append(re.compile("\d\d[\/]\w+[\/]\w+(?:[:-]\d{2}){3}[ +][+]\d\w+"))
ls.append(re.compile("[G][E]\w+|[P][O]\w+"))
ls.append(re.compile("(?:[\/][d,p]\w*){2,5}"))
ls.append(re.compile(" \d{3} "))
ls.append(re.compile("\d \"\-\""))

def reg_exper(line):
    data = ''
    for i in ls:
        data = data + ''.join(re.findall(i, line)).rstrip().lstrip() + ', '
    return data.replace('  ', '').replace(' "-",', '')

with open('nginx_logs.txt', 'r', encoding='UTF8') as f:
    file_data = (i.rstrip().lstrip() for i in f.readlines())
for line in file_data:
    print(reg_exper(line))