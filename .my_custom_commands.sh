#!/bin/bash
function create() {
  cd YOURPROJECTFOLDER
  python PYTHONSCRIPTPATH $1 
  cd YOURPROJECTFOLDER/$1
  git init
  touch README.md
  git add README.md
  git commit -m "Initial commit"
  git remote add origin https://github.com/GITHUBUSERNAME/$1.git
  git push -u origin master
}