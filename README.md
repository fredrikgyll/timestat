TimeStat
=======

This is a simple REST API, implemented with Flask. Its purpose is to hold information about a timetable, specifically the popularity of the various time slots. This API will be consumed by a React frontend, which is the main focus of this project.

## Setup

#### clone the repo

```$ git clone git@github.com:fredrikgyll/timestat.git```

#### Install packages

Navigate to the project root and install the dependencies by running

```$ pip install -r development.txt```

#### Run the server

Hopefully everything went well and you can start the flask server by running

```$ flask run```

## Changing the models

If you make changes to the models you have to make a migration that specifies the changes. This is done with the following command

```$ flask db migrate```

When you are sure about the changes, you can apply then to the actual database by running

```$ flask db upgrade```

