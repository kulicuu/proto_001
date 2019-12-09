###  Python & Flask prototype API

_....not an idiomatically pure (e.g. 'RESTful') API, just a prototype_

To me an API is a parametrically polymorphic function, and to the extent those are ubiquitous ("evenything is an API"), they are pretty generically a way to expose a function or functions.

Here we use Python, Flask and Redis, providing some mock user data to test the system.

No fancy URL encodings, everything is a POST request.

## The API exposes a user-management function, with (sub)-functions:

### Batch Upload Members: by CSV file
Upload a CSV file keyed as `members_csv`


### Read members by Account Number:
Provide `account_id` in the JSON and you will be rewarded with all the members on that account.

### Create Member
Must provide JSON keyed with `id`, `first_name`, `last_name`, `phone_number`, `client_member_id`, and `account_id`.

### Read Member
Must pass JSON keyed with properties for `phone number`, `id`, and `member_client_id`, though any of those can have empty values.  System will return anything found by anything provided.


## Setup:

I'm using Python3 and the latest stable version of Redis.  In a real life development cycle, this would be containerized, but I guess that's overkill for a generic prototype.  You'll need NodeJS and Npm for the tests.  Do an `npm i` to install those dependencies.


Start your Redis server.  

Start the Python3 script `__init.py`.

Then start `bot_48.coffee` with either `coffee` or `nodemon`, both of which can be installed with `npm` globally.
