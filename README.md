# radtools


-----
## Naming Convention

All of these tools begin with 'rad', e.g. 'radpush'.  This seems safe, since 'apt list rad*' doesn't produce any package names.

-----

## radpush(7)

### NAME
**radpush** - push markdown text to discourse

### SYNOPSIS
`radpush [-pl] {[-f FILENAME] -t TOPIC_NUMBER} | -F ENCODED_FILENAME | {-c -T "title string"}`

### DESCRIPTION
**radpush** converts markdown text from FILENAME to discourse JSON and pushes it to a discourse TOPIC_NUMBER. Requires a topic number. Gets markdown from **stdin** in the absence of **[-fF]**.

**radpush** outputs nothing unless the **-p** ("print") or **-l** ("log") options are selected.

Mandatory arguments to long options are mandatory for short options too.

* **-c, --create** - create the topic if it doesn't exist; must be accompanied by a -T option to set the topic title.

* **-C, --credentials** - path to file where API credentials are found; if this option is not given, **radpush** will attempt to pull the needed credentials from `/etc/rad/dc.yaml`.

* **-f, --file=<u>FILENAME</u>** - specify a filename containing the markdown to push; if neither **-f** nor **-F** are used, **radpush** takes its markdown from **stdin**; must be accompanied by a -t option to set the topic number.

* **-F, --efile=<u>ENCODED_FILENAME</u>** - specify a specially-encoded filename, consisting of "anytitle-topicno.md" (e.g., my-updates-3947, where 3947 is the topic number that will be updated); wildcards may be used with this option.

* **-l, --log** - copy pushed discourse JSON to one JSON file per topic pushed, with filename "base-filename-topicno.json"

* **-p, --print** - copy pushed discourse JSON to **stdout**; does not separate JSON from multiple files, if wildcards are used with -F

* **-t, --topic=TOPIC_NUMBER** - discourse topic number to which the markdown should be pushed

* **-T, --title="title string"** - user-viewable title of the new topic, only used with -c option.

## FILES

**radtools** looks in `/etc/rad/dc.yaml` for API credentials if no **-C** option is given.

-----

## radpull(7)

### NAME
**radpull** - pull markdown text from discourse

### SYNOPSIS
radpull {-t <topic number> [-f <output filename]} | -T <topic range>

### DESCRIPTION
**radpull** pulls markdown text from one or more discourse topics and print it to `stdout` or to a specified filename(s).

`radpull` accepts the following options:

###### to stdout


###### -T <topic number list>

####### outputs topics from a list of topic numbers to filenames of the form <topic-slug-topicno.md>
####### topic numbers can be listed as ranges (e.g., 1-5), comma separated lists (3,6,98), or both
####### (1-5, 17, 28, 240-251)

##### how can this be made even more flexible, considering the inefficiency of pulling from discourse?

###### -m

####### used with -f or -T, sets the file's modtime to the last edit timestamp from discourse
####### using local system timezone; used with stdout, prints the last modified timestamp, using
####### local system timezone, immediately following the markdown output

###### -M

####### appends the username of the user last modifying the file to the end of the output,
####### regardless of whether -f, -T, or stdout are used to output the file

-----

``` nohighlight
#####################################################################################
### radtools: what CLI tools can I create to help with my discourse doc workflow? ###
#####################################################################################


### how do i pull markdown from the primary post of a discourse API/topic?


### how do i validate discourse markdown as well-formed?

### how do i spell-check the markdown?

### how do i change the title (not title slug) of a discourse API/topic?

### how do i get the timestamp when a discourse/API topic was last edited?

### how do i get the username of the person last editing a discourse/API topic?

### how do i diff a published version of a discourse/API topic with another version?

## what git operations need automating?

### how do i clone a master doc set to my cwd?

### how do i push repo changes from a clone with a specific commit comment?

### how do i reset a repo to remove staged changes?

### how do i check whether the upstream repo has been changed externally?

### how do i pull down a changed repo?

## what rad operations need automating?

### how do i create a specific rad version using selectors?

### how do i adjust rad links for a specific selector?

### how do i add rad menus for specific product versions?

## what HTML operations need automating?

### how do i create an HTML version of a document from discourse markdown?

## what emacs editing operations need automating?

## what workflow operations need scripting?

### how do i diff external edits with the master documentation?

### how do i produce a specific rad version from a master and push it to discourse?

### how do i produce an html doc set and place it in the build directory?

### how do i identify whether a master is newer than the published version?

### how do i identify whether a master is older than the published version?

### how do i identify when the master is the same as the published version?

### how do i set up a makefile which manages this workflow?
```
