# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.network "forwarded_port", guest: 5432, host: 5432
  config.vm.define "dev", primary: true do |dev|
    dev.vm.box = "ubuntu/trusty64"

    dev.vm.provision :shell, path: "vagrant/provision.sh"
    dev.vm.hostname = "afg-dev"
    dev.vm.provider :virtualbox do |vb|
      vb.name = "afg-postgis"
      vb.memory = 1024
    end
  end
end
