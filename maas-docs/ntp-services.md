||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/ntp-services-snap-2-7-cli/2958) ~ [UI](/t/ntp-services-snap-2-7-ui/2959)|[CLI](/t/ntp-services-snap-2-8-cli/2960) ~ [UI](/t/ntp-services-snap-2-8-ui/2961)|[CLI](/t/ntp-services-snap-2-9-cli/2962) ~ [UI](/t/ntp-services-snap-2-9-ui/2963)|[CLI](/t/ntp-services-snap-3-0-cli/4053) ~ [UI](/t/ntp-services-snap-3-0-ui/4054)|
Packages|[CLI](/t/ntp-services-deb-2-7-cli/2964) ~ [UI](/t/ntp-services-deb-2-7-ui/2965)|[CLI](/t/ntp-services-deb-2-8-cli/2966) ~ [UI](/t/ntp-services-deb-2-8-ui/2967)|[CLI](/t/ntp-services-deb-2-9-cli/2968) ~ [UI](/t/ntp-services-deb-2-9-ui/2969)|[CLI](/t/ntp-services-deb-3-0-cli/4055) ~ [UI](/t/ntp-services-deb-3-0-ui/4056)|

MAAS provides managed NTP services (with [Chrony](https://chrony.tuxfamily.org/)) for all region and rack controllers. This arrangement allows MAAS to both keep its controllers synchronised, and keep deployed machines synchronised as well. You can configure NTP on the 'Network services' tab of the 'Settings' page.

The region controller configures the NTP service to keep its time synchronised from one or more external sources. By default, the MAAS region controller uses `ntp.ubuntu.com`. Rack controllers also configure the NTP service, synchronising their time with the region controllers.  Rack controllers also configure DHCP with the correct NTP information. Any machine on the network that obtains a DHCP lease from MAAS will benefit from NTP support.

<a href="#heading--setting-ntp-server"><h2 id="heading--setting-ntp-server">Setting an external NTP server</h2></a>

External sites, such as an existing NTP infrastructure, can be used directly as a time source for both rack controllers and machines.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
You can specify an external site by choosing the NTP server(s) and selecting the 'External Only' option. The region controller always uses an external site.

On the 'Settings' page, select the 'Network services' tab and scroll down to the 'NTP' section:

<a href="https://assets.ubuntu.com/v1/69180b4a-installconfig-network-ntp__2.6-configure-ntp.png" target = "_blank"><img src="https://assets.ubuntu.com/v1/69180b4a-installconfig-network-ntp__2.6-configure-ntp.png"></a>

Enter the address of the desired NTP server. Apply any changes by pressing the 'Save' button.
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 
You can specify an external NTP server with two successive commands:

```
maas $PROFILE maas set-config name=ntp_servers value=$NTP_IP_ADDRESS
```

followed by:

```
maas admin maas set-config name=ntp_external_only value=true
```

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->
