MAAS bugs are reported via Launchpad. We'll provide the link in a moment, but first, some necessary prerequisites.

Filing a good bug report makes all the difference in how quickly we can triage and address your problem.  This brief how-to guide will walk you through the steps of filing a bug.  Some of these steps are necessary preparation, and the better you prepare before you file, the better the bug report.

[note]
Note that in the examples that follow, a `>>` symbol indicates the newest line added to the draft report.  It isn't necessary for you to type these characters.
[/note]

<a href="#heading--understand-rqmts"><h2 id="heading--understand-rqmts">Step 1: Understand what's required</h2>

You need to gather or prepare some information before you file your bug report.  Here is the short list of pre-filing tasks that will smooth the process:

* [Prepare a concise summary](#heading--concise-summary)
* [Identify your version and build first](#heading--version-and-build)
* [Explain whether you're using the UI, CLI, or API](#heading--which-interface)
* [Explain what happens](#heading--what-happens)
* [Explain how to reproduce your issue](#heading--reproducing-your-issue)
* [Take screenshots, if relevant](#heading--screenshots)
* [Locate and capture logfiles, if at all possible](#heading--logfiles)

Open a text editor with a new file, so you can capture and refine this information in advance.

<a href="#heading--concise-summary"><h3 id="heading--concise-summary">Prepare a concise summary</h3></a>

Keep your bug summary short and concise.  We recommend something of the form:

```text
<something specific happens> with MAAS <involved feature(s)>
```

or

```text
MAAS <behaves some unexpected way> when I <try to use a particular feature>
```

For example:

```
>>MAAS fails to PXE boot IBM LPAR machines as KVM hosts
```

Add this information to your text file.

<a href="#heading--version-and-build"><h3 id="heading--version-and-build">Identify your version and build</h3></a>

We need to know the version and build (and packaging format) that you're running.

<h4>If you're using a snap</h4>

If you're using a snap, execute `snap listmaas` at the command line, which will return some lines like this:

```text
Name  Version                       Rev    Tracking     Publisher   Notes
maas  3.0.0~beta2-9796-g.2182ab55f  13292  latest/edge  canonical✓  -
```

We want the know the `Version` field; in this case, that's `3.0.0~beta2-9796-g.2182ab55f`. Add a line like this to your text file:

```text
MAAS fails to PXE boot IBM LPAR machine as VM host

>>I'm using snap version/build 3.0.0~beta2-9796-g.2182ab55f.
```

<h4>If you're using a debian package</h4>

If you're using a deb, execute `apt list maas` at the command line, and enter whatever it returns into your text file, as in the snap example above, being sure to specify:

```text
I'm using debian package version/build...
```

<a href="#heading--which-interface"><h3 id="heading--which-interface">Using CLI, UI, or API?</h3></a>

Next, you'll need to specify which interface you're using, and generally what command(s) you were attempting.  For example:

```text
MAAS fails to PXE boot IBM LPAR machine as VM host

I'm using snap version/build 3.0.0~beta2-9796-g.2182ab55f.

>>I tried to create a VM host using a previously discovered IBM LPAR machine,
using the MAAS UI.
```

<a href="#heading--what-happens"><h3 id="heading--what-happens">Explain what happens</h3></a>

Being as concise and specific as you can, explain what seemed to go wrong.  For example:

```text
MAAS fails to PXE boot IBM LPAR machine as VM host

I'm using snap version/build 3.0.0~beta2-9796-g.2182ab55f.

I tried to create a VM host using a previously discovered IBM LPAR machine,
using the MAAS UI.

>>I was able to select the machine under "Add KVM," define its parameters,
and select a project.  I was also able to push "Authenticate," and the
expected commissioning process began.  After the machine powered on, though,
the commissioning process timed out trying to PXE boot the machine.  Looking
at the machine, it had indeed been powered on, but nothing happened after that.
```

<a href="#heading--reproducing-your-issue"><h3 id="heading--reproducing-your-issue">Explain how to reproduce your issue</h3></a>

In addition to the explanation above, you should create a step-by-step list of what you did to reproduce the problem.  For example:

```text
MAAS fails to PXE boot IBM LPAR machine as VM host

I'm using snap version/build 3.0.0~beta2-9796-g.2182ab55f.

I tried to create a VM host using a previously discovered IBM LPAR machine, using the MAAS UI.

I was able to select the machine under "Add KVM," define its parameters,
and select a project.  I was also able to push "Authenticate," and the
expected commissioning process began.  After the machine powered on, though,
the commissioning process timed out trying to PXE boot the machine.  Looking
at the machine, it had indeed been powered on, but nothing happened after that.

>>Steps to reproduce:
1. Confirm that at least one IBM LPAR 700 model is discovered and in the
Ready state (see screenshot-1).

2. Select the KVM tab (see screenshot-2).

3. Press the "Add KVM" button.

4. Select the KVM host type according to your network (I selected "<selection>").

5. Enter a name for the KVM host (I entered "<entered-name>").

6. Enter a bridge address to reach the KVM host (I entered "<power-address>").

7. Enter the appropriate password.

8. Press the "Authenticate" button.

9. On the project screen which pops up, select the "default" project.

10. Press the "Add KVM" button.

11. Return to the machine list and find the machine you just added as a KVM.
It should show "Powering on."

12. Watch until the machine enters the "Performing PXE boot" stage.

13. Wait for the machine to time out without reaching "Loading ephemeral"
stage, as normal.

14. Examine the logfiles (see attached logfiles).
```

<a href="#heading--screenshots"><h3 id="heading--screenshots">Take relevant screenshots</h3></a>

If you think it will help -- especially when using the UI -- try and capture screenshots of any unexpected results or ambiguous actions.  Your goal isn't to document your experience in pictures, but to provide a visual reference where verbal descriptions fall short.  Name these so you can sync them with your explanation (e.g., "screenshot-1"). You'll attach them later on in the process.

<a href="#heading--logfiles"><h3 id="heading--logfiles">Locate and capture logfiles</h3></a>

If at all possible, capture at least the following logfiles, for the time period surrounding your error situation:

1. maas.log
2. regiond.log
3. rackd.log
4. the rsyslog file of the affected machine(s), if it exists.

On snap, these files are located as follows:

* /var/snap/maas/common/log/maas.log
* /var/snap/maas/common/log/regiond.log
* /var/snap/maas/common/log/rackd.log
* /var/snap/maas/common/log/rsyslog/$MACHINE_NAME/$RELEVANT_DATE/messages

If you're using packages, you'll find the files in these locations:

* /var/log/maas/maas.log
* /var/log/maas/regiond.log
* /var/log/maas/rackd.log
* /var/log/maas/rsyslog/$MACHINE_NAME/$RELEVANT_DATE/messages

<a href="#heading--compress-logfiles"><h4>How to compress these logfiles into a tar.gz file for efficient upload</h4></a>

The following animation shows a recommended process for creating a `tar.gz` file.  The mistakes are intentional, so that you'll know what to do if you forget an option now and then, or forget to use `sudo` in a step or two:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c8e05533fc4f076774d26e592fe02418bc70ecf7.gif" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c8e05533fc4f076774d26e592fe02418bc70ecf7.gif"></a>

<a href="#heading--filing-bug"><h2 id="heading--filing-bug">Step 2: Filing your bug</h2></a>

Have your prepared text file handy.  In our example, it looks like this:

```text
MAAS fails to PXE boot IBM LPAR machine as VM host

I'm using snap version/build 3.0.0~beta2-9796-g.2182ab55f.

I tried to create a VM host using a previously discovered IBM LPAR machine, using the MAAS UI.

I was able to select the machine under "Add KVM," define its parameters,
and select a project.  I was also able to push "Authenticate," and the
expected commissioning process began.  After the machine powered on, though,
the commissioning process timed out trying to PXE boot the machine.  Looking
at the machine, it had indeed been powered on, but nothing happened after that.

Steps to reproduce:
1. Confirm that at least one IBM LPAR 700 model is discovered and in the
Ready state (see screenshot-1).

2. Select the KVM tab (see screenshot-2).

3. Press the "Add KVM" button.

4. Select the KVM host type according to your network (I selected "<selection>").

5. Enter a name for the KVM host (I entered "<entered-name>").

6. Enter a bridge address to reach the KVM host (I entered "<power-address>").

7. Enter the appropriate password.

8. Press the "Authenticate" button.

9. On the project screen which pops up, select the "default" project.

10. Press the "Add KVM" button.

11. Return to the machine list and find the machine you just added as a KVM.
It should show "Powering on."

12. Watch until the machine enters the "Performing PXE boot" stage.

13. Wait for the machine to time out without reaching "Loading ephemeral"
stage, as normal.

14. Examine the logfiles (see attached logfiles).
```

To file a bug, go to the [launchpad bug report page](https://bugs.launchpad.net/maas/+filebug). You'll see a screen similar to this one:

<a href="https://discourse.maas.io/uploads/default/original/2X/f/f445ad576553b45468775c1de98fdaf075bd03a0.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/f/f445ad576553b45468775c1de98fdaf075bd03a0.png"></a>

Enter your concise summary in the "Summary:" line:

<a href="https://discourse.maas.io/uploads/default/original/2X/7/7cb71e56284024d72d46c05767df1080e099b329.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/7/7cb71e56284024d72d46c05767df1080e099b329.png"></a>

Press enter to get to the next screen:

<a href="https://discourse.maas.io/uploads/default/original/2X/6/609dc8a082bafc1c3e12a60dbfe19920307ecdb6.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/6/609dc8a082bafc1c3e12a60dbfe19920307ecdb6.png"></a>

Paste the rest of your text file into the "Further information" box:

<a href="https://discourse.maas.io/uploads/default/original/2X/c/c6ab47abae93d7bc2a0143472a517911e346f864.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/c/c6ab47abae93d7bc2a0143472a517911e346f864.png"></a>

Attach your screenshots and logfiles by opening the "Extra options" section and browsing for your attachments.  Ideally, you'd attach the files one at a time, with a comprehensible description.

When you're done, simply choose "Submit Bug Report" and check your work on the screen that follows:

<a href="https://discourse.maas.io/uploads/default/original/2X/a/a2d7f7207d92891d237b852fc67f201a37993973.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/2X/a/a2d7f7207d92891d237b852fc67f201a37993973.png"></a>

If you want, you can view a [sample bug](https://bugs.launchpad.net/maas/+bug/1923516) with precisely these parameters.

