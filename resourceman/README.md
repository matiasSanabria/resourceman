Command line instructions


Git global setup

git config --global user.name "Matt"
git config --global user.email "matt31sanabria@gmail.com"

Create a new repository

git clone git@gitlab.com:matiasSanabria/resourceman.git
cd resourceman
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Existing folder

cd existing_folder
git init
git remote add origin git@gitlab.com:matiasSanabria/resourceman.git
git add .
git commit -m "Initial commit"
git push -u origin master

Existing Git repository

cd existing_repo
git remote add origin git@gitlab.com:matiasSanabria/resourceman.git
git push -u origin --all
git push -u origin --tags