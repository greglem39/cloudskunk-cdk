#!/usr/bin/env python3
# import os

import aws_cdk as cdk
from rosecourt_pipeline.rosecourt_pipeline import RosecourtPipeline


app = cdk.App()
RosecourtPipeline(
    app,
    "RosecourtPipelineStack",
    env=cdk.Environment(account="058264153331", region="us-east-1"),
)

app.synth()
