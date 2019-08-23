import pulumi
from putils import opts
from staticsite import StaticSite
from pulumi_aws import route53

config = pulumi.Config('castle')

zone = route53.get_zone(name='dingbots.dev')

# Create an AWS resource (S3 Bucket)
site = StaticSite(
    'MainSite',
    domain=config.require('domain'),
    zone=zone,
    content_dir='www',
    **opts(),
)
pulumi.export('website',  site.url)
