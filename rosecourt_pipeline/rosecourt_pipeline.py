from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct


class RosecourtPipeline(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # This is where we're going to define ourselves our CDK pipeline
        # Ideally, we're gonna use GitHub for this
