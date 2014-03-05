
# requirements: Vagrant and VirtualBox installed on dev machine

mkdir value-objects-vagrant
cd value-objects-vagrant

# create Vagrantfile
vagrant init precise32 http://files.vagrantup.com/precise32.box

# bring up virtual machine
vagrant up

# enter virtual machine
vagrant ssh

# next step: run the commands in run_inside_vagrant.sh

