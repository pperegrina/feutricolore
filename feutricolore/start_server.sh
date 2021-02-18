#!/bin/bash
cd $(readlink -e $(dirname $0)/..)
source djenv/bin/activate
cd feutricolore
nohup python server.py >/dev/null 2>&1 &

