Vagrant.configure("2") do |config|
  config.vm.box = "centos/8"
  config.vm.box_version = "1905.1"

  config.vm.provider "virtualbox" do |specs|
    specs.cpus = 1
    specs.memory = 512
  end

  config.vm.define "vm1" do |machine|
    machine.vm.network "private_network", ip: "172.16.0.11"
  end

  config.vm.define "vm2" do |machine|
    machine.vm.network "private_network", ip: "172.16.0.12"
  end

  # Parallel Provisioning
  config.vm.define 'controller' do |machine|
    machine.vm.network "private_network", ip: "172.16.0.10"

    config.vm.provision "ansible_local" do |ansible|
      ansible.become = true
      ansible.inventory_path = "inventory"
      ansible.limit = "all"
      ansible.playbook = "playbook.yml"
      ansible.version = "2.8.5"
    end
  end
end
