#!/bin/sh

git config --global user.name "Travis CI"
git config --global user.email "noreply@travis.com"

git clone --quiet --branch=install https://fossasia:$GITHUB_API_KEY@github.com/fossasia/pslab-desktop install > /dev/null
    
cd install 

rm -rf pslab-desktop-$TRAVIS_BRANCH-$TRAVIS_JOB_NAME*

find ../dist -maxdepth 1 -type f \( -name '*.snap' -o -name '*.deb' -o -name '*.exe' \) -exec sh -c 'file=$(basename "{}");cp "{}" "temp-$file";' \;

for file in temp-*; do
    filename=$(basename -- "$file")
    mv "$file" "pslab-desktop-$TRAVIS_BRANCH-$TRAVIS_JOB_NAME.${filename##*.}"
done

git checkout --orphan temporary
git add --all .
git commit -am "[Auto] Update Install Packages ($(date +%Y-%m-%d.%H:%M:%S))"
git branch -D install
git branch -m install

git push origin install --force --quiet > /dev/null
