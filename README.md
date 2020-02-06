# Vodafone API
A sample API app utilising a broad stack.

## Control Plane
Control Plane is used to run development tools without having to install a ton of helping libraried into the host OS. Tools are running within the control plane's cotainer, but output is shared with the host OS file system as well. This environemnt neither can be though as a development environment nor can be used to run the API.

### Build control plane
From with the control plane folder, run:
```
docker build . -t {tag_name}
```

### Run control plane
```
docker run -it --rm -v ${PWD}:/app {tag_name}
```

## Load balancer
This folder contains everything required to build an ningx docker image that can load balance request between all running instances of the Vodafone API. Unfortunately we do not have any means of service discovery for Vodafone API instances to register theirself, hence our load balancer is hardcoded to load balance among 2 Vodafone API instances.

In a more production ready environment, `Consul Template` can be used to retrieve all registered Vodafone API instances from a service discovery like Consule, regenerate nginx's config and trigger an conf reload.

### Building load balancer
Load balancer build will be triggered automatically by Vodafone API docker image build, however in case we want to build it on your owns, run from within the folder:
```
docker build . -t {tag_name}
``` 

## Vodafone API
The Vodafone API was written in Python using the Flash framework.
The are 3 resources served from the Vodafone API right now:
- datetime
- user
- auth

The Vodafone API can be built and run in 2 differnt modes.
That is either for development purposed or for production demonstrating purposes supporting load balancing as well.

### Running the API
Building the API for development is useful during development time.
For the majority of the task we will use targets from a Makefile, hence the `make` tool is a requiredment.


#### Build
##### Link docker-compose file
For development
```
ln -s docker-compose-development.yaml docker-compose.yml
```

For production
```
ln -s docker-compose-scaleout.yml docker-compose.yml
```

then run:
```
make build
```

#### Run
```
make run
```

#### Database migrations
```
make db-upgrade
```
Note: Before running db migrations, allow a few momment for the `make run` to bring the MySQL database up.

#### Visit swagger
Swagger and a Web based UI client that can be used to consume the API. Get swagger's ui by pointing your browser to:
[Swagger UI for development builds](http://0.0.0.0:5000/swagger-ui)
or
[Swagger UI for production builds](http://0.0.0.0:80/swagger-ui)

Note: Depending on how you run Vodafone API, one of the abose links will be functional each time.

### Testing the API
To unit test the API, run
```
make test
```

### Sample use case
#### Authenticate
In order to use any of the API calls, you first need to authenticate and retrive a session token.
Sample admin user:
```
username: admin
password: Ky7]gzc~Udh~]LcD4U
```

Then you need to pass the authentication token on each API request.