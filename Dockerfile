FROM python:3.10.5
WORKDIR /usr/src/DedMorozBot
COPY . /usr/src/DedMorozBot
RUN pip install --user -r /usr/src/DedMorozBot/req.txt
CMD ["python", "main.py"]