# Ansible_Benchmarker

<pre>
|-----------|eth0      e1|----------|            |----------|
|  Ansible  |------------|  Switch  |            |  Switch  |
|-----------|            |----------|            |----------|
                               |e0                     |e0
                               |                       |
                               |                       |
                               |                       |
                               |G0/0               G0/0|
                         |-----------|       G0/1|-----------|
                         |  Router1  |-----------|  Router2  |
                         |-----------|G0/1       |-----------|
Ansible:
eth0 - 192.168.0.2

Router 1:
G0/0 - 192.168.0.1
G0/1 - 10.1.1.1

Router 2:
G0/0 - 192.168.1.1
G0/1 - 10.1.1.2


File Tree:
etc/ansible/
├── benchmarks/
├── filters/
│   ├── combine_routers.py
│   ├── filter_mtu.py
│   └── filter_ping.py
├── group_vars/
│   └── routers.yml
├── host_vars/
├── hosts
├── logs/
├── playbook/
│   └── show_MTU.yml
├── roles/
└── templates/
    └── results.j2

</pre>