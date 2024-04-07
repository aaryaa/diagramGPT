software_design_requirements_prompt_template="""As an expert in writing software design details, use below summary to provide template with below points:

User Summary: {user_summary}

Software Design Template:
1. **Overview:**
   - Provide a high-level overview of the software design.

2. **Components:**
   - Identify and describe the key components of the system.

3. **Entities:**
   - Extract entities such as libraries, packages, cloud tools, frameworks, etc., mentioned in the summary.

4. **Relationships:**
   - Illustrate the relationships between the identified components.

5. **Context:**
   - Extract the contextual information related to the software design based on the user's summary.

6. **Technology Stack:**
   - Specify the technologies and tools that will be used in the software design.
Note: Please provide above details using 500 words"""
software_design_diagram_dot_language = """As an expert in understanding software design requirements and creating diagram, Please use the 
{generated_design_requirement} to generate digram in dot language."""
software_design_diagram_code_prompt_template="""
As an expert in writing diagram code using the diagrams Python library (version 0.23.4), please generate the complete diagram code for the following software design requirement:

Instructions:
1. Indentation: Ensure the generated code has correct indentation.
2. Completeness: Generate a full code block without any missing segments.
3. Identify the tools and libraries from the {generated_dot_diagram} and use the following import statements as example for Diagrams version 0.23.4 
# Basic Diagram Components
from diagrams import Diagram, Edge

# AWS Components
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.integration import SNS
from diagrams.aws.network import VPC

# GCP Components
from diagrams.gcp.compute import GCE
from diagrams.gcp.database import Bigtable
from diagrams.gcp.network import VPN

# Azure Components
from diagrams.azure.compute import VM
from diagrams.azure.database import SQLDatabase
from diagrams.azure.integration import EventGrid
from diagrams.azure.network import VirtualNetwork

# On-Premises Components
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Internet

# Programming Languages
from diagrams.programming.language import Python, Go

# Container Orchestration
from diagrams.k8s.compute import Pod
from diagrams.k8s.infra import Node

4. Edge Connections: Use the -> or >> operators to connect components, as add_edge is not available in version 0.23.4.
5. Set show=False,filename="gpt_generated_diagram"

Important:
Do not use methods or features introduced in later Diagrams versions, such as add_edge, NodeHighlight, or with Diagram(...) as diagram:.
Store only python code in below template format:
{output_template}

"""

software_design_diagram_code_prompt_template_test="""
As an expert in writing diagram code, please convert the dot language diagram into diagram code using the diagrams Python library (version 0.23.4)
{generated_dot_diagram}
Instructions:
1) strictly adhering to the features and syntax of version 0.23.4
2) Set show=False,filename="static/gpt_generated_diagram"
3) Use correct import statements

Sample of working python code:
from diagrams import Diagram, Cluster, Edge,Node
from diagrams.aws.analytics import Kinesis
from diagrams.aws.database import RDS
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Mysql
from diagrams.onprem.queue import Kafka

with Diagram("ETL_Pipeline", show=False, filename="gpt_generated_diagram"):
    with Cluster("ETL Pipeline for Twitter Data Analysis"):
        overview = Server("Overview")
        data_extraction = SQS("Data Extraction: \n Twitter API")
        data_transformation = Spark("Data Transformation: \n Spark")
        data_loading = RDS("Data Loading: \n MySQL")
        data_streaming = Kinesis("Data Streaming: \n AWS Kinesis")

        overview - Edge(label="extracts data from") - data_extraction
        data_extraction - Edge(label="transforms data using") - data_transformation
        data_transformation - Edge(label="loads data into") - data_loading
        data_loading - Edge(label="streams data to") - data_streaming

    aws = S3("AWS")
    spark = Spark("Spark")
    mysql = Mysql("MySQL")
    kinesis = Kinesis("AWS Kinesis")

    data_extraction - Edge(label="connects to") - aws
    data_transformation - Edge(label="runs on") - spark
    data_loading - Edge(label="stores data in") - mysql
    data_streaming - Edge(label="streams data to") - kinesis


Important:
Do not use methods or features introduced in later Diagrams versions, such as add_edge, NodeHighlight, or with Diagram(...) as diagram:.
Analyse the code carefully while writing and use above sample code for reference
Store only python code in below template format:
{output_template}

"""


output_template = '''generated diagram code'''

modify_code_prompt = """
As an expert in fixing the python code please look into the error message and modify the code
{code}{error_message}
"""

