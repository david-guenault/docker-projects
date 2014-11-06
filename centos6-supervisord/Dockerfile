FROM                centos:centos6
MAINTAINER      David GUENAULT

# clean all
RUN     yum clean all

# prerequisites
RUN     yum install -y wget supervisor yum install yum-plugin-priorities

RUN     yum -y install http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
RUN     yum -y install http://mirror-fr1.bbln.org/epel/6/i386/epel-release-6-8.noarch.rpm
RUN     yum clean all

# supervisor
ADD     files/skel.conf /etc/supervisord.d/skel.conf
RUN     echo "[include]" >> /etc/supervisord.conf
RUN     echo "files = /etc/supervisord.d/*.conf" >> /etc/supervisord.conf
