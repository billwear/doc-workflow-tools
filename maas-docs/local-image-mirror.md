||2.7|2.8|2.9|3.0|
|-----:|:-----:|:-----:|:-----:|:-----:|
Snap|[CLI](/t/local-image-mirror-snap-2-7-cli/2802) ~ [UI](/t/local-image-mirror-snap-2-7-ui/2803)|[CLI](/t/local-image-mirror-snap-2-8-cli/2804) ~ [UI](/t/local-image-mirror-snap-2-8-ui/2805)|[CLI](/t/local-image-mirror-snap-2-9-cli/2806) ~ [UI](/t/local-image-mirror-snap-2-9-ui/2807)|[CLI](/t/local-image-mirror-snap-3-0-cli/3981) ~ [UI](/t/local-image-mirror-snap-3-0-ui/3982)|
Packages|[CLI](/t/local-image-mirror-deb-2-7-cli/2808) ~ [UI](/t/local-image-mirror-deb-2-7-ui/2809)|[CLI](/t/local-image-mirror-deb-2-8-cli/2810) ~ [UI](/t/local-image-mirror-deb-2-8-ui/2811)|[CLI](/t/local-image-mirror-deb-2-9-cli/2812) ~ [UI](/t/local-image-mirror-deb-2-9-ui/2813)|[CLI](/t/local-image-mirror-deb-3-0-cli/3983) ~ [UI](/t/local-image-mirror-deb-3-0-ui/3984)|

Mirroring images is worthy of consideration.  The SimpleStreams protocol delivers Images to MAAS, which is especially useful when your Internet link is slow or unreliable. In this mirrored configuration, images will be instantly available when MAAS requests them.

Canonical provides two SimpleStreams for MAAS images: candidate and stable. Both streams contain Ubuntu images, CentOS images, bootloaders extracted from the Ubuntu archive, and release notifications. Either stream can be used in any version of MAAS greater than 2.1, but not all images are supported in older versions.

#### Six questions you may have:

1. [What is the candidate stream?](#heading--candidate-stream)
2. [What is the stable stream?](#heading--stable-stream)
3. [What happened to the daily stream?](#heading--daily-stream)
4. [How do I change the stream with the UI?](#heading--changing-the-stream)
5. [How do I change the stream with the CLI?](#heading--changing-stream-with-cli)
6. [How do I set up a local image mirror?](#heading--set-up-local-mirror)

<a href="#heading--candidate-stream"><h2 id="heading--candidate-stream">Candidate stream</h2></a>

The candidate stream contains images and bootloaders which have not been explicitly tested with MAAS. Canonical's automated build process dumps all images and bootloaders here before they are tested with MAAS. This stream is useful when testing a bug fix before an image or bootloader has been promoted to stable. Think of the candidate stream as a preview: it should never be used in a production environment; and users are encouraged to provide feedback on any issues they find with this stream.

This stream is available [here](http://images.maas.io/ephemeral-v3/candidate).

<a href="#heading--stable-stream"><h2 id="heading--stable-stream">Stable stream</h2></a>

The stable stream contains images and bootloaders which have been tested with the latest version of MAAS. This is the default stream which should be used in production environments.  This stream is available [here](http://images.maas.io/ephemeral-v3/stable).

<a href="#heading--daily-stream"><h2 id="heading--daily-stream">Sunset of "daily" stream</h2></a>

Previously there was only one MAAS stream available, daily. This stream has been replaced by the stable stream. Any client using this stream will be automtically redirected to the stable stream.

<a href="#heading--changing-the-stream"><h2 id="heading--changing-the-stream">Changing the stream - UI</h2></a>

To switch to the candidate stream simply select "custom" on the images page, set the URL to `http://images.maas.io/ephemeral-v3/candidate`, and click "Connect"

<a href="https://discourse.maas.io/uploads/default/original/1X/0588c8d2e5792edad3f53e90e38e9990a6d86d9a.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/0588c8d2e5792edad3f53e90e38e9990a6d86d9a.jpeg"></a>

MAAS uses the stable stream by default. To switch back to it simply select `maas.io` on the images page

<a href="https://discourse.maas.io/uploads/default/original/1X/5e20342f04e30f96ac0e29a5bd3117aa71dacd40.jpeg" target = "_blank"><img src="https://discourse.maas.io/uploads/default/original/1X/5e20342f04e30f96ac0e29a5bd3117aa71dacd40.jpeg"></a>

<a href="#heading--changing-stream-with-cli"><h2 id="heading--changing-stream-with-cli">Changing the stream - API/CLI</h2></a>

To switch to a stream with the CLI, enter the following commands:

```
BOOT_SOURCE_ID=$(maas $PROFILE boot-sources read | jq '.[] | select(.url | contains("images.maas.io/ephemeral-v3")) | .id')
maas $PROFILE boot-source update $BOOT_SOURCE_ID url=$STREAM_URL
```
<a href="#heading--set-up-local-mirror"><h2 id="heading--set-up-local-mirror">Setting up a local mirror</h2></a>

To use mirroring, you begin by installing the necessary software on the host that will house the mirror:

``` bash
sudo apt install simplestreams
```

First define some variables to unclutter eventual CLI commands:

``` bash
KEYRING_FILE=/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
IMAGE_SRC=https://images.maas.io/ephemeral-v3/stable
IMAGE_DIR=/var/www/html/maas/images/ephemeral-v3/stable
```

The below example selects all available kernels that are compatible with either Ubuntu 18.04 (Bionic) and Ubuntu 20.04 (Focal) for the amd64 architecture, resulting in a download of approximately 3.1 GB. The second command mirrors the bootloaders.

``` bash
sudo sstream-mirror --keyring=$KEYRING_FILE $IMAGE_SRC $IMAGE_DIR \
    'arch=amd64' 'release~(bionic|focal)' --max=1 --progress
sudo sstream-mirror --keyring=$KEYRING_FILE $IMAGE_SRC $IMAGE_DIR \
    'os~(grub*|pxelinux)' --max=1 --progress
```

To know in advance what the `sstream-mirror` command will grab, or if you want to save bandwidth and time by avoiding bad selections, include the `--dry-run` option. When you are satisfied, remove that option to initiate the download.

MAAS will write the images to disk in the directory defined by the variable 'IMAGE_DIR' above, and the 'location' of the new boot source will be:

`URL=http://<myserver>/maas/images/ephemeral-v3/stable/`

Where `<myserver>` identifies your server's hostname or IP address.

Verify the availability of the images by visiting the above URL.

The final `sstream-mirror` command should be invoked at regular intervals (i.e. with `cron`) to ensure the mirror contains the latest images.

