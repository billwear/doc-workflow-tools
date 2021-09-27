#!/usr/bin/python3

# what libraries does this program need?
import getopt, sys, errno, maas_discourse, json, re
import os.path
from os import path

# set/unset the debug parameter
debug = False

# how do we print the usage instructions (and exit)?
def usage():
    print("usage: md2org [-i INPUT_FILE] [-o OUTPUT_FILE]")
    sys.exit(errno.EINVAL)

def wrap_line(line, out_lines):
    out_lines.append("#+BEGIN_EXPORT HTML\n")
    out_lines.append(line)
    out_lines.append("#+END_EXPORT HTML\n")

# what is the main execution flow?
def main():

    # can we successfully get valid program options?
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(errno.EINVAL)

    # where do i store the option values?
    output_file = "stdout"
    input_file = "stdin"

    # how do i pull out the options?
    for o, a in opts:
        if o == "-i":
            input_file = a
        elif o == "-o":
            output_file = a
        else:
            assert False

    # create an out_lines buffer list
    out_lines = []
    
    # decide whether to read stdin or a file
    if input_file == "stdin":
        # read from stdin
        if debug == True:
            print("reading from stdin")
        lines = sys.stdin.readlines()
    else:
        # read from file
        if debug == True:
            print("reading from file", input_file)
        file1 = open(input_file, 'r')
        lines = file1.readlines()
        file1.close()

    # print all lines that have "<a href" in them
    for line in lines:
        if "<a href" in line:
            try:
                x = re.search("<h([0-9]*)",line).group(1)
                pattern = r'<a href=.*"><h.*">'
                newline = re.sub(pattern, '', line)
                pattern = r'</h.*>'
                newline = re.sub(pattern, '', newline)
                out_lines.append("*" * int(x) + " " + newline)
                if debug == True:
                    print("x is", x)
                
            except:
                if debug == True:
                    print("skipping non-heading href")
                    pass
            wrap_line(line, out_lines)
        elif "details>" in line or "summary>" in line:
            wrap_line(line, out_lines)
        elif "rad-begin" in line or "rad-end" in line:
            out_lines.append("# " + line)
        elif "](" in line:
            linklist = re.findall("\[([^\]]*)\]\(([^)]*)\)", line)
            for i in linklist:
                oldlink = "\["+i[0]+"\]\("+i[1]+"\)"
                oldlink = oldlink.replace("?","\?")
                newlink = "[["+i[1]+"]["+i[0]+"]]"
                line = re.sub(oldlink, newlink, line)
            out_lines.append(line)
        elif "#" in line:
            try:
                x = re.search("^([#]*)",line).group(1)
                line = re.sub(x, "*"*int(len(x))+" ", line)
                out_lines.append(line)
            except:
                out_lines.append(line)
        else:
            out_lines.append(line)
    
    # decide whether to write to stdout or a file
    if output_file == "stdout":
        # write to stdout
        if debug == True:
            print("writing to stdout")
        for line in out_lines:
            sys.stdout.write(line)
    else:
        # write to file
        if debug == True:
            print("writing to file", output_file)
        file1 = open(output_file, 'w')
        file1.writelines(out_lines)
        file1.close


if __name__ == '__main__':
    main()