
# findCP RESTful API

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![CI-CD](https://github.com/findCP/findCP-webservice/actions/workflows/main.yml/badge.svg)](https://github.com/findCP/findCP-webservice/actions/workflows/main.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=findCP_findCP-webservice&metric=alert_status)](https://sonarcloud.io/dashboard?id=findCP_findCP-webservice) [![codecov](https://codecov.io/gh/findCP/findCP-webservice/branch/main/graph/badge.svg?token=89X5LKO912)](https://codecov.io/gh/findCP/findCP-webservice)

## Table of Contents
- [License](#license)
- [Requirements](#requirements)
- [Install dependencies](#install-dependencies)
- [Run](#run)
- [Test](#test)
- [Deployment](#deployment)
- [Maintainers](#maintainers)


## License

findCPcli is released under [GPLv3 license](LICENSE).

## Requirements
- Python>=3.7
- [Redis](https://redis.io/)
- MySQL
- [GLPK](https://www.gnu.org/software/glpk/) (recommended)

## Install dependencies
```
pip install -r requirements.txt
```
or
```
python3 -m pip install -r requirements.txt
```
## Run
1. Change Redis and MySQL params on ```.env```.
2. Run celery worker
    ```
    celery -A src.restapi.celery_app.celery_app worker --loglevel=debug
    ```
3. Run flower
   ```
   celery flower -A src.restapi.celery_app.celery_app -port=5555
   ```
4. Run Flask application
   ```
   python -m src.restapi.app
   ```

See:
- http://127.0.0.1:5000/apidocs
- http://localhost:5555

## Test

```
pytest -v
```

## Deployment

### Requirements

- Python>=3.7
- [Redis](https://redis.io/)
- MySQL
- [GLPK](https://www.gnu.org/software/glpk/) (recommended)
- [Gunicorn](https://docs.gunicorn.org/en/latest/index.html) (recommended). 
  - See [Deploying Flask applications](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html)
- [Nginx](https://nginx.org/en/) (recommended). 
  - See [Nginx gunicorn config](https://docs.gunicorn.org/en/latest/deploy.html) 

### Run
1. Change Redis and MySQL params on ```.env```.
2. Run celery worker
    ```
    celery -A src.restapi.celery_app.celery_app worker --loglevel=info --concurrency=1 &> logs/celery.out
    ```
3. Run flower
   ```
   celery flower -A src.restapi.celery_app.celery_app -port=5555
   ```
4. Run Gunicorn app with unix socket bind and eventlet workers (See [Flask-socketIO Deploy](https://flask-socketio.readthedocs.io/en/latest/deployment.html#gunicorn-web-server))
   ```
   gunicorn --worker-class eventlet -w 1 --bind unix:/tmp/gunicorn.sock src.restapi.wsgi:app
   ```
5. Setup and run Nginx according to:
   1. [Gunicorn Nginx deployment](https://docs.gunicorn.org/en/latest/deploy.html)
   2. [Flask-SocketIO deployment](https://flask-socketio.readthedocs.io/en/latest/deployment.html#using-nginx-as-a-websocket-reverse-proxy)
   
## Maintainers
[@alexOarga](https://github.com/alexOarga)

