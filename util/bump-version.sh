#!/bin/bash

set -ex

if [ -z "$1" ]; then
    echo "New version not specified. Usage: bump-version.sh NEW_VERSION"
    exit 1
fi

NEW_VERSION=$1
CURRENT_VERSION=$(sed -ne "s/^VERSION = \"\(.*\)\"/\1/p" cli/setup.py)
sed -i "s/VERSION = \"$CURRENT_VERSION\"/VERSION = \"$NEW_VERSION\"/g" cli/setup.py

sed -i "s/\"parallelcluster\": \"$CURRENT_VERSION\"/\"parallelcluster\": \"$NEW_VERSION\"/g" cli/src/pcluster/constants.py
sed -i "s/aws-parallelcluster-cookbook-$CURRENT_VERSION/aws-parallelcluster-cookbook-$NEW_VERSION/g" cli/src/pcluster/constants.py
