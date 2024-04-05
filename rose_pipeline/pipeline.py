from constructs import Construct

from aws_cdk import Stack, pipelines
from network_stage import RoseNetworkStage


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

        pipeline = pipelines.CodePipeline(self, "RosePipeline", synth=synth)

        deploy_network = RoseNetworkStage(self, "deploy_network")

        pipeline.add_stage(deploy_network)
