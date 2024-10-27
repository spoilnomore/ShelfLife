.PHONY: run docker-build docker-run

UNAME_S := $(shell uname -s)

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
	-docker stop `docker ps -aqf "ancestor=shelflife"`
	-docker rm `docker ps -aqf "ancestor=shelflife"`

old-run:
	npm run serve

logs log:
	# we use ancestor and follow
	docker logs  --follow `docker ps -aqf "ancestor=shelflife"`

shell:
	docker exec -it `docker ps -aqf "ancestor=shelflife"` ash
