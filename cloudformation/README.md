Security Knowledge Framework - AWS
=================================

This will allow you to run the OWASP Security Knowledge Framework in
AWS by using a [CloudFormation template](https://aws.amazon.com/cloudformation/) to
create all the required resources automatically.

The solution consists of a load balancer, which is the entry point for your requests, 
and one server that should always run in a private zone.

The solution might either be publicly accessible (i.e. from the internet) or just privately.
You have to select which one you prefer, and you should select the appropriate load balancer
subnets for that. So in case of a publicly accessible solution, select public subnets for
the load balancer.

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
able to use that, otherwise you'll need to do the following:

1. create/purchase an SSL certificate
2. use the AWS CLI tool to upload it to AWS

How you accomplish the first point will depend on you / your company's
preferences. To upload the certificate to your AWS account you can
[follow AWS' instructions for uploading a new certificate](http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ssl-server-cert.html#upload-cert).
The "Uploading the Server Certificate" section is the bit you're
after. The output of this command will give you the new certificate's
ARN (Amazon Resource Name). Make a note of it because you'll need it
in a moment.

The data for the SKF will be backed up periodically to an S3 bucket of 
your choice, and used when a new instance is launched.

### 2. CloudFormation

Log into the AWS console using your IAM username and password. Make
sure your user has full admin access because CloudFormation will
require lots of permissions.

Once you have logged in, go to the 'CloudFormation' section of the
console.

Make sure you are in the correct region, using the drop down in the
top right of the console.

> *Note* You will need a VPC to run the SKF. If your AWS account was
> created after December 2013 you will have a "default VPC"
> available. If not, or if you have deleted the default VPC make sure
> you first set up a VPC in the region you want to use the SKF.

Click the `Create Stack` button to create a new stack using
CloudFormation.

On the `Select Template` screen, choose the JSON file you created in
the previous step and click `Next`.

Next you'll see the `Specify Details` screen. This is where you
configure the Security Knowledge Framework for your needs.

#### Stack name

This is the name to give to this AWS stack. Something like
`security-knowledge-framework` is simple, but whatever makes sense to
you.

#### Parameters

The stack requires a number of the parameters, for each parameter a brief
explanation of what is necessary is provided.

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

### 4. DNS

The last step is to point the domain you'd like to use at the new
stack. You can do this by creating a CNAME record that points to the
`LoadBalancerUrl` we saw above. To look up the `LoadBalancerUrl` go to
the CloudFormation section of the AWS console, choose the stack you
created for the security knowledge framework and look at the
`Outputs` tab.
