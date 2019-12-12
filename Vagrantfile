Vagrant.configure("2") do |config|
  config.vm.box = "centos/8"
  config.vm.box_version = "1905.1"

  config.vm.provider "virtualbox" do |specs|
    specs.cpus = 1
    specs.memory = 512
  end

  vms = {
    'vm1' => '172.16.2.11',
    'vm2' => '172.16.2.12',
  }

  vms.each_with_index do |(hostname, ip), idx|
    config.vm.define "vm#{idx}" do |machine|
      machine.vm.hostname = hostname
      machine.vm.network "private_network", ip: ip

      # Workaround for missing python on the image
      machine.vm.provision "shell", inline: "which python36 || sudo yum install -y python36"

      # Only execute once the Ansible provisioner,
      # when all the machines are up and ready.
      if idx == vms.size - 1
        machine.vm.provision :ansible do |ansible|
          ansible.become = true
          ansible.galaxy_role_file = "requirements.yml"
          ansible.limit = "all"
          ansible.playbook = "playbook.yml"
          ansible.version = "2.7.5"
        end
      end
    end
  end
end
