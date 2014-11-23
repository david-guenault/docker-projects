DOCKER = /usr/bin/docker

pull:
	- $(DOCKER) pull dguenault/shinken:logstash
	- $(DOCKER) pull dguenault/elk:1.0-beta
	- $(DOCKER) pull svendowideit/ambassador	

init:
	- $(DOCKER) run -d --name elk dguenault/elk:1.0-beta 
	- $(DOCKER) run -d --name elk_ambassador --link elk:elk -p 6379:6379 svendowideit/ambassador  
	- $(DOCKER) run -d --name shinken --link elk_ambassador:elk dguenault/shinken:master-logstash 

start:
	- $(DOCKER) start elk
	- $(DOCKER) start elk_ambassador
	- $(DOCKER) start shinken

stop:
	- $(DOCKER) stop shinken
	- $(DOCKER) stop elk_ambassador
	- $(DOCKER) stop elk

clean: stop
	- $(DOCKER) rm shinken
	- $(DOCKER) rm elk_ambassador
	- $(DOCKER) rm shinken 
	- $(DOCKER) rmi dguenault/shinken:logstash
	- $(DOCKER) rmi dguenault/elk:1.0-beta
	- $(DOCKER) rmi svendowideit/ambassador	
