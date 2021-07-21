``` nohighlight
#####################################################################################
### radtools: what CLI tools can I create to help with my discourse doc workflow? ###
#####################################################################################

# what is the naming convention for these tools?

All of these tools begin with 'rad', e.g. 'radpush'.

This seems safe, since 'apt list rad*' doesn't produce any package names.

# what ops in my doc workflow need automating?

## what basic discourse operations need automating?

### how do i push markdown to the primary post of a discourse API/topic?

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
