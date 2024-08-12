from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct


class CloudSkunkNetwork(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.rose_vpc = ec2.Vpc(
            self,
            "cloudskunk_network",
            vpc_name="cloudskunk_network",
            ip_addresses=ec2.IpAddresses.cidr("10.16.0.0/16"),
            default_instance_tenancy=ec2.DefaultInstanceTenancy.DEFAULT,
            max_azs=3,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="cloudskunk-pub1",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=20,
                ),
                ec2.SubnetConfiguration(
                    name="cloudskunk-pub2",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=20,
                ),
                ec2.SubnetConfiguration(
                    name="cloudskunk-privegress",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=20,
                ),
                ec2.SubnetConfiguration(
                    name="cloudskunk-priviso",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=20,
                ),
            ],
            nat_gateways=0,  # specify for the number of AZs for max  avail
        )
