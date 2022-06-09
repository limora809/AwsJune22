# Create a Bucket

## TL;DR

1. Create SSE-S3 encrypted bucket in the same region of your EC2 instance.
2. Connect to your Windows Server instance, from a PowerShell session, use [Write-S3Object Cmdlet](https://docs.aws.amazon.com/powershell/latest/reference/items/Write-S3Object.html) to upload an object to your bucket.  

--- 

## Create a Bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3).

2. Choose **Create bucket**.

   The **Create bucket** wizard opens.

3. In **Bucket name**, enter a DNS-compliant name for your bucket.

   The bucket name must:
    + Be unique across all of Amazon S3.
    + Be between 3 and 63 characters long.
    + Not contain uppercase characters.
    + Start with a lowercase letter or number.
    
4. In **Region**, choose the AWS Region where you want the bucket to reside.

   Choose the Region where you provisioned your EC2 instance.

5. Under **Object Ownership**, leave ACLs disabled.

7. Enable Default encryption with SSE-S3 encryption type.

6. Choose **Create bucket**.


You've created a bucket in Amazon S3.

## Attach IAM role to your EC2 Instance with permissions over S3

**To replace an IAM role for an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2).

1. In the navigation pane, choose **Instances**.

1. Select the instance, choose **Actions**, **Security**, **Modify IAM role**.

1. Choose `arn:aws:iam::964849360084:instance-profile/ec2-default-dev` as the IAM role, click **Save**. 

## Upload an object from your EC2 instance

**To connect to your Windows instance using an RDP client**

1. In the EC2 navigation pane, select **Instances**. Select the instance and then choose **Connect**.

1. On the **Connect to instance** page, choose the **RDP client** tab, and then choose **Get password**.  
   ![\[Get password for RDP.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-connect-get-password.png)

1. Choose **Browse** and navigate to the private key \(`.pem`\) file you created when you launched the instance. Select the file and choose **Open** to copy the entire contents of the file to this window.

1. Choose **Decrypt Password**. The console displays the default administrator password for the instance under **Password**, replacing the **Get password** link shown previously. Save the password in a safe place.
   ![\[Password location for RDP.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-connect-password.png)

1. Choose **Download remote desktop file**. Your browser prompts you to either open or save the RDP shortcut file. When you have finished downloading the file, choose **Cancel** to return to the **Instances** page.
    + If you opened the RDP file, you'll see the **Remote Desktop Connection** dialog box.
    + If you saved the RDP file, navigate to your downloads directory, and open the RDP file to display the dialog box\.

1. The administrator account is chosen by default\. Copy and paste the password that you saved previously\.

**To upload an object to your created bucket**

1. Create a file

2. In your instance, open a PowerShell terminal session. 

3. Type 
```
   Write-S3Object -BucketName <bucketName> -Key <ObjectName> -File <path/to/your/file>
``` 
While `<bucketName>` os your bucket name. `<ObjectName>` is the object name that will be stored in your bucket. 

4. Make sure the object has been uploaded successfully. 