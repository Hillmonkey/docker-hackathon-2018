#!/bin/bash
# https://stackoverflow.com/questions/7172784/how-to-post-json-data-with-curl-from-terminal-commandline-to-test-spring-rest
# curl the docker container on port 80 from the local machine
curl -H "Content-Type: application/json" -X POST -d '{"msg":"passing me by"}' http://localhost/api/v1/larry
