#!/bin/sh

# path
#ROOT=`readlink -f $(dirname $0)`
ROOT=~/Seaside.app
LINUX="$ROOT/Contents/Linux"
RESOURCES="$ROOT/Contents/Resources"

# icon (note: gvfs-set-attribute is found in gvfs-bin on Ubuntu
# systems and it seems to require an absolute filename)
gvfs-set-attribute \
	"$0" \
	"metadata::custom-icon" \
	"file://$RESOURCES/Squeak.png" \
		2> /dev/null

image="$RESOURCES/Seaside.image"

# execute
exec "$LINUX/squeak" \
	-plugins "$LINUX" \
	-encoding latin1 \
	-vm-display-null \
	-vm-sound-null \
	"$image" \
	2>&1 >/dev/null \
	$RESOURCES/startup.st
