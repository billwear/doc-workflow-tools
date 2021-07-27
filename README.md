# radtools

## radtools quick reference

```
radget -t TOPIC_NUMBER [-a AUTH_FILE] - print discourse TOPIC_NUMBER markdown to STDOUT

radput -t TOPIC_NUMBER [-a AUTH_FILE] - replace discourse TOPIC_NUMBER with markdown from STDIN

radnew -T "TITLE STRING" [-a AUTH_FILE] - create a new discourse topic loaded with markdown from STDIN, returning the newly-assigned topic number to STDOUT

raddel -t TOPIC_NUMBER [-a AUTH_FILE] - delete discouse topic TOPIC_NUMBER

radf -b "begin marker" -e "end marker" -s "selector" - filter a markdown document, including all sections bracketed with "begin marker" and "end marker" for which "selector" is present on the "begin marker" line, and excluding all other such bracketed sections; takes input from STDIN and issues output to STDOUT

radlastmod -t TOPIC_NUMBER - retrieves the last modtime and the username of the user making that mod to STDOUT as a comma-separated tuple
```

## About radtools

radtools allow a user to edit discourse topics remotely, as markdown, on any desired text editor.  They provide the basic functionality to:

 * put and get topics.
 * create new topics.
 * delete topics.
 * get the time and username associated with the last modification.
 * use an arbitrary filter system to include and exclude sections.

In addition, there are three special tools designed to handle the Canonical RAD ("Reader Adaptive Documentation") format:

 * radRdbload, which captures URLs v. topic numbers for a Canonical doc set.
 * radRlink, which converts "/t/topic-slug/nnnn" to the correct RAD link.
 * radRmenu, which adds a RAD menu for "topic-slug" to the top of the output.

radtools are implemented in Python. They are designed to be standard UNIX CLI tools, taking input from STDIN and sending it to STDOUT wherever that makes sense.  Command line options and usage messages are also styled after UNIX CLI utilities.

### History

radtools grew out of a different instance also labeled "RAD," the Canonical Reader Adaptive Documentation project.  That project was intended to be a temporary stopgap measure until a better interface could be designed and implemented.  The practice of remote editing, though, is extremely useful to someone preparing documentation for discourse, because:

 * it is often useful to have an entire doc set, in plain text, available to grep.
 * it is faster and more efficient to work in one's preferred text editor.
 * it is possible to apply UNIX CLI tools to the text when editing documents.
 * it is possible to keep a complex master, that is, a master which contains several versions of the documentation, but for which only one version is published at a time.

Since the shape of Canonical documentation is always evolving (a good thing), and since it's not very FOSS-friendly to write and later discard useful scripts, I decided to make these tools generic and public.  Where there were specific format requirements, I created special, limited-purpose tools to cover those (most likely temporary) situations.

### Helper files

There are two helper files which enable radtools: dc.yaml, and rad.db.  dc.yaml is an API authorization file that contains the username, API key, and API URL for the discourse API being accessed.  rad.db is a SQLITE3 database mapping Canonical discourse URLs to discourse topic numbers (only useful for Canonical documentation pages).  Both of these reside by default in the directory "/etc/rad", although both of them can be entered on the approrpriate command lines, if desired. 

### About the tools

The following section gives explains the operation of each tool.

#### radget

radget is designed to get a discourse topic, by number, and print the markdown for the main topic post to STDOUT.  It deals with the main topic post because that is where most discourse-related documentation resides.  If it's useful to someone, it should be relatively simple to add a numeric argument to the argument list to indicate which post is desired.  Just remember that only post number 1 (the main post) is guaranteed to be part of a discourse topic.

#### radput

radput is designed to take markdown coming into STDIN and replace the markdown for the main post of the passed topic number with this incoming markdown.

#### radnew

radnew creates an entirely new post, loaded with the passed markdown.  It returns the newly-assigned topic number to STDOUT for user convenience; it's up to the user to figure out how to capture and employ that new topic number.

#### raddel

raddel deletes the passed discourse topic entirely.  This makes the topic invisible to non-administrative users.  No warning is given, although for most discourse systems, topics can be manually "undeleted" for an indefinite period of time.

#### radlastmod

radlastmod returns the last edited time and the last editing user to STDOUT, as a comma-separated tuple.  The last edited time is in whatever timezone your chosen discourse instance is using, usually Zulu time.  Conversion and use of the output timestamp is up to the end user.  The last edited user is printed as the username of the account which performed this last edit.  Cross-referencing that username to the discourse user list is up to the end user.

#### radf

radf filters markdown received via STDIN according to command-line options, and outputs the filtered markdown to STDOUT.  A simple example is the easiest illustration.

Suppose that you have sections of your document that you want to include or exclude, depending on which edition of a document you're publishing.  You can use any sort of string for the "begin marker" and "end marker," as long as (1) it's consistent, and (2) it won't appear organically in your markdown text.

Markers must appear on lines above and below the text being marked, with the "begin marker" line also carrying one or more selectors.  Selectors are simply any text string that you'd like to user to identify sections for inclusion or exclusion.  Selectors can appear elsewhere in your markdown text, because only the presence of the "begin marker" + the selector triggers a filtering operation.

For example, if you have two different versions of your product, you might have two paragraphs marked like this:

```
my-begin-marker Windows
Here is some text relevant to your Windows product.  It can be anything you want, and it can contain any text that isn't the begin or end markers.  It can be as long or as short as you want.
my-end-marker

my-begin-marker Ubuntu-20.04
Here is different text, relevant instead to your Ubuntu 20.04 version.  Likewise, it can be anything you want, and it can contain any text that isn't the begin or end markers, even the selector itself:

 sudo lsb_release
 Ubuntu-20.04

It can also be as long or short as you want, and contain images, links, or any other valid markdown.
my-end-marker
```

When you filter the above text like this:

```
radf -b "my-begin-marker" -e "my-end-marker" -s "Windows"
```

then your STDOUT will contain the paragraph marked with "Windows", but none of the text marked with "Ubuntu-20.04."

### About the special tools

Three special tools are currently included with radtools, mainly because they are (1) hard to make generic, (2) unlikely to have value as a generic tool, and (3) probably going away, or at least changing unrecognizably, as Canonical documentation changes over time.  For these reasons, it seemed unnecessary to spend the additional 80% of the effort for less than 20% of the gain.  If this balance flips, additional tools will be added to the base set.

If none of this section makes any sense to you as written, you probably don't need these tools for anything much.  Of course, you're still free to play with them on your own discourse, if you want.

What is valuable about these special tools is the general pattern of the code, which should give you a good start on writing your own special purpose tools for your own situation, and including them in this github with similar doc.  Nothing wrong with having a big set of special purpose tools: Eventually, one of them will be close enough to something somebody else needs to save them some serious time.  That's what FOSS is all about, anyway.

#### radRdbload

This tool uses the calling sequence:

```
radRdbload -d DB_FILE_NAME -n INDEX_TOPIC_NUMBER [-a AUTH_FILE]
```

This file consults the URL table in the bottom of the Canonical documentation discourse main index topic INDEX_TOPIC_NUMBER and writes a list of fully-qualifed doc URLs against a list of topic numbers.  This DB can be used by the other RAD special tools to speed up their work, by consulting the database instead of pulling the main index topic every time to figure out which URL goes with which topic number.

#### radRlink

The calling sequence is:

```
radRlink -s selector
```

Since each RAD file is a unique combination of packaging method, product version, and interface (e.g., "/snap/3.0/UI"), any links to other documents need to be adjusted to point to the correct version of the linked file.  For example, "About MAAS (snap/3.0/ui)" has to point to "High availability (snap/3.0/ui)" and not some other RAD version of the high availability document.

Discourse links depend on topic numbers, not recognizable titles, so if I have eight different RAD versions going at the same time, I would have to repeat each link-containing paragraph eight times, changing only the topic numbers for the links.  That's unnecessary work.

Instead, I can supply a known base URL in the link, use "nnnn" for the topic number, and allow radRlink to insert the correct topic number as each RAD version is generated.  It looks like this, for example:

```
...[High availability](/t/high-availabilty/nnnn)...
```

The radRlink tool will find these patterns, go look up the correct topic number for whatever version of the document is currently being generated (based on the selector), and replace the "nnnn" with the correct topic number.  It saves a tremendous amount of effort and more than a little disk space.

#### radRmenu

The calling sequence for this tool is:

```
rmenu -b base_url
```

Every RAD document needs a link menu at the top, which allows users to select the version of the document they want to see. Ideally, selecting a specific RAD version of one document should automatically make all the links and navigation point to that same version, but that's still being implemented at this writing.  As a temporary accommodation, these menus go at the top of every document:

```
|      |    2.9   |    3.0   |
|------|----------|----------|
| SNAP | CLI ~ UI | CLI ~ UI |
|  DEB | CLI ~ UI | CLI ~ UI |
```

If the user happens to be looking at the SNAP 2.9 UI version, but wants to see the DEB 3.0 CLI version, they can easily get there from this menu.  Again, this is just intended as a stopgap, so if this doesn't interest you or doesn't mean anything to you, no need to worry about it.

