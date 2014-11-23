NAMESPACE = dguenault
NAME = elk
VERSION = 1.0
RELEASE = beta
BROWSER = /usr/bin/google-chrome

clean: containerclean imageclean

imageclean:
	- docker rmi $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE)
	- docker rmi $$(docker images |grep "none" |awk '{print $3'})

containerclean:
	- docker stop $(NAME)-$(VERSION)-$(RELEASE)
	- docker rm $(NAME)-$(VERSION)-$(RELEASE)

build: 
	docker build --force-rm -t $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) .

run:
	JOB=$$(docker run -v /etc/localtime:/etc/localtime:ro --name $(NAME)-$(VERSION)-$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) > /dev/null 2>&1 &)

interactive:
	docker run -ti --rm -v /etc/localtime:/etc/localtime:ro --name $(NAME)-$(VERSION)-$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) /bin/bash

start:
	docker start $(NAME)-$(VERSION)-$(RELEASE)

stop:
	docker stop $(NAME)-$(VERSION)-$(RELEASE)

supervisor:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(NAME)-$(VERSION)-$(RELEASE)):9001
	
enter:
	sudo ./go.sh $(NAME)-$(VERSION)-$(RELEASE)

ip:
	docker inspect --format='{{.NetworkSettings.IPAddress}}' $(NAME)-$(VERSION)-$(RELEASE)
