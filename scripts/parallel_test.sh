#!/bin/bash

function x() {
    # generate a random string
    id=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
    echo "Starting $id"
    sleep 2
    echo "Ending $id"
}

for i in `seq 1 5`; do
    for j in `seq 1 2`; do
        x &
    done
    wait
done



# list of files
filelist = [f for f in os.listdir('.') if os.path.isfile(f)]

# copy each file to outputs/, but rename it using the name of the original file

mkdir -p outputs

for filepath in `cat filelist.txt`; do
    # make a local directory for the file, which has the same path as the file
    localpath=`dirname $filepath`
    mkdir -p "outputs/$localpath
    echo "Copying $filepath to $localpath"
    fileutil cp $filepath $localpath/
done