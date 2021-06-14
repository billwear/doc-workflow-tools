||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/network-testing-snap-2-7-cli/2934) ~ [UI](/t/network-testing-snap-2-7-ui/2935)|[CLI](/t/network-testing-snap-2-8-cli/2936) ~ [UI](/t/network-testing-snap-2-8-ui/2937)|[CLI](/t/network-testing-snap-2-9-cli/2938) ~ [UI](/t/network-testing-snap-2-9-ui/2939)|[CLI](/t/network-testing-snap-3-0-cli/4049) ~ [UI](/t/network-testing-snap-3-0-ui/4050)|
Packages|[CLI](/t/network-testing-deb-2-7-cli/2940) ~ [UI](/t/network-testing-deb-2-7-ui/2941)|[CLI](/t/network-testing-deb-2-8-cli/2942) ~ [UI](/t/network-testing-deb-2-8-ui/2943)|[CLI](/t/network-testing-deb-2-9-cli/2944) ~ [UI](/t/network-testing-deb-2-9-ui/2945)|[CLI](/t/network-testing-deb-3-0-cli/4051) ~ [UI](/t/network-testing-deb-3-0-ui/4052)|

MAAS provides a comprehensive suite of network and link testing capabilities.  MAAS can check whether or not links are connected, detect slow links, and report link and interface speeds via UI or API.  In addition, you can test Internet connectivity against a user-provided list of URLs or IP addresses.  Bonded NICS will be separated during this testing, so that each side of a redundant interface is fully evaluated.

Network testing also includes customisable network testing and commissioning scripts. There are no particular restrictions on these scripts, allowing you to test a wide variety of possible conditions and situations.

#### Four questions you may have:

1. [How do I use network link testing?](#heading--network-link-testing)
2. [How can I detect slow network links?](#heading--slow-link-detection)
3. [How do I use network validation and testing scripts?](#heading--network-validation-scripts-and-testing)
4. [How can I customise network testing?](#heading--customisable-network-testing)

<a href="#heading--network-link-testing"><h2 id="heading--network-link-testing">Network link testing</h2></a>

MAAS can check whether links are connected or disconnected, so that you can detect unplugged cables.  If you are not running MAAS 2.7, you must first upgrade and then recommission your machines to find disconnected links.  MAAS not only reports unplugged cables, but also gives a warning when trying to configure a disconnected interface.  In addition, administrators can change the cable connection status after manually resolving the issue.

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To check network testing results, enter the following command:

```
maas $PROFILE interfaces read $SYSTEM_ID \
| jq -r '(["LINK_NAME","LINK_CONNECTED?","LINK_SPEED", "I/F_SPEED"]
| (., map(length*"-"))), (.[] | [.name, .link_connected, .link_speed, .interface_speed])
| @tsv' | column -t
```

which produces an output similar to this:

```
LINK_NAME  LINK_CONNECTED?  LINK_SPEED  I/F_SPEED
---------  ---------------  ----------  ---------
ens3       false            -           1 Gpbs
```

From this screen, you can see that the `ens3` link is not connected (hence an unreported link speed). 
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
When MAAS detects a broken network link, users will see a screen similar to this one: 

<a href="https://discourse.maas.io/uploads/default/original/1X/687feb2ddea8b317f0deba239bcb1779fd5f33d3.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/687feb2ddea8b317f0deba239bcb1779fd5f33d3.jpeg"></a> 

If you're already using a version of MAAS less than 2.7, you will want to upgrade and recommission your existing machines to check link status.  Note that you will also receive a warning from MAAS when trying to configure a disconnected interface.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

Once you have manually repaired the broken connection, an administrator can change cable connection status:

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
```
maas $PROFILE interface update $SYSTEM_ID $INTERFACE_ID link_connected=true
```
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/b8b24a2e5fbc40b6469a24733a518b510cf0d955.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b8b24a2e5fbc40b6469a24733a518b510cf0d955.jpeg"></a> 
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<a href="#heading--slow-link-detection"><h2 id="heading--slow-link-detection">Detect slow network links</h2></a>

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
As servers and hardware get faster, the chances increase that you might encounter a speed mismatch when connecting your NIC to a network device.  MAAS can warn you if your interface is connected to a link slower than what the interface supports, when you run the above command:

```
maas $PROFILE interfaces read $SYSTEM_ID \
| jq -r '(["LINK_NAME","LINK_CONNECTED?","LINK_SPEED", "I/F_SPEED"]
| (., map(length*"-"))), (.[] | [.name, .link_connected, .link_speed, .interface_speed])
| @tsv' | column -t
```

From the resulting output, you can detect when your link/interface speeds are slower than expected. Depending on your physical hardware, the problem may not be repairable, but once you identify a slow link, you can replace a slow switch without recommissioning.  

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
As servers and hardware get faster, the chances increase that you might encounter a speed mismatch when connecting your NIC to a network device.  MAAS can warn you if your interface is connected to a link slower than what the interface supports, by automatically detecting link and interface speed and reporting them via the UI:

<a href="https://discourse.maas.io/uploads/default/original/1X/e73a81df222f44c0b364eefcd0880e2a84c7303b.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/e73a81df222f44c0b364eefcd0880e2a84c7303b.jpeg"></a>  

Depending on your physical hardware, the problem may not be repairable, but once you identify a slow link, you can replace a slow switch without recommissioning.  
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

Administrators can change or update the link and interface speeds after manual changes
to the connection:

```
maas $PROFILE interface update $SYSTEM_ID $INTERFACE_ID link_speed=$NEW_LINK_SPEED \
interface_speed=$NEW_INTERFACE_SPEED
```

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<a href="#heading--network-validation-scripts-and-testing"><h2 id="heading--network-validation-scripts-and-testing">Network validation and testing scripts</h2></a>

MAAS allows you to configure network connectivity testing in a number of ways. If MAAS can’t connect to the rack controller, deployment can’t complete.  MAAS can check connectivity to the rack controller and warn you if there’s no link, long before you have to try and debug it. For example, if you can’t connect to your gateway controller, traffic can’t leave your network. 

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
MAAS can check this link and recognise that there’s no connectivity, which alleviates hard-to-detect network issues:

<a href="https://discourse.maas.io/uploads/default/original/1X/c4f81cb3ef1a90f0a46fb62c893a4cc9f7e5f45a.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/c4f81cb3ef1a90f0a46fb62c893a4cc9f7e5f45a.jpeg"></a> 
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

Users can now test their network configuration to check for:

1. Interfaces which have a broken network configuration
2. Bonds that are not fully operational
3. Broken gateways, rack controllers, and Internet links

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
In addition, MAAS can comprehensively test Internet connectivity testing. You can give a list of URLs or IP addresses to check:

<a href="https://discourse.maas.io/uploads/default/original/1X/b92a8ca1821bc1ccf60cf7fddcb57f3fbeda4408.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/b92a8ca1821bc1ccf60cf7fddcb57f3fbeda4408.jpeg"></a> 
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
In addition, MAAS can comprehensively test Internet connectivity testing. You can give a list of URLs or IP addresses to check from the network testing screen:

<a href="https://discourse.maas.io/uploads/default/original/1X/12dd87ce0bffd54c2e459c4dea850af5fcbe14d0.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/12dd87ce0bffd54c2e459c4dea850af5fcbe14d0.jpeg"></a> 
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

In the ephemeral environment, standard DHCP is still applied, but when network testing runs, MAAS can apply your specific configuration for the duration of the test.  While all URLs / IPs are tested with all interfaces, MAAS can test each of your interfaces individually, including breaking apart bonded NICS and testing each side of your redundant interfaces. You can also run different tests on each pass, e.g., a different set of URLs, although each run would be a different testing cycle.

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
To test individual interfaces, for example, you could issue the following command:

<a href="https://discourse.maas.io/uploads/default/original/1X/7fadb56a2939f7a781510a55813141de03521e0d.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/7fadb56a2939f7a781510a55813141de03521e0d.jpeg"></a> 

Note that in this command, we are testing internet connectivity to the single interface "br0."
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<a href="#heading--customisable-network-testing"><h2 id="heading--customisable-network-testing">Customise network testing</h2></a>

MAAS allow you to customise network testing according to your needs.  You can create your own commissioning scripts and tests related to networking, and you can run them during the network testing portion of the MAAS workflow.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="https://discourse.maas.io/uploads/default/original/1X/0dcf089dbd8efc2fc9d0782d3b15f47647e950b8.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/0dcf089dbd8efc2fc9d0782d3b15f47647e950b8.jpeg"></a> 
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

There are no particular restrictions on these scripts, so you can test a wide variety of possible conditions and situations.  Administrators can upload network tests and test scripts.  Administrators can also create tests which accept an interface parameter, or scripts which apply custom network configurations.  

Users can specify unique parameters using the API, override machines which fail network testing (allowing their use), and suppress individual failed network tests.  Users can also review the health status from all interface tests, even sorting them by interface name and MAC.  In addition, MAAS can report the overall status of all interfaces.
