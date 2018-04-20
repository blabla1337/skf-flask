Security Knowledge Framework - AWS
=================================

This will allow you to run the OWASP Security Knowledge Framework in
AWS by using a
[CloudFormation template](https://aws.amazon.com/cloudformation/) to
create all the required resources automatically.

This guide assumes you have an AWS account and some experience using
AWS.

**Please be aware that following these steps will incur ongoing costs
in AWS**.

## Usage

If you're experienced with AWS then the steps are as follows:

1. create SSL cert and upload to your AWS account
2. create a new CloudFormation stack from the JSON file
3. CNAME your domain to the `LoadBalancerUrl` in the stack's `Outputs`

Further details on each step are below.

### 1. Create an SSL certificate for the Security Knowledge Framework

You will need an SSL certificate before you can set the SKF up in
AWS. If you already have an appropriate certificate in your account
(perhaps you've already set it up or you have a wildcard) you will be
able to use that.

If you do not already have a certificate the easiest way is to use
[AWS Certificate Manager](https://aws.amazon.com/certificate-manager/).

Once you've created the certificate make a note of its ARN.

### 2. CloudFormation

Log into the AWS console using your IAM username and password. Make
sure your user has full admin access because CloudFormation will
require lots of permissions.

Once you have logged in, go to the 'CloudFormation' section of the
console.

Make sure you are in the correct region using the drop down in the
top right of the console.

> *Note* You will need a VPC to run the SKF. If your AWS account was
> created after December 2013 you will have a "default VPC"
> available. If not, or if you have deleted the default VPC make sure
> you first set up a VPC in the region you want to use the SKF.

Click the `Create Stack` button to create a new stack using
CloudFormation.

On the `Select Template` screen, choose the
[owasp-security-knowledge-framework.template.yaml](owasp-security-knowledge-framework.template.yaml)
file from this repository and click `Next`.

Next you'll see the `Specify Details` screen. This is where you
configure the Security Knowledge Framework for your needs.

#### Stack name

This is the name to give to this AWS stack. Something like
`security-knowledge-framework` is simple, but whatever makes sense to
you.

#### Parameters

The following parameters are required for the CloudFormation.

##### AMI

The CloudFormation stack will spin up an EC2 instance that runs the
OWASP Security Knowledge Framework. This parameter selects the Amazon
Machine Image that should be used to start the image. This corresponds
to the choice of operating system and version. You should look up the
latest AMI for Ubuntu 14.04 LTS (Trusty Tahr) and use this.

This script will look up the most up-to-date version of Ubuntu 14.04
LTS that is currently available, suitable for use here.

```bash
aws --region REGION ec2 describe-images \
    --filters Name=root-device-type,Values=ebs Name=architecture,Values=x86_64 Name=virtualization-type,Values=hvm Name=name,Values=*ubuntu-trusty-14.04-amd64-server* \
    --query 'Images[*].[ImageId,CreationDate]' \
    --output text \
  | sort -k2,2 | tail -n1 | cut -f1
```

##### DataBucketName

This stack will create an S3 bucket to persist the Security Knowledge
Framework's database. This means that if the EC2 instance dies another
one will appear in its place a few moments later and no-one will even
notice that it died.

S3 bucket names must be globally unique so choose something that's
specific to you, for example
`company-name-security-knowledge-framework`

##### HttpsAccessCidr

This allows you to lock down access to the SKF. If you have an IP
range you can put that in here (e.g. for an office). If you'd like to
lock it down to a single IP address then you can do that by specifying
a single IP as the range e.g. `10.11.12.13/32`. If you want to allow
access from anywhere in the world you can allow any traffic using
`0.0.0.0/0`.

##### KeyName

The EC2 instance that runs the SKF will need an ssh key, specified by
name. The field will auto-complete with available key names.

This key can be used to ssh into the box if required. If you need
access choose (or create) a key that you have access to. If you don't
want to ssh into the box then just create an ssh key and discard the
private key.

##### SSHAccessCidr

This is the IP range that you would like to allow ssh connections
from. You can specify an IP range, a single IP (with `v.x.y.z/32`) or
leave it completely open (NOT RECOMMENDED) with `0.0.0.0/0`.

##### SSLCertificateArn

This is the ARN of the SSL certificate to use. If you set it up
earlier you'll have the ARN to hand, if not you can run the
`list-server-certificates` CLI command to see the available
certificates.

##### Subnets

Choose the subnet or subnets that the SKF should run in. This will
autocomplete from the available subnets.

##### VpcId

The VPC that the SKF should run in. Generally you'll only have one
available. If you have multiple VPCs make sure you choose the right
one and ensure it matches the choice of subnets.

#### Options

Here you may add tags to the stack and setup advanced options. Feel
free to ignore both and click `Next`.

#### Review

This last step is to confirm everything before the stack gets
created. If it all looks OK then select the confirmation checkbox and
click `Create`.

#### Creation

AWS will go ahead and create all the components necessary for running
the SKF. This includes Load Balancers, an AutoscalingGroup, all the
required AWS Permissions and Security Groups, the S3 bucket that will
persist the database and of course, the EC2 instance that will run the
SKF.

When it completes look at the `Outputs` tab of that stack and you will
see `LoadBalancerUrl`. Make a note of this for the next step.

### 3. DNS

The last step is to point the domain you'd like to use at the new
stack. You can do this by creating a CNAME record that points to the
`LoadBalancerUrl` we saw above. To look up the `LoadBalancerUrl` go to
the CloudFormation section of the AWS console, choose the stack you
created for the security knowledge framework and look at the
`Outputs` tab.

