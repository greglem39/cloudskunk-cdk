from constructs import Construct
from aws_cdk import Stage

from rose_network.vpc import CourtOfRosesNetwork


class RoseNetworkStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        network = CourtOfRosesNetwork(self, "CourtOfRosesNetwork")
