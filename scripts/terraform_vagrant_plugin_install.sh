#!/bin/bash

#download the terraform vagrant provider
curl -OL https://github.com/bmatcuk/terraform-provider-vagrant/releases/download/v2.0.0/terraform-provider-vagrant_v2.0.0_darwin_amd64.tar.gz
#extract the package
tar -xvf terraform-provider-vagrant_v2.0.0_darwin_amd64.tar.gz
#create a plugins directory in the installed terraform location (Skip the step if plugins dir already there)
mkdir ~/.terraform.d/plugins
#moving the terraform vagrant provider to the plugins directory
cp terraform-provider-vagrant_v2.0.0 ~/.terraform.d/plugins
