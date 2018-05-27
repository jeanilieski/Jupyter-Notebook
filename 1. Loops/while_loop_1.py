while True:
    line=raw_input('>')
    if line[0]=='#':#if the first caracter of the line is "#" print nothing but continue
        continue
    if line=='done':
        break
    print line
print 'end'
