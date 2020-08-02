Vagrant.configure("2") do |config|
	#spinning webserver1 vm and assigning ip
	config.vm.define "webserver1" do |webserver1|
		webserver1.vm.box = "hashicorp/bionic64"
    webserver1.vm.network "private_network", ip: "192.168.33.10"
	end
  #spinning webserver2 vm and assigning ip
	config.vm.define "webserver2" do |webserver2|
		webserver2.vm.box = "hashicorp/bionic64"
    webserver2.vm.network "private_network", ip: "192.168.33.20"
	end
  #spinning loadbalancer vm and assigning ip
  config.vm.define "loadbalancer" do |loadbalancer|
		loadbalancer.vm.box = "hashicorp/bionic64"
    loadbalancer.vm.network "private_network", ip: "192.168.33.30"
	end

end
