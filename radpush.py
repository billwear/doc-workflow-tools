#!/usr/bin/python3

#
# ## radpush(7)
#
# ### NAME
# **radpush** - push markdown text to discourse
#
# ### SYNOPSIS
# `radpush [-pl] {[-f FILENAME] -t TOPIC_NUMBER} | -F ENCODED_FILENAME | {-c -T "title string"}`
#
# ### DESCRIPTION
# **radpush** converts markdown text from FILENAME to discourse JSON and pushes it to a discourse TOPIC_NUMBER. Requires a topic number. Gets markdown from **stdin** in the absence of **[-fF]**.
#
# **radpush** outputs nothing unless the **-p** ("print") or **-l** ("log") options are selected.
#
# Mandatory arguments to long options are mandatory for short options too.
#
# * **-c, --create** - create the topic if it doesn't exist; must be accompanied by a -T option to set the topic title.
#
# * **-f, --file=<u>FILENAME</u>** - specify a filename containing the markdown to push; if neither **-f** nor **-F** are used, **radpush** takes its markdown from **stdin**; must be accompanied by a -t option to set the topic number.
#
# * **-F, --efile=<u>ENCODED_FILENAME</u>** - specify a specially-encoded filename, consisting of "anytitle-topicno.md" (e.g., my-updates-3947, where 3947 is the topic number that will be updated); wildcards may be used with this option.
#
# * **-l, --log** - copy pushed discourse JSON to one JSON file per topic pushed, with filename "base-filename-topicno.json"
#
# * **-p, --print** - copy pushed discourse JSON to **stdout**; does not separate JSON from multiple files, if wildcards are used with -F
#
# * **-t, --topic=TOPIC_NUMBER** - discourse topic number to which the markdown should be pushed
#
# * **-T, --title="title string"** - user-viewable title of the new topic, only used with -c option.
#
#

import getopt, sys, errno

def usage():
    print('usage: radpush [-pl] {[-f FILENAME] -t TOPIC_NUMBER} | -F ENCODED_FILENAME | {-c -T "title string"}')

# step one: process options
def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "plf:t:F:cT:")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(errno.EINVAL)

    # how do i know if they didn't type enough options?
    if len(sys.argv) < 2:
        usage()
        sys.exit(errno.EINVAL)

    # where do i store the option values?
    printout = False
    log      = False
    create   = False
    filename = ""
    topic    = 0
    encfile  = ""
    title    = ""

    # how do i pull out the options?
    for o, a in opts:
        if o == "-p":
            printout = True
        elif o == "-l":
            log = True
        elif o == "-c":
            create = True
        elif o == "-f":
            filename = a
        elif o == "-t":
            topic = o
        elif o == "-F":
            encfile = a
        elif o == "-T":
            title = a
        else:
            assert False

    # check for conflicting/complementary options
    # `radpush [-pl] {[-f FILENAME] -t TOPIC_NUMBER} | -F ENCODED_FILENAME | {-c -T "title string"}`
    if filename != "" and topic == 0:
        print("radpush: missing topic for filename", filename)
        usage()
        sys.exit(errno.EINVAL)
    if filename != "" and encfile != "":
        print("radpush: contradictory options: -f and -F")
        usage()
        sys.exit(errno.EINVAL)
    if filename != "" and create == True:
        print("radpush: contradictory options: -f and -c")
        usage()
        sys.exit(errno.EINVAL)
    if filename != "" and title != "":
        print("radpush: contradictory options: -f and -T")
        usage()
        sys.exit(errno.EINVAL)
    if topic != 0 and encfile != "":
        print("radpush: contradictory options: -t and -F")
        usage()
        sys.exit(errno.EINVAL)
    if topic != 0 and create == True:
        print("radpush: contradictory options: -t and -c")
        usage()
        sys.exit(errno.EINVAL)
    if topic != 0 and title != "":
        print("radpush: contradictory options: -t and -T")
        usage()
        sys.exit(errno.EINVAL)
    if encfile != "" and create == True:
        print("radpush: contradictory options: -F and -c")
        usage()
        sys.exit(errno.EINVAL)
    if encfile != "" and title != "":
        print("radpush: contradictory options: -F and -T")
        usage()
        sys.exit(errno.EINVAL)
    if create == True and title == "":
        print("radpush: create option set, but no document title given")
        usage()
        sys.exit(errno.EINVAL)
    if create == False and title != "":
        print("radpush: document title given, but create option not set")
        usage()
        sys.exit(errno.EINVAL)

if __name__ == '__main__':
    main()
