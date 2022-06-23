# Storage


2. In what ways does Amazon Simple Storage Service (Amazon S3) object storage differ from block
   and file storage? (Choose 2 answers)
   A. Amazon S3 stores data in fixed size blocks.
   B. Objects are identified by a numbered address.
   C. Objects can be any size.
   D. Objects contain both data and metadata.
   E. Objects are stored in buckets.


3. Which of the following are not appropriates use cases for Amazon Simple Storage Service (Amazon
   S3)? (Choose 2 answers)
   A. Storing web content
   B. Storing a file system mounted to an Amazon Elastic Compute Cloud (Amazon EC2) instance
   C. Storing backups for a relational database
   D. Primary storage for a database
   E. Storing logs for analytics


4. What are some of the key characteristics of Amazon Simple Storage Service (Amazon S3)? (Choose
   3 answers)
   A. All objects have a URL.
   B. Amazon S3 can store unlimited amounts of data.
   C. Objects are world-readable by default.
   D. Amazon S3 uses a REST (Representational State Transfer) Application Program Interface (API).
   E. You must pre-allocate the storage in a bucket.


5. Which features can be used to restrict access to Amazon Simple Storage Service (Amazon S3) data?
   (Choose 3 answers)
   A. Enable static website hosting on the bucket.
   B. Create a pre-signed URL for an object.
   C. Use an Amazon S3 Access Control List (ACL) on a bucket or object.
   D. Use a lifecycle policy.
   E. Use an Amazon S3 bucket policy.


6. Your application stores critical data in Amazon Simple Storage Service (Amazon S3), which must
   be protected against inadvertent or intentional deletion. How can this data be protected? (Choose 2
   answers)
   A. Use cross-region replication to copy data to another bucket automatically.
   B. Set a vault lock.
   C. Enable versioning on the bucket.
   D. Use a lifecycle policy to migrate data to Amazon Glacier.
   E. Enable MFA Delete on the bucket.


7. Your company stores documents in Amazon Simple Storage Service (Amazon S3), but it wants to
   minimize cost. Most documents are used actively for only about a month, then much less frequently.
   However, all data needs to be available within minutes when requested. How can you meet these
   requirements?
   A. Migrate the data to Amazon S3 Reduced Redundancy Storage (RRS) after 30 days.
   B. Migrate the data to Amazon Glacier after 30 days.
   C. Migrate the data to Amazon S3 Standard – Infrequent Access (IA) after 30 days.
   D. Turn on versioning, then migrate the older version to Amazon Glacier.


8. How is data stored in Amazon Simple Storage Service (Amazon S3) for high durability?
   A. Data is automatically replicated to other regions.
   B. Data is automatically replicated within a region.
   C. Data is replicated only if versioning is enabled on the bucket.
   D. Data is automatically backed up on tape and restored if needed.


9. Based on the following Amazon Simple Storage Service (Amazon S3) URL, which one of the
   following statements is correct? https://bucket1.abc.com.s3.amazonaws.com/folderx/myfile.doc
   A. The object “myfile.doc” is stored in the folder “folderx” in the bucket “bucket1.abc.com.”
   B. The object “myfile.doc” is stored in the bucket “bucket1.abc.com.”
   C. The object “folderx/myfile.doc” is stored in the bucket “bucket1.abc.com.”
   D. The object “myfile.doc” is stored in the bucket “bucket1.”


10. To have a record of who accessed your Amazon Simple Storage Service (Amazon S3) data and from
    where, you should do what?
    A. Enable versioning on the bucket.
    B. Enable website hosting on the bucket.
    C. Enable server access logs on the bucket.
    D. Create an AWS Identity and Access Management (IAM) bucket policy.
    E. Enable Amazon CloudWatch logs.


11. What are some reasons to enable cross-region replication on an Amazon Simple Storage Service
    (Amazon S3) bucket? (Choose 2 answers)
    A. You want a backup of your data in case of accidental deletion.
    B. You have a set of users or customers who can access the second bucket with lower latency.
    C. For compliance reasons, you need to store data in a location at least 300 miles away from the first region.
    D. Your data needs at least five nines of durability.


12. Your company requires that all data sent to external storage be encrypted before being sent. Which
    Amazon Simple Storage Service (Amazon S3) encryption solution will meet this requirement?
    A. Server-Side Encryption (SSE) with AWS-managed keys (SSE-S3)
    B. SSE with customer-provided keys (SSE-C)
    C. Client-side encryption with customer-managed keys
    D. Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)


14. What is needed before you can enable cross-region replication on an Amazon Simple Storage
    Service (Amazon S3) bucket? (Choose 2 answers)
    A. Enable versioning on the bucket.
    B. Enable a lifecycle rule to migrate data to the second region.
    C. Enable static website hosting.
    D. Create an AWS Identity and Access Management (IAM) policy to allow Amazon S3 to replicate objects on your behalf.


15. Your company has 100TB of financial records that need to be stored for seven years by law.
    Experience has shown that any record more than one-year old is unlikely to be accessed. Which of
    the following storage plans meets these needs in the most cost efficient manner?
    A. Store the data on Amazon Elastic Block Store (Amazon EBS) volumes attached to t2.micro instances.
    B. Store the data on Amazon Simple Storage Service (Amazon S3) with lifecycle policies that change the storage class to Amazon Glacier after one year and delete the object after seven years.
    C. Store the data in Amazon DynamoDB and run daily script to delete data older than seven years.
    D. Store the data in Amazon Elastic MapReduce (Amazon EMR).


16. Amazon Simple Storage Service (S3) bucket policies can restrict access to an Amazon S3 bucket
    and objects by which of the following? (Choose 3 answers)
    A. Company name
    B. IP address range
    C. AWS account
    D. Country of origin
    E. Objects with a specific prefix


18. What must be done to host a static website in an Amazon Simple Storage Service (Amazon S3)
    bucket? (Choose 3 answers)
    A. Configure the bucket for static hosting and specify an index and error document.
    B. Create a bucket with the same name as the website.
    C. Enable File Transfer Protocol (FTP) on the bucket.
    D. Make the objects in the bucket world-readable.
    E. Enable HTTP on the bucket.


19. You have valuable media files hosted on AWS and want them to be served only to authenticated
    users of your web application. You are concerned that your content could be stolen and distributed
    for free. How can you protect your content?
    A. Use static web hosting.
    B. Generate pre-signed URLs for content in the web application.
    C. Use AWS Identity and Access Management (IAM) policies to restrict access.
    D. Use logging to track your content.


20. Amazon Glacier is well-suited to data that is which of the following? (Choose 2 answers)
    A. Is infrequently or rarely accessed
    B. Must be immediately available when needed
    C. Is available after a three- to five-hour restore period
    D. Is frequently erased within 30 days


21. What is the best way to protect a file in Amazon S3 against accidental delete?
    A. Upload the files in multiple buckets so that you can restore from another when a file is deleted
    B. Back up the files regularly to a different bucket or in a different region
    C. Enable versioning on the S3 bucket
    D. Use MFA for deletion
    E. Use cross-region replication


3. Amazon S3 provides 99.999999999 percent durability. Which of the following
   are true statements? (Choose all that apply.)
   A. The data is mirrored across multiple AZs within a region.
   B. The data is mirrored across multiple regions to provide the durability SLA.
   C. The data in Amazon S3 Standard is designed to handle the concurrent loss of two facilities.
   D. The data is regularly backed up to AWS Snowball to provide the durability SLA.
   E. The data is automatically mirrored to Amazon Glacier to achieve high availability.


4. To set up a cross-region replication, what statements are true? (Choose all
   that apply.)
   A. The source and target bucket should be in a same region.
   B. The source and target bucket should be in different region.
   C. You must choose different storage classes across different regions.
   D. You need to enable versioning and must have an IAM policy in place to replicate.
   E. You must have at least ten files in a bucket.


5. You want to move all the files older than a month to S3 IA. What is the best way
   of doing this?
   A. Copy all the files using the S3 copy command
   B. Set up a lifecycle rule to move all the files to S3 IA after a month
   C. Download the files after a month and re-upload them to another S3 bucket with IA
   D. Copy all the files to Amazon Glacier and from Amazon Glacier copy them to S3 IA


6. What are the various way you can control access to the data stored in S3?
   (Choose all that apply.)
   A. By using IAM policy
   B. By creating ACLs
   C. By encrypting the files in a bucket
   D. By making all the files public
   E. By creating a separate folder for the secure files


7. How much data can you store on S3?
   A. 1 petabyte per account
   B. 1 exabyte per account
   C. 1 petabyte per region
   D. 1 exabyte per region
   E. Unlimited


9. What is the best way to delete multiple objects from S3?
   A. Delete the files manually using a console
   B. Use multi-object delete
   C. Create a policy to delete multiple files
   D. Delete all the S3 buckets to delete the files


12. I shut down my EC2 instance, and when I started it, I lost all my data. What
    could be the reason for this?
    A. The data was stored in the local instance store.
    B. The data was stored in EBS but was not backed up to S3.
    C. I used an HDD-backed EBS volume instead of an SSD-backed EBS volume.
    D. I forgot to take a snapshot of the instance store.


13. I am running an Oracle database that is very I/O intense. My database administrator
    needs a minimum of 3,600 IOPS. If my system is not able to meet that number, my
    application won’t perform optimally. How can I make sure my application always
    performs optimally?
    A. Use Elastic File System since it automatically handles the performance
    B. Use Provisioned IOPS SSD to meet the IOPS number
    C. Use your database files in an SSD-based EBS volume and your other files in an HDD-based EBS volume
    D. Use a general-purpose SSD under a terabyte that has a burst capability


14. Your application needs a shared file system that can be accessed from multiple
    EC2 instances across different AZs. How would you provision it?
    A. Mount the EBS volume across multiple EC2 instances
    B. Use an EFS instance and mount the EFS across multiple EC2 instances across
    multiple AZs
    C. Access S3 from multiple EC2 instances
    D. Use EBS with Provisioned IOPS


15. You want to run a mapreduce job (a part of the big data workload) for a noncritical
    task. Your main goal is to process it in the most cost-effective way. The task is
    throughput sensitive but not at all mission critical and can take a longer time.
    Which type of storage would you choose?
    A. Throughput Optimized HDD (st1)
    B. Cold HDD (sc1)
    C. General-Purpose SSD (gp2)
    D. Provisioned IOPS (io1)

