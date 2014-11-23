DOCKER = /usr/bin/docker
ELKIMG = dguenault/elk:latest
AMBASSADORIMG = svendowideit/ambassador
SHINKENIMG = dguenault/shinken:master-logstash
ELKNAME = elk
AMBASSADORNAME = elk_ambassador
SHINKENNAME = shinken
BROWSER = /usr/bin/google-chrome

pull:
	- $(DOCKER) pull $(SHINKENIMG) 
	- $(DOCKER) pull $(ELKIMG) 
	- $(DOCKER) pull $(AMBASSADOR)	

init:
	- $(DOCKER) run -d --name $(ELKNAME) $(ELKIMG) 
	- $(DOCKER) run -d --name $(AMBASSADORNAME) --link $(ELKNAME):$(ELKNAME) -p 6379:6379 $(AMBASSADORIMG)  
	- $(DOCKER) run -d --name $(SHINKENNAME) --link $(AMBASSADORNAME):$(ELKNAME) $(SHINKENIMG) 

start:
	- $(DOCKER) start $(ELKNAME) 
	- $(DOCKER) start $(AMBASSADORNAME) 
	- $(DOCKER) start $(SHIKENNAME) 

stop:
	- $(DOCKER) stop $(SHINKENNAME) 
	- $(DOCKER) stop $(AMBASSADORNAME) 
	- $(DOCKER) stop $(ELKNAME) 

clean: stop
	- $(DOCKER) rm $(SHINKENNAME) 
	- $(DOCKER) rm $(AMBASSADORNAME) 
	- $(DOCKER) rm $(ELKNAME) 
	- $(DOCKER) rmi $(ELKIMG) 
	- $(DOCKER) rmi $(SHINKENIMG)
	- $(DOCKER) rmi $(AMBASSADORIMG) 

kibana:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(ELKNAME))/kibana

elastichq:
	$(BROWSER) http://$$(docker inspect --format='{{.NetworkSettings.IPAddress}}' $(ELKNAME)):9200/_plugin/HQ

entershinken:
	sudo ./go.sh $(SHINKENNAME)

enterelk:
	sudo ./go.sh $(ELKNAME)
