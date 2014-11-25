## Informations 

<img src="http://www.shinken-monitoring.org/fichiers/img/mascot.png" height="250px">
<img src="https://raw.githubusercontent.com/docker-library/docs/master/centos/logo.png" height="250px">
<img src="http://blog.docker.com/wp-content/uploads/2013/06/Docker-logo-011.png" height="250px">

This is a simple way to create a shinken docker image from shinken master branch. Usefull for testing but not for production use. This is just shinken without any additional module or configuration pack (except nagios-plugins-all)

- Source image : centos:centos6
- Additional repo : epel6
- Shinken : from master branch
- Additional packages : nagios-plugins-all and supervisord

## Create your own shinken-master docker image

### Usage

For the build we use a Makefile (so you will need to install make). Makefile allow to control the build process, run (aka first launch for container creation), start and stop container. Daemons are managed by supervisord (nice python tool), it provide a web interface to control the shinken daemons. Make file provide a way to access the webinterface (make supervisor). Take care to update the makefile so the BROWSER variable point to YOUR browser. 

- Build the image : make build
- Start the container for the first time : make run
- Stop the container : make stop
- Start again : make start
- Display container ip : make ip
- Enter container : make enter (caution this use sudo with nsenter so you will need to install nsenter and sudo before. See : https://github.com/jpetazzo/nsenter)

### First use example

```
# Clone repo
git pull https://github.com/david-guenault/docker-projects
cd docker-projects/shinken-2.2-master
# build the image
make build
# start the container for the first time
make run
# stop the container
make stop
# start again 
make start
# enter the container (yup no need to ssh ...)
make enter
# remove everything (image and container)
make stop && make clean
```

### Customization

You can customize some settings before building. Edit the Makefile and change the following values

- NAMESPACE = dguenault
- NAME = shinken
- VERSION = 2.2
- RELEASE = master
- BROWSER = /usr/bin/google-chrome

NAMESPACE NAME VERSION RELEASE are used to give a name to the image and the container :

- imagename = $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE)
- container name = $(NAME):$(VERSION)-$(RELEASE)

BROWSER is just the path to your webrowser. 

### Docker Image on docker hub registry

Automated build are available at https://registry.hub.docker.com/u/dguenault/shinken-master/
