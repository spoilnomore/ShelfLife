.PHONY: run docker-build docker-run

UNAME_S := $(shell uname -s)

alltogether: stop
	@if [ ! -f .env ]; then \
		echo ".env file does not exist. Please create it before running make and review the readme on how to set up the .env"; \
		exit 1; \
	fi
	docker-compose up --build -d

ifeq ($(UNAME_S),Linux)
run: stop build
	-@docker network create spoilnomore > /dev/null 2>&1 || true
	docker run \
		-p 80:8081 \
		-p 3000:3000 \
		-v ${CURDIR}/src:/app/src \
		-v ${CURDIR}/uploads:/app/uploads \
		-v ${CURDIR}/.env:/app/.env \
		-e CHOKIDAR_USEPOLLING=true \
		--network=spoilnomore \
	-d shelflife
	make logs
else
run: stop build
	-@docker network create spoilnomore > /dev/null 2>&1 || true
	docker run \
		-p 8080:8080 \
		-p 3000:3000 \
		-v ${CURDIR}/src:/app/src \
		-v ${CURDIR}/uploads:/app/uploads \
		-v ${CURDIR}/.env:/app/.env \
		-e CHOKIDAR_USEPOLLING=true \
		-e HOST=0.0.0.0 \
	-d shelflife
	make logs
endif


build:
	docker build -t shelflife .

stop down:
	docker-compose down
	-docker stop shelfdb
	-docker rm shelfdb
	-docker stop flaskserver
	-docker rm flaskserver

olddown:
	-docker stop `docker ps -aqf "ancestor=shelflife"`
	-docker rm `docker ps -aqf "ancestor=shelflife"`

old-run:
	npm run serve

logs log:
	# we use ancestor and follow
	docker logs  --follow `docker ps -aqf "ancestor=shelflife"`

shell:
	docker exec -it `docker ps -aqf "ancestor=shelflife"` ash
