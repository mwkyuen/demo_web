FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# install app
RUN pip install -e . 

# initialize DB
RUN flask --app todo init-db

CMD ["flask", "--app", "todo", "run", "--host=0.0.0.0", "--port", "5555"]
