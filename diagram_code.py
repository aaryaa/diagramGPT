from diagrams import Diagram, Cluster, Node
from diagrams.aws.analytics import Kinesis
from diagrams.onprem.analytics import Spark
from diagrams.onprem.database import MySQL


with Diagram("ETL_Pipeline", show=False,filename="static/gpt_generated_diagram"):
    with Cluster("Overview: \n ETL Pipeline for Twitter Data Analysis"):
        DataExtraction = Kinesis("Data Extraction Component: \n AWS Kinesis")
        DataTransformation = Spark("Data Transformation Component: \n Apache Spark")
        DataLoader = MySQL("Data Loading Component: \n SQL Database")
    
    AWSKinesis = Kinesis("AWS Kinesis")
    ApacheSpark = Spark("Apache Spark")
    SQLDatabase = MySQL("SQL Database")
    
    AWSKinesis >> ApacheSpark
    ApacheSpark >> SQLDatabase
    
    with Cluster("Context: \n Real-time analysis of Twitter data"):
        Context = Node("Context")
    
    with Cluster("Technology Stack: \n AWS, Spark, SQL, Kinesis"):
        TechnologyStack = Node("Technology Stack")
    
    Context >> DataExtraction
    Context >> DataTransformation
    Context >> DataLoader
    
    DataExtraction >> AWSKinesis
    DataTransformation >> ApacheSpark
    DataLoader >> SQLDatabase
