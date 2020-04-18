# Ansible_Benchmarker
\
|-----------|\
|  Ansible  |eth0      e1|----------|            |----------|&nbsp;
|           |------------|  Switch  |            |  Switch  |&nbsp;
|192.168.0.2|            |----------|            |----------|&nbsp;
|-----------|                  |e0                     |e0&nbsp;
                               |                       |&nbsp;
                               |                       |&nbsp;
                               |                       |&nbsp;
                               |G0/0               G0/0|&nbsp;
                         |-----------|       G0/1|-----------|&nbsp;
                         |  Router1  |-----------|  Router2  |&nbsp;
                         |-----------|G0/1       |-----------|&nbsp;
Ansible:&nbsp;
eth0 - 192.168.0.2&nbsp;
&nbsp;
Router 1:&nbsp;
G0/0 - 192.168.0.1&nbsp;
G0/1 - 10.1.1.1&nbsp;
&nbsp;
Router 2:&nbsp;
G0/0 - 192.168.1.1&nbsp;
G0/1 - 10.1.1.2&nbsp;
