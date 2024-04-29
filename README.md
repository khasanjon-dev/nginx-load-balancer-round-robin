### Env variables
```bash
# WEB
# DEBUG must be empty in production
DEBUG=
SECRET_KEY=django-insecure-hk8!j)66r7*oup29x9)n-8n+5l_ccuqcx7ondc(2v8o&r@zd
DJANGO_SETTINGS_MODULE=root.settings
# DATABASE
DB_HOST=db
DB_NAME=news
DB_USERNAME=postgres
DB_PASSWORD=helloworld
DB_PORT=5432
# POSTGRES
POSTGRES_USER=postgres
POSTGRES_PASSWORD=helloworld
POSTGRES_DB=news
```

# Run the project

> step 1:
- **clone the project**
```shell
git clone https://github.com/khasanjon-dev/nginx-load-balancer-round-robin.git
```
> step 2
- **cd project file**
```shell
cd nginx-load-balancer-round-robin
```
> step 3
```shell
docker compose up --build
```

> step 4 
- **open the new terminal and run this command for testing**
```shell
python test.py
```

# Technologies used

<p>
  <a>
    <img src="https://skillicons.dev/icons?i=python,django,docker,postgres,nginx" />
  </a>
</p>

* ```Python```
* ```Django```
* ```DjangoRestFramework```
* ```Docker```
* ```docker compose```
* ```PostgreSQL```
* ```Nginx```
