# demo_web
Demo web app using Flask

## Irregularities
Not sure why the text display in update.html (L10) has to be a `value` instead of the default value inside an html <input></input> tag

The `MANIFEST.in` and `setup.py` files are used to make the app installable. However, when using the dockerized app, there is no apparent need to install the app (using L16 in `Dockerfile`: `RUN pip install -e .`, instead it makes no difference since the `CMD` is used within the app directory. Included in this repo just cause.

## Hmmm
I wonder if the `requirements.txt` is really needed. I used it only in the `Dockerfile`. Could the `Dockerfile` use the `environment.yml` instead? I guess there is no need for a conda environment in a docker container, so the `requirements.txt` is more appropriate.

