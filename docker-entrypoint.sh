#!/bin/sh

set -e

rm -rf build
mkdir build
cp -r assets build/assets
python main.py