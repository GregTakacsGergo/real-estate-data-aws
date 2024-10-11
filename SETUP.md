# **Project Setup Guide**

## **Prerequisites to run this project**

Before you begin, ensure you have the following software installed on your system:

- **VS Code** (recommended) https://code.visualstudio.com/
- **Python** (version 3.12.6) https://www.python.org/downloads/release/python-3116/
- **Git** https://git-scm.com/downloads/
- **AWS account** if you don't already have one, you can create a free account with access to S3 bucket and IAM user with access to S3 bucket. https://aws.amazon.com/free/

### **Step 1: Clone the Repository**

1. Open up Vs Code and Clone the repository to your local machine

```cmd
git clone https://github.com/GregTakacsGergo/real-estate-data-aws.git
```

### **Step 2: Create a virtual environment**

```bash
python3.12 -m venv .yourvenv
.yourvenv\Scripts\activate
```
place *.yourvenv* in the .gitignore !

### **Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```
### **Step 4: Configure SCRAPING_TARGET**

- Create a config.py file in the root directory of the project
- Add the target URL to the SCRAPING_TARGET variable in the config.py file

### **Step 4: Configure AWS CLI** 

1. Install AWS CLI on your system: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions
2. Configure your AWS CLI by running the following command:

   ```bash
   aws configure
   ```
3. Enter your AWS Access Key ID, AWS Secret Access Key, and Default Region when prompted.
4. You can test your AWS CLI configuration by running the following command:

   ```bash
   aws s3 ls
   ```   
If the command returns a list of your S3 buckets, you have successfully configured your AWS CLI. 

### **Step 5: Set up an S3 bucket**

1. Create an S3 bucket in the AWS Management Console.
2. Download *realestate_env.zip* (containing all the resources required for the project)from the repository and upload it to your S3 bucket.

### **Step 6: Create a lambda function**

1. Create a new lambda function in the AWS Management Console.
2. Choose Python 3.11 as the runtime. 

### **Step 7: Configure a layer for the lambda function**

1. Create a new layer in the AWS Management Console.
2. Choose Python 3.11 as the runtime.
3. Since the *realestate_env* package exceeds the maximum size limit of 10MB, choose *Upload a file from Amazon S3* 
4. Copy the S3 URL of the *realestate_env.zip* file from your S3 bucket.
5. Create the layer. 
6. Add the layer to the lambda function. 

### **Step 8: Configure the lambda function** 

1. In your lambda function code source section, choose *Upload from* and select the *lambda_package_new.zip* file from the cloned repository from your local machine. 
2.  Configure the lambda function by adding the SCRAPING_TARGET, or upload your *config.py* file to the lambda function. 
3. Set up a lambda function trigger using amazon event bridge or cloudwatch events. Since this is a real estate data project, we don't need to set up a trigger more frequent than once a day. An example of a cloudwatch event cron expression could be: *cron(0 8 * * ? *)* which triggers the lambda function every day at 8am. 
4. Important Runtime setting: make sure to set the lambda handler to *lambda_function.lambda_handler* !

### **Step 9: Test the lambda function**

- Deploy the lambda function by clicking on the *Deploy* button in the AWS Management Console.  
- Test the lambda function by running dynamodb_handler.py from the cloned repository. And you should see the test data ('2024-07-04', 500000, 1300, 2) being inserted into the dynamodb table. 

## Okay, you have successfully set up the project!
 Now you can start scraping the real estate data and storing it in the dynamodb table. 
 Next project step will be to fetch the data from the dynamodb table, store it locally, and visualize it using a data visualization library like matplotlib or seaborn.
