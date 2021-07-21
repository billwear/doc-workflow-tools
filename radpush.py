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

# what libraries does this program need?
import getopt, sys, errno, maas_discourse, json
ENOERR = 0

# how do we print the usage instructions (and exit) ?
def usage():
    print('usage: radpush [-pl] {[-f FILENAME] -t TOPIC_NUMBER} | -F ENCODED_FILENAME | {-c -T "title string"}')
    sys.exit(errno.EINVAL)

# what is the main execution flow?
def main():

    # can we successfully get valid program options?
    try:
        opts, args = getopt.getopt(sys.argv[1:], "plf:t:F:cT:C:")
    except getopt.GetoptError as err:
        print(err)
        sys.exit(errno.EINVAL)

    # how do i know if they didn't type enough options?
    if len(sys.argv) < 2:
        usage()

    # where do i store the option values?
    printout = False
    log      = False
    create   = False
    filename = ""
    topic    = 0
    encfile  = ""
    title    = ""
    credfile = "/etc/rad/dc.yaml"

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
            topic = a
        elif o == "-F":
            encfile = a
        elif o == "-T":
            title = a
        elif o == "-C":
            credfile = a
        else:
            assert False

    # how do i make sure the options don't conflict with each other?
    # `radpush [-pl] {[-f FILENAME] -t TOPIC_NUMBER} | -F ENCODED_FILENAME | {-c -T "title string"}`
    if filename != "" and topic == 0:
        print("radpush: missing topic for filename", filename)
        usage()

    if filename != "" and encfile != "":
        print("radpush: contradictory options: -f and -F")
        usage()

    if filename != "" and create == True:
        print("radpush: contradictory options: -f and -c")
        usage()

    if filename != "" and title != "":
        print("radpush: contradictory options: -f and -T")
        usage()

    if topic != 0 and encfile != "":
        print("radpush: contradictory options: -t and -F")
        usage()

    if topic != 0 and create == True:
        print("radpush: contradictory options: -t and -c")
        usage()

    if topic != 0 and title != "":
        print("radpush: contradictory options: -t and -T")
        usage()

    if encfile != "" and create == True:
        print("radpush: contradictory options: -F and -c")
        usage()

    if encfile != "" and title != "":
        print("radpush: contradictory options: -F and -T")
        usage()

    if create == True and title == "":
        print("radpush: create option set, but no document title given")
        usage()

    if create == False and title != "":
        print("radpush: document title given, but create option not set")
        usage()

    # make sure we can get the credentials; if not, error output

    # since there are no contraditions, what does the user want to do?
    ## does the user want to just send stdin to a discourse topic?
    if topic != 0 and filename =="":
        error, credentials = maas_discourse.md_get_credentials(credfile)
        if error != ENOERR:
            print("radpush: error", error, "trying to retrieve API credentials")
            sys.exit(errno.EINVAL)

        # how do i load the markdown to post?
        markdown = sys.stdin.read()

        # how do i get the topic_json?
        error, topic_json = maas_discourse.md_api_get_topic( topic, credentials)
        if error != ENOERR:
            print("error number", error," trying to retrieve topic", topic, "from discourse")
            sys.exit(errno.EINVAL)

        # how do i get the post_id?
        error, post_number = maas_discourse.md_get_post_number(topic_json)
        if error != ENOERR:
            print("error number", error," trying to retrieve post_id from ", topic, "JSON")
            sys.exit(errno.EINVAL)

        # how do i write the markdown file to discoure?
        error, new_json = maas_discourse.md_api_put_post( post_number, markdown, credentials )
        if error != ENOERR:
            print("error number", error," trying to write new markdown to", topic, "in discourse")
            sys.exit(errno.EINVAL)

        if log == True:
            outfile = "stdin-"+topic+".json"
            f = open(outfile, "w+")
            f.write(json.dumps(new_json))
            f.close

        if printout == True:
            sys.stdout.write(json.dumps(new_json))

    ## does the user want to send a specific file to a discourse topic?
    elif topic != 0 and filename != "":
        print("send markdown from", filename, "to discourse topic", topic)

    ## does the user want to use encoded filename(s) to send markdown?
    elif encfile != "":
        print("use", encfile, "to send markdown to discourse")

    ## does the user want to create a new topic?
    elif create == True:
        print("create a new topic entitled", title)

if __name__ == '__main__':
    main()
