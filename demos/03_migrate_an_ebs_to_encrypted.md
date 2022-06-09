# Create encrypted EBS and migrate disks in Windows EC2 instance

## TL;DR

1. In KMS, [create encryption key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk). Make sure your IAM user can administer this key and delete it.
2. [Create a volume snapshot](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-creating-snapshot.html#ebs-create-snapshot) of your unencrypted EBS.
3. Create encrypted EBS from the EBS snapshot. Use the encrypted keys you’ve just created in KMS.
4. Attach and mount the encrypted volume to your instance. Make sure the data from the unencrypted volume has been migrated successfully to the encrypted volume.

#### Extension

5. In KMS page, disable your encryption key. What happened to the data in your instance?
6. Stop the machine and start it again, [what happened](https://docs.aws.amazon.com/kms/latest/developerguide/services-ebs.html#ebs-cmk) to the data in your instance?
