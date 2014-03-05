

# 

# http://www.vagrantup.com/
# after brining up Ubuntu using Vagrant + VirtualBox, you can provision the machine with this script
# so that Python 2.6, 2.7, 3.1, 3.2, and 3.3 can be tested via Tox

# update package list
# - http://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do
sudo apt-get update

# install the add-apt-repository command
# - http://stackoverflow.com/questions/13018626/add-apt-repository-not-found
sudo apt-get -y install python-software-properties
sudo apt-get -y install software-properties-common
which add-apt-repository # verify

# git
# - use ppa to get a recent version, older versions may not work with Jenkins
# - http://askubuntu.com/questions/279172/upgrade-git-on-ubuntu-10-04-lucid-lynx
sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get -y install git
git --version # verify

# pip
sudo apt-get -y install python-pip
	
# tox
sudo pip install tox

# python versions
sudo apt-add-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get -y install python2.6
sudo apt-get -y install python2.7
sudo apt-get -y install python3.2
sudo apt-get -y install python3.3

# checkout code and run tests via Tox
git clone https://github.com/stevewedig/value-objects-in-python.git
cd value-objects-in-python
sudo tox

