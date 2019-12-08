###  API proto 000

#### Basically:
A two hour project hard timebox.

#### Doing:
A simple Python API to some notional functions, implemented in Flask, with a network test in Coffeescript.

### Notes:
I haven't used Python for something like this (API server) in awhile, so I spent some time actually setting up my environment and doing some cursory research.  Actually am working with a new (one month) computer and new OS (Windows from Ubuntu and Mac before) environment, so I reinstalled Python, and messed around with Cygwin and stuff like this for about the first 30 minutes.


There is a simple e2e test in the Coffeescript 'bot' file.  CS is very fast for prototyping stuff, so infrastructure/tooling gets done that way sometimes.  I could switch to Python for this.  I call it 'bot', because in my paradigm of back-end development, following the TDD idea, but starting from the top full integration test level rather than at the bottom --unit test-- level, we should have a failing comprehensive test of our application before its implementation.  For a very simple application such as this one, that test can be trivially implemented, but for something more complex, this would require a bot-net, with orchestration, event-logging, compute-node analysis, etc.


The assignment called for treating this as production ready, and I considered this as a target, but optimization is a follow-on process by nature, and I'm just getting back into this Python context  -- I was last using it in numerical context with Numpy/Scipy/Keras/Pandas/Tensorflow stuff.
