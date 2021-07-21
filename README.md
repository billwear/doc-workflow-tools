# radtools

CLI tools to help with a remote doc publishing workflow

## Naming Convention

All of these tools begin with 'rad', e.g. 'radpush'.  This seems safe, since 'apt list rad*' doesn't produce any package names.

## radpush(7)

### NAME
   radpush - push markdown text to discourse

### SYNOPSIS
    radpush [-pl] {[-f <markdown filename>] -t topic_number} | -F filename-topicno.md` 


`radpush` takes its input from `stdin` by default, but it will take its input from a file instead, if either the `-f` or `-F` options are specified.  `radpush` requires a topic number in one of the two forms listed above:

* if the base markdown filename terminates with a "-#", where "#" is the topic number, using the `-F` option will indicate to `radpush` that it must pick up the topic number from that filename.  If no topic number can be deduced from the `-F filename`, the program prints an error and exits.

* if the markdown comes in via `stdin` or a `-f filename` option, the topic number must be supplied by the `-t` option, regardless of whether a topic number is embedded in the filename.

With the `-F` option, wildcards may be used, since `radpush` can pick up the topic numbers from the individual filenames.

`radpush` outputs nothing unless the `-p` ("print") or `-l` ("log") options are selected.

* The `-p` option will cause `radpush` to output the JSON for each topic pushed to stdout, as the push is completed.  Note that `radpush` does not separate JSON output from multiple files, for example, if `-F` is used with a wildcard.

* The `-l` option causes `radpush` to create one JSON file for each topic pushed, labeled with `<base-filename-topicno>.json`.

Both options may be used, if desired.

-----

## radpull

```
radpull {-t <topic number> [-f <output filename]} | -T <topic range>

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
