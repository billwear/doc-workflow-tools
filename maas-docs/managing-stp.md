||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/managing-stp-snap-2-7-cli/2910) ~ [UI](/t/managing-stp-snap-2-7-ui/2911)|[CLI](/t/managing-stp-snap-2-8-cli/2912) ~ [UI](/t/managing-stp-snap-2-8-ui/2913)|[CLI](/t/managing-stp-snap-2-9-cli/2914) ~ [UI](/t/managing-stp-snap-2-9-ui/2915)|[CLI](/t/managing-stp-snap-3-0-cli/4037) ~ [UI](/t/managing-stp-snap-3-0-ui/4038)|
Packages|[CLI](/t/managing-stp-deb-2-7-cli/2916) ~ [UI](/t/managing-stp-deb-2-7-ui/2917)|[CLI](/t/managing-stp-deb-2-8-cli/2918) ~ [UI](/t/managing-stp-deb-2-8-ui/2919)|[CLI](/t/managing-stp-deb-2-9-cli/2920) ~ [UI](/t/managing-stp-deb-2-9-ui/2921)|[CLI](/t/managing-stp-deb-3-0-cli/4039) ~ [UI](/t/managing-stp-deb-3-0-ui/4040)|

Some switches use the Spanning-Tree Protocol (STP) to negotiate a loop-free path through a root bridge. While scanning, it can cause each port to wait up to 50 seconds before sending data. This delay, in turn, can cause problems with some applications/protocols such as PXE, DHCP and DNS, of which MAAS makes extensive use.

To alleviate this problem, you should enable [Portfast](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst4000/8-2glx/configuration/guide/stp_enha.html#wp1019873) for Cisco switches (or its equivalent on other vendor equipment), which allows the ports to come up almost immediately.
