# Setup Instructions

I used [uv](https://docs.astral.sh/uv/) for python package management, which you'll need to install if you don't have it already. Official installation instructions can be found [here](https://docs.astral.sh/uv/getting-started/installation/#installation-methods). Once installed, restart your command prompt so the `uv` command is added to your `PATH`.

For the remainder, you'll need to have two command prompts open: one for the backend and one for the frontend.

## Setting up and running the backend

Make sure you `cd backend` before running any commands, else packages will be installed in the wrong place.

To start the backend, run:

`uv run uvicorn main:app --host 127.0.0.1 --port 8000`

This command should install an appropriate python version, if one isn't found, install all required packages, and run an HTTP server at `http://127.0.0.1:8000`. 

You shouldn't need to do this, but if for some reason you run into an error stating something along the lines of a missing python version, run:

`uv python install 3.12`

Then run the command to start the backend again. You can uninstall the python version again later by using:

`uv python uninstall 3.12`

I created a `seed_db.py` script just in case there were issues with the database. You can delete the db and run that script with `uv run seed_db.py` to recreate the data.

## Setting up and running the frontend

Make sure you `cd frontend` before running any commands.

To install required packages:

`npm install`

This gave me a few warnings about my node version (`v20.14.0`) being out of date, but it worked fine for me even before I upgraded. So if you don't want to upgrade node, give things a try anyway.

Then to run the tests:

`npm run test`

And to start the frontend:

`npm run dev`

Copy the URL from the command prompt and open it in your browser.

You should see the company's logo with a numeric field input and a `Load Policy` button. There are three policies in the database with ids of `1`, `2`, and `3`, respectively. If you load a policy with any of those ids, a `Policy Details` section should appear underneath. For any other id, including invalid ones, no policy details are shown. 

## Notes

I want to emphasise python is not my daily driver. uv, uvicorn, FastAPI, SQLModel and SQLAlchemy were all new to me. I put a lot of time into trying to make my solution reproducible on your machines, so I'd appreciate a little leeway in case something goes wrong.

Generally, there are many improvements that could be made:

1. The backend has no tests
1. The structure of the backend could be improved
1. no linter is configured for the backend
1. There are no end-to-end tests
1. We cannot search by the name of the policy holder or anything else
1. No message stating "Policy not found", is shown when the API returns a 404
1. No error message is shown if something goes wrong when loading a policy; it's just logged to the console
1. Styling. :-)

As I'm new to much of the backend, my focus was on delivering something that works rather than on architecture.

## References

- https://www.bitecode.dev/p/why-not-tell-people-to-simply-use
- https://www.bitecode.dev/p/installing-python-the-bare-minimum
- https://www.bitecode.dev/p/back-to-basics-with-pip-and-venv
- https://www.bitecode.dev/p/relieving-your-python-packaging-pain
- https://docs.astral.sh/uv/guides/install-python/
- https://docs.astral.sh/uv/concepts/projects/init/
- https://fastapi.tiangolo.com/advanced/dataclasses/
- https://fastapi.tiangolo.com/tutorial/handling-errors/#raise-an-httpexception-in-your-code
- https://docs.sqlalchemy.org/en/20/dialects/sqlite.html
- https://fastapi.tiangolo.com/tutorial/sql-databases/
- https://sqlmodel.tiangolo.com/#select-from-the-database
- https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/#why-arent-we-getting-more-data
- https://sqlmodel.tiangolo.com/tutorial/connect/read-connected-data/