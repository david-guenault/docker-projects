NAMESPACE=dguenault
NAME=centos6_supervisord
VERSION=6.6
RELEASE=1

clean:
	- docker rm $(NAME)-$(VERSION).$(RELEASE)
	- docker rmi $(NAMESPACE)/$(NAME):$(VERSION).$(RELEASE)
build:
	docker build --force-rm -t $(NAMESPACE)/$(NAME):$(VERSION).$(RELEASE) .

run:
	docker run -ti --rm --name $(NAME)-$(VERSION).$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION).$(RELEASE) /bin/bash