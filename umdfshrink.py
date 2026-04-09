lines:list[str]

blocked = [
    "skill6"
    "skill7"
    "skill8"
    "coop"
    "dm"
    "class2"
    "class3"
    "class4"
    "class5"
    "xpanningfloor"
    "ypanningfloor"
    "xpanningceiling"
    "ypanningceiling"
    "rotationfloor"
    "rotationceiling"
]

with open("TEXTMAP.txt","rt") as tsf:
    lines = [lines.strip() for line in tsf]

i = 0
while(i < len(lines)):

    #trim useless newlines
    if(lines[i] == "{"):
        lines[i-1].append("{")
        lines.pop(i)
        continue

    #Remove Empty lines
    if(lines[i] == ""):
        lines.pop(i)
        continue

    #Strip out redundant flags
    for keyword in blocked:
        if (keyword in lines[i]):
            lines.pop(i)
            continue

    #Defloat keyvalues
    for j in range(len(lines[i])):
        if lines[i][j] == '.':
            lines[i] = lines[i][0:j]
            lines[i][j] = ';'
        if lines[i][j+1] == ' ' and lines[i][j+2] == '/' and lines[i][j+3] == '/':
            lines[i] = lines[i][0:j]

    i += 1

with open("TEXTMAP_EXP.txt","wt") as tsf:
    tsf.write("\n".join(lines))
        