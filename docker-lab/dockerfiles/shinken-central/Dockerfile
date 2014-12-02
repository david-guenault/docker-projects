# Shinken with all daemons from shinken 2.0.3 base image
# modules
#	livestatus
#	logstore sqlite
#	logstore mongodb
#	
# VERSION	2.0.3

FROM     	dguenault/shinken:2.0.3	
MAINTAINER	David GUENAULT

# install repo

# prerequisites
RUN     yum -y install nagios-plugins-all python-pymongo python-sqlite2 

# install supervisor configuration 
ADD     files/supervisor/shinken-arbiter.conf /etc/supervisord.d/
ADD     files/supervisor/shinken-poller.conf /etc/supervisord.d/
ADD     files/supervisor/shinken-reactionner.conf /etc/supervisord.d/
ADD     files/supervisor/shinken-receiver.conf /etc/supervisord.d/
ADD     files/supervisor/shinken-broker.conf /etc/supervisord.d/
ADD     files/supervisor/shinken-scheduler.conf /etc/supervisord.d/

# fix some path and permisions
RUN     chown root:shinken /usr/lib64/nagios/plugins/check_icmp
RUN     chmod u+s /usr/lib64/nagios/plugins/check_icmp

# install shinken modules
RUN	su - shinken -c "shinken --init && \
	shinken install livestatus && \
	shinken install logstore-mongodb && \
	shinken install logstore-sqlite"

# config 
RUN	sed -i "s/^\(\s\+modules\).*$/\1 livestatus/g" /etc/shinken/brokers/broker-master.cfg
RUN	sed -i "s/\/usr\/lib\/nagios\/plugins/\/usr\/lib64\/nagios\/plugins/g" /etc/shinken/resource.d/paths.cfg

# put broker in debug mode if you want
#RUN     sed -i "s/log_level=.*/log_level=DEBUG/g" /etc/shinken/daemons/brokerd.ini
