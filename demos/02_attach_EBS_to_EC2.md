# Create a new Block Storage Disk for an EC2 instance

## TL;DR

1. Create an EBS volume
2. [Attach](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-attaching-volume.html) is to your instance.
3. [Make](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-using-volumes.html) the volume available to use in your instance.
4. Create some data in the volume. 

---

## Create an EBS volume and attach it to your instance

1. In the EC2 navigation pane, choose **Volumes**\.

2. Choose **Create volume**\.

3. For **Volume type**, choose General Purpose SSD\. For more information, see [Amazon EBS volume types](ebs-volume-types.md)\.

4. For **Size**, enter 10GiB\. For more information, see [Constraints on the size and configuration of an EBS volume](volume_constraints.md)\.

5. For **Availability Zone**, choose the same Availability Zone of your EC2 instance.

6. In the **Tags** section, choose **Add tag**, and then enter a tag key and value pair\.

7. Choose **Create volume**\.
   **Note**  
   The volume is ready for use when the **Volume state** is **available**\.

8. To use the volume, attach it to an instance\. For more information, see [Attach an Amazon EBS volume to an instance](ebs-attaching-volume.md)\.


## Format and mount the volume 


1. Log in to your Windows instance using Remote Desktop\. 

1. Start the Disk Management utility\. On the taskbar, open the context \(right\-click\) menu for the Windows logo, and choose **Disk Management**\.

1. Bring the volume online\. In the lower pane, open the context \(right\-click\) menu for the left panel for the disk for the EBS volume\. Choose **Online**\.  
   ![\[Bring the volume online.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-volume-online.png)

1. \(Conditional\) You must initialize the disk before you can use it\.

1. Open the context \(right\-click\) menu for the right panel for the disk, and choose **New Simple Volume**\.  
   ![\[Mount a simple volume.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-new-simple-volume.png)

1. In the **New Simple Volume Wizard**, choose **Next**\.  
   ![\[Begin the New Simple Volume Wizard.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-new-simple-volume-wizard-welcome.png)

1. If you want to change the default maximum value, specify the **Simple volume size in MB**, and then choose **Next\.**  
   ![\[Specify the volume size.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-new-simple-volume-wizard-size.png)

1. Specify a preferred drive letter, if necessary, within the **Assign the following drive letter** dropdown, and then choose **Next\.**  
   ![\[Specify a drive letter.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-new-simple-volume-wizard-letter.png)

1. Specify a **Volume Label** and adjust the default settings as necessary, and then choose **Next\.**  
   ![\[Specify settings to format the volume.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-new-simple-volume-wizard-format.png)

1. Review your settings, and then choose **Finish** to apply the modifications and close the New Simple Volume wizard\.  
   ![\[Review your settings and finish the wizard.\]](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/images/windows-2016-new-simple-volume-wizard-finish.png)


1. Create some data in your new disk