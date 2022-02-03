# shaxbozaka/task

# system requirements
### python, flask


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt, before we have to create environment let's do it.

```
python3 -m venv .env
```

And exactly we will activate it.
### linux
```
source .env/bin/activate
```
### windows
```
.\env\Scripts\activate
```

So, we can install requirements
``` bash
pip install -r requirements.txt
```

## RUN
```
flask run

```
## All done server listen on ```localhost:5000```

## URLS

```html

POST /file/create 

--header X-api-key
body [title, content]

```

# Techlogies
### flask, celery, JSON

# DOCKERIZE

```
sudo docker-compose up
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
