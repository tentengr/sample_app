# sample_app
A sample API app utilising a broad stack.

## Control plane
Control plane is used to run any tools required for the support of the API development. This is neither a development environment, nor a staging one where the API can run.
### Build control plane
```
docker build . -t python_dev:0.0.1
```
### Run control plane
```
docker run -it --rm -v ${PWD}:/app python_dev:0.0.1
```

### Delete control plane
```
docker rmi python_dev:0.0.1; \
```