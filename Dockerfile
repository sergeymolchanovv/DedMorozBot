FROM python:3.10.5
WORKDIR /usr/src/dedmorozbot
COPY . /usr/src/dedmorozbot
RUN pip install --user -r /usr/src/dedmorozbot/req.txt
CMD ["python", "main.py"]