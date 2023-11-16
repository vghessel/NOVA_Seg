aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name myqueue
aws --endpoint-url=http://localhost:4566 sns create-topic --name mytopic
aws --endpoint-url=http://sqs.us-east-1.localhost.localstack.cloud:4566 sqs list-queues
aws --endpoint-url=http://sqs.us-east-1.localhost.localstack.cloud:4566 sqs receive-message --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/myqueue
aws --endpoint-url=http://sqs.us-east-1.localhost.localstack.cloud:4566 sqs receive-message --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/myqueue --max-number-of-messages 10
