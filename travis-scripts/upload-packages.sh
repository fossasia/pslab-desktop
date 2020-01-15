#!/bin/sh

curl "https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh" -o dropbox_uploader.sh
chmod +x dropbox_uploader.sh

openssl aes-256-cbc -K $enc_key -iv $enc_iv -in .dropbox_uploader.enc -out ~/.dropbox_uploader -d

find dist -maxdepth 1 -type f \( -name '*.snap' -o -name '*.deb' -o -name '*.exe' -o -name '*.dmg' \) -exec sh -c 'file=$(basename "{}");cp "{}" "temp-$file";' \;

for file in temp-*; do
    filename=$(basename -- "$file")
    ./dropbox_uploader.sh upload "$file" "PsLab-Desktop/pslab-desktop-$TRAVIS_BRANCH-$TRAVIS_JOB_NAME.${filename##*.}"
done