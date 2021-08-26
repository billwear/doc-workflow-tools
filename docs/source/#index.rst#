.. radtools documentation master file, created by
   sphinx-quickstart on Thu Aug 26 09:57:35 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

NAME
====

radtools - "Remote Access to Discourse" tools: permits remote editing of
discourse markdown and use of command line tools for text processing

SYNOPSIS
========

radget -t TOPIC_NUMBER [-a AUTH_FILE]
-------------------------------------

print discourse TOPIC_NUMBER markdown to STDOUT

radput -t TOPIC_NUMBER [-a AUTH_FILE]
-------------------------------------

replace discourse TOPIC_NUMBER with markdown from STDIN

radnew -T TITLE STRING [-a AUTH_FILE]
-------------------------------------

create a new discourse topic loaded with markdown from STDIN, returning
the newly-assigned topic number to STDOUT

raddel -t TOPIC_NUMBER [-a AUTH_FILE]
-------------------------------------

delete discourse topic TOPIC_NUMBER

radf -b begin marker -e end marker -s selector
----------------------------------------------

filter a markdown document, including all sections bracketed with "begin
marker" and "end marker" for which "selector" is present on the "begin
marker" line, and excluding all other such bracketed sections; takes
input from STDIN and issues output to STDOUT

radlastmod -t TOPIC_NUMBER
--------------------------

retrieves the last modtime and the username of the user making that mod
to STDOUT as a comma-separated tuple

DESCRIPTION
===========

**radtools** allow a user to edit discourse topics remotely, on any
desired text editor. They provide the basic functionality to:

   - put and get topics.

   - create new topics.

   - delete topics.

   - get the time and username associated with the last modification.

   - use an arbitrary filter system to include and exclude text
   sections.

In addition, there are three special tools designed to handle the
Canonical RAD ("Reader Adaptive Documentation") format:

   - radRdbload, which captures URLs v. topic numbers for a Canonical
   doc set.

   - radRlink, which converts "/t/topic-slug/nnnn" to the correct RAD
   link.

   - radRmenu, which adds a RAD menu for "topic-slug" to the top of the
   output.

The special tools are specific to the MAAS documentation set, so they
aren't explained in manpages, but they're available as examples if you
can use them.

radget
------

**radget** is designed to get a discourse topic, by number, and print
the markdown for the main topic post to STDOUT. It deals with the main
topic post because that is where most discourse-related documentation
resides. If it's useful to someone, it should be relatively simple to
add a numeric argument to the argument list to indicate which post is
desired. Just remember that only post number 1 (the main post) is
guaranteed to be part of a discourse topic.

radput
------

**radput** is designed to take markdown coming into STDIN and replace
the markdown for the main post of the passed topic number with this
incoming markdown.

radnew
------

**radnew** creates an entirely new post, loaded with the passed
markdown. It returns the newly-assigned topic number to STDOUT for user
convenience; it's up to the user to figure out how to capture and employ
that new topic number.

raddel
------

**raddel** deletes the passed discourse topic entirely. This makes the
topic invisible to non-administrative users. No warning is given,
although for most discourse systems, topics can be manually "undeleted"
for an indefinite period of time.

radlastmod
----------

**radlastmod** returns the last edited time and the last editing user to
STDOUT, as a comma-separated tuple. The last edited time is in whatever
timezone your chosen discourse instance is using, usually Zulu time.
Conversion and use of the output timestamp is up to the end user. The
last edited user is printed as the username of the account which
performed this last edit. Cross-referencing that username to the
discourse user list is up to the end user.

As an aside, **radlastmod** shouldn't be needed too much. There is a
wonderful report (the Post Edit report) that discourse generates, which
is way faster, much less stress on the system, and much easier to see
what changed. Even if you use radlastmod, cleverly in a shell script, to
get the list of last mods and who modded, you'll still have to go look
at the changes, which means pulling down text and then generating
similar, side-by-side text for a diff, and.... Nevermind all that; just
use the discourse report, it's much easier. But the tool is here if you
want to use it.

radf
----

**radf** filters markdown received via STDIN according to command-line
options, and outputs the filtered markdown to STDOUT. A simple example
is the easiest illustration.

Suppose that you have sections of your document that you want to include
or exclude, depending on which edition of a document you're publishing.
You can use any sort of string for the "begin marker" and "end marker,"
as long as (1) it's consistent, and (2) it won't appear organically in
your markdown text.

Markers must appear on lines above and below the text being marked, with
the "begin marker" line also carrying one or more selectors. Selectors
are simply any text string that you'd like to user to identify sections
for inclusion or exclusion. Selectors can appear elsewhere in your
markdown text, because only the presence of the "begin marker" + the
selector triggers a filtering operation.

For example, if you have two different versions of your product, you
might have two paragraphs marked like this:

   | my-begin-marker Windows
   | Here is some text relevant to your Windows product. It can be
     anything you want, and it can contain any text that isn't the begin
     or end markers. It can be as long or as short as you want.
   | my-end-marker

   | my-begin-marker Ubuntu-20.04
   | Here is different text, relevant instead to your Ubuntu 20.04
     version. Likewise, it can be anything you want, and it can contain
     any text that isn't the begin or end markers, even the selector
     itself:

      sudo lsb_release Ubuntu-20.04

   | It can also be as long or short as you want, and contain images,
     links, or any other valid markdown.
   | my-end-marker

When you filter the above text like this:

   radf -b "my-begin-marker" -e "my-end-marker" -s "Windows"

then your STDOUT will contain the paragraph marked with "Windows", but
none of the text marked with "Ubuntu-20.04," like this:

   Here is some text relevant to your Windows product. It can be
   anything you want, and it can contain any text that isn't the begin
   or end markers. It can be as long or as short as you want.

Special-purpose tools
=====================

A few special tools are currently included with radtools, mainly because
they are (1) hard to make generic, (2) unlikely to have value as a
generic tool, and (3) probably going away, or at least changing
unrecognizably, as Canonical documentation changes over time. For these
reasons, it seemed unnecessary to spend the additional 80% of the effort
for less than 20% of the gain. If this balance flips, additional tools
will be added to the base set.

If none of this section makes any sense to you as written, you probably
don't need these tools for anything much. Of course, you're still free
to play with them on your own discourse, if you want.

What is valuable about these special tools is the general pattern of the
code, which should give you a good start on writing your own special
purpose tools for your own situation, and including them in this github
with similar doc. Nothing wrong with having a big set of special purpose
tools: Eventually, one of them will be close enough to something
somebody else needs to save them some serious time. That's what FOSS is
all about, anyway.

An example: radRmake
--------------------

In this shell script, we can see the power of these tools, combined with
the command line. With this script, I can make all RAD versions of any
master document, without looking up topic numbers or URLs.

Here's the entire script:

   sqlite3 /etc/rad/rad.db 'select \* from links' \| grep $1 \| grep -v
   "2`7" \| grep -v "2`8" \| cut -f2,3 -d"|" \| cut -f3- -d"/" \| sed -e
   's/|/ /g' \| sed -e 's/^//' \| sed -e 's/i/i /' \| awk '{print "cat
   /home/stormrider/git/maas-offline-docs/src/" $2 ".md \| radf -b
   rad-begin -e rad-end -s " $1 " \| radRlink -s " $1 " \| radRmenu -b "
   $2 " \| radput -t " $3}' > /tmp/Rmake.sh chmod 777 /tmp/Rmake.sh
   /tmp/Rmake.sh rm /tmp/Rmake.sh

It's pretty simple, and it takes a base URL fragment (the shell $1, in
the second line) to match. By judiciously using that grep string, you
can match quite a few of the topics (for example, if you enter
"machines" as a grep fragment, you'll update "Machines," "Deploy
machines," "Commission machines," "Add machines," ....

Note that wildcards don't work the same in this context, but because of
delays that the discourse server inserts when you have more than 10-15,
back-to-back requests, a massive, full-set make isn't really do-able
anyway.

maas_discourse.py
-----------------

There is also the **maas_discourse.py** Python library, which contains
generic routines for communicating with a discourse server. It is called
"maas"_discourse because it hasn't been vetted against any other
discourse server, so it's not clear whether it's completely generic. It
should be, but YMMV, hence the name.

**radtools** are implemented in Python. They are designed to be standard
UNIX CLI tools, taking input from STDIN and sending it to STDOUT
wherever that makes sense. Command line options and usage messages are
also styled after UNIX CLI utilities.

HISTORY
=======

**radtools** grew out of a different instance also labeled "RAD," the
Canonical Reader Adaptive Documentation project. That project was
intended to be a temporary stopgap measure until a better interface
could be designed and implemented.

The practice of remote editing, though, is extremely useful to someone
preparing documentation for discourse, because:

   - it is often useful to have an entire doc set, in plain text,
   available to grep.

   - it is faster and more efficient to work in one's preferred text
   editor.

   - it is possible to apply UNIX CLI tools to the text when editing
   documents.

   - it is possible to keep a complex master, that is, a master which
   contains several versions of the documentation, but for which only
   one version is published at a time.

Since the shape of Canonical documentation is always evolving (a good
thing), and since it's not very FOSS-friendly to write and later discard
useful scripts, I decided to make these tools generic and public.

The goal was to write the minimum necessary complement of tools to be
able to build special-case scripts for (potentially) temporary
situations. Where there were MAAS-specific format requirements, I just
create special scripts.

FILES
=====

There are two helper files which enable **radtools** to operate more
efficiently: the **dc.yaml** and **rad.db** files.

**dc.yaml** is an API authorization file that contains the username, API
key, and API URL for the discourse API being accessed. **rad.db** is a
SQLITE3 database mapping Canonical discourse URLs to discourse topic
numbers (only useful for Canonical documentation pages). Both of these
reside by default in the directory "/etc/rad".

AUTHOR
======

| Bill Wear

   | wowear@gmail.com
   | bill.wear@canonical.com
   | https://stormrider.io
   | WA5149-SWL

GITHUB REPOSITORY
=================

This utility is part of the radtools repository at
https://github.com/billwear/radtools/.

LICENSE
=======

This software is covered by the Simplifed BSD License, described at
https://opensource.org/licenses/BSD-2-Clause.
