# Canopsis - Open source hypervisor from sources on centos:centos6

FROM 		centos:centos6

MAINTAINER 	David GUENAULT 

RUN     	yum -y install http://mirrors.ircam.fr/pub/fedora/epel/6/i386/epel-release-6-8.noarch.rpm && \
		yum clean all

RUN 		yum -y install wget make redhat-lsb gcc gcc-c++ zlib-devel ncurses-devel git libcurl-devel && \
		yum -y install xorg-x11-server-Xvfb libevent-devel libevent libevent-headers && \
		yum -y install openldap openldap-devel openssl openssl-devel python-pip

#RUN		git clone https://github.com/capensis/canopsis.git && \
#		cd canopsis && \
#		git submodule init && \
#		git submodule update 
#
#RUN		cd canopsis/sources/externals/python-libs && \
#		wget https://pypi.python.org/packages/source/i/isit/isit-0.3.2.tar.gz && \
#		rm -f isit.tar.gz && \
#		ln -s isit-0.3.2.tar.gz isit.tar.gz && \
#		cd .. && \
#		tar zxvf Ubik.tgz && \
#		cd Ubik && \
#		sed -i "s/isit==0.2.6/isit==0.3.2/g" setup.py && \
#		cd .. && \
#		tar czvf Ubik.tgz Ubik && \
#		cd .. 
#		./build-install.sh 
		
	
#RUN		pip install --upgrade git+https://github.com/socketubs/ubik.git@0.1

RUN 		useradd -m -d /opt/canopsis -s /bin/bash canopsis   

#RUN	su - canopsis -c "mkdir tmp && \
#			cd tmp && \
#			wget http://repo.canopsis.org/stable/canopsis_installer.tgz && \
#			tar xfz canopsis_installer.tgz && \
#			cd canopsis_installer && \
#			./install.sh"

# Launch wsshd when launching the container
#ENTRYPOINT ["sudo su - canopsis -c \"hypcontrol start\""]

