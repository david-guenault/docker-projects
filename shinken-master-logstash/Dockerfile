# Shinken from master branch 
# VERSION	2.2

FROM     dguenault/shinken:master
MAINTAINER	David GUENAULT

# install repo
RUN	rpm --import http://packages.elasticsearch.org/GPG-KEY-elasticsearch
ADD	files/repos/logstash.repo /etc/yum.repos.d/

# prerequisites
RUN     yum clean all && yum -y install logstash java-1.7.0-openjdk

# install supervisor configuration 
ADD     files/supervisor/logstash.conf /etc/supervisord.d/logstash.conf

# logstash
ADD	files/logstash/logstash.conf /etc/logstash/

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
