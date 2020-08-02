#custom provider vagrant check the installation steps in script
provider "vagrant" {}

variable sticky_session {}

resource "vagrant_vm" "my_vagrant_vms" {

  # Excuting steps present in the Vagrantfile present in the pwd
  vagrantfile_dir = "."

  # Excute the ansible playbook after running spinning up the vms
  provisioner "local-exec" {
    command = "ansible-playbook -i inventory/hosts ansible_web_deploy.yaml  --extra-vars 'sticky_session=${var.sticky_session}' "
  }
}
