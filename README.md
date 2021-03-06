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

**Stick Session Configuration**

Repeatedly RUN `curl 192.168.33.30` or RUN `192.168.33.30` in browser (192.168.33.30 is loadbalancer ip), we will get only either one the webpages (based on bind cookie).

![snapshot 1](https://github.com/Nogutsune/HA_Proxy_WebServer_Setup/blob/master/Screenshots/ScreenShot1.png)
If one of the node (webserver) is down the loadbalancer automatically serves traffic from healhy node.

## Executing Automated Infrastructure tests

I have used testinfra as a automated testing tool for testing the Infrastructure. More Details (https://testinfra.readthedocs.io/en/latest/).

**For testing Webservers** 

I have written 4 testcases for testing webservers

- TestCase for having root prevelleges
- TestCase for validating apache is installed on the webservers
- TestCase for validating the apache service is running on the webservers
- TestCase for checking curl is working for webservers

RUN `python -m pytest -v  --ansible-inventory=inventory/hosts --connection=ansible tests/webservers_test.py  --force-ansible`

Result

![snapshot 3](https://github.com/Nogutsune/HA_Proxy_WebServer_Setup/blob/master/Screenshots/ScreenShot3.png)

**For testing Loadbalancer**
 
 I have written 5 testcases for testing loadbalancer
 
- TestCase for having root prevelleges
- TestCase for validating haproxy is installed on the loadbalancer
- TestCase for validating the haproxy service is running on the loadbalancer
- Testcase for validating loadbalancer is working fine even one node is down
- TestCase for checking curl is working for loadbalancer

RUN `python -m pytest -v  --ansible-inventory=inventory/hosts --connection=ansible tests/loadbalancer_test.py  --force-ansible`

Result

![snapshot 4](https://github.com/Nogutsune/HA_Proxy_WebServer_Setup/blob/master/Screenshots/ScreenShot4.png)

## Bonus Tasks

- Brief summary of what you liked about your solution

This solution demonstrate knowlegde on lot of DevOps tools like Vagrant, Terraform, Ansible, HAproxy and Testinfra(python).

- Brief summary of what you disliked about your solution

Instead of assigning fixed ips to the VMs, I could have used dynamic ips. But I haven't hardcoded ips anywhere. Ansible playbook read ips from inventory file only. 

- Configurable Round Robin / Sticky Load Balancer

Yes, I have added both the configurations for loadbalancer. Based on the value of sticky_session passed by the user, playbook will set haproxy.cnf file in loadbalance vm. Basically I have two jinja2 templates `templates/haproxy.cfg.j2` for roundrobbin and `templates/haproxy_sticky_session.cfg.j2` for stickysession.

- Return instance identifier of your webserver in addition to “Hello World”

Yes, I have included webserver identifier and webserver ip along with Hello World. My webpages will return

`Hello World from <webserver1/webserver2>, ip: <webserver ip>`
