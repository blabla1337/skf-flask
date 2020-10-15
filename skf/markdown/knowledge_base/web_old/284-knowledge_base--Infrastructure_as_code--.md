##Description:

Infrastructure as code (IaC) is the process of managing and provisioning 
applications and infrastrucutre through machine-readable definition files, 
rather than physical hardware configuration or interactive configuration tools

##Mitigation:

Verify that the application build and deployment processes are performed
in a secure and repeatable way, such as CI / CD automation, automated 
configuration management, and automated deployment scripts.

By doing so your infrastructure and application deployment also becomes immutable
and is easier to patch and maintain. Also, having your provisioning
of the application/infrastructure as code also means it has versioning
and other important benefits from having a versioning control system in place.

Other great benifits are,

- Speed and simplicity
  IaC allows you to spin up an entire infrastructure architecture by running a script.
- Configuration consistency
  Standard operating procedures can help maintain some consistency in 
  the infrastructure deployment process
- Quick rollback
  When a mistake or vulnerable peace of code has been pushed to a production environment
  with IaC it is easy to roll back to a stable/secure version.
