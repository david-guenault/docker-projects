NAMESPACE=dguenault
NAME=shinken
RUNNAME=shinken:w!
TAG=master
BROWSER=/usr/bin/google-chrome

clean:
	- docker rm $(RUNNAME)
	- docker rmi $(NAMESPACE)/$(NAME):$(TAG)
	- docker rmi $$(docker images |grep "none" |awk '{print $3'})

build: 
	docker build --force-rm -t $(NAMESPACE)/$(NAME):$(TAG) .

run:
	JOB=$$(docker run -v /etc/localtime:/etc/localtime:ro --name $(RUNNAME) $(NAMESPACE)/$(NAME):$(TAG) > /dev/null 2>&1 &)

start:
	docker start $(NAME)

stop:
	docker stop $(NAME)

supervisor:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(NAME)):9001
	
enter:
	sudo ./go.sh $(NAME)

ip:
	docker inspect --format='{{.NetworkSettings.IPAddress}}' $(NAME)
