from fastapi import FastAPI
from pydantic import BaseModel
from pyctuator.pyctuator import Pyctuator
import boto3

class Inputs(BaseModel):
    nome: str
    cpf: str
    seguros: list
    cep: str

app = FastAPI()

# Configurações do LocalStack
aws_region = 'us-east-1'
sqs_url = 'http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/myqueue'
#sns_topic_arn = 'arn:aws:sns:us-east-1:000000000000:mytopic'

# Cliente SQS e SNS
sqs_client = boto3.client('sqs', region_name=aws_region, endpoint_url='http://localhost:4566')
#sns_client = boto3.client('sns', region_name=aws_region, endpoint_url='http://localhost:4566')

@app.post("/contratacao")
async def contratar_seguro(inputs: Inputs):
    # Enviar mensagem para a fila SQS
    sqs_message = f"Nome: {inputs.nome}, CPF: {inputs.cpf}, Seguros: {inputs.seguros}, CEP: {inputs.cep}"
    sqs_client.send_message(QueueUrl=sqs_url, MessageBody=sqs_message)

    # Publicar mensagem no tópico SNS
    #sns_message = f"Nome: {inputs.nome}, CPF: {inputs.cpf}, Seguros: {inputs.seguros}, CEP: {inputs.cep}"
    #sns_client.publish(TopicArn=sns_topic_arn, Message=sns_message)

    return {"message": "Contratação de seguro realizada com sucesso"}

Pyctuator(
    app,
    "FastAPI Pyctuator",
    app_url="http://host.docker.internal:8000",
    pyctuator_endpoint_url="http://host.docker.internal:8000/pyctuator",
    registration_url="http://localhost:8080/instances"
)