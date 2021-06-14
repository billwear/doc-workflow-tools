||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/hardening-your-maas-installation-snap-2-7-cli/2658) ~ [UI](/t/hardening-your-maas-installation-snap-2-7-ui/2659)|[CLI](/t/hardening-your-maas-installation-snap-2-8-cli/2660) ~ [UI](/t/hardening-your-maas-installation-snap-2-8-ui/2661)|[CLI](/t/hardening-your-maas-installation-snap-2-9-cli/2662) ~ [UI](/t/hardening-your-maas-installation-snap-2-9-ui/2663)|[CLI](/t/hardening-your-maas-installation-snap-3-0-cli/3937) ~ [UI](/t/hardening-your-maas-installation-snap-3-0-ui/3938)|
Packages|[CLI](/t/hardening-your-maas-installation-deb-2-7-cli/2664) ~ [UI](/t/hardening-your-maas-installation-deb-2-7-ui/2665)|[CLI](/t/hardening-your-maas-installation-deb-2-8-cli/2666) ~ [UI](/t/hardening-your-maas-installation-deb-2-8-ui/2667)|[CLI](/t/hardening-your-maas-installation-deb-2-9-cli/2668) ~ [UI](/t/hardening-your-maas-installation-deb-2-9-ui/2669)|[CLI](/t/hardening-your-maas-installation-deb-3-0-cli/3939) ~ [UI](/t/hardening-your-maas-installation-deb-3-0-ui/3940)|

As a MAAS administrator, you have the critical responsibility of hardening your installation to help repudiate attacks and malicious actors.  While there are too many variables to make meaningful suggestions for your deployed machines, there are a number of steps you can take to improve the overall security of your MASS setup.  This article provides a few suggestions.

#### Six questions you may have:

1. [How do I setup a firewall for MAAS?](#heading--firewalls)
2. [How do I configure a TLS-terminating load balancer (and what's the impact on my MAAS setup?)](#heading--tls)
3. [How do I use logs to identify security issues?](#heading--using-logs-for-security)
4. [How do I implement PostgreSQL security?](#heading--postgres-security)
5. [What else can I do to harden MAAS?](#heading--what-else-to-do)
6. [Whom do I contact for MAAS security consulting?](#heading--security-consulting)

<a href="#heading--firewalls"><h2 id="heading--firewalls">Use a firewall</h2></a>
<p>Each rack controller must be able to initiate TCP connections on the following ports:</p>
<table>
<thead>
<tr>
<th>Port(s)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>5240</code></td>
<td>HTTP communication with each region controller. Note that port <code>80</code> is typically used in high-availability environments.
</tr>
<tr>
<td>
<code>5241</code> - <code>5247</code>
</td>
<td>Reserved for internal MAAS services.</td>
</tr>
<tr>
<td><code>5248</code></td>
<td>Reserved for rack HTTP communication.</td>
</tr>
<tr>
<td>
<code>5250</code> - <code>5270</code>
</td>
<td>Reserved for region workers (RPC).</td>
</tr>
</tbody>
</table>

Consider setting your [firewall ](https://help.ubuntu.com/lts/serverguide/firewall.html#firewall-logs) on your rack and region controllers to disallow communication on all ports except those used by MAAS. For example, assuming you have installed `ufw`, you could execute:

    sudo ufw enable
    sudo ufw default deny incoming

You could then follow that with commands similar to these:

    sudo ufw allow 5240
    sudo ufw allow 5248
    sudo ufw allow 5241:5247/tcp
    sudo ufw allow 5241:5247/udp
    sudo ufw allow 5250:5270/tcp
    sudo ufw allow 5250:5270/udp

Recognise that your particular configuration and version may vary, so consult the appropriate firewall manual pages for your specific MAAS host system.

<a href="#heading--tls"><h2 id="heading--tls">Configure a TLS-terminating load balancer</h2></a>

One of the best steps you can take to improve both security and availability of your MAAS installation is to install TLS-terminating load balancer.  For MAAS, we recommend using [HAProxy ](https://www.haproxy.com).  This section explains how to set one up.

<details><summary>What is a TLS-terminated load balancer?</summary>

<!-- deb-2-7-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2688) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-2-7-cli -->

<!-- deb-2-7-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2689) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-2-7-ui -->

<!-- deb-2-8-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2690) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-2-8-cli -->

<!-- deb-2-8-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2691) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-2-8-ui -->

<!-- deb-2-9-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2692) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-2-9-cli -->

<!-- deb-2-9-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2693) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-2-9-ui -->

<!-- deb-3-0-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/3947) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-3-0-cli -->

<!-- deb-3-0-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/3948) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 deb-3-0-ui -->

<!-- snap-2-7-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2682) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-2-7-cli -->

<!-- snap-2-7-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2683) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-2-7-ui -->

<!-- snap-2-8-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2684) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-2-8-cli -->

<!-- snap-2-8-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2685) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-2-8-ui -->

<!-- snap-2-9-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2686) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-2-9-cli -->

<!-- snap-2-9-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/2687) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-2-9-ui -->

<!-- snap-3-0-cli
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/3945) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-3-0-cli -->

<!-- snap-3-0-ui
In the context of MAAS, a [load balancer ](https://www.nginx.com/resources/glossary/load-balancing/) distributes the incoming Web UI and API requests across multiple region controllers.  This reduces both load on MAAS and wait times for user requests.  Typically, this is known as a high-availability (HA) configuration, although there are two other [HA configurations](/t/high-availability/3946) that can be enabled for MAAS: one for BMC access (for powering on machines), and one for DHCP, which enables primary and secondary DHCP instances that manage the same VLAN.
 snap-3-0-ui -->

A TLS-terminated load balancer is a load balancer that carries encryption and decryption as far down the pipe as possible, in this case, all the way to the load balancer itself. Note that, even though the "SSL" keyword may be used to enable operation, the term SSL is considered obsolete.  Hence we choose to use the term "TLS" instead, referring to **Transport Layer Security**.

TLS is meant to provide privacy and data integrity between two or more applications.  Privacy is provided by [symmetric cryptography ](https://en.wikipedia.org/wiki/Symmetric-key_algorithm), based on a shared secret and uniquely-generated keys negotiated at the start of a session (during the [TLS handshake ](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_handshake)).  Identity of each app can be authenticated, though this feature can be optional.  Authenticity of messages is ensured by using [message authentication codes ](https://en.wikipedia.org/wiki/Message_authentication_code) to detect tampering.

</details>

<a href="#heading--pem-file"><h3 id="heading--pem-file">PEM file</h3></a>

As a first step, you'll need an SSL certificate (`mysite.com.crt`) with a key pair (`mysite.com.key`), combined into a PEM file:

    cat mysite.com.crt mysite.com.key > mysite.com.pem
    sudo cp mysite.com.pem /etc/ssl/private/

Depending upon your chosen certificate authority, you may also need to copy your CA root certificate and one or more intermediate CA certificates into the same PEM file.

<a href="#heading--install-ha-proxy"><h3 id="heading--install-ha-proxy">Install and configure HA proxy</h3></a>

To install HAProxy, execute the following commands:

    sudo apt-get update
    sudo apt-get install haproxy

Next, edit `/etc/haproxy/haproxy.cfg` as follows.  In the `global` section of the file, add this line:

    maxconn <number of concurrent connections>

Be aware that there's a balance between accepting many connections and overloading the API by trying to serve too many requests.  Also, you should consider adding a line like this one to the same section:

    tune.ssl.default-dh-param 2048

This parameter configures the maximum size of temporary DHE keys that are generated.

Next, in the `defaults` section, add the following lines under `mode http`:

    option forwardfor
    option http-server-close

The option `forwardfor` tells HAProxy to add X-Forward-For headers to each request.  The `http-server-close` option reduces latency between HAProxy and your users by closing connections but maintaining a keep-alive.

Finally, you'll set the frontend and backend parameters that define the connections between HAProxy and MAAS.  For the frontend, you can set parameters this way:

    frontend maas
        bind *:443 ssl crt /etc/ssl/private/mysite.com.pem
        reqadd X-Forwarded-Proto:\ https
        retries 3
        option redispatch
        default_backend maas

This stanza defines a frontend name `maas`; tells HAProxy to handle incoming traffic to port 443, providing SSL encryption, enabled by the certificates and keys you earlier concatenated into your PEM file; allows three retries and redispatch; and forwards these requests to `maas` as the backend server, which is defined something like this:

    backend maas
        timeout server 90s
        balance source
        hash-type consistent
        server localhost localhost:5240 check
        server maas-api-1 <ip-address-of-a-region-controller>:5240 check
        server maas-api-2 <ip-address-of-another-region-controller>:5240 check

This stanza defines a backend server group named `maas`; sets consistent hashing, 90 second timeout, and balanced sources; sets the server address and port (`localhost:5240`); and engages two region controllers, named `maas-api-1` and `maas-api-2`.  Note that the "1" and "2" designations are completely arbitrary, as there is no sense of "primary" or "secondary" associated with this configuration.

Finally, restart the (already-running) load balancer so that these changes can take effect and the HAProxy will begin to forward requests:

    sudo systemctl restart haproxy

Note that you can also [enable HAProxy logging ](https://www.digitalocean.com/community/tutorials/how-to-implement-ssl-termination-with-haproxy-on-ubuntu-14-04) if desired.  This logging is an optional feature of the HAProxy tool and is thus left to your discretion.  

<!-- deb-2-7-cli
If desired, you can [bypass the use of SSL](/t/high-availability/2688#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2544) without implementing HAProxy.
 deb-2-7-cli -->

<!-- deb-2-7-ui
If desired, you can [bypass the use of SSL](/t/high-availability/2689#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2545) without implementing HAProxy.
 deb-2-7-ui -->

<!-- deb-2-8-cli
If desired, you can [bypass the use of SSL](/t/high-availability/2690#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2546) without implementing HAProxy.
 deb-2-8-cli -->

<!-- deb-2-8-ui
If desired, you can [bypass the use of SSL](/t/high-availability/2691#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2547) without implementing HAProxy.
 deb-2-8-ui -->

<!-- deb-2-9-cli
If desired, you can [bypass the use of SSL](/t/high-availability/2692#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2548) without implementing HAProxy.
 deb-2-9-cli -->

<!-- deb-2-9-ui
If desired, you can [bypass the use of SSL](/t/high-availability/2693#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2549) without implementing HAProxy.
 deb-2-9-ui -->

<!-- deb-3-0-cli
If desired, you can [bypass the use of SSL](/t/high-availability/3947#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2548) without implementing HAProxy.
 deb-3-0-cli -->

<!-- deb-3-0-ui
If desired, you can [bypass the use of SSL](/t/high-availability/3948#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2549) without implementing HAProxy.
 deb-3-0-ui -->

<!-- snap-2-7-cli
If desired, you can [bypass the use of SSL](/t/high-availability/2682#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2538) without implementing HAProxy.
 snap-2-7-cli -->

<!-- snap-2-7-ui
If desired, you can [bypass the use of SSL](/t/high-availability/2683#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2539) without implementing HAProxy.
 snap-2-7-ui -->

<!-- snap-2-8-cli
If desired, you can [bypass the use of SSL](/t/high-availability/2684#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2540) without implementing HAProxy.
 snap-2-8-cli -->

<!-- snap-2-8-ui
If desired, you can [bypass the use of SSL](/t/high-availability/2685#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2541) without implementing HAProxy.
 snap-2-8-ui -->

<!-- snap-2-9-cli
If desired, you can [bypass the use of SSL](/t/high-availability/2686#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2542) without implementing HAProxy.
 snap-2-9-cli -->

<!-- snap-2-9-ui
If desired, you can [bypass the use of SSL](/t/high-availability/2687#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2543) without implementing HAProxy.
 snap-2-9-ui -->

<!-- snap-3-0-cli
If desired, you can [bypass the use of SSL](/t/high-availability/3945#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2542) without implementing HAProxy.
 snap-3-0-cli -->

<!-- snap-3-0-ui
If desired, you can [bypass the use of SSL](/t/high-availability/3946#heading--load-balancing-with-haproxy-optional) in your HAProxy.  Alternatively, you can [set up TLS encryption on your MAAS web UI](/t/configuring-tls-encryption/2543) without implementing HAProxy.
 snap-3-0-ui -->


<a href="#heading--using-logs-for-security"><h2 id="heading--using-logs-for-security">Use logs to identify security issues</h2></a>

There are four categories of log files that you can use to help identify security issues:

1. firewall logs
2. Web server logs
3. MAAS log files
4. system log files

This section will offer some advice, as well as links to more detailed information on these categories.

<a href="#heading--firewall-logs-subsection"><h3 id="heading--firewall-logs-subsection">Firewall logs</h3></a>

The Ubuntu firewall, [UFW ](https://wiki.ubuntu.com/UncomplicatedFirewall), is a front-end for [iptables ](https://help.ubuntu.com/community/IptablesHowTo), so the UFW log output is very similar to what you'll encounter in iptables itself.  If you want to secure your MAAS installation, it's very important to periodically review your UFW logs, found in `/var/log/ufw*`.

Learning to recognise issues in the UFW/iptables log is an art form, so we're not going to give an extended tutorial here.  Still, there are some key indicators that might help you spot security issues.

You might look for something probing a port that's not supporting an application service.  Attackers use port scanners to look for openings.  You might see entries like these:

    blocked incoming tcp connection request from 96.39.208.43:8240 to 128.17.92.85:6002
    blocked incoming tcp connection request from 96.39.208.43:8240 to 128.17.92.85:6003
    blocked incoming tcp connection request from 96.39.208.43:8240 to 128.17.92.85:6004

You can also compare attempts on unusual port numbers against [well-known hacker tools ](http://www.relevanttechnologies.com/resources_4.asp).  For instance, repeated attempts against port 12361 might mean that someone is attempting to attack with the Whack-a-mole exploit.

Also suspicious are repeated, unsuccessful access attempts, against the same port or service, from the same domain, IP address, or subnet. These attempts may be spread out in time (`grep` is your friend, here).  For example, a group of login attempts that look like this may indicate that an attacker is trying to disguise port scans by switching IP addresses within a block of addresses available to them:

    blocked incoming tcp connection request from 96.39.208.43:49343 to 64.242.119.18:31337
    blocked incoming tcp connection request from 96.39.208.62:49343 to 64.242.119.18:31337
    blocked incoming tcp connection request from 96.39.209.243:49343 to 64.242.119.18:31337
    blocked incoming tcp connection request from 96.39.208.135:49343 to 64.242.119.18:31337
    .
    .
    .
    blocked incoming tcp connection request from 96.39.208.208:49343 to 64.242.119.18:31337

Watch out for suspicious messages or connections originating inside your network, which may indicate that you have a Trojan residing inside your UFW:

    blocked outgoing tcp packet from 192.168.23.100:5240 to 96.38.231.18:443 as FIN:ACK received, but there is no active connection.

This message will usually be repeated a number of times, since Trojans are fairly persistent.

Look for source-routed packets, that is, packets with a source address internal to your network, but which originate from outside your network, indicating that someone is trying to spoof one of your internal addresses.

Review the IP addresses that are being rejected and dropped.  Try to identify them with a `ping -a <IP address>`.  Spoofed addresses won't have an owner (and you can block them).  Real addresses have a [whois ](http://www.internic.net/whois.html) entry, so it's possible you can contact the ISP to report and resolve this issue.

There are many other firewall log analysis techniques, and a number of good open-source and commercial log analysis programs.  If you decide to analyse directly, though, you're basically looking for blocked connection issues, connections to (potentially) open ports you're not using, and suspicious-looking outbound connections.

<a href="#heading--web-server-logs-subsection"><h3 id="heading--web-server-logs-subsection">Web server logs</h3></a>

Detecting malicious activity directed toward your Web server is best done with a log analysis tool.  If you want to review the raw logs directly, you can look for them in two places:

1. `/var/log/httpd/`, `/var/log/apache`, or `/var/log/apache2` (in the case of Apache), or

2. the path given in `/etc/nginx/nginx.conf` or given in your site configuration file, which itself is found at the path `/etc/nginx/sites-available` (in the case of nginx -- look for the `access_log` directive).

Web server log analysis is also an art form, so we don't plan to offer a comprehensive tutorial here, but here are few examples of things to look for in your logs:

1. multiple requests in less than one second, or some other appropriate time-frame.

2. multiple secure/login page accesses in a one-minute window, especially when they fail.

3. attempts to access non-existent pages using different paths or query parameters (e.g., `135.25.48.19:5250/maas/index.html`).

4. look out for SQL injection attacks, for example:

    84.55.41.57- - [14/Apr/2016:08:22:13 0100]
    "GET /wordpress/wp-content/plugins/custom_plugin/check_user.php?userid=1 
    AND (SELECT 6810 FROM(SELECT COUNT(*),CONCAT(0x7171787671,(SELECT 
    (ELT(6810=6810,1))),0x71707a7871,FLOOR(RAND(0)*2))x FROM 
    INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) HTTP/1.1" 200 166 "-" "Mozilla/5.0 
    (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 
    3.5.30729)"

5. attempts to run a Web shell, for instance:

    192.168.1.102 29/Oct/2018:14:52:16 GET /b374k.php HTTP/1.1 200 2125 Mozilla/5.0

As mentioned above, there are a large number of Web server exploits, and this document does not propose to enumerate them all.  If you want to ensure secure operation, though, it's useful to familiarise yourself with these kinds of Web server attacks.

<a href="#heading--maas-log-file-subsection"><h3 id="heading--maas-log-file-subsection">MAAS log files</h3></a>

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli 
Presently, your primary use of MAAS log files to improve security is to periodically check log files for login failures.  You can check for this activity in the `regiond.log` file, found at `/var/log/maas/regiond.log`.  For reference, a valid login request looks like this entry: 
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
Presently, your primary use of MAAS log files to improve security is to periodically check log files for login failures.  You can check for this activity in the `regiond.log` file, found at `/var/snap/maas/common/log/regiond.log`.  For reference, a valid login request looks like this entry: 
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-cli snap-3-0-ui -->

    2020-03-31 21:17:56 regiond: [info] 10.132.172.1 GET /MAAS/accounts/login/ HTTP/1.1
    --> 200 OK (referrer: http://10.132.172.231:5240/MAAS/r/; agent: Mozilla/5.0 (X11;
    Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149
    Safari/537.36)````

If a login fails due to bad input (username/password), the regiond log will contain an entry something like this one:

    2020-03-31 21:18:08 regiond: [info] 10.132.172.1 POST /MAAS/accounts/login/ HTTP/1.1
    --> 400 BAD_REQUEST (referrer: http://10.132.172.231:5240/MAAS/r/; agent:
    Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/80.0.3987.149 Safari/537.36)````

An entry like this one would also be suspect, since it involves omitting username/password entries at the login prompt:

    2020-03-31 21:18:45 regiond: [info] 10.132.172.1 POST /MAAS/accounts/login/ HTTP/1.1
    --> 204 NO_CONTENT (referrer: http://10.132.172.231:5240/MAAS/r/; agent: Mozilla/5.0
    (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149
    Safari/537.36)````

The key differentiator to distinguish problems from routine failures is the frequency.  If you notice a lot of these last two entries in a given period of time, you may want to investigate more thoroughly.

<a href="#heading--system-log-file-subsection"><h3 id="heading--system-log-file-subsection">System log files</h3></a>

You can also use the standard system logs to detect malicious activity, though this subject is largely beyond the scope of this document.  As a simple example, consider using `journalctl` to detect and source an SSH brute force attack:

    [root@maasserver ~]# journalctl -u sshd | grep "Failed password"
    Jun 06 13:45:19 router sshd[2487]: Failed password for root from 234.19.184.6 port 42258 ssh2
    Jun 06 13:45:24 router sshd[2487]: Failed password for root from 234.19.184.6 port 42258 ssh2
    Jun 06 13:45:35 router sshd[2487]: Failed password for root from 234.19.184.6 port 38834 ssh2
    Jun 06 13:45:48 router sshd[2487]: Failed password for root from 234.19.184.6 port 35444 ssh2

From here, you can either use `whois` to locate the attacker and work with the ISP to block them, or simply use your UFW firewall to block them directly.

As mentioned, this subject is far too complex for a detailed tutorial in this section.  For more information, try the [Ubuntu journalctl manpage ](http://manpages.ubuntu.com/manpages/cosmic/man1/journalctl.1.html) or [another, similar source ](https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs).  

<a href="#heading--postgres-security"><h2 id="heading--postgres-security">Implement PostgreSQL security</h2></a>

PostgreSQL contains secrets, and should be encrypted for maximum protection.  You should consider [full disk encryption ](https://help.ubuntu.com/community/Full_Disk_Encryption_Howto_2019).  Also recommended is [TLS encryption between MAAS and PostgreSQL ]( https://www.postgresql.org/docs/current/ssl-tcp.html).

<a href="#heading--what-else-to-do"><h2 id="heading--what-else-to-do">Other things you can do to harden MAAS</h2></a>

In addition to the items mentioned above, you should be aware of a few other points about hardening MAAS.

<a href="#heading--maas-and-root-users"><h3 id="heading--maas-and-root-users">Good passwords</h2></a>

You should pick good passwords and store them securely (e.g. in a KeePassX password database). Perform user administration only via the web UI. Only share the `maas` and `root` user passwords with administrators.

<a href="#heading--conf-file-permissions"><h3 id="heading--conf-file-permissions">File permissions</h2></a>

MAAS configuration files should be set to have permission `640`: readable by logins belonging to the `maas` group and writeable only by the `root` user. Currently, the `regiond.conf` file contains the login credentials for the PostgreSQL database used by MAAS to keep track of all machines, networks, and configuration.

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli
``` bash
chmod 640 /etc/maas/rackd.conf
chmod 640 /etc/maas/regiond.conf
```

After:

``` no-highlight
-rw-r----- 1 root maas   90 Sep 27 14:13 rackd.conf
-rw-r----- 1 root maas  157 Sep 27 14:14 regiond.conf
```
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli deb-3-0-ui deb-3-0-cli -->

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli
``` bash
chmod 640 /var/snap/maas/current/rackd.conf
chmod 640 /var/snap/maas/current/regiond.conf
```

After:

``` no-highlight
-rw-r----- 1 root maas   90 Sep 27 14:13 rackd.conf
-rw-r----- 1 root maas  157 Sep 27 14:14 regiond.conf
```
<a href="#heading--snaps-and-security"><h3 id="heading--snaps-and-security">About snap security</h3></a>

Since snaps are fully confined or "sandboxed," they bring a lot of inherent security to the contained application.  More detailed information can be found in [this snap blog ](https://snapcraft.io/blog/where-eagles-snap-snap-security-overview).
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-ui snap-3-0-cli -->

<a href="#heading--shared-secrets"><h3 id="heading--shared-secrets">Shared secrets</h2></a>

When you add a new rack or region controller, MAAS asks for a shared secret it will use to communicate with the rest of MAAS. This secret is also exposed in the web UI when you click the 'Add rack controller' button on the Controllers page.  MAAS automatically generates this secret when your first region controller installed, and stores the secret in a plain text file.  This file is automatically protected with the correct permissions, so there is no need for any action on your part.

<a href="#heading--security-consulting"><h2 id="heading--security-consulting">Whom to contact about MAAS security consulting</h2></a>

If you need help implementing MAAS security, please [contact us ](https://maas.io/contact-us).  We will be happy to assist you in arranging security consulting appropriate to your needs.
