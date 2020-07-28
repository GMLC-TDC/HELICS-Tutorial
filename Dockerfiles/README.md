# Dockerfiles

A Dockerfile exists for each component (ie. federate) needed for the
tutorials. The Docker Compose files for each tutorials will reference
the relevant Dockerfiles as the `build` argument for each container.
Alternatively, each image can be built by running `make build` in the
relevant directory, or all the images can be built by running `make
build` in this directory.
