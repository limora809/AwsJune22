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
