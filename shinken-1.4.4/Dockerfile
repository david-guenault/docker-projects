# Shinken from master branch 
# VERSION	2.2

FROM     centos:centos6
MAINTAINER	David GUENAULT

# install repo
RUN     yum -y install http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-8.noarch.rpm

# prerequisites
RUN     yum -y install openssh-server python-pycurl python-pip python-setuptools git vim-enhanced python-paramiko nagios-plugins-all sysstat wget curl python-pyro python-ldap python-pymongo python-sqlite2 mailx

# install shinken
RUN	adduser shinken
RUN	cd /home/shinken && git clone https://github.com/naparuba/shinken.git
RUN	cd /home/shinken/shinken && git checkout tags/1.4.4
RUN     cd /home/shinken/shinken && python setup.py install

# create folders
RUN     mkdir -p /var/run/shinken /var/log/shinken /usr/local/shinken/var/archives
RUN     chown -R shinken:shinken /etc/shinken /var/run/shinken /var/log/shinken /var/lib/shinken /home/shinken/shinken /usr/local/shinken

# fix some configurations issues
RUN	sed -i "s/\(\s\+modules\s\+\)\(Livestatus.*\)$/\1/g" /etc/shinken/shinken-specific.cfg
RUN	sed -i "s/^\(log_level=\)\(.*\)/\1DEBUG/g" /etc/shinken/*.ini
RUN	sed -i "s/^pack_distribution_file=.*$/pack_distribution_file=\/var\/run\/shinken\/pack_distribution.dat/g" /etc/shinken/nagios.cfg
RUN	ln -s /bin/mail /usr/bin/mail

# install supervisor and configuration 
RUN     pip install supervisor
RUN     mkdir -p /etc/supervisord.d
RUN     mkdir -p /var/log/supervisord
ADD     files/supervisor/supervisord.conf /etc/supervisord.conf
ADD     files/supervisor/scheduler.conf /etc/supervisord.d/scheduler.conf
ADD     files/supervisor/receiver.conf /etc/supervisord.d/receiver.conf
ADD     files/supervisor/reactionner.conf /etc/supervisord.d/reactionner.conf
ADD     files/supervisor/poller.conf /etc/supervisord.d/poller.conf
ADD     files/supervisor/broker.conf /etc/supervisord.d/broker.conf
ADD     files/supervisor/arbiter.conf /etc/supervisord.d/arbiter.conf
ADD     files/supervisor/shinken.conf /etc/supervisord.d/shinken.conf

# fix some path and permisions
RUN     chown root:shinken /usr/lib64/nagios/plugins/check_icmp
RUN     chmod u+s /usr/lib64/nagios/plugins/check_icmp

# config 
RUN	sed -i "s/\/usr\/lib\/nagios\/plugins/\/usr\/lib64\/nagios\/plugins/g" /etc/shinken/resource.cfg

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
EXPOSE  80

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
