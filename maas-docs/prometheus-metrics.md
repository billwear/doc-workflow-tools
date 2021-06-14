||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/prometheus-metrics-snap-2-7-cli/3018) ~ [UI](/t/prometheus-metrics-snap-2-7-ui/3019)|[CLI](/t/prometheus-metrics-snap-2-8-cli/3020) ~ [UI](/t/prometheus-metrics-snap-2-8-ui/3021)|[CLI](/t/prometheus-metrics-snap-2-9-cli/3022) ~ [UI](/t/prometheus-metrics-snap-2-9-ui/3023)|[CLI](/t/prometheus-metrics-snap-3-0-cli/4073) ~ [UI](/t/prometheus-metrics-snap-3-0-ui/4074)|
Packages|[CLI](/t/prometheus-metrics-deb-2-7-cli/3024) ~ [UI](/t/prometheus-metrics-deb-2-7-ui/3025)|[CLI](/t/prometheus-metrics-deb-2-8-cli/3026) ~ [UI](/t/prometheus-metrics-deb-2-8-ui/3027)|[CLI](/t/prometheus-metrics-deb-2-9-cli/3028) ~ [UI](/t/prometheus-metrics-deb-2-9-ui/3029)|[CLI](/t/prometheus-metrics-deb-3-0-cli/4075) ~ [UI](/t/prometheus-metrics-deb-3-0-ui/4076)|

MAAS services can provide [Prometheus](https://prometheus.io/) endpoints for collecting performance metrics.  These include five endpoints of particular interest to MAAS users:

1.   TFTP server file transfer latency
2.   HTTP requests latency
3.   Websocket requests latency
4.   RPC calls (between MAAS services) latency
5.   Per request DB queries counts

All available metrics are prefixed with `maas_`, to make it easier to look them up in Prometheus and Grafana UIs.

#### Three questions you may have:

1. [How do I enable Prometheus endpoints?](#heading--enabling-prometheus-endpoints)
2. [How do I configure Prometheus endpoints?](#heading--configuring-prometheus)
3. [How can I deploy Prometheus and Grafana?](#heading--deploying-prometheus-and-grafana)

<a href="#heading--enabling-prometheus-endpoints"><h2 id="heading--enabling-prometheus-endpoints">Enabling Prometheus endpoints</h2></a>

Whenever you install the `python3-prometheus-client` library, Prometheus endpoints are exposed over HTTP by the `rackd` and `regiond` processes under the default `/metrics` path.

[note]
Currently, prometheus metrics are shared when rack and region controllers are running on the same machine, even though each service provides its own port.  You can safely only query one of the two ports if you're running both controllers.
[/note]

<!-- snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli snap-3-0-cli deb-3-0-cli 
For a snap-based MAAS installation, the libraries already included in the snap so that metrics will be available out of the box.
snap-2-7-ui snap-2-7-cli snap-2-8-ui snap-2-8-cli snap-2-9-ui snap-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli snap-3-0-cli deb-3-0-cli 
For a Debian-based MAAS installation, install the library and restart MAAS services as follows:

    sudo apt install python3-prometheus-client
    sudo systemctl restart maas-rackd
    sudo systemctl restart maas-regiond

MAAS also provides optional stats about resources registered with the MAAS server itself.  These include four broad categories of information:

1.   The number of nodes by type, arch, ...
2.   Number of networks, spaces, fabrics, VLANs and subnets
3.   Total counts for machines CPU cores, memory and storage
4.   Counters for VM host resources

After installing the `python3-prometheus-client` library as describe above, run the following to enable stats:

    maas $PROFILE maas set-config name=prometheus_enabled value=true
deb-2-7-ui deb-2-7-cli deb-2-8-ui deb-2-8-cli deb-2-9-ui deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<a href="#heading--configuring-prometheus"><h2 id="heading--configuring-prometheus">Configuring Prometheus</h2></a>

Once the `/metrics` endpoint is available in MAAS services, Prometheus can be configured to scrape metric values from these. You can configure this by adding a stanza like the following to the [prometheus configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/):

``` yaml
    - job_name: maas
      static_configs:
        - targets:
          - <maas-host1-IP>:5239  # for regiond
          - <maas-host1-IP>:5249  # for rackd
          - <maas-host2-IP>:5239  # regiond-only
          - <maas-host3-IP>:5249  # rackd-only
```

If the MAAS installation includes multiple nodes, the `targets` entries must be adjusted accordingly, to match services deployed on each node.

If  you have enabled MAAS stats,  you must add an additional Prometheus job to the config:

``` yaml
    - job_name: maas
      metrics_path: /MAAS/metrics
      static_configs:
        - targets:
          - <maas-host-IP>:5240
```

In case of a multi-host deploy, adding a single IP for any of the MAAS hosts running `regiond` will suffice.

<a href="#heading--deploying-prometheus-and-grafana"><h2 id="heading--deploying-prometheus-and-grafana">Deploying Prometheus and Grafana</h2></a>

[Grafana](https://grafana.com/) and Prometheus can be easily deployed using Juju.

The [MAAS performance repo](https://git.launchpad.net/~maas-committers/maas/+git/maas-performance) repository provides a sample `deploy-stack` script that will deploy and configure the stack on LXD containers.

First, you must install juju via:

    sudo snap install --classic juju

Then you can run the script from the repo:

    grafana/deploy-stack <MAAS-IP>

To follow the progress of the deployment, run the following:

    watch -c juju status --color

Once you deploy everything, the Grafana UI is accessible on port `3000` with the credentials `admin`/`grafana`. The Prometheus UI will be available on port `9090`.

The repository also provides some sample dashboard covering the most common use cases for graphs. These are available under `grafana/dashboards`.  You can import them from the Grafana UI or API.
