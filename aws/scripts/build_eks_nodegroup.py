#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from os import path

config_dir = path.join(path.dirname(path.abspath(__file__)), '..', 'config')

asg_contents = []
with open(path.join(config_dir, 'autoscaling-group.yaml')) as asg_file:
    asg_template = asg_file.read()
with open(path.join(config_dir, 'env-list.txt')) as env_list_file:
    for env in env_list_file:
        env = env.strip()
        if not env or env.startswith('#'):
            continue
        asg_contents.append(asg_template.replace('{{Env}}', env).replace('{{env}}', env.lower()))

with open(path.join(config_dir, 'amazon-eks-nodegroup-base.yaml')) as base_file:
    content = base_file.read().replace('{{ASG}}', '\n'.join(asg_contents))

outfile_path = path.join(config_dir, 'amazon-eks-nodegroup.yaml')
with open(outfile_path, 'w') as outfile:
    outfile.write(content)

print('YAML file for worker nodes is created.\nThe file path: {}'.format(outfile_path))
