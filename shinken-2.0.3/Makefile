NAMESPACE = dguenault
NAME = shinken
VERSION = 2.0.3
RELEASE = 1 
BROWSER = /usr/bin/google-chrome

clean:
	- docker rm $(NAME)-$(VERSION)-$(RELEASE)
	- docker rmi $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE)
	- docker rmi $$(docker images |grep "none" |awk '{print $3'})

build: 
	docker build --force-rm -t $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) .

run:
	JOB=$$(docker run -v /etc/localtime:/etc/localtime:ro --name $(NAME)-$(VERSION)-$(RELEASE) $(NAMESPACE)/$(NAME):$(VERSION)-$(RELEASE) > /dev/null 2>&1 &)

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
