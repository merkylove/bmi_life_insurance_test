# bmi_life_insurance_test

## Install dependencies
$ make install-configure-poetry

## Run validations
$ make fmt && make lint && make test

## Run Web service to get a quote

$ docker build -t loc1 -f docker/Dockerfile . && docker container run -p 8080:8080 -t loc1 sh scripts/run_api.sh

## Web service request example

$ curl -X GET "0.0.0.0:8080/get_quote?weight=10&height=10&age=31&gender=MALE"