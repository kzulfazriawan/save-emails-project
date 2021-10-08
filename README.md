# installation

1. Install requirements ``pip install -r requirements.txt``
2. Copy the .env.example to .env ``cp .env.example .env``
3. Setup the .env
4. Go to migrations directory and setup alembic.ini 
6. Migrate using alembic ``alembic upgrade head`` or ``python -m alembic upgrade head``
7. Start the application ``python main.py``

# Endpoint available
- To create an email /email **POST & GET**
- To create an event /event **POST & GET**
- To save_email /save_emails **POST & GET**

# Public/Frontend

1. Go to public directory
2. run the ``npm install --save``
3. run the ``npm run dev`` to rebuild webpack
4. run the webserver for **index.html** ( you can use http-server from npm or ``python3 -m http.server``)
