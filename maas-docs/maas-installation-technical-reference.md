||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/maas-installation-technical-reference-snap-2-7-cli/4522) ~ [UI](/t/maas-installation-technical-reference-snap-2-7-ui/4519)|[CLI](/t/maas-installation-technical-reference-snap-2-8-cli/4523) ~ [UI](/t/maas-installation-technical-reference-snap-2-8-ui/4520)|[CLI](/t/maas-installation-technical-reference-snap-2-9-cli/4524) ~ [UI](/t/maas-installation-technical-reference-snap-2-9-ui/4521)|[CLI](/t/maas-installation-technical-reference-snap-3-0-cli/4525) ~ [UI](/t/maas-installation-technical-reference-snap-3-0-ui/4516)|
Packages|[CLI](/t/maas-installation-technical-reference-deb-2-7-cli/4530) ~ [UI](/t/maas-installation-technical-reference-deb-2-7-ui/4526)|[CLI](/t/maas-installation-technical-reference-deb-2-8-cli/4531) ~ [UI](/t/maas-installation-technical-reference-deb-2-8-ui/4527)|[CLI](/t/maas-installation-technical-reference-deb-2-9-cli/4532) ~ [UI](/t/maas-installation-technical-reference-deb-2-9-ui/4528)|[CLI](/t/maas-installation-technical-reference-deb-3-0-cli/4533) ~ [UI](/t/maas-installation-technical-reference-deb-3-0-ui/4529)|

This article provides technical data relevant the MAAS installation.  Note that all headings are linked for easy bookmarking.

#### The following technical data is available in this document:

* [Minimum hardware requirements for using MAAS](#heading--minimum-hardware-requirements)
* [MAAS initialisation modes](#heading--maas-init-modes)
* [The MAAS shared secret](#heading--shared-secret)
* [MAAS re-initialisation](#heading--maas-reinit)

These sections are presented for reference, so they are not intended to be read in any particular order.

<a href="#heading--minimum-hardware-requirements"><h2 id="heading--minimum-hardware-requirements">Minimum hardware requirements for using MAAS</h2></a>

This section provides the following technical data:

* [Minimum hardware requirements for a MAAS test environment](#heading--min-hardware-test-environment)
* [Minimum hardware requirements for a MAAS production environment](#heading--min-hardware-production-environment)

The minimum requirements for the machines that run MAAS vary widely depending on local implementation and usage.  Below, you will find resource estimates based on MAAS components and operating system (Ubuntu Server). We consider both a test configuration (for proof of concept) and a production environment.

<a href="#heading--min-hardware-test-environment"><h3 id="heading--test-environment">Minimum hardware requirements for a MAAS test environment</h3></a>

Here is a proof-of-concept scenario, with all MAAS components installed on a single host. This scenario assumes two complete sets of images (latest two Ubuntu LTS releases) for a single architecture (amd64).

| | Memory (MB) | CPU (GHz) | Disk (GB) |
|:-----|-----:|-----:|-----:|
| [Region controller](/t/concepts-and-terms/785#heading--controllers) (minus PostgreSQL) | 512 | 0.5 | 5 |
| PostgreSQL | 512 | 0.5 | 5 |
| [Rack controller](/t/concepts-and-terms/785#heading--controllers") | 512 | 0.5 | 5 |
| Ubuntu Server (including logs)| 512 | 0.5 | 5 |

Based on this table, the approximate requirements for this scenario are 2 GB memory, 2 GHz CPU, and 20 GB of disk space.

<a href="#heading--min-hardware-production-environment"><h3 id="heading--min-hardware-production-environment">Minimum requirements for a MAAS production environment</h3></a>

Here is a production scenario designed to handle a high number of sustained client connections. This scenario implements both high availability (region and rack) and load balancing (region). MAAS reserves extra space for images (database and rack controller), while some images, such as those for Microsoft Windows, may require a lot more -- so plan accordingly.

| | Memory (MB) | CPU (GHz) | Disk (GB) |
|:-----|-----:|-----:|-----:|
| [Region controller](/t/concepts-and-terms/785#heading--controllers) (minus PostgreSQL) | 2048 | 2.0 | 5 |
| PostgreSQL | 2048 | 2.0 | 20 |
| [Rack controller](/t/concepts-and-terms/785#heading--controllers") | 2048 | 2.0 | 20 |
| Ubuntu Server (including logs)| 512 | 0.5 | 5 |

So, based on the above, the approximate requirements for this scenario are:

1. A region controller (including PostgreSQL) installed on one host, with 4.5 GB memory, 4.5 GHz CPU, and 45 GB of disk space.
2. A duplicate region controller (including PostgreSQL) on a second host, also with 4.5 GB memory, 4.5 GHz CPU, and 45 GB of disk space.
3. A rack controller installed on a third host, with 2.5 GB memory, 2.5 GHz CPU, and 40 GB of disk space.
4. A duplicate rack controller on a fourth host, also with 2.5 GB memory, 2.5 GHz CPU, and 40 GB of disk space.

<!-- deb-2-7-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3012) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2588).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-7-cli -->

<!-- deb-2-7-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3013) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2689).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-7-ui -->

<!-- deb-2-8-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3014) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2690).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-8-cli -->

<!-- deb-2-8-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3015) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2691).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-8-ui -->

<!-- deb-2-9-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3016) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2692).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-9-cli -->

<!-- deb-2-9-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3017) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2693).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 deb-2-9-ui -->

<!-- snap-2-7-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3006) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2682).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-7-cli -->

<!-- snap-2-7-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3007) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2683).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-7-ui -->

<!-- snap-2-8-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3008) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2684).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-8-cli -->

<!-- snap-2-8-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3009) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2685).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-8-ui -->

<!-- snap-2-9-cli
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3010) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2686).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-9-cli -->

<!-- snap-2-9-ui
[note]
The tables above refer to MAAS infrastructure only. They do not cover the resources needed by subsequently-added nodes. Note that machines should have IPMI-based BMC controllers for power cycling, see [Power management](/t/power-management/3011) for more details.
[/note]

Some examples of factors that influence hardware specifications include:

1. the number of connecting clients (client activity)
2. how you decide to distribute services
3. whether or not you use [high availability/load balancing](/t/high-availability/2687).
4. the number of images that you choose to store (disk space affecting PostgreSQL and the rack controller)
 snap-2-9-ui -->

Also, this discussion does not take into account a possible local image mirror, which would be a large consumer of disk space.

One rack controller should only service 1000 machines or less, regardless of how you distribute them across subnets. There is no load balancing at the rack level, so you will need additional, independent rack controllers. Each controller must service its own subnet(s).

<a href="#heading--maas-init-modes"><h2 id="heading--maas-init-modes">MAAS initialisation modes</h2></a>

MAAS supports the following modes, which dictate what services will run on the local system:

| Mode          | Region | Rack | Database | Description                           |
|---------------|--------|------|----------|---------------------------------------|
| `region`      | X      |      |          | Region API server only                |
| `rack`        |        | X    |          | Rack controller only                  |
| `region+rack` | X      | X    |          | Region API server and rack controller |
| `none`        |        |      |          | Reinitialises MAAS and stops services |

<a href="#heading--maas-init-options"><h3 id="heading--maas-init-options">MAAS initialisation options</h3></a>

MAAS initialisation options correspond to these choices.  For example, the command:

```bash
sudo maas init --help
```

produces the following output:

```
usage: maas init [-h] {region+rack,region,rack} ...

Initialise MAAS in the specified run mode.

optional arguments:
  -h, --help            show this help message and exit

run modes:
  {region+rack,region,rack}
    region+rack         Both region and rack controllers
    region              Region controller only
    rack                Rack controller only

When installing region or rack+region modes, MAAS needs a
PostgreSQL database to connect to.

If you want to set up PostgreSQL for a non-production deployment on
this machine, and configure it for use with MAAS, you can install
the maas-test-db snap before running 'maas init':

    sudo snap install maas-test-db
    sudo maas init region+rack --database-uri maas-test-db:///
```

<a href="#heading--maas-url"><h3 id="heading--maas-url">The MAAS URL</h3></a>

All run modes (except `none`) prompt for a MAAS URL, interpreted differently depending on the mode:

-   `region+rack`: Used to create a new region controller as well as to tell the rack controller how to find the region controller.
-   `region`: Used to create a new region controller.
-   `rack`: Used to locate the region controller.

<a href="#heading--shared-secret"><h2 id="heading--shared-secret">Shared secret</h2></a>

When you add a new rack or region controller, MAAS asks for a shared secret it will use to communicate with the rest of MAAS. This secret is also exposed in the web UI when you click the "Add rack controller" button on the Controllers page. MAAS automatically generates this secret when your first region controller installed, and stores the secret in a plain text file. This file is automatically protected with the correct permissions, so there is no need for any action on your part.

<a href="#heading--maas-reinit"><h3 id="heading--maas-reinit">MAAS re-initialisation</h3></a>

Re-initialising MAAS resets the MAAS URL when the configuration changes.  For example, when hosting MAAS on a system that gets its IP from DHCP, you must reinitialise when the DHCP lease gets renewed, as your base MAAS IP address will need to be updated.  Likewise, if you switch the MAAS configuration from `rack` to `region`, you'll need to re-initialise as well. 

