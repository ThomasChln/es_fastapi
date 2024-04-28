FROM python:3.11

run pip install elasticsearch fastapi sentence_transformers uvicorn

add ./app/install.py /install.py
run python /install.py



# 


WORKDIR /code

# 


COPY ./requirements.txt /code/requirements.txt

# 


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 

COPY ./app /code/app

# 


#CMD python app/indexer.py && uvicorn app.main:app --host 0.0.0.0 --port 80

