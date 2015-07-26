# Python-Lightning
A Python 3 implementation of the Lightning Network.

### Development

This project includes a Dockerfile for development. The standard procedure would be:

```
git clone git@github.com:scmorse/Python-Lightning.git && cd Python-Lightning
cp docker/Dockerfile-dev Dockerfile
docker build -t pln .
docker run -it -p 8090:8090 -v `pwd`:/opt/code/pln pln /bin/bash

# From within the docker container:
./init.sh
```

### Updating libraries

Note that `ignore = dirty` has been added to each submodule descriptor within `.gitmodules` due to build files being placed in the directory and the project not properly git ignoring them. This means that to update the commit that a submodule references, you must:

 - Remove each instance of `ignore = dirty` from `.gitmodules`
 - Update and commit the new reference hash for the submodule
 - Put `ignore = dirty` back into each entry of `.gitmodules`
