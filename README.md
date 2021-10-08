# installation

1. Install requirements ``pip install -r requirements.txt``
2. Copy the .env.example to .env ``cp .env.example .env``
3. Setup the .env
4. Go to migrations directory and setup alembic.ini 
6. Migrate using alembic ``alembic upgrade head`` or ``python -m alembic upgrade head``
7. Start the application ``python main.py``