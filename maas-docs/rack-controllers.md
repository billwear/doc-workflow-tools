||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/rack-controllers-snap-2-7-cli/3054) ~ [UI](/t/rack-controllers-snap-2-7-ui/3055)|[CLI](/t/rack-controllers-snap-2-8-cli/3056) ~ [UI](/t/rack-controllers-snap-2-8-ui/3057)|[CLI](/t/rack-controllers-snap-2-9-cli/3058) ~ [UI](/t/rack-controllers-snap-2-9-ui/3059)|[CLI](/t/rack-controllers-snap-3-0-cli/4089) ~ [UI](/t/rack-controllers-snap-3-0-ui/4090)|
Packages|[CLI](/t/rack-controllers-deb-2-7-cli/3060) ~ [UI](/t/rack-controllers-deb-2-7-ui/3061)|[CLI](/t/rack-controllers-deb-2-8-cli/3062) ~ [UI](/t/rack-controllers-deb-2-8-ui/3063)|[CLI](/t/rack-controllers-deb-2-9-cli/3064) ~ [UI](/t/rack-controllers-deb-2-9-ui/3065)|[CLI](/t/rack-controllers-deb-3-0-cli/4091) ~ [UI](/t/rack-controllers-deb-3-0-ui/4092)|

A rack controller can connect to multiple VLANs, each from a different network interface. A rack controller can only connect to one MAAS instance at any given time, and must connect to an instance that matches its MAAS version (major and minor).  This configuration provides a scaling factor that can help as a network architecture grows in size.

#### Seven questions you may have:

<!-- deb-2-7-cli
1. [How does MAAS communication work?](/t/maas-communication/2832)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2688#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-2-7-cli -->

<!-- deb-2-7-ui
1. [How does MAAS communication work?](/t/maas-communication/2833)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2689#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-2-7-ui -->

<!-- deb-2-8-cli
1. [How does MAAS communication work?](/t/maas-communication/2834)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2690#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-2-8-cli -->

<!-- deb-2-8-ui
1. [How does MAAS communication work?](/t/maas-communication/2835)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2691#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-2-8-ui -->

<!-- deb-2-9-cli
1. [How does MAAS communication work?](/t/maas-communication/2836)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2692#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-2-9-cli -->

<!-- deb-2-9-ui
1. [How does MAAS communication work?](/t/maas-communication/2837)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2683#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-2-9-ui -->

<!-- deb-3-0-cli
1. [How does MAAS communication work?](/t/maas-communication/3991)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/3947#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-3-0-cli -->

<!-- deb-3-0-ui
1. [How does MAAS communication work?](/t/maas-communication/3992)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/3948#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 deb-3-0-ui -->

<!-- snap-2-7-cli
1. [How does MAAS communication work?](/t/maas-communication/2826)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2682#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-2-7-cli -->

<!-- snap-2-7-ui
1. [How does MAAS communication work?](/t/maas-communication/2827)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2683#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-2-7-ui -->

<!-- snap-2-8-cli
1. [How does MAAS communication work?](/t/maas-communication/2828)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2684#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-2-8-cli -->

<!-- snap-2-8-ui
1. [How does MAAS communication work?](/t/maas-communication/2829)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2685#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-2-8-ui -->

<!-- snap-2-9-cli
1. [How does MAAS communication work?](/t/maas-communication/2830)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2686#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-2-9-cli -->

<!-- snap-2-9-ui
1. [How does MAAS communication work?](/t/maas-communication/2831)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/2687#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-2-9-ui -->

<!-- snap-3-0-cli
1. [How does MAAS communication work?](/t/maas-communication/3989)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/3945#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-3-0-cli -->

<!-- snap-3-0-ui
1. [How does MAAS communication work?](/t/maas-communication/3990)
2. [How do I install a rack controller?](#heading--install-a-rack-controller)
3. [How do I list rack controllers?](#heading--list-rack-controllers)
4. [How do I configure MAAS for multiple API servers?](/t/high-availability/3946#heading--multiple-region-endpoints)
5. [How do I unregister a rack controller?](#heading--unregister-a-rack-controller)
6. [How do I move a rack controller from one MAAS instance to another?](#heading--move-rack-controller)
7. [What are the potential dangers of moving a rack controller?](#heading--dangers-moving-rack-controller)
 snap-3-0-ui -->

<a href="#heading--install-a-rack-controller"><h2 id="heading--install-a-rack-controller">Install a rack controller</h2></a>

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli
To install and register a rack controller with the MAAS:

``` bash
sudo apt install maas-rack-controller
sudo maas-rack register --url $MAAS_URL --secret $SECRET
```

[note]
The register command is not required when you are adding a rack controller to a system that already houses an API server.
[/note]

The $SECRET is stored in file `/var/lib/maas/secret` on the API server.
 deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli-->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
To install and register a rack controller with the MAAS:

``` bash
sudo snap install maas
sudo maas init rack --maas-url $MAAS_URL --secret $SECRET
```

The $SECRET is stored in file `/var/lib/maas/secret` on the API server.
 snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli-->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Note that on the UI, you can find complete instructions for adding a rack controller under the "Controllers" tab.  Simply click on the button labeled, "Add rack controller" and choose the instructions relevant to your build model (snap or packages).  The commands there will already include the correct MAAS URL and secret, so you can cut and paste them at the command line.
 snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<a href="#heading--list-rack-controllers"><h2 id="heading--list-rack-controllers">List rack controllers</h2></a>

<!-- deb-2-7-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2688) configurations.
 deb-2-7-cli -->

<!-- deb-2-7-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Packages 2.7 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2689) configurations.
 deb-2-7-ui -->

<!-- deb-2-8-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2690) configurations.
 deb-2-8-cli -->

<!-- deb-2-8-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Packages 2.8 CLI" link at the top of the page to find out how. Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2691) configurations.
 deb-2-8-ui -->

<!-- deb-2-9-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2692) configurations.
 deb-2-9-cli -->

<!-- deb-2-9-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Packages 2.9 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2693) configurations.
 deb-2-9-ui -->

<!-- deb-3-0-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/3947) configurations.
 deb-3-0-cli -->

<!-- deb-3-0-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Packages 2.9 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/3948) configurations.
 deb-3-0-ui -->

<!-- snap-2-7-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2682) configurations.
 snap-2-7-cli -->

<!-- snap-2-7-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Snap 2.7 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2683) configurations.
 snap-2-7-ui -->

<!-- snap-2-8-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2684) configurations.
 snap-2-8-cli -->

<!-- snap-2-8-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Snap 2.8 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2685) configurations.
 snap-2-8-ui -->

<!-- snap-2-9-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

 Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2686) configurations.
 snap-2-9-cli -->

<!-- snap-2-9-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Snap 2.9 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/2687) configurations.
 snap-2-9-ui -->

<!-- snap-3-0-cli
You can also list and confirm all registered rack controllers:

``` bash
maas $PROFILE rack-controllers read | grep hostname | cut -d '"' -f 4
```

 Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/3945) configurations.
 snap-3-0-cli -->

<!-- snap-3-0-ui
You can also list and confirm all registered rack controllers via the CLI; select the "Snap 2.9 CLI" link at the top of the page to find out how.  Note that you will need multiple rack controllers to achieve specific [high availability](/t/high-availability/3946) configurations.
 snap-3-0-ui -->

<div class="p-notification">
<p class="p-notification__response">If you are using VM nodes, you must ensure that the new rack controller can communicate with the VM host.</p>
</div>

<a href="#heading--unregister-a-rack-controller"><h2 id="heading--unregister-a-rack-controller">Unregister a rack controller</h2></a>

Most likely, you would only “unregister” an extra, unnecessary rack controller.  In this case, you need to <em>delete</em> it from the region API server; there is no ‘unregister’ command.

To do so, navigate to the ‘Controllers’ page of the web UI. Enter the controller’s page by clicking on the machine you want to delete and select ‘Delete’ from the drop-down (and then ‘Delete controller’). MAAS will do the right thing if the controller is used for DHCP HA; that is, the DHCP HA needs to be disabled.

Although similar, this is not the same as deletion. Here, you are deleting a machine that is a part of MAAS itself.

<div class="p-notification">
<p class="p-notification__response">Unless you remove the software on this machine, rebooting it will cause the machine to re-instate itself as a rack controller. This behaviour may change with future versions of MAAS.</p>
</div>

<a href="#heading--move-rack-controller"><h2 id="heading--move-rack-controller">Move a rack controller from one MAAS instance to another</h2></a>

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
In effect, there is no such action as moving a rack controller, although you can delete a rack controller from one MAAS and reinstantiate the same controller (binary-wise) on another MAAS instance.  First, delete the rack controller.  In the "Controllers" tab in the UI, select the rack controller you with to delete, choose "Take action" and select "Delete."  You will be asked to confirm with a red button, entitled "Delete 1 controller."
 snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

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
 snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

Next, you must register a new rack controller, which is always done from the command line.

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli
For this exercise, we're assuming you are using the already installed rack controller code that was previously running on the "from" MAAS instance.  All that's necessary is that you register a new rack controller with the "to" MAAS instance, like this:

```
sudo maas-rack register --url $MAAS_URL_OF_NEW_MAAS --secret $SECRET_FOR_NEW_MAAS
```

where the secret is found in `/var/lib/maas/secret`.
 deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
For this exercise, we're assuming you are using the already installed rack controller code that was previously running on the "from" MAAS instance.  All that's necessary is that you register a new rack controller with the "to" MAAS instance, like this:

```
sudo maas init rack --maas-url $MAAS_URL_OF_NEW_MAAS --secret $SECRET_FOR_NEW_MAAS
```

where the secret is found in `/var/snap/maas/common/maas/secret`.
 snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->

<!-- deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-ui snap-2-8-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui 
Note that in the UI, if you go to the "Controllers" tab and press the button entitled, "Add rack controller," at the top of the Controllers screen, MAAS will give you a complete command string, including the correct URL and secret values.  Simply cut and paste that string to move the rack controller, paying attention to whether you are using snap or package build modes.
 deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-2-7-ui snap-2-8-ui snap-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<a href="#heading--move-rack-controller"><h3 id="heading--dangers-moving-rack-controller">Dangers of moving a rack controller</h3></a>

There are dangers associate with moving a rack controller -- dangers that may generate errors, get you into a non-working state, or cause you significant data loss.  These dangers are precipitated by one caveat and two potential mistakes:

* **Using the same system as a rack controller and a VM host:** While not forbidden or inherently dangerous, using the same machine as both a rack controller and a VM host may cause resource contention and poor performance.  If the resources on the system are not more than adequate to cover both tasks, you may see slowdowns (or even apparent "freeze" events) on the system.

* **Moving a rack controller from one version of MAAS to another:** MAAS rack controller software is an integral part of each version of MAAS.  If you delete a rack controller from, say, a 2.6 version of MAAS, and attempt to register that 2.6 version of the rack controller code to, say, a 2.9 version of MAAS, you may experience errors and potential data loss.  Using the above example, if you are running both a VM host and a rack controller for MAAS 2.6 on one system, and you suddenly decide to delete that rack controller from 2.6 and attempt to register the same code to a 2.9 MAAS, the VM host may fail or disappear.  This will possibly delete all the VMs you have created or connected to that VM host -- which may result in data loss.  This action is not supported.

* **Connecting one instance of a rack controller to two instances of MAAS, regardless of version:** Trying to connect a single rack controller to two different instances of MAAS can result in all sorts of unpredictable (and potentially catastrophic) behavior.  It is not a supported configuration.

Take these warnings to heart.  It may seem like a faster approach to "bridge" your existing rack controllers from one MAAS to another -- or from one version of MAAS to another -- while they're running.  Ultimately, though, it will probably result in more work than just following the recommended approach.
