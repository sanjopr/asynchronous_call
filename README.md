# asynchronous_call
The project demonstrates the importance of using Asynchronous calls in Python 3.8

The project uses flask and aysncio.

For Testing the time difference between asynchronous and synchronous API calls, we use postal code information API from https://api.zippopotam.us.
As a sample input 270 postal codes from Ontario, Canada have been used. 

Asynchronous calls have been timed on average under 1 second
Synchronous calls have been timed on average around 75 seconds.

<code>python3 -m venv .env</code><br/>
<code>source .env/bin/activate</code><br/>
<code>pip install -r requirements.txt</code><br/>
<code>python app.py</code><br/>


Visit http://127.0.0.1:5000/
