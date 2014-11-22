# Shinken from master branch 
# VERSION	2.2

FROM     centos:centos6
MAINTAINER	David GUENAULT

# install repo
RUN     yum -y install http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-8.noarch.rpm

# prerequisites
RUN     yum -y install openssh-server python-pycurl python-pip python-setuptools git vim-enhanced python-paramiko nagios-plugins-all sysstat wget curl

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
ADD     files/supervisor/shinken-scheduler.conf /etc/supervisord.d/shinken-scheduler.conf
ADD     files/supervisor/shinken-receiver.conf /etc/supervisord.d/shinken-receiver.conf
ADD     files/supervisor/shinken-reactionner.conf /etc/supervisord.d/shinken-reactionner.conf
ADD     files/supervisor/shinken-poller.conf /etc/supervisord.d/shinken-poller.conf
ADD     files/supervisor/shinken-broker.conf /etc/supervisord.d/shinken-broker.conf
ADD     files/supervisor/shinken-arbiter.conf /etc/supervisord.d/shinken-arbiter.conf
ADD     files/supervisor/shinken-group.conf /etc/supervisord.d/shinken-group.conf

# install modules and packs from shinken.io
RUN	su - shinken -c "shinken --init"

# fix some path and permisions
RUN     chown root:shinken /usr/lib64/nagios/plugins/check_icmp
RUN     chmod u+s /usr/lib64/nagios/plugins/check_icmp

# config 
RUN	sed -i "s/\/usr\/lib\/nagios\/plugins/\/usr\/lib64\/nagios\/plugins/g" /etc/shinken/resource.d/paths.cfg

# put broker in debug mode if you want
#RUN     sed -i "s/log_level=.*/log_level=DEBUG/g" /etc/shinken/daemons/brokerd.ini

# Expose needed tcp ports
EXPOSE  7766
EXPOSE  7767
EXPOSE  7768
EXPOSE  7769
EXPOSE  7770
EXPOSE  7771
EXPOSE  7772
EXPOSE  22
EXPOSE  80

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
