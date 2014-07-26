
# requirements: you are inside the fresh ubuntu virtual machine

# download provision script from GitHub
# - wget is built into the Ubuntu VM. Git is not.
wget --no-check-certificate https://raw.github.com/stevewedig/value-objects-in-python/master/vagrant/3_provision_and_test.sh

# run provision script
chmod +x 3_provision_and_test.sh
./3_provision_and_test.sh

# next steps...
# - "exit" to exit ubuntu vm
# - "vagrant destroy" to halt and delete the vm

