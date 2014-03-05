
# before: install on Vagrant and VirtualBox on dev machine

mkdir my-vagrant-folder
cd my-vagrant-folder
vagrant init precise32 http://files.vagrantup.com/precise32.box
vagrant up
vagrant ssh

# next: run the commands in run_inside_vagrant.sh

