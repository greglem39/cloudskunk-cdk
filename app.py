#!/usr/bin/env python3
# import os

import aws_cdk as cdk

from cloudskunk_pipeline.pipeline import SkunkPipeline
from cloudskunk_network.vpc import CloudSkunkNetwork


app = cdk.App()

env_primary = cdk.Environment(account="339712902882", region="us-east-1")

# SkunkPipeline(app, "SkunkPipeline", env=env_primary)

CloudSkunkNetwork(app, "CloudSkunkNetwork", env=env_primary)


app.synth()
