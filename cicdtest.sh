#!/bin/bash
v1="https://github.com/patilajayv/CI-CD-Pipeline.git"
v2="/var/www/html"
fold="CICDpractise"
# if [ -d "$fold" -a ! -h "$fold" ]
# cd CICDpractise
folder_path="/home/ajay/CICDpractise"
if [ ! -d "$folder_path" ]; then
    echo "Folder does not exist. Creating..."
    git clone $v1
    cd $fold
    git checkout main
    git pull
    cp index.html $v2 
    echo "after 1st cp"
    service nginx restart 
else
    echo "Folder already exists."
    cd $fold
    # echo "cd 123"
    git checkout main
    git pull
    cp index.html $v2 
    echo "after 2nd cp"
    service nginx restart 
fi
# git checkout dev
# sudo cp index.html $v2
# sudo service nginx restart
