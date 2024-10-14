run: stop
    -docker network create spoilnomore
    docker build -t shelfdb-image .
    docker run --name shelfdb -v shelfdb-data:/var/lib/postgresql/data \
    --network=spoilnomore \
    -p 5432:5432 -d shelfdb-image

stop down:
    -docker stop shelfdb
    -docker rm shelfdb

shell:
    docker exec -it shelfdb bash

logs:
    docker logs shelfdb