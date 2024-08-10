from constructs import Construct
from aws_cdk import Stage

from cloudskunk_network.vpc import CloudSkunkNetwork


class CloudSkunkNetworkStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        network = CloudSkunkNetwork(self, "CloudSkunkNetwork")
