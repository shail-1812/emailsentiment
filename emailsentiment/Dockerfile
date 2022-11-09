FROM public.ecr.aws/lambda/python:3.9

COPY app.py . ${LAMBDA_TASK_ROOT}
COPY requirements.txt .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
RUN pip install spacy-download
RUN python -m spacy download en

COPY tokenizer.pickle .
COPY finalized_model.sav .
CMD ["app.handler"]


