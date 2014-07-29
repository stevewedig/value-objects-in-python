
# update package list
# - http://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do
sudo apt-get update

# install the add-apt-repository command
sudo apt-get -y install software-properties-common
sudo apt-get -y install python-software-properties
which add-apt-repository # verify

# optionally install a text editor
# sudo apt-get -y install emacs vim

# git
# - use ppa to get a recent version
# - http://askubuntu.com/questions/279172/upgrade-git-on-ubuntu-10-04-lucid-lynx
sudo add-apt-repository -y ppa:git-core/ppa
sudo apt-get update
sudo apt-get -y install git
git --version # verify

# python versions
sudo apt-add-repository -y ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get -y install python2.6
sudo apt-get -y install python2.7
sudo apt-get -y install python3.2
sudo apt-get -y install python3.3
sudo apt-get -y install python3.4

# pip
sudo apt-get -y install python-pip
	
# tox
sudo pip install tox

# checkout code and run tests via tox
# - tox apparently does something requiring sudo
git clone https://github.com/stevewedig/value-objects-in-python.git
cd value-objects-in-python
sudo tox

