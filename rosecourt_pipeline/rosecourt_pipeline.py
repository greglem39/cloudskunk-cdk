from aws_cdk import (
    # Duration,
    Stack,
    pipelines,
)
from constructs import Construct


class RosecourtPipeline(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # This is where we're going to define ourselves our CDK pipeline
        # Ideally, we're gonna use GitHub for this

        # define pipeline source
        source = pipelines.CodePipelineSource.git_hub("greglem39/rosecourt-cdk", "main")

        pipeline = pipelines.CodePipeline(
            scope,
            "RoseCourtPipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=source,
                commands=[
                    "npm install -g aws-cdk",
                    "pip install -r requirements.txt",
                    "cdk synth",
                ],
                env={"COMMIT_ID": source.source_attribute("CommitId")},
            ),
        )
