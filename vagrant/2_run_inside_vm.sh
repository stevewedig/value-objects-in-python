
# requirements: you are inside the fresh ubuntu virtual machine

# download provision script from GitHub
# - wget is built into the Ubuntu VM. Git is not.
wget --no-check-certificate https://raw.githubusercontent.com/stevewedig/value-objects-in-python/master/vagrant/3_provision.sh

# run provision script
chmod +x 3_provision.sh
./3_provision.sh

# checkout code
git clone https://github.com/stevewedig/value-objects-in-python.git
cd value-objects-in-python

# run tests via tox (tox apparently does something requiring sudo)
sudo tox

# next steps...
# - "exit" to exit ubuntu vm
# - "vagrant destroy" to halt and delete the vm

