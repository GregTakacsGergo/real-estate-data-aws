# **Project Setup Guide**

## **Prerequisites to run this project**

Before you begin, ensure you have the following software installed on your system:

- **VS Code** (recommended) https://code.visualstudio.com/
- **Python** (version 3.12.6) https://www.python.org/downloads/release/python-3116/
- **Git** https://git-scm.com/downloads/
- **AWS account**(if you don't have one, you can create a free account) with access to S3 bucket and IAM user with access to S3 bucket. https://aws.amazon.com/free/

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
put *.yourvenv* in the .gitignore !

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
2. Download *realestate_env*.zip from the repository and upload it to your S3 bucket.

### **Step 6: Create a lambda function**

1. Create a new lambda function in the AWS Management Console.
2. Choose Python 3.12 as the runtime.
