# Shinken from master branch 
# VERSION	2.0.3

FROM     	centos:centos6
MAINTAINER	David GUENAULT

# install repo
RUN     yum -y install http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-8.noarch.rpm

# prerequisites
RUN     yum -y install openssh-server python-pycurl python-pip python-setuptools git vim-enhanced python-paramiko sysstat wget curl 

# sshd agent
RUN 	mkdir /var/run/sshd
RUN 	echo 'root:root' | chpasswd
RUN 	sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# install shinken
RUN	adduser shinken
RUN	cd /home/shinken && git clone https://github.com/naparuba/shinken.git
RUN	cd /home/shinken/shinken && git checkout tags/2.0.3
RUN     cd /home/shinken/shinken && python setup.py install

# create folders
RUN     mkdir -p /var/run/shinken /var/log/shinken
RUN     chown shinken:shinken /var/run/shinken /var/log/shinken /home/shinken/shinken

# install supervisor and configuration 
RUN     pip install supervisor
RUN     mkdir -p /etc/supervisord.d
RUN     mkdir -p /var/log/supervisord
ADD     files/supervisor/supervisord.conf /etc/supervisord.conf
ADD     files/supervisor/sshd.conf /etc/supervisord.d/

# install modules and packs from shinken.io
RUN	su - shinken -c "shinken --init && \
        shinken install linxu-ssh && \
        shinken install linux-snmp"

# config 
RUN	sed -i "s/\/usr\/lib\/nagios\/plugins/\/usr\/lib64\/nagios\/plugins/g" /etc/shinken/resource.d/paths.cfg

# Expose needed tcp ports
EXPOSE  7766
EXPOSE  7767
EXPOSE  7768
EXPOSE  7769
EXPOSE  7770
EXPOSE  7771
EXPOSE  7772

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
