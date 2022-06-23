# Enable bucket point-in-time backup-restore ability

## TL;DR

1. Enable versioning on your bucket bucket.
2. Create lifecycle rule to manage non-current versions of your objects:
   1. Move noncurrent versions of objects to Standard-IA storage class
   2. Permanently delete noncurrent versions of objects after 90 days

--- 

## Enable versioning on your bucket bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

2. In the **Buckets** list, choose the name of the bucket that you want to enable versioning for\.

3. Choose **Properties**\.

4. Under **Bucket Versioning**, choose **Edit**\.

5. Choose **Enable**, and then choose **Save changes**\.

6. Upload multiple object with the same key, make sure versioning is working.

## Create lifecycle rule to manage non-current versions

1. Choose the **Management** tab, and choose **Create lifecycle rule**\.

1. In **Lifecycle rule name**, enter a name for your rule\.

1. Choose the scope of the lifecycle rule (in this demo we will apply this lifecycle rule to all objects in the bucket).

1. Under **Lifecycle rule actions**, choose the actions that you want your lifecycle rule to perform:
   + Transition *noncurrent* versions of objects between storage classes
   + Permanently delete *noncurrent* versions of objects

1. Under **Transition non\-current versions of objects between storage classes**:

   1. In **Storage class transitions**, choose **Standard\-IA**.

   1. In **Days after object becomes non\-current**, enter 30.

1. Under **Permanently delete previous versions of objects**, in **Number of days after objects become previous versions**, enter 90 days.

1. Choose **Create rule**\.

   If the rule does not contain any errors, Amazon S3 enables it, and you can see it on the **Management** tab under **Lifecycle rules**\.


## Objects deletion in bucket versioning enabled

1. In the **Buckets** list, choose a versioning enabled bucket\.
2. Choose **Upload** and upload an object multiple times under the same key, such that it has non-current versions. 
3. In the bucket console, choose the **Objects** tab, and delete the object you have just uploaded.
4. After the deletion action, can you see the object in the bucket's objects list?

We will examine through AWS CLI what happened. 

1. First we need to allow programmatic access from your local machine. Go to the [IAM console](https://console.aws.amazon.com/iam)\.

2. Under **Users**, in the navigation bar on the upper right, choose your user name, and then choose **My Security Credentials**\.   

3. Expand the **Access keys \(access key ID and secret access key\)** section\.

4. Choose **Create New Access Key**\. To copy the key to paste it somewhere else for safekeeping, choose **Show Access Key**\. To save the access key ID and secret access key to a `.csv` file to a secure location on your computer, choose **Download Key File**\.

2. From your local machine, open a command terminal with [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)) installed. 
```shell
aws --version
```
5. Configure your AWS cli to work with your identity using `aws configure`.


Now we are ready...


6. List the versions of you object. Replace `<bucket-name>` by you bucket name and `<object-key>` by the object key:
   ```shell
   aws s3api list-object-versions --bucket <bucket-name> --prefix <object-key>
   ```
   Can you confirm that you object has not been deleted? Inspect `DeleteMarkers`.
7. Delete the _delete mark_ by:
   ```shell
   aws s3api delete-object --bucket <bucket-name> --key <object-key> --version-id <delete-mark-version-id>
   ```
8. Can you see the object in the bucket's object list in the AWS Web Console? Can you confirm that the object was "deleted softly"?
9. How can you **permanently** delete an object (and its non-current versions) from a version-enabled bucket?   
