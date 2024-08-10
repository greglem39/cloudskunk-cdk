from constructs import Construct

from aws_cdk import Stack, pipelines
from cloudskunk_pipeline.network_stage import CloudSkunkNetworkStage


class SkunkPipeline(Stack):  # triggering self mutation ...
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repo = pipelines.CodePipelineSource.git_hub("greglem39/cloudskunk-cdk", "main")

        synth = pipelines.ShellStep(
            "Synth",
            input=repo,
            commands=[
                "npm install -g aws-cdk",
                "pip install -r requirements.txt",
                "cdk synth",
            ],
        )

        pipeline = pipelines.CodePipeline(self, "CloudSkunkPipeline", synth=synth)

        deploy_network = CloudSkunkNetworkStage(self, "deploy-network")

        pipeline.add_stage(deploy_network)
