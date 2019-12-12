vms = {
  'vm0' => { "ip" => "172.16.2.10" },
  'vm1' => { "ip" => "172.16.2.11" },
  'vm2' => { "ip" => "172.16.2.12" },
}

ansible_groups = {
  "docker_swarm_manager" => ["vm0"],
  "docker_swarm_worker"  => ["vm1", "vm2"]
}

Vagrant.configure("2") do |config|
  config.vagrant.plugins = [ "vagrant-disksize" ]

  config.vm.box = "centos/7"
  config.vm.box_version = "1905.1"
  config.disksize.size = "50GB"

  config.vm.provider "virtualbox" do |specs|
    specs.cpus = 1
    specs.memory = 256
  end

  vms.each_with_index do |(hostname, opts), idx|
    config.vm.define "vm#{idx}" do |machine|
      machine.vm.hostname = hostname
      machine.vm.network "private_network", ip: opts["ip"]

      # Workaround for missing python on the image
      machine.vm.provision "shell", inline: "which python36 || sudo yum install -y python36"

      # Only execute once the Ansible provisioner,
      # when all the machines are up and ready.
      if idx == vms.size - 1
        machine.vm.provision :ansible do |ansible|
          ansible.become = true
          ansible.galaxy_role_file = "requirements.yml"
          ansible.groups = ansible_groups
          ansible.limit = "all"
          ansible.playbook = "playbooks/setup.yml"
          ansible.version = "2.7.5"
        end
      end
    end
  end
end
