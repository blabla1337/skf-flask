### Distributing, Fielding/Deploying, Operations, and Disposal

No course can teach everything. This course focuses on *developing* secure software, including its distribution. We have intentionally not focused on processes after development, including distributing, fielding (deploying), operations, and disposal of software. One reason is that there are already many documents and guidelines that try to help people do this securely, but these efforts are hampered because they are trying to twiddle configuration knobs to turn insecure software into secure software. It is generally far more effective, if you want a secure system, to start with secure software.

Of course, distributing, deployment, operations, and disposal all matter. Many projects apply a DevOps or DevSecOps approach, which intentionally blend these processes together with development. Even if development is done by a different group, having secure distribution, fielding, operations, and disposal is critical for software to be secure in the real world. So while this course does not focus on these processes, here are a few tips on these processes that may help you.

When distributing:

* Use HTTPS (TLS), so that people can verify that it is the intended domain and the information cannot be manipulated between the server and recipient.

* Where practical, sign the distributed information using a private key *not* available to the server. That enables external verification (using the corresponding public key) even if the server is compromised. Unfortunately, this requires ensuring that public keys are securely distributed to the receivers. In some cases, ensuring that the receivers have the correct public keys can be a challenging problem, while in other cases this is easy. A common solution for software updates is to accept an update if it is signed by the same key that signed the currently-installed version of the software.

Note that our earlier discussion about software acquisition discussed distribution problems from the opposite side. That is, when acquiring software you want to ensure that you receive what you were supposed to receive, and when distributing software you want to make it easy for recipients to verify this.

When fielding/deploying:

* Configure your production environment to be secure, including all components you depend on, and keep it updated. Security misconfiguration is such a common mistake in web applications that it is 2017 OWASP Top 10 #6. For example:

    * Your environment should be configured to provide least privilege and use maximum security settings your system allows.

    * Beware of *“insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages containing sensitive information”* (as OWASP notes).

    * Harden your environment by maximally enabling security countermeasures and eliminating unused components (so their vulnerabilities cannot be exploited). These components include your operating systems, database systems, virtual machine monitor, virtual machines, container runtime infrastructure, containers, and anything else you use or depend on. There are many documents that discuss how to harden various components; use them!

    * Where it is reasonable, enable automatic updates.

* Avoid giving direct access to your database unless it is necessary *and* you have verified it is secure.

* Ensure that all data sets have *limited* privilege. In particular, if you use AWS S3 buckets for non-public data, ensure that they have very limited access (many S3 buckets with non-public data have been made publicly readable).

* Where it makes sense, enable full disk encryption and/or database encryption.

* Enable monitoring systems that will warn you, or automatically update, when a component in use has a known vulnerability.

* Turn on logging and redirect it to a central protected location for monitoring. Enable automated systems to detect and warn about likely security problems.

When operating:

* Update components in a timely way (this is sometimes called *patch and vulnerability management*). Using components with known vulnerabilities is such a common web application vulnerability that it is 2017 OWASP Top 10 #9. In some organizations this job is split between developers who update components within an application and operators who update external components depended on by the application. No matter how you do it, components need to be updated in a timely way or an attacker will be able to exploit them.

* Examine warnings and/or logs routinely. Determine which ones are indicators of an incident. Insufficient logging and monitoring is such a common web application vulnerability that it is 2017 OWASP Top 10 #10.

* Respond in a timely way to incidents.

* Once a vulnerability or incident is resolved, use root cause analysis to figure out *why it happened* so changes can be made to prevent a similar recurrence.

* Create backups, and store them securely (attackers love to get copies of backups). Test to ensure you can recover from them. Make sure you have offline (“cold”) backups to counter ransomware (which breaks in, encrypts your data, and holds it for ransom).

* When you receive a vulnerability report, process and fix it in a timely manner. Then give the reporter public credit unless the reporter requests otherwise.

When disposing, make sure you fully destroy any data you are supposed to destroy. Just removing a file does not actually remove its contents from most storage devices.