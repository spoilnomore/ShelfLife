# Backend Makefile
APP_NAME = flaskserver
DOCKER_IMAGE = flaskserver-image
DOCKER_NETWORK = spoilnomore
PORT = 8081

.PHONY: build run stop logs shell


run: stop build
	-@docker network create $(DOCKER_NETWORK) > /dev/null 2>&1 || true
	docker run --name $(APP_NAME) -p $(PORT):8081 --network=$(DOCKER_NETWORK) -d $(DOCKER_IMAGE)

build:
	docker build -t $(DOCKER_IMAGE) .

stop down:
	-docker stop $(APP_NAME)
	-docker rm $(APP_NAME)

logs:
	docker logs -f $(APP_NAME)

shell:
	docker exec -it $(APP_NAME) bash
