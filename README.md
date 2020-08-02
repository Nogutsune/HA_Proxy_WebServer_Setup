# HA_Proxy_WebServer_Setup
Sample project having one loadbalancer and two webserver setup using Vagrant, Terraform, Ansible, HA proxy and Testinfra

## Prerequisites

Following softwares/packages must be install in your system for running this project :-

- Virtualbox (https://www.virtualbox.org/)
- Vagrant (https://www.vagrantup.com/)
- Terraform (https://learn.hashicorp.com/terraform/getting-started/install.html)
- Ansible (https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- Testinfra (https://testinfra.readthedocs.io/en/latest/)

## Setup of project using terraform

- **Step 1**. I have used custom terrform vagrant provider. So first we need to install vagrant plugin for terraform, I have written the script *terraform_vagrant_plugin_install.sh* for that. We need to run it.

`sudo sh scripts/terraform_vagrant_plugin_install.sh`

Note: If any issues faced, try alternate setup without terraform. 

- **Step 2**. RUN `terraform init`

- **Step 3**. RUN `terraform apply -var sticky_session=false --auto-approve`. Variable sticky_session is for the deciding the HA proxy routing configuration

**sticky_session=false** means running with roundrobbin routing policy.

**sticky_session=true** means running with sticky session routing policy.

## Alternative way to setup project without terraform (vagrant and ansible)

- **Step 1**. RUN `vagrant up`

- **Step 2**. RUN `ansible-playbook -i inventory/hosts ansible_web_deploy.yaml  --extra-vars 'sticky_session=false'`. Variable sticky_session is for the deciding the HA proxy routing configuration

**sticky_session=false** means running with roundrobbin routing policy.

**sticky_session=true** means running with sticky session routing policy.

## Results

**Round Robbin Configuration**
Repeatedly RUN `curl 192.168.33.30` or RUN `192.168.33.30` in browser (192.168.33.30 is loadbalancer ip), we will get alternatively
![snapshot 1](https://github.com/Nogutsune/HA_Proxy_WebServer_Setup/blob/master/Screenshots/ScreenShot1.png)  
![snapshot 2](https://github.com/Nogutsune/HA_Proxy_WebServer_Setup/blob/master/Screenshots/ScreenShot2.png) 
