#!/usr/bin/env python3
# import os

import aws_cdk as cdk

from cloudskunk_pipeline.pipeline import SkunkPipeline


app = cdk.App()

env_primary = cdk.Environment(account="058264153331", region="us-east-1")

SkunkPipeline(app, "SkunkPipeline", env=env_primary)

app.synth()
