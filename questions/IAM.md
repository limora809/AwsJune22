# IAM


1. Which of the following methods will allow an application using an AWS SDK to be authenticated as
   a principal to access AWS Cloud services? (Choose 2 answers)
   1. **Create an IAM user and store the username and password for the user in the application’s configuration.**
   2. Create an IAM user and store both parts of the access key for the user in the application’s configuration.
   3. **Run the application on an Amazon EC2 instance with an assigned IAM role.**
   4. Make all the API calls over an SSL connection.


2. Which of the following are found in an IAM policy? (Choose 2 answers)
   1. **Service Name**
   2. Region
   3. **Action**
   4. Password


3. Your AWS account administrator left your company today. The administrator had access to the root
   user and a personal IAM administrator account. With these accounts, he generated other IAM
   accounts and keys. Which of the following should you do today to protect your AWS infrastructure?
   (Choose 3 answers)
   1. **Change the password and add MFA to the root user.**
   2. Put an IP restriction on the root user.
   3. **Rotate keys and change passwords for IAM accounts.**
   4. Delete all IAM accounts.
   5. **Delete the administrator’s personal IAM account.**
   6. Relaunch all Amazon EC2 instances with new roles.


4. Which of the following actions can be authorized by IAM? (Choose 2 answers)
   1. Installing ASP.NET on a Windows Server
   2. **Launching an Amazon Linux EC2 instance**
   3. Querying an Oracle database
   4. **Adding a message to an Amazon Simple Queue Service (Amazon SQS) queue**


5. Which of the following are IAM security features? (Choose 2 answers)
   1. **Password policies**
   2. Amazon DynamoDB global secondary indexes
   3. **MFA**
   4. Consolidated Billing


6. Which of the following are benefits of using Amazon EC2 roles? (Choose 2 answers)
   1. No policies are required.
   2. **Credentials do not need to be stored on the Amazon EC2 instance.**
   3. Key rotation is not necessary.
   4. **Integration with Active Directory is automatic.**


7. Which of the following are based on temporary security tokens? (Choose 2 answers)
   1. **Amazon EC2 roles**
   2. **MFA**
   3. Root user
   4. Federation


8. Your security team is very concerned about the vulnerability of the IAM administrator user accounts
   (the accounts used to configure all IAM features and accounts). What steps can be taken to lock
   down these accounts? (Choose 3 answers)
   1. **Add multi-factor authentication (MFA) to the accounts.**
   2. Limit logins to a particular U.S. state.
   3. **Implement a password policy on the AWS account.**
   4. Apply a source IP address condition to the policy that only grants permissions when the user is on the corporate network.
   5. **Add a CAPTCHA test to the accounts.**


9. You want to grant the individuals on your network team the ability to fully manipulate Amazon EC2
   instances. Which of the following accomplish this goal? (Choose 2 answers)
   1. Create a new policy allowing EC2:* actions, and name the policy NetworkTeam.
   2. Assign the managed policy, EC2FullAccess, to a group named NetworkTeam, and assign all the team members’ IAM user accounts to that group.
   3. Create a new policy that grants EC2:* actions on all resources, and assign that policy to each individual’s IAM user account on the network team.
   4. Create a NetworkTeam IAM group, and have each team member log in to the AWS Management Console using the user name/password for the group.



10. What is the format of an IAM policy?
    1. XML
    2. Key/value pairs
    3. JSON
    4. Tab-delimited text


11. Can you add an IAM role to an IAM group?
    1. Yes
    2. No
    3. Yes, if there are ten members in the group
    4. Yes, if the group allows adding a role
 
12. What happens if you delete an IAM role that is associated with a running EC2
    instance?
    1. Any application running on the instance that is using the role will be denied access immediately.
    2. The application continues to use that role until the EC2 server is shut down.
    3. The application will have the access until the session is alive.
    4. The application will continue to have access.


15. For implementing security features, which of the following would you choose?
    1. Username/password
    2. MFA
    3. Using multiple S3 buckets
    4. Login using the root user


16. You want EC2 instances to give access without any username or password to S3
    buckets. What is the easiest way of doing this?
    1. By using a VPC S3 endpoint
    2. By using a signed URL
    3. By using roles
    4. By sharing the keys between S3 and EC2


17. Using the shared security model, the customer is responsible for which of the
    following? (Choose two.)
    1. The security of the data running inside the database hosted in EC2
    2. Maintaining the physical security of the data center
    3. Making sure the hypervisor is patched correctly
    4. Making sure the operating system is patched correctly
