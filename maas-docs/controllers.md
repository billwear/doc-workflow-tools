||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/controllers-snap-2-7-cli/2718) ~ [UI](/t/controllers-snap-2-7-ui/2719)|[CLI](/t/controllers-snap-2-8-cli/2720) ~ [UI](/t/controllers-snap-2-8-ui/2721)|[CLI](/t/controllers-snap-2-9-cli/2722) ~ [UI](/t/controllers-snap-2-9-ui/2723)|[CLI](/t/controllers-snap-3-0-cli/3897) ~ [UI](/t/controllers-snap-3-0-ui/3898)|
Packages|[CLI](/t/controllers-deb-2-7-cli/2724) ~ [UI](/t/controllers-deb-2-7-ui/2725)|[CLI](/t/controllers-deb-2-8-cli/2726) ~ [UI](/t/controllers-deb-2-8-ui/2727)|[CLI](/t/controllers-deb-2-9-cli/2728) ~ [UI](/t/controllers-deb-2-9-ui/2729)|[CLI](/t/controllers-deb-3-0-cli/3899) ~ [UI](/t/controllers-deb-3-0-ui/3900)|

Most of the functionality of MAAS is contained in a series of controllers.  There are two basic types: a region controller and one or more rack controllers. The region controller deals with operator requests, while the rack controller(s) provides high-bandwidth services to the individual machines.  In essence, the region controller interacts with the user, while the rack controllers manage the bare metal.

<!-- deb-2-7-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2688).
[/note]
deb-2-7-cli -->

<!-- deb-2-7-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2689).
[/note]
deb-2-7-ui -->

<!-- deb-2-8-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2690).
[/note]
deb-2-8-cli -->

<!-- deb-2-8-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2691).
[/note]
deb-2-8-ui -->

<!-- deb-2-9-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2692).
[/note]
deb-2-9-cli -->

<!-- deb-2-9-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2693).
[/note]
deb-2-9-ui -->

<!-- deb-3-0-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/3947).
[/note]
deb-3-0-cli -->

<!-- deb-3-0-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/3948).
[/note]
deb-3-0-ui -->

<!-- snap-2-7-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2682).
[/note]
snap-2-7-cli -->

<!-- snap-2-7-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2683).
[/note]
snap-2-7-ui -->

<!-- snap-2-8-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2684).
[/note]
snap-2-8-cli -->

<!-- snap-2-8-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2685).
[/note]
snap-2-8-ui -->

<!-- snap-2-9-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2686).
[/note]
snap-2-9-cli -->

<!-- snap-2-9-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/2687).
[/note]
snap-2-9-ui -->

<!-- snap-3-0-cli
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/3945).
[/note]
snap-3-0-cli -->

<!-- snap-3-0-ui
[note]
Note that both region and rack controllers can be scaled out, as well as made [highly available](/t/high-availability/3946).
[/note]
snap-3-0-ui -->

#### Four questions you might have:

1. [What does a region controller do?](#heading--region-controller)
2. [What does a rack controller do?](#heading--rack-controllers)
3. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
4. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)

<a href="#heading--region-controller"><h2 id="heading--region-controller">What a region controller does</h2></a>

A region controller consists of five components:

1.   REST API server (TCP port 5240)
2.   PostgreSQL database
3.   DNS
4.   caching HTTP proxy
5.   web UI

Region controllers are responsible for either a data centre or a single region. Multiple fabrics are used by MAAS to accommodate subdivisions within a single region, such as multiple floors in a data centre.

<a href="#heading--rack-controllers"><h2 id="heading--rack-controllers">What a rack controller does</h2></a>

A rack controller provides four services:

1.   DHCP
2.   TFTP
3.   HTTP (for images)
4.   power management

A rack controller is attached to each "fabric". As the name implies, a typical setup is to have a rack controller in each data centre server rack. The rack controller will cache large items for performance, such as operating system install images, but maintains no independent state other than the credentials required to talk to the region controller.

<details><summary>Tell me about fabrics</summary>

A fabric is simply a way of linking [VLANs](/t/concepts-and-terms/785#heading--vlans) (Virtual LANs) together.  If you're familiar with a VLAN, you know that it's designed to limit network traffic to specific ports (e.g., on a [switch](/t/concepts-and-terms/785#heading--switch)) or by evaluating labels called "tags" (unrelated to MAAS tags).  By definition, this would mean that two VLANs can't communicate with each other -- it would defeat the purpose of the VLAN -- unless you implement some extraordinary measures.

<!-- deb-2-7-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2652) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-2-7-cli -->

<!-- deb-2-7-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2653) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-2-7-ui -->

<!-- deb-2-8-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2654) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-2-8-cli -->

<!-- deb-2-8-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2655) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-2-8-ui -->

<!-- deb-2-9-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2656) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-2-9-cli -->

<!-- deb-2-9-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2657) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-2-9-ui -->

<!-- deb-3-0-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/3947) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-3-0-cli -->

<!-- deb-3-0-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/3948) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
deb-3-0-ui -->

<!-- snap-2-7-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2646) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-2-7-cli -->

<!-- snap-2-7-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2647) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-2-7-ui -->

<!-- snap-2-8-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2648) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-2-8-cli -->

<!-- snap-2-8-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2649) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-2-8-ui -->

<!-- snap-2-9-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2650) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-2-9-cli -->

<!-- snap-2-9-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/2651) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-2-9-ui -->

<!-- snap-3-0-cli
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/3945) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-3-0-cli -->

<!-- snap-3-0-ui
For example, let's say that your [hospital](/t/give-me-an-example-of-maas/3946) has three key functions: Patient management, Accounting, and Facilities, each on their own VLAN.  Let's say that there are some situations in which you need to share data between all three of these functions.  To accomplish this, you can create a fabric that joins these three VLANS.  Since this fabric just makes it possible for these VLANs to communicate, you can manage the cross-VLAN access with additional software, or permissions, depending on your application software architecture.
snap-3-0-ui -->


You can learn more about fabrics in the [Concepts and terms](/t/concepts-and-terms/785#heading--fabrics) section of this documentation.
</details>

<a href="#heading--move-rack-controller"><h2 id="heading--move-rack-controller">Move a rack controller from one MAAS instance to another</h2></a>

In the course of normal operations, you may wish to move a device acting as a rack controller from one MAAS instance to another.  From the point of view of MAAS, there is no such action as moving a rack controller, although you can delete a rack controller from one MAAS and reinstantiate the same controller (binary-wise) on another MAAS instance. From your perspective, of course, you are moving one box performing rack controller functions, either physically or network-wise, from one MAAS to another. 

<a href="#heading--move-rack-controller"><h3 id="heading--dangers-moving-rack-controller">Dangers of moving a rack controller</h3></a>

Before you execute the move, you should realize that there are dangers associate with moving a rack controller -- dangers that may generate errors, get you into a non-working state, or cause you significant data loss.  These dangers are precipitated by one caveat and two potential mistakes:

* **Using the same system as a rack controller and a VM host:** While not forbidden or inherently dangerous, using the same machine as both a rack controller and a VM host may cause resource contention and poor performance.  If the resources on the system are not more than adequate to cover both tasks, you may see slowdowns (or even apparent "freeze" events) on the system.

* **Moving a rack controller from one version of MAAS to another:** MAAS rack controller software is an integral part of each version of MAAS.  If you delete a rack controller from, say, a 2.6 version of MAAS, and attempt to register that 2.6 version of the rack controller code to, say, a 2.9 version of MAAS, you may experience errors and potential data loss.  Using the above example, if you are running both a VM host and a rack controller for MAAS 2.6 on one system, and you suddenly decide to delete that rack controller from 2.6 and attempt to register the same code to a 2.9 MAAS, the VM host may fail or disappear.  This will possibly delete all the VMs you have created or connected to that VM host -- which may result in data loss.  This action is not supported.

* **Connecting one instance of a rack controller to two instances of MAAS, regardless of version:** Trying to connect a single rack controller to two different instances of MAAS can result in all sorts of unpredictable (and potentially catastrophic) behavior.  It is not a supported configuration.

Take these warnings to heart.  It may seem like a faster approach to "bridge" your existing rack controllers from one MAAS to another -- or from one version of MAAS to another -- while they're running.  Ultimately, though, it will probably result in more work than just following the recommended approach.

<h3>Moving the controller</h3>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
To move a rack controller using the MAAS UI, first, delete the rack controller.  In the "Controllers" tab in the UI, select the rack controller you with to delete, choose "Take action" and select "Delete."  You will be asked to confirm with a red button, entitled "Delete 1 controller."
 snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
In effect, there is no such action as moving a rack controller, although you can delete a rack controller from one MAAS and reinstantiate the same controller (binary-wise) on another MAAS instance.  First, delete the rack controller, with the command:

```
maas $PROFILE rack-controller delete $SYSTEM_ID
```

where `$PROFILE` is your admin profile name, and `$SYSTEM_ID` can be found by examining the output of the command:

```
maas $PROFILE rack-controllers read
```

There is no confirmation step, so make sure you have the right rack controller before proceeding.
 snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

Next, you must register a new rack controller, which is always done from the command line.

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli 
For this exercise, we're assuming you are using the already installed rack controller code that was previously running on the "from" MAAS instance.  All that's necessary is that you register a new rack controller with the "to" MAAS instance, like this:

```
sudo maas-rack register --url $MAAS_URL_OF_NEW_MAAS --secret $SECRET_FOR_NEW_MAAS
```

where the secret is found in `/var/lib/maas/secret`.
 deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-cli deb-3-0-cli 
For this exercise, we're assuming you are using the already installed rack controller code that was previously running on the "from" MAAS instance.  All that's necessary is that you register a new rack controller with the "to" MAAS instance, like this:

```
sudo maas init rack --maas-url $MAAS_URL_OF_NEW_MAAS --secret $SECRET_FOR_NEW_MAAS
```

where the secret is found in `/var/snap/maas/common/maas/secret`.
 snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-cli deb-3-0-cli  -->

<!-- deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-ui snap-2-8-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui  
Note that in the UI, if you go to the "Controllers" tab and press the button entitled, "Add rack controller," at the top of the Controllers screen, MAAS will give you a complete command string, including the correct URL and secret values.  Simply cut and paste that string to move the rack controller, paying attention to whether you are using snap or package build modes.
 deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-ui snap-2-8-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui  -->

