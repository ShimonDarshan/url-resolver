FROM python:3.13-slim

LABEL org.opencontainers.image.source https://github.com/ShimonDarshan/url-resolver


WORKDIR /api

COPY **.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "bash", "-c" ]

#! For some reason is not working and to run the app need to run the following command \
    #! while creating the container:
        #! fastapi run /api/main.py --host 0.0.0.0 --port 8000 \
        #! so if you are using docker run you need to add this command at the end of the docker run command \
        #! e.g. docker run <image_id> "fastapi run /api/main.py --host 0.0.0 --port 8000"
CMD ["fastapi", "run", "/api/main.py", "--host", "0.0.0.0", "--port", "8000"]
