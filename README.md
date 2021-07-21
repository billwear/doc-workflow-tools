# radtools

CLI tools to help with a remote doc publishing workflow

## Naming Convention

All of these tools begin with 'rad', e.g. 'radpush'.  This seems safe, since 'apt list rad*' doesn't produce any package names.

## radpush

```
radpush [-pl] {[-f <markdown filename>] -t topic_number} | -F filename-topicno.md` 
```

`radpush` takes its input from `stdin` by default, but it will take its input from a file instead, if either the `-f` or `-F` options are specified.  `radpush` requires a topic number in one of the two forms listed above:

* if the base markdown filename terminates with a "-#", where "#" is the topic number, using the `-F` option will indicate to `radpush` that it must pick up the topic number from that filename.  If no topic number can be deduced from the `-F filename`, the program prints an error and exits.

* if the markdown comes in via `stdin` or a `-f filename` option, the topic number must be supplied by the `-t` option, regardless of whether a topic number is embedded in the filename.

In the case of `-F` wildcards may be used, since `radpush` can pick up the topic numbers from the individual filenames.

`radpush` outputs nothing unless the `-p` ("print") or `-l` ("log") options are selected.  The `-p` option will cause `radpush` to output the JSON for each topic pushed to stdout, as the push is completed.  The `-l` option causes `radpush` to create one JSON file for each topic pushed, labeled with `<base-filename-topicno>.json`.

``` nohighlight
#####################################################################################
### radtools: what CLI tools can I create to help with my discourse doc workflow? ###
#####################################################################################


# what ops in my doc workflow need automating?

## what basic discourse operations need automating?


###### comes in from stdin

##### what is the topic number?

###### -t <topic-number>

#### what options are needed to make this tool flexible?

##### markdown filename can be used: -f <filename>

#### what options are needed to make this tool more flexible?

##### wildcard markdown files can be specified -F <filename/wildcard>
##### where <filename> = discourse-title-slug-#.md, where '#' is the topic number

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
