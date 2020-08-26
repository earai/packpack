# Welcome to PackPack
Packpack is a Bayesian backpack packing inference engine. 
If you need to perform probabilistic calculations to determine what
you'll need in your pack, you've come to the right place. 

# Getting Started
## Docker
If you have Docker installed, you can build a ready-to-run image 
with `./bin/build_docker_image.sh`. Installing `docker-compose` is 
recommended, and `docker-compose.yml` defines services with the code 
bound into a volume for convenient development. You can also point 
PyCharm at the resulting image and use the interpreter to run scripts 
and tests from within the IDE. 

Once the image is built, you can run the tests for the project with:
```
docker-compose run --rm tests
```

>The Dockerfile uses `pipenv` to install packages into the container's 
>system packages from `Pipfile.lock`. To update dependencies, update 
>`Pipfile.lock` by using `pipenv install` into a virtualenv. 
 
## Pipenv
You can also use `pipenv` to easily create a local 
environment. Using the virtualenv as opposed to the Docker container will let you
show plots interactively with matplotlib. 

You'll need to satisfy some system requirements 
first: 
```
python 3.8 with development headers 
pip
pipenv
```

On Ubuntu 18.04, this is something like: 
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3-pip python3.8 python3.8-dev python3.8-tk
pip install --user pipenv
```

If you try to `pipenv` and the command cannot be found, you may need
to augment your `PATH` with e.g. `export PATH="/home/yourname/.local/bin:$PATH"`. 
If you want the virtualenv to end up in the project folder, be sure to set
`export PIPENV_VENV_IN_PROJECT=1` as well. 
 
With the system dependencies satisfied, you should be able to 
simply: 
```
pipenv install
```

And then `pipenv shell` to enter the virtualenv or `pipenv run` to run 
scripts directly. 

>It is easy to forget to install the Python headers. The 
>virtualenv will still be created, but if you try to `import pymc3`
>you may see `ImportError: Version check of the existing lazylinker compiled file. Looking for version 0.211, but found None`. 
>Make sure you have the python-dev package installed appropriate to the python version!

>The python3.8-tk package, which is necessary for matplotlib
>to be able to render using the `tkagg` backend, may fail to install
>if you already have e.g. python3-tk installed. 
