FROM		centos:centos6	
MAINTAINER 	David GUENAULT <david.guenault@gmail.com>

RUN     yum -y install http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-8.noarch.rpm && \
	yum clean all && \
	yum -y install http://www.thruk.org/files/pkg/v1.84-6/rhel6/x86_64/thruk-1.84-6.rhel6.x86_64.rpm && \
	yum -y install httpd python-pip 

RUN	pip install supervisor && \
	mkdir -p /etc/supervisord.d && \
	mkdir -p /var/log/supervisord

ADD	files/supervisor/supervisord.conf /etc/
ADD	files/supervisor/httpd.conf /etc/supervisord.d/

EXPOSE	80

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
