#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu" ]]; then
    sudo apt-get update
    sudo apt-get install python3.6

elif [[ "$OSTYPE" == "darwin"* ]]; then
       xcode-select --install
       /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
       brew doctor
       brew install python3
fi

pip3 install tk
pip3 install validators