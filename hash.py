#
f = open("/home/wow/文档/Cached Ticket-cmd-ny.log","r") w = open("/home/wow/文档/hash1.txt","w") lines = f.readlines() length = len(lines) i=0 number =[] while i<length:

if lines[i].find('RID')>=0 and lines[i+1].find('User')>=0 and lines[i+2].find('LM')>=0 and lines [i+3].find('NTLM')>=0:
    if len(lines[i+2])>10 and lines[i+1].find('$')<0:
        if lines[i][17:len(lines[i])-2] not in number:
            mixline = lines[i+1][7:len(lines[i+1])-1]+':'+lines[i][17:len(lines[i])-2]+':'+lines[i+2][7:len(lines[i+2])-1]+':'+lines[i+3][7:len(lines[i+3])-1]+':::'
            w.write(mixline)
            w.write('\n')
            number.append(lines[i][17:len(lines[i])-2])
else:
    pass
i=i+1
