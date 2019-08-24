FROM python:3
ADD pythonAssignment_quiz.py /
ADD quiz.json /
RUN pip install
CMD [ "python", "./pythonAssignment_quiz.py" ]
