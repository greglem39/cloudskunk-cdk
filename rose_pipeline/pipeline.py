from constructs import Construct

from aws_cdk import Stack, pipelines


class RosePipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo = pipelines.CodePipelineSource.git_hub("greglem39/rosecourt-cdk", "main")

        synth = pipelines.ShellStep(
            "Synth",
            input=repo,
            commands=[
                "npm install -g aws-cdk",
                "pip install -r requirements.txt",
                "cdk synth",
            ],
        )

        pipelines.CodePipeline(self, "RosePipeline", synth=synth)
