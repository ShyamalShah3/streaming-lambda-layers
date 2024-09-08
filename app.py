#!/usr/bin/env python3.12
import os
import aws_cdk as cdk
from infra.streaming_lambda_layers_stack import StreamingLambdaLayersStack

app = cdk.App()
StreamingLambdaLayersStack(app, "StreamingLambdaLayersStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()