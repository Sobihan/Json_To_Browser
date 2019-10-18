#!/bin/bash

rm -rf json_to_browser.app
python3 setup.py py2app -A
mv dist/json_to_browser.app ./
rm -rf build
rm -rf dist

echo "Your Program is ready :)"