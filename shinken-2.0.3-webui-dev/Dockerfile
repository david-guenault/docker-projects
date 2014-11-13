# Shinken 2.0.3 All in one with webui devel
# 
# VERSION	2.0.3

FROM	 centos:centos6
MAINTAINER	David GUENAULT

# install repo
ADD     files/repo/10gen.repo /etc/yum.repos.d/
RUN     yum -y install http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-8.noarch.rpm

# prerequisites
RUN	yum clean all
RUN	yum -y update
RUN 	yum -y install yum-plugin-priorities
RUN 	yum clean all
RUN     yum -y install openssh-server python-pycurl python-pip python-setuptools git vim-enhanced python-paramiko nagios-plugins-all sysstat  python-importlib python-mock mongodb-org-server pymongo pymongo-gridfs mongodb-org-shell mongodb-org-tools

# install shinken
RUN	adduser shinken
RUN	cd /root && git clone https://github.com/naparuba/shinken.git
RUN	cd /root/shinken && git checkout tags/2.0.3
RUN     cd /root/shinken && python setup.py install

# create folders
RUN     mkdir -p /var/run/shinken /var/log/shinken
RUN     mkdir -p /data/db
RUN     chown shinken:shinken /var/run/shinken /var/log/shinken

# install supervisor and configuration 
RUN     pip install supervisor
RUN     mkdir -p /etc/supervisord.d
RUN     mkdir -p /var/log/supervisord
ADD     files/supervisor/supervisord.conf /etc/supervisord.conf
ADD     files/supervisor/mongodb.conf /etc/supervisord.d/01-mongodb.conf
ADD 	files/supervisor/sshd.conf /etc/supervisord.d/02-sshd.conf
ADD     files/supervisor/shinken-scheduler.conf /etc/supervisord.d/03-shinken-scheduler.conf
ADD     files/supervisor/shinken-receiver.conf /etc/supervisord.d/04-shinken-receiver.conf
ADD     files/supervisor/shinken-reactionner.conf /etc/supervisord.d/05-shinken-reactionner.conf
ADD     files/supervisor/shinken-poller.conf /etc/supervisord.d/06-shinken-poller.conf
ADD     files/supervisor/shinken-broker.conf /etc/supervisord.d/07-shinken-broker.conf
ADD     files/supervisor/shinken-arbiter.conf /etc/supervisord.d/08-shinken-arbiter.conf
ADD     files/supervisor/shinken-group.conf /etc/supervisord.d/09-shinken-group.conf

# for ssh
RUN	mkdir /root/.ssh
RUN	mkdir /var/run/sshd
RUN	ssh-keygen -b 1024 -t rsa -f /etc/ssh/ssh_host_key
RUN	ssh-keygen -b 1024 -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN	ssh-keygen -b 1024 -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN	su - shinken -c "ssh-keygen -q -t rsa -f ~/.ssh/id_rsa -N \"\""
RUN	su - shinken -c "cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys"
RUN	su - shinken -c "chown shinken:shinken /home/shinken/.ssh/authorized_keys"
RUN     su - shinken -c "chmod ug+rx /home/shinken/.ssh/"
RUN	su - shinken -c "chmod 400 /home/shinken/.ssh/authorized_keys"
RUN     cat /home/shinken/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
RUN     chmod 0600 /root/.ssh/authorized_keys

# install modules and packs
RUN	su - shinken -c "shinken --init"
RUN	su - shinken -c "shinken install linux-ssh"
RUN     su - shinken -c "shinken install webui"
RUN     su - shinken -c "shinken install mod-mongodb"
RUN	su - shinken -c "shinken install auth-cfg-password"
RUN     su - shinken -c "shinken install logstore-mongodb"
# RUN	su - shinken -c "shinken install livestatus"

# initialize mongodb database files
RUN /etc/init.d/mongod start && /etc/init.d/mongod stop

# use latest webui release
# RUN     mkdir -p /var/lib/shinken/modules/webui/
# RUN     git clone https://github.com/shinken-monitoring/mod-webui.git
# # RUN     cd mod-webui && git checkout develop
# RUN     cp mod-webui/etc/modules/webui.cfg /etc/shinken/modules/webui.cfg 
# RUN     cp -a mod-webui/module/* /var/lib/shinken/modules/webui/
# RUN     chown -R shinken:shinken /var/lib/shinken/modules/webui

use latest livestatus release
RUN     mkdir -p /var/lib/shinken/modules/livestatus/
RUN     git clone https://github.com/shinken-monitoring/mod-livestatus.git
RUN     cp mod-livestatus/etc/modules/livestatus.cfg /etc/shinken/modules/livestatus.cfg 
RUN     cp -a mod-livestatus/module/* /var/lib/shinken/modules/livestatus/
RUN     chown -R shinken:shinken /var/lib/shinken/modules/livestatus

# use latest mongodb release
# RUN     mkdir -p /var/lib/shinken/modules/mongodb/
# RUN     git clone https://github.com/shinken-monitoring/mod-mongodb.git
# RUN     cp mod-mongodb/etc/modules/mongodb.cfg /etc/shinken/modules/mongodb.cfg 
# RUN     cp -a mod-mongodb/module/* /var/lib/shinken/modules/mongodb/
# RUN     chown -R shinken:shinken /var/lib/shinken/modules/mongodb

# patch webui for module reloading
RUN     yum -y install patch
ADD     files/webui-module-reload.patch /var/lib/shinken/modules/webui/
RUN     cd /var/lib/shinken/modules/webui && patch module.py < webui-module-reload.patch

# fix some path and permisions
RUN	chown root:shinken /usr/lib64/nagios/plugins/check_icmp
RUN	chmod u+s /usr/lib64/nagios/plugins/check_icmp

# config 
RUN     sed -i "s/\(.*modules\).*/\1 livestatus, webui/g" /etc/shinken/brokers/broker-master.cfg
RUN     sed -i "s/\(.*modules\).*/\1 auth-cfg-password, mongodb/g" /etc/shinken/modules/webui.cfg
RUN     sed -i "s/\(.*uri\).*/\1 mongodb:\/\/127.0.0.1\/\?safe=false/g" /etc/shinken/modules/mongodb.cfg
RUN     sed -i "s/\(.*modules\).*/\1 logstore-mongodb/g" /etc/shinken/modules/livestatus.cfg
RUN	sed -i "s/\/usr\/lib\/nagios\/plugins/\/usr\/lib64\/nagios\/plugins/g" /etc/shinken/resource.d/paths.cfg
RUN     sed -i "s/\(generic\-host\)/\1, linux\-ssh/g" /etc/shinken/hosts/localhost.cfg

# Expose needed tcp ports
EXPOSE  7766
EXPOSE  7767
EXPOSE  7768
EXPOSE  7769
EXPOSE  7770
EXPOSE  7771
EXPOSE  7772
EXPOSE  22

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]