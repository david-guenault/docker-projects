NAMESPACE=dguenault
NAME=skdata
RUNNAME=skdata
TAG=latest

clean: stop cleancontainer cleanimage

cleanimage:
	- docker rmi $(NAMESPACE)/$(NAME):$(TAG)
	- docker rmi $$(docker images |grep "none" |awk '{print $3'})

cleancontainer:
	- docker rm $(RUNNAME)

build:  
	docker build --no-cache --force-rm -t $(NAMESPACE)/$(NAME):$(TAG) .

run: stop cleancontainer
	JOB=$$(docker run -v /etc/localtime:/etc/localtime:ro --name $(RUNNAME) $(NAMESPACE)/$(NAME):$(TAG) > /dev/null 2>&1 &)

start:
	- docker start $(RUNNAME)

stop:
	- docker stop $(RUNNAME)

