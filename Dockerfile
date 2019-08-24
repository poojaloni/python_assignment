FROM python:3
ADD pythonAssignment_quiz.py /
RUN pip install
CMD [ "python", "./pythonAssignment_quiz.py" ]
