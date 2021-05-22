#!/bin/sh

MSG=$1

hugo
git add .
git commit -m "$MSG"
git push
