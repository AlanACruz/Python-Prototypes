# Copyright (C) 2021 Alan Cruz
# Python-Prototypes

# Git Clone
```
git clone git@github.com:AlanACruz/Python-Prototypes.git ~/git/Python-Prototypes
```

# Install Docker on Chromebook
https://github.com/AlanACruz/DevSecOps/blob/master/docker/Install-Docker-On-Chromebook.md

# Build Container
```
docker build \
    --no-cache \
    -t python-prototypes \
    ~/git/Python-Prototypes
```

# Run Container
```
docker run \
    -i \
    -t \
    --rm \
    -v ~/git:/root/git/:Z \
    python-prototypes:latest \
    /bin/bash
```

# Run Jupyter Notebook from Container
```
docker run \
    -i \
    -t \
    --rm \
    -p 8888:8888 \
    -v ~/git:/root/git/:Z \
    python-prototypes \
    /bin/bash -c "jupyter notebook \
      --notebook-dir=~/git \
      --ip='*' \
      --port=8888 \
      --no-browser \
      --allow-root"
```

# Run Python Tests
```
~/git/Python-Prototypes/run-tests.sh
```
