NAMESPACE = dguenault
NAME = shinken-all
VERSION = 2.0.3
RELEASE = webui-devel
BROWSER = /usr/bin/google-chrome

clean:
	- docker rm $(NAME)-$(VERSION)-$(RELEASE)
	- docker rmi $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE)
	- docker rmi $$(docker images |grep "none" |awk '{print $3'})

build: 
	docker build --force-rm -t $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) .

run:
	docker run -v /etc/localtime:/etc/localtime:ro --rm -ti --name $(NAME)-$(VERSION)-$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) /bin/bash

start:
	docker run -v /etc/localtime:/etc/localtime:ro --rm --name $(NAME)-$(VERSION)-$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) 

detach:
	JOB=$$(docker run -v /etc/localtime:/etc/localtime:ro --rm --name $(NAME)-$(VERSION)-$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) > /dev/null 2>&1 &)

stop:
	docker stop $(NAME)-$(VERSION)-$(RELEASE)

webui:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(NAME)-$(VERSION)-$(RELEASE)):7767

supervisor:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(NAME)-$(VERSION)-$(RELEASE)):9001
	
enter:
	sudo ./go.sh $(NAME)-$(VERSION)-$(RELEASE)
