||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/using-maas-in-an-air-gapped-environment-snap-2-7-cli/4286) ~ [UI](/t/using-maas-in-an-air-gapped-environment-snap-2-7-ui/4285)|[CLI](/t/using-maas-in-an-air-gapped-environment-snap-2-8-cli/4272) ~ [UI](/t/using-maas-in-an-air-gapped-environment-snap-2-8-ui/4271)|[CLI](/t/using-maas-in-an-air-gapped-environment-snap-2-9-cli/4274) ~ [UI](/t/using-maas-in-an-air-gapped-environment-snap-2-9-ui/4273)|[CLI](/t/using-maas-in-an-air-gapped-environment-snap-3-0-cli/4153) ~ [UI](/t/using-maas-in-an-air-gapped-environment-snap-3-0-ui/4154)|
Packages|[CLI](/t/using-maas-in-an-air-gapped-environment-deb-2-7-cli/4287) ~ [UI](/t/using-maas-in-an-air-gapped-environment-deb-2-7-ui/4288)|[CLI](/t/using-maas-in-an-air-gapped-environment-deb-2-8-cli/4269) ~ [UI](/t/using-maas-in-an-air-gapped-environment-deb-2-8-ui/4268)|[CLI](/t/using-maas-in-an-air-gapped-environment-deb-2-9-cli/4270) ~ [UI](/t/using-maas-in-an-air-gapped-environment-deb-2-9-ui/4275)|[CLI](/t/using-maas-in-an-air-gapped-environment-deb-3-0-cli/4155) ~ [UI](/t/using-maas-in-an-air-gapped-environment-deb-3-0-ui/4156)|
Many MAAS users maintain their data centres in an air-gapped environment -- that is, one that does not have an external Internet connection. MAAS runs well in this configuration, though keeping MAAS supplied with updates and images requires a bit of extra effort.

There are essentially four things that must be available to an air-gapped MAAS for smooth operation:

1. Snap updates (via the snap proxy)
2. Packages (via a local repo, possibly with a transparent proxy)
3. MAAS-maintained images (via  local mirror, possibly with a transparent proxy)
4. Other OS images (various methods)

There is at least one way to make each of these things available in an air-gapped environment.  Some of these can be set up to use a transparent proxy, which minimises changes to other components of the MAAS environment.

#### Five questions you may have:

1. [How do I use the snap proxy to refresh snaps in an air-gapped environment?](#heading--snap-proxy)
2. [How do I make package updates available in an air-gapped environment?](#heading--apt-mirror)
3. [How do I retrieve or update MAAS images in an air-gapped environment?](#heading--local-image-mirroring)
4. [How do I retrieve or update non-MAAS-maintained images in an air-gapped environment?](#heading--non-maas-images)
5. [How do I set up a transparent proxy?](#heading--transparent-proxy)

<h2 id="heading--snap-proxy"><a href="#heading--snap-proxy">Using the snap proxy</a></h2>

Using snaps in an air-gapped environment is possible with the Snap Store Proxy, which can be deployed in networks that are disconnected from the Internet.  Currently, the features required to use this proxy in an [air-gapped](https://docs.ubuntu.com/snap-store-proxy/en/airgap) mode are part of a password-protected internal Beta.  

Client devices connect to the air-gapped proxy and never contact the general Snap Store nor the Internet.  Proxy operators will need to side-load all needed snaps and updates into the proxy. 

There are three main steps to setting up this proxy:

1. Register an offline Snap Store Proxy on an Internet-connected machine.
2. Set up HTTPS access to ensure adequate security.
3. Fetch the necessary snaps as needed by your MAAS environment (on the Internet-connected machine).

This proxy requires a properly configured PostgreSQL database -- see the [setup instructions](https://docs.ubuntu.com/snap-store-proxy/en/airgap) for the Snap Store Proxy for more details.

<h2 id="heading--apt-mirror"><a href="#heading--apt-mirror">Using local package repos</a></h2>

The simplest way to use local package repos is via the [reprepro](http://manpages.ubuntu.com/manpages/focal/man1/reprepro.1.html) command.  There is an older command, `apt-mirror`, which is no longer maintained; it's not recommended.

The `reprepro` command manages a local repository of Debian packages.  You can add files manually or download them from some other repository.  It does not require an external database.  This command also handles signatures of mirrored repos, and can create signatures for the generated package indices, if desired.  

You may wish to create a [transparent proxy](#heading--transparent-proxy) to make using your local repo easier.

<h2 id="heading--local-image-mirroring"><a href="#heading--local-image-mirroring">Local image mirrors</a></h2>
 
MAAS has an [established process](https://maas.io/docs/snap/2.9/ui/local-image-mirror) for mirroring images locally.   The steps are relatively simple:

1. Install the `simplestreams` package.
2. Define some variables to simplify CLI usage.
3. Create the desired mirrors, specifying where you want your images stored.
4. Set up a new boot source on your local server, referring to the local mirror.

See the [local image mirror](https://maas.io/docs/snap/2.9/ui/local-image-mirror) for details.  Note that you can use the menu at the top of that page to switch to specific instructions for the version, build-type, and interface you prefer.

<h2 id="heading--non-maas-images"><a href="#heading--non-maas-images">Using other OS images in an air-gapped environment</a></h2>

MAAS allows you to deploy many types of OSes, and, once deployed, install specific software.  MAAS can configure a user specified repository for Ubuntu, so a user can mirror the Ubuntu apt repositories and point MAAS at those repos. When Ubuntu deploys apt will automatically be configured to use the user defined apt mirrors. 

MAAS only does this for Ubuntu, not CentOS or RHEL. If you deploy CentOS or RHEL with MAAS, the repos that built the image will be deployed.  But this won't work in an air \-gapped environment. To access non-MAAS-maintained images in an air-gapped environment, you will need to use one of two methods:

1. Use `user_data`.
2. Create custom images and store them in your local mirror.

Here's a thumbnail sketch of both of these methods.

<h3 id="heading--other-os-user-data"><a href="#heading--other-os-user-data">Using user_data to access non-MAAS-maintained images</a></h3>

A user can create custom `user_data` which will configure CentOS or RHEL to use a specific mirror.  Check out the [custom machine setup](https://maas.io/docs/snap/2.9/ui/custom-machine-setup) page for details on how to make this work.

<h3 id="heading--store-custom-images"><a href="#heading--store-custom-images">Storing customer images for non-MAAS-maintained images</a></h3>

You can also create custom images and store them in your local mirror.  Use the [MAAS Image Builder](https://maas.io/docs/image-builder) to create custom images as desired.  Once you have the image built, consult the page on [local image mirrors](https://maas.io/docs/snap/2.9/ui/local-image-mirror) to see how to incorporate your newly-built image into the local stash.

<h2 id="heading--transparent-proxy"><a href="#heading--transparent-proxy">Creating a transparent proxy</a></h2>

If you don't wish to disturb the default configurations for Ubuntu and MAAS, you can create a transparent proxy for Debian packages and images, via the following general steps:

1. Configure Ubuntu to get packages via HTTP.
2. Configure MAAS to get packages via HTTP.
3. Create a local mirror repo for `archive.ubuntu.com`.
4. Create a local image mirror for `images.maas.io`.
5. Configure DNS to point to the local mirrors for both of those URLs.

This avoids any need to change the default settings for MAAS or Ubuntu.
