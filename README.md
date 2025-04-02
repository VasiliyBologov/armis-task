# armis-task
complex data pipeline for Silk recruiting

## Local start
* install dependencies
  
    ```pip install -r requirements.txt```

* Set ENV variables in `.env` file

```
CROWDSTRIKE=https://...
QUALIS=https://...
TOKEN=***
MONGO_URL=mongodb+srv://...
MONGO_DB=***
CROWDSTRIKE_COLLECTION=***
QUALIS_COLLECTION=***
```

* Run `main.py` with argument (qualys or crowdstrike)

    ```python main.py qualys```
    ```python main.py crowdstrike```

## Run in a Docker container

* Build the image

    ```sudo docker build -t armis . -f Dockerfile```

* Run the image

    ```sudo docker run -it --rm --name=armis -p 9300:9300 armis```

* when container is runned you can see the app in http://localhost:9300/
