#!/bin/bash

source /Users/subha/Desktop/Programming/Python/python_rabbitmq_redshift_batch_processing_project/producer/venv/bin/activate

cd /Users/subha/Desktop/Programming/Python/python_rabbitmq_redshift_batch_processing_project/producer

python producer.py >> logs/etl.log 2>&1