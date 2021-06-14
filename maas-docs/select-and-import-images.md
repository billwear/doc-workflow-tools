||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/select-and-import-images-snap-2-7-cli/3090) ~ [UI](/t/select-and-import-images-snap-2-7-ui/3091)|[CLI](/t/select-and-import-images-snap-2-8-cli/3092) ~ [UI](/t/select-and-import-images-snap-2-8-ui/3093)|[CLI](/t/select-and-import-images-snap-2-9-cli/3094) ~ [UI](/t/select-and-import-images-snap-2-9-ui/3095)|[CLI](/t/select-and-import-images-snap-3-0-cli/4101) ~ [UI](/t/select-and-import-images-snap-3-0-ui/4102)|
Packages|[CLI](/t/select-and-import-images-deb-2-7-cli/3096) ~ [UI](/t/select-and-import-images-deb-2-7-ui/3097)|[CLI](/t/select-and-import-images-deb-2-8-cli/3098) ~ [UI](/t/select-and-import-images-deb-2-8-ui/3099)|[CLI](/t/select-and-import-images-deb-2-9-cli/3100) ~ [UI](/t/select-and-import-images-deb-2-9-ui/3101)|[CLI](/t/select-and-import-images-deb-3-0-cli/4103) ~ [UI](/t/select-and-import-images-deb-3-0-ui/4104)|

MAAS is only useful once it has images available to provision its nodes. Therefore, one key post-install task is to select and import images from the boot source. Once MAAS imports images, it will update them on an hourly basis, via a default synch mechanism.  This page explains how to select and import the images that MAAS requires to provision its nodes.

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  

#### Three questions you may have:

1. [How do I import standard images from maas.io?](#heading--import-maasio-image-ui)
2. [How do I use other image mirrors to download images?](#heading--image-mirrors)
3. [How do I import and provision non-Ubuntu images?](#heading--other-images)

snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/2857).
 deb-2-7-ui -->

<!-- deb-2-8-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/2859).
 deb-2-8-ui -->

<!-- deb-2-9-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/2861).
 deb-2-9-ui -->

<!-- deb-3-0-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/4000).
 deb-3-0-ui -->
 
<!-- snap-2-7-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/2851).
 snap-2-7-ui -->

<!-- snap-2-8-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/2853).
 snap-2-8-ui -->

<!-- snap-2-9-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/2855).
 snap-2-9-ui -->

<!-- snap-3-0-ui
Note that it is possible to build your own images in a limited sense: see [MAAS Image Builder](/t/maas-image-builder/3998).
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  

<a href="#heading--import-maasio-image-ui"><h2 id="heading--import-maasio-image-ui">Importing images from maas.io</h2></a>

The 'Images' page shows what images and architectures have been selected and downloaded. By default, MAAS will automatically grab the most recent Ubuntu LTS releases (and amd64 architecture). Below, we have selected two additional releases:

<a href="https://discourse.maas.io/uploads/default/original/1X/d208922f1126ec92f6ef06cfaa5e16dbbfc613d0.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/d208922f1126ec92f6ef06cfaa5e16dbbfc613d0.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui  snap-3-0-ui deb-3-0-ui -->

<!-- deb-2-7-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/2701#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-2-7-ui -->

<!-- deb-2-8-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/2703#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-2-8-ui -->

<!-- deb-2-9-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/2705#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-2-9-ui -->

<!-- deb-3-0-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/3960#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-3-0-ui -->

<!-- snap-2-7-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/2695#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-2-7-ui -->

<!-- snap-2-8-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/2697#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-2-8-ui -->

<!-- snap-2-9-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/2699#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-2-9-ui -->

<!-- snap-3-0-ui
You can tell MAAS to sync images hourly, at the region level, using a toggle switch in the top-right corner of the screen.  See [Boot image sources](/t/images/3958#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
Click the 'Save selection' button to initiate the import. MAAS will present existing images along with the newly-selected ones. The latter will have their status updated as the import is processed:

<a href="https://discourse.maas.io/uploads/default/original/1X/f7daa92c97f1ada61c2172044d43856ed3e14b5f.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/f7daa92c97f1ada61c2172044d43856ed3e14b5f.png"></a>

To remove an image, unselect it and click 'Save selection'.

<a href="#heading--image-mirrors"><h2 id="heading--image-mirrors">Image mirrors</h2></a>

You can also host Ubuntu images on a mirror. Configure this mirror by selecting 'Custom' beneath 'Choose source'. Enter the mirror URL and click 'Connect'.

Advanced options, such as using a GPG key or keyring to validate the mirror path (snap installation location: /snap/maas/current/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg), are revealed by clicking 'Show advanced options':

<a href="https://discourse.maas.io/uploads/default/original/1X/dbe44a827e70e318a6139c3e335019a6a27c4374.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/dbe44a827e70e318a6139c3e335019a6a27c4374.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- deb-2-7-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2808) for instructions.
 deb-2-7-cli -->

<!-- deb-2-7-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2809) for instructions.
 deb-2-7-ui -->

<!-- deb-2-8-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2810) for instructions.
 deb-2-8-cli -->

<!-- deb-2-8-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2811) for instructions.
 deb-2-8-ui -->

<!-- deb-2-9-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2812) for instructions.
 deb-2-9-cli -->

<!-- deb-2-9-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2813) for instructions.
 deb-2-9-ui -->

<!-- deb-3-0-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/3983) for instructions.
 deb-3-0-cli -->

<!-- deb-3-0-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/3984) for instructions.
 deb-3-0-ui -->

<!-- snap-2-7-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2802) for instructions.
 snap-2-7-cli -->

<!-- snap-2-7-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2803) for instructions.
 snap-2-7-ui -->

<!-- snap-2-8-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2804) for instructions.
 snap-2-8-cli -->

<!-- snap-2-8-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2805) for instructions.
 snap-2-8-ui -->

<!-- snap-2-9-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2806) for instructions.
 snap-2-9-cli -->

<!-- snap-2-9-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/2807) for instructions.
 snap-2-9-ui -->

<!-- snap-3-0-cli
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/3981) for instructions.
 snap-3-0-cli -->

<!-- snap-3-0-ui
Optionally, a local mirror can be set up as the boot source. MAAS will then use it instead of the standard internet-based server. Local mirroring significantly reduces the time required import images. See [Local image mirror](/t/local-image-mirror/3982) for instructions.
 snap-3-0-ui -->

<!-- snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui 
<a href="#heading--other-images"><h2 id="heading--other-images">Other images</h2></a>

It is also possible to import and provision images other than Ubuntu. Images supported and provided by MAAS will appear beneath the 'Other Images' section. Currently, images for CentOS 6.6, CentOS 7.0, and CentOS 8.0 are available. These images can be imported and used just like the Ubuntu images above.

<a href="https://discourse.maas.io/uploads/default/original/1X/198aa78b2dd3a650f1b3909ae2c9269e159ca1dc.png" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/198aa78b2dd3a650f1b3909ae2c9269e159ca1dc.png"></a>
snap-2-7-ui snap-2-8-ui snap-2-9-ui deb-2-7-ui deb-2-8-ui deb-2-9-ui snap-3-0-ui deb-3-0-ui  -->

<!-- deb-2-7-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/2700#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-2-7-cli -->

<!-- deb-2-8-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/2702#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-2-8-cli -->

<!-- deb-2-9-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/2704#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-2-9-cli -->
 
<!-- deb-3-0-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/3959#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 deb-3-0-cli -->
 
<!-- snap-2-7-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/2694#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-2-7-cli -->
 
<!-- snap-2-8-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/2696#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-2-8-cli -->

<!-- snap-2-9-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/2698#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-2-9-cli -->

<!-- snap-3-0-cli
You can tell MAAS to sync images hourly, at the region level.  See [Boot image sources](/t/images/3957#boot-image-sources)) for more details. We highly recommended synching images hourly. Syncing at the rack controller level (from regiond) occurs every 5 min and cannot be disabled.
 snap-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

#### Eight questions you may have:

1. [How do I get started with the MAAS CLI?](/t/maas-cli/802)
2. [How do I list boot sources?](#heading--list-boot-sources)
3. [How do I select images?](#heading--select-image)
4. [How do I list image selections?](#heading--list-image-selections)
5. [How do I import newly-selected images?](#heading--import-newly-selected-images)
6. [How do I list currently available images?](#heading--list-currently-available-images)
7. [How do I delete a boot source?](#heading--delete-a-boot-source)
8. [How do I edit a boot source?](#heading--edit-a-boot-source)

<a href="#heading--list-boot-sources"><h2 id="heading--list-boot-sources">List boot sources</h2></a>

If you want to download boot sources, i.e., the locations from which you may download images, try the following:

``` bash
maas $PROFILE boot-sources read
```

[note]
Although multiple boot sources may be listed, MAAS can only practically work with a single boot source.
[/note]

<a href="#heading--select-images"><h2 id="heading--select-images">Select images</h2></a>

Use the `boot-source-selections` command to select images from a boot source. After selecting new images, you will need to [import](#heading--import-newly-selected-images) them.

``` bash
maas $PROFILE boot-source-selections create $SOURCE_ID \
    os="ubuntu" release="$SERIES" arches="$ARCH" \
    subarches="$KERNEL" labels="*"
```

For example, to select all kernels for 64-bit Trusty from a boot source with an id of '1':

``` bash
maas $PROFILE boot-source-selections create 1 \
    os="ubuntu" release="trusty" arches="amd64" \
    subarches="*" labels="*"
```

<a href="#heading--hardware-enablement-hwe"><h3 id="heading--hardware-enablement-hwe">Hardware enablement (HWE)</h3></a>

For example, to get just the latest amd64 HWE kernel available for Trusty, which, at time of writing, is from Xenial:

``` bash
maas $PROFILE boot-source-selections create 1 \
    os="ubuntu" release="trusty" arches="amd64" \
    subarches="hwe-x" labels="*"
```

For Xenial kernels (and starting with MAAS 2.1), notation has changed. To select the latest amd64 HWE kernel available for Xenial:

``` bash
maas $PROFILE boot-source-selections create 1 \
    os="ubuntu" release="xenial" arches="amd64" \
    subarches="hwe-16.04" labels="*"
```

<a href="#heading--list-image-selections"><h2 id="heading--list-image-selections">List image selections</h2></a>

To list image selections for a boot source:

``` bash
maas $PROFILE boot-source-selections read $SOURCE_ID
```

<a href="#heading--import-newly-selected-images"><h2 id="heading--import-newly-selected-images">Import newly-selected images</h2></a>

To import newly-selected images (boot resources):

``` bash
maas $PROFILE boot-resources import
```

Once newly-selected images are imported, a sync mechanism is enabled (by default) to keep them up to date. The refresh time interval is 60 minutes.

Available images resulting from this action are reflected in the web UI.

<a href="#heading--list-currently-available-images"><h2 id="heading--list-currently-available-images">List currently available images</h2></a>

To list currently available/imported images (boot resources):

``` bash
maas $PROFILE boot-resources read
```

<a href="#heading--delete-a-boot-source"><h2 id="heading--delete-a-boot-source">Delete a boot source</h2></a>

To delete a boot source (the location from which you can download images): 

``` bash
maas $PROFILE boot-source delete $SOURCE_ID
```

If you delete the sole boot source, then the fields 'Sync URL' and 'Keyring Path' in the web UI will take on null values.

<a href="#heading--edit-a-boot-source"><h2 id="heading--edit-a-boot-source">Edit a boot source</h2></a>

You can edit an existing boot source by changing the GPG keyring file ($KEYRING_FILE) and the location ($URL).

Update the boot source:

``` bash
maas $PROFILE boot-source update $SOURCE_ID \
    url=$URL keyring_filename=$KEYRING_FILE
```

At this time MAAS only supports a boot source containing official MAAS images. As a result, you can only edit a boot source if you have set up a mirror of its images. The location can change, but the keyring remains constant:

KEYRING_FILE=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg

<a href="#heading--add-a-boot-source"><h2 id="heading--add-a-boot-source">Add a boot source</h2></a>

[note]
To avoid unnecessary complexity, you should probably delete any existing boot sources before adding a new one.
[/note]

Presented below are two use cases for adding a boot source:

1.  Use a local image mirror (official images)
2.  If you deleted the default image, recreate it

The general syntax is:

``` bash
maas $PROFILE boot-sources create \
    url=$URL keyring_filename=$KEYRING_FILE
```

The output will include a new numeric ID that identifies the boot source ($SOURCE_ID).

Since MAAS can only practically work with a single boot source, so you will need to delete any existing sources. Note that the location (URL) is the only variable. The only supported keyring is:

KEYRING_FILE=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg

If you added a sole boot source, then the fields 'Sync URL' and 'Keyring Path' in the web UI will reflect its values.

<a href="#heading--using-a-local-image-mirror"><h3 id="heading--using-a-local-image-mirror">Using a local image mirror</h3></a>

snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli  snap-3-0-cli deb-3-0-cli -->

<!-- deb-2-7-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/2808) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 deb-2-7-cli -->

<!-- deb-2-8-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/2810) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 deb-2-8-cli -->

<!-- deb-2-9-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/2812) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 deb-2-9-cli -->

<!-- deb-3-0-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/3983) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 deb-3-0-cli -->

<!-- snap-2-7-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/2802) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 snap-2-7-cli -->

<!-- snap-2-8-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/2804) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 snap-2-8-cli -->

<!-- snap-2-9-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/2806) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 snap-2-9-cli -->

<!-- snap-3-0-cli
Once the mirror is set up according to [Local image mirror](/t/local-image-mirror/3981) it is just a matter of specifying the mirror location (URL). Since the images come from the default source, you should use the default keyring. If you are following the above mirror document, the variable values should be:
 snap-3-0-cli -->

<!-- snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli 

1.   URL=https://$MIRROR/maas/images/ephemeral-v3/stable/
2.   KEYRING_FILE=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg

Where $MIRROR is the mirror server's hostname or IP address.

<a href="#heading--recreate-the-default-boot-source"><h3 id="heading--recreate-the-default-boot-source">Recreate the default boot source</h3></a>

Recreate the default boot source if it was ever deleted using the following variable values:

1.   URL=https://images.maas.io/ephemeral-v3/stable/
2.   KEYRING_FILE=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
snap-2-7-cli snap-2-8-cli snap-2-9-cli deb-2-7-cli deb-2-8-cli deb-2-9-cli snap-3-0-cli deb-3-0-cli -->
