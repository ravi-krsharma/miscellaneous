

import os

new_licence = """
# 
# ©2023, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.
# 
""" 


def get_copyright_and_comment(txt):
    got_copyright = ""
    got_licence = False
    getting_comment = False
    comment = []
    linenum = 0
    for line in txt.splitlines():
        linenum += 1

        def strip(s):
            return s.strip("* /")

        if line.startswith(" */"):
            break
        if line.startswith(" * Copyright (C)"):
            got_copyright = strip(line)
            continue
        if got_copyright and line.startswith(" * You should have received a copy of the GNU General Public License"):
            got_licence = True
            continue
        if got_copyright and got_licence and line.startswith(" * Boston"):
            getting_comment = True
            continue

        if getting_comment and line != " *":
            comment.append(strip(line))

    return got_copyright, comment, linenum

def generate_header(people, comment):
    header = "/*\n"
    for p in people:
        header += " * %s\n" % p
    header += new_licence
    for c in comment:
        header += " * %s\n" % c
    header += " */\n"
    return header

def update_source(filename):
    print(filename)
    fdata = file(filename, "r+").read()
    if fdata.count("This file is part of wasp, some code taken from paparazzi (GPL)"):
        print("\tskip")
        return
    elif fdata.count("You should have received a copy of the GNU General Public License"):
        old_author, comments, linenum = get_copyright_and_comment(fdata)
        header = generate_header([old_author], comments)
        print("\tupdate")
    else:
        linenum = 0
        header = generate_header([], [])
        print("\tadd")

    f = file(filename,"w")
    f.write(header)
    for l in fdata.splitlines()[linenum:]:
        f.write(l)
        f.write("\n")

def recursive_traversal(dir, excludedir):
    fns = os.listdir(dir)
    print("listing "+dir)
    for fn in fns:
        fullfn = os.path.join(dir,fn)
        if fullfn in excludedir:
            continue
        if os.path.isdir(fullfn):
            recursive_traversal(fullfn, excludedir)
        else:
            if fullfn.endswith(".c") or fullfn.endswith(".h"):
                update_source(fullfn)

if __name__ == "__main__":
    recursive_traversal(".", ["./generated", "./arm7/lpcusb", "./arm7/include"])