# Copyright (C) 2021 Alan Cruz
# Python-Prototypes

# git clone
```
git clone git@github.com:AlanACruz/Python-Prototypes.git ~/git/
```

# install docker
```
sudo apt update

sudo apt install -y \
   apt-transport-https \
   ca-certificates \
   curl \
   gnupg2 \
   software-properties-common

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
   
sudo apt update

sudo apt install -y \
   docker-ce \
   docker-ce-cli \
   containerd.io
```

# Enable non-root docker (Chromebook)
```
sudo usermod -aG docker $USER

sudo chmod 666 /var/run/docker.sock
```

# Pull Python image
```
docker pull python:latest
```

# Run Python build from container
```
docker build \
    -t python-prototypes \
    ~/git/Python-Prototypes

docker run \
    -i \
    -t \
    --rm \
    --name python-prototypes \
    python-prototypes
```

# Run Python tests locally
```
sudo apt install -y \
   python

~/git/Python-Prototypes/run-tests.sh
```
