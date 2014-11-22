## Informations 

- Source image : centos:centos6
- Additional repo : epel6
- Shinken : from master branch
- Additional packages : see docker file

## Usage

- Build the image : make build
- Start the container for the first time : make run
- Stop the container : make stop
- Start again : make start
- Display container ip : make ip
- Enter container : make enter (caution this use sudo with nsenter so you will need to install nsenter and sudo before)

## Customization

You can customize some settings before building. Edit the Makefile and change the following values

- NAMESPACE = dguenault
- NAME = shinkenl
- VERSION = 2.2
- RELEASE = master
- BROWSER = /usr/bin/google-chrome

NAMESPACE NAME VERSION RELEASE are used to give a name to the image and the container :

- imagename = $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE)
- container name = $(NAME):$(VERSION)-$(RELEASE)

BROWSER is just the path to your webrowser. 
