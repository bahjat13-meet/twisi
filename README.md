# Twisi
## How to Set-Up in 5 Minutes:
```bash
git clone https://github.com/bahjat13-meet/twisi.git
cd twisi
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Setup additional packages
```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y git ruby python-pip python-virtualenv libpq-dev python-dev
sudo apt-get install -y postgresql postgresql-contrib
sudo apt-get install -y libncurses-dev
wget -O- https://toolbelt.heroku.com/install.sh | sh
```
## For OSX
```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install postgresql
```
