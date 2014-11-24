# Shinken from master branch 
# VERSION	2.2

FROM     dguenault/shinken:master-logstash
MAINTAINER	David GUENAULT

WORKDIR	/etc/supervisord.d
RUN	rm -f shinken-arbiter
RUN	rm -f shinken-broker
RUN	rm -f shinken-reactionner
RUN	rm -f shinken-receiver
RUN	rm -f shinken-scheduller

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
