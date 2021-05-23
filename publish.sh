#!/bin/sh

# Retrieve args
if [ $# -ne 1 ]
then
	echo "Usage: ./publish \"commit message\""
	exit 1
fi

MSG=$1

# Build the site
mv docs/CNAME .
rm -rf docs

hugo
if [ $? -ne 0 ]
then
	echo "Hugo failed to build. Cleaning up."
	mkdir docs
	mv CNAME docs/
	exit $?
fi

mv CNAME docs/

# Push to github and publish the site
git add .
git commit -m "$MSG"
git push
