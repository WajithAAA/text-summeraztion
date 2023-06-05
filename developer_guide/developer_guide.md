
# End-to-end ml projects steps

- create local project directory
- open anaconda prompt and type `code .` to open the vscode project
- create new virtual env `conda create -p venv python==3.7 -y`
- activate virtual environment `conda activate venv/`

- create new git repository
- connect to new git repository with local project
    - `git init`
    - `git add README.md`
    - `git commit -m "first commit"`
    - `git status`
    - `git branch -M main`
    - `git remote -v`
    - `git push -u origin main`

- add change in git repository to local repository
    - `git pull`
- add changes in local repository to existing git repository
    - `git add .`
    - `git commit -m "second commit"`
    - `git push -u origin main`

- create git ignore file in `.gitignore` in git repository

- create setup.py file and requirements.txt 
    - install requirements.txt `pip install -r requirements.txt`

- create components and pipelines directory in src directory
- update logger and exception handler files




## Docker
- important image commands
  - `FROM python:3.8`
  - `COPY . /app`
  - `WORKDIR /app` 
  - `RUN pip install -r requirements.txt`
  - `CMD python app.py`
- build command for docker
  - `docker build -t (app_name) .`
- check docker image
  - `docker images`
- docker command for running
  - `docker run -p 5000:5000 (app_name)`
  - `docker ps`
  - `docker stop (app_name)`

## deployment in docker hub
- login to docker in terminal - `docker login`
- remove docker image `docker image rm -f (app_name)` if your app already exists remove and build again
- build `docker build -t (dockerhub acc_name\app_name) .`
- rename `docker tag oldname newname `
- push `docker push (dockerhub acc_name\app_name):latest`


## following steps for end to end project

 - create git repository and clone it to the local machine
 - open IDE `code` for vs code
 - create venv
 - create folder structure `template.py`
 - 