REPO = dguenault
NAME = canopsis
RUNNAME = canopsis
TAG = ficus
BROWSER = /usr/bin/google-chrome
IMAGE=$(REPO)/$(NAME):$(TAG)

clean:
	- docker rm $(RUNNAME)
	- docker rmi $(IMAGE) 
	- docker rmi $$(docker images |grep "none" |awk '{print $3'})

build: 
	docker build --force-rm -t $(IMAGE) .

run:
	JOB=$$(docker run -v /etc/localtime:/etc/localtime:ro --name $(RUNNAME) $(IMAGE) > /dev/null 2>&1 &)

interactive:
	docker run -ti --rm -v /etc/localtime:/etc/localtime:ro --name $(RUNNAME) $(IMAGE) /bin/bash 

start:
	docker start $(RUNNAME) 

stop:
	docker stop $(RUNNAME) 

supervisor:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(RUNNAME)):9001

canopsis:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(RUNNAME)):8082
	
enter:
	sudo ./go.sh $(RUNNAME)

ip:
	docker inspect --format='{{.NetworkSettings.IPAddress}}' $(RUNNAME)
