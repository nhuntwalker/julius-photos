# Photos by Julius

**Author**: Nicholas Hunt-Walker (nhuntwalker@gmail.com)

An application for the photo gallery site for Julius Doyle, anthropologist and photographer.

## Setup

Clone the repo and set up a new Python 3.6 virtual environment.
If you don't have Python 3.6, you can obtain it here: https://www.python.org/downloads/
You'll also need `pip` to install Python packages if you don't already have it.

```
$ git clone https://github.com/nhuntwalker/julius-photos.git
$ cd julius-photos
$ python3 -m venv ENV
$ source ENV/bin/activate
(ENV) $
```

`pip install` the `requirements.txt` file found at the project's root.

```
(ENV) $ pip install -r requirements.txt
```

Create a PostgreSQL database for this project and save the full database URL as an environment variable called `DATABASE_URL`.
You'll also want to save a `SECRET_KEY` your environment and a `DEBUG` variable whose value is `True`

```
(in ENV/bin/activate)
export DATABASE_URL=postgres://your.database.url:5432/yourdbname
export SECRET_KEY='some string it could be anything really'
export DEBUG=True
```

After setting your environment variables, restart your environment.