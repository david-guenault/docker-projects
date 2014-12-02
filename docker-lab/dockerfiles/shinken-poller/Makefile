REPO = dguenault
NAME = shinken-poller
RUNNAME = shinken-poller
TAG = 2.0.3
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

start:
	docker start $(RUNNAME) 

stop:
	docker stop $(RUNNAME) 

supervisor:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(RUNNAME)):9001
	
enter:
	sudo ./go.sh $(RUNNAME)

ip:
	docker inspect --format='{{.NetworkSettings.IPAddress}}' $(RUNNAME)
