lines:list[str]

blocked = [
    "skill6",
    "skill7",
    "skill8",
    "coop",
    "dm",
    "class2",
    "class3",
    "class4",
    "class5",
    "xpanningfloor",
    "ypanningfloor",
    "xpanningceiling",
    "ypanningceiling",
    "rotationfloor",
    "rotationceiling"
]

from os import chdir
from os.path import dirname,abspath
chdir(dirname(abspath(__file__)))

with open("TEXTMAP.txt","rt") as tsf:
    lines = [line.strip() for line in tsf]

i = 0
while(i < len(lines)):

    #trim useless newlines
    if(lines[i] == "{"):
        lines[i-1] += "{"
        lines.pop(i)
        continue

    #Remove Empty lines
    if(lines[i] == ""):
        lines.pop(i)
        continue

    #Strip out redundant flags
    for kwd in blocked:
        #print(f"{kwd=}, {lines[i]=}")
        if kwd in lines[i]:
            #print("removed")
            lines.pop(i)
            continue

    #Defloat keyvalues
    for j in range(len(lines[i])):

        if (lines[i][j] == '.'):
            lines[i] = lines[i][0:j]
            lines[i] += ";"
            break

        if (j > 1) and (lines[i][j-2] == ' ' and lines[i][j-1] == '/' and lines[i][j] == '/'):
            lines[i] = lines[i][0:j-2]
            break

    i += 1

print(i)

with open("TEXTMAP_EXP.txt","wt") as tsf:
    tsf.write("\n".join(lines))
        