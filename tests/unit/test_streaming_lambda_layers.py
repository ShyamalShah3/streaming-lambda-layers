import aws_cdk as core
import aws_cdk.assertions as assertions

from infra.streaming_lambda_layers_stack import StreamingLambdaLayersStack

# example tests. To run these tests, uncomment this file along with the example
# resource in streaming_lambda_layers/streaming_lambda_layers_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StreamingLambdaLayersStack(app, "streaming-lambda-layers")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
