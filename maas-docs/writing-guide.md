||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/writing-guide-snap-2-7-cli/3258) ~ [UI](/t/writing-guide-snap-2-7-ui/3259)|[CLI](/t/writing-guide-snap-2-8-cli/3260) ~ [UI](/t/writing-guide-snap-2-8-ui/3261)|[CLI](/t/writing-guide-snap-2-9-cli/3262) ~ [UI](/t/writing-guide-snap-2-9-ui/3263)|[CLI](/t/writing-guide-snap-3-0-cli/4185) ~ [UI](/t/writing-guide-snap-3-0-ui/4186)|
Packages|[CLI](/t/writing-guide-deb-2-7-cli/3264) ~ [UI](/t/writing-guide-deb-2-7-ui/3265)|[CLI](/t/writing-guide-deb-2-8-cli/3266) ~ [UI](/t/writing-guide-deb-2-8-ui/3267)|[CLI](/t/writing-guide-deb-2-9-cli/3268) ~ [UI](/t/writing-guide-deb-2-9-ui/3269)|[CLI](/t/writing-guide-deb-3-0-cli/4187) ~ [UI](/t/writing-guide-deb-3-0-ui/4188)|
This page contains detailed information on how to become a successful MAAS documentation writer. Welcome to the club.

<h2 id="heading--edit-rad">Update: Editing RAD/offline documentation</h2>

After 20 September 2020, many documents in the [MAAS documentation set](https://maas.io/docs) have been converted to the RAD (Reader Adapative Documentation) style, and enabled for conversion to offline documentation.  Editing RAD documentation is a bit different from standard doc, so it's worth explaining how to do it correctly.

First, some assurance: RAD is generated from a separate set of masters, published by a special tool called `xpub`, which prevents overwriting files that have been changed and warns the user that changes have been made.  Any changes you make to the doc will be noticed, at the latest, when an update is attempted, and your changes will be evaluated and, if reasonable, very likely added to the masters.  So don't worry about losing edits; we are trying to be very careful to make sure that doesn't happen.

That said, there is a bit of art to editing RAD pages and making sure your edits are suitable for offline doc conversion, namely, throughout RAD documents, you'll see HTML comments like this one:

    <!-- snap-2-11-cli snap-2-11-ui deb-2-11-cli deb-2-11-ui

Sometimes, they have multiple "tags" (e.g., `snap-2-6-cli` is a tag), and sometimes they only have one, like this:

    <!-- snap-2-11-cli

The tags should generally be self-explantory.  For example, the tag above refers to the snap delivery of MAAS version 2.11, specifically for someone using the CLI interface.

NOTE that is there no 2.11 version of MAAS: we've used an example that won't be accidentally processed by the RAD tools, but any version from 2.7 - 3.0 and beyond can be represented.


<h2 id="heading--contribution-overview">Contribution overview</h2>

Once you have permission to edit the doc, you can modify any article by choosing the link at the bottom, entitled, "Help improve this document in the forum."  Recognise that what you change will be posted instantly.  Check your work carefully before saving your edits!

Some questions to ask yourself as you are contributing:

* Does your reply improve the conversation in some way?

* Is your contribution kind to fellow community members?

* Is your constructive criticism focused on ideas, and not people?

* Are you certain of the technical accuracy of your contribution?

If you can answer these questions in the affirmative, your edits should be welcome.

<h2 id="heading--style-and-language">Style and language</h2>

Please follow these guidelines for style and language:

-   Use a spell checker.
-   Resist being overly formal.
-   Verify hyperlinks and examples.
-   Target audience: intermediate system administrator, not a developer.
-   Use British English (en-GB). See [language details](/t/language-details-contributing-to-maas-docs/745), including a comparison with American English (en-US).
-   Never break a hyperlink with a carriage return. 

Note that the document markup is not particularly complicated.  For the most part, if you rely on the formatting bar just above the editor window -- or use standard HTML -- you shouldn't have much difficulty.

<h2 id="heading--headers">Headers</h2>

Headers are simple to create, using standard HTML:

    <h2 id="optional-unique-id">Heading Level 2</h2>
    <h3 id="optional-unique-id">Heading Level 3</h3>
    ... and so on...
    
<h2 id="bold-and-italic">Bold and Italic Text</h2>

Bold and italic text can be indicated in two different ways.  You can use standard HTML markup:

    <strong>Bold Text</strong>
    <em>Italic Text</em>

You can also use the local editor markup:

    **strong**
    _italic_ (note that's just a single underbar)

<h2 id="heading--code-blocks">Code blocks</h2>

A code block (or pre-formatted text) is inserted by indenting four spaces:

    maas command do something
    maas command do something else
    ```
You can use this style anytime you want to present:

 - a command line sequence,
 - a pre-formatted block of text,
 - a block of text in which you need to escape markup sequences (as above),
 - a code listing where indentation and monospace font are important.

<h2 id="heading--inline-code">Inline code</h2>

Use a &lt;code&gt; tag to mark <code>inline filenames and other literals</code> as code examples. Alternatively, you can also use the `backtick`, like this:

    ...can also use the `backtick`, like this...

<h2 id="heading--notes">Admonishments</h2>

An admonishment distinguishes information from the rest of the text. The syntax begins with the markup tag <code>[note]</code> and ends with the corresponding closure <code>[/note]</code>:

    [note type="admonishment-type" status="Admonishment title"]
    Admonishment text.
    [/note]

Where:

-   `admonishment-type` can be 'Note', 'Warning', 'Positive', or 'Negative'.
-   `Admonishment title` is an optional title, formatted with whatever markups you desire.
-   `Admonishment text` is the text you wish to convey.

<h3 id="heading--admonishment-examples">Admonishment examples</h3>

<strong><em>Note Admonishment</em></strong>

A 'Note' type admonishment is marked up like this:

```
[note status="Note"]
If KVM-backed nodes are used, ensure that the 'maas' user on the rack
controller can connect to the KVM host using a passphraseless private SSH
key.
[/note]
```

And it will appear as:
[note status="Note"]
If KVM-backed nodes are used, ensure that the 'maas' user on the rack controller can connect to the KVM host using a passphraseless private SSH key.
[/note]

<strong><em>Warning Admonishment</em></strong>

Mark up a standard 'Warning' type admonishment this way:

``` no-highlight
[note type="caution" status="Warning"]
Data will be lost unless you do the right thing.
[/note]
```
And it will appear like this:

[note type="caution" status="Warning"]
Data will be lost unless you do the right thing.
[/note]

<strong><em>Positive Admonishment</em></strong>

A 'Positive' type admonishment should be entered as follows:

```
[note type="positive" status="High score"]
A positive note that should include a title.
[/note]
```
It will show up in the document like this:

[note type="positive" status="High score"]
A positive note that should include a title.
[/note]

<strong><em>Negative Admonishment</em></strong>

Finally, a 'Negative' type admonishment, with its title, could be marked up like this:

```
[note type="negative" status="Game over"]
A negative note that should include a title.
[/note]
```
And will look this way to the reader:

[note type="negative" status="Game over"]
A negative note that should include a title.
[/note]

<h2 id="heading--comments">Comments</h2>

Occasionally it may be appropriate to include a comment to explain or organise some text. This ends up as an HTML comment -- which can be read online, even if only in the browser inspection window -- so take it seriously:

```
<!--
The below text may be removed soon.
-->
```

<h2 id="heading--hyperlinks">Hyperlinks</h2>

Links to internal files or external URLs use the following format:

```
[visible text](URL)
```

The `visible text` is what will appear on the web page. The `URL` is used to refer to the destination, which is a  fully-qualified URL.  For example:

    Refer to [Google](https://www.google.com).

which would show up as "Refer to [Google](https://www.google.com)."

<h2 id="heading--images">Images</h2>

An image should not be overly cropped - allow for context. When ready, place the image file in the `uploads` directory.

In terms of linking, they are managed very similarly to hyperlinks. However, they are placed on their own line; are preceded by an exclamation point; and both the label and destination have a specific naming convention:

````
<a href="https://discourse.maas.io/uploads/default/original/1X/1f2e6cf2879e391e7ae1ad537cc9ce1baa119f86.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/1f2e6cf2879e391e7ae1ad537cc9ce1baa119f86.png"></a>
````
This image would appear in this way:

<a href="https://discourse.maas.io/uploads/default/original/1X/1f2e6cf2879e391e7ae1ad537cc9ce1baa119f86.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/1f2e6cf2879e391e7ae1ad537cc9ce1baa119f86.png"></a>

<h2 id="heading--tiered-sections">Tiered sections</h2>

You can create optional detail sections (something like and "in-line sidebar") by using these constructions:

    <details>
    <summary>this summary appears with an arrow next to it</summary>
    this text toggles when you click on the arrow
    <details>
    <summary>You can do multiple levels of this.</summary>
    this is yet another hidden level
    </details>
    </details>

This sequence would present like this in the finished document:

<details>
<summary>this summary appears with an arrow next to it</summary>
this text toggles when you click on the arrow
<details>
<summary>You can do multiple levels of this.</summary>
this is yet another hidden level
</details>
</details>

<h2 id="heading--capitalization">Capitalisation</h2>

Do not use a "Caps Everywhere" style. It is only used in level one headers and the title metadata. References (visible text) to these page titles (including the navigation) should just capitalise the first letter. Obviously, this does not pertain to words that should always be capitalised according to basic grammar rules (e.g. acronyms, proper nouns).


------
****
------
