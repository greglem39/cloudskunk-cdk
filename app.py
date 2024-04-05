#!/usr/bin/env python3
# import os

import aws_cdk as cdk

# from rose_network.vpc import CourtOfRosesNetwork
from rose_pipeline.pipeline import RosePipeline


app = cdk.App()

env_primary = cdk.Environment(account="058264153331", region="us-east-1")

# CourtOfRosesNetwork(app, "CourtOfRosesNetwork", env=env_primary)
RosePipeline(app, "RosePipeline", env=env_primary)

app.synth()
