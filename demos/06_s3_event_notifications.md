# S3 Event Notifications

## Preliminaries

2. Install Git to get the source code ([reference](https://git-scm.com/download/win)).
```powershell
Invoke-WebRequest https://github.com/git-for-windows/git/releases/download/v2.36.1.windows.1/Git-2.36.1-64-bit.exe -OutFile Git-2.36.1-64-bit.exe
```

3. Install the aws cmd cli (not PS module) ([reference](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
```powershell
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

3. Install Docker to build the image ([reference](https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=Windows-Server)).
```powershell
Install-Module -Name DockerMsftProvider -Repository PSGallery -Force
Install-Package -Name docker -ProviderName DockerMsftProvider
Restart-Computer -Force
```

## TL;DR

1. Get the source code by cloning our shared repo
2. Create an Elastic Container Registry (ECR) repository named `<your-name>-yolov5` in the same region of your EC2 instance. In the repository console, click **view push commands** and follow the instructions to build the Docker image defined in `object-detection` directory in the git repo.
3. Create a Lambda Function based on the container you've just pushed.
4. Enable event notifications in your S3 bucket such that the Lambda function will be triggered upon new objects in `images/`.

--- 

## Get the code into your EC2 instance 

```shell
git clone https://github.com/alonitac/AwsJune22.git
cd AwsJune22/object-detection
```

## Create a private Docker container repository in ECR, build the YoloV5 Docker container and push it

1. Open the Amazon ECR console at [https://console\.aws\.amazon\.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories)\.

2. From the navigation bar, choose the Region to create your repository in\.

3. In the navigation pane, choose **Repositories**\.

4. On the **Repositories** page, choose **Create repository**\.

5. For **Repository name**, enter a unique name for your repository\ (for example `alonit-yolov5`\)\.

6. Choose **Create repository**\.

7. Select the repository that you created and choose **View push commands** to view the steps to push an image to your new repository\.

8. Following the instructions in **View push commands**, build, tag and push the Docker container specified in `img-object-detection` directory in our shared Git repo. **You must build and push the container from an EC2 instance located in the same region of your container registry**.


## Create a Lambda Function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console\.

2. Choose **Create function**\.
3. Choose **Container image** function type.  

4. Under **Basic information**, do the following:

   1. For **Function name**, enter `img-object-detection-<alias>`\, while `<alias>` is your name.

   2. For **Container image URI**, click on **Browse images** and choose your container image.

5. Choose **Create function**\.


## Create Lambda notifications


1. Open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

2. In the **Buckets** list, choose the name of the bucket that you want to enable events for\.

3. Choose **Properties**\.

4. Navigate to the **Event Notifications** section and choose **Create event notification**\.

5. In the **General configuration** section, specify descriptive event name for your event notification\. Optionally, you can also specify a prefix and a suffix to limit the notifications to objects with keys ending in the specified characters\.

   1. Enter `img-object-detect` for the **Event name**\.

   2. Filter event notifications by prefix, enter `images/`.

6. In the **Event types** section **All object create events**.

7. In the **Destination** section, choose your **Lambda Function** as the event notification destination\.
8. Choose **Save changes**, and Amazon S3 sends a test message to the event notification destination\.
9. Test your work by uploading an image into `images/`.
