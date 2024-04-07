
from diagrams import Diagram, Cluster, Edge, Node
from diagrams.onprem.analytics import Pandas
from diagrams.onprem.compute import Scikit_Learn
from diagrams.onprem.database import TensorFlow_Keras
from diagrams.onprem.network import Cloud_Platform
from diagrams.onprem.storage import Python

with Diagram("Software_Design", show=False, filename="static/gpt_generated_diagram"):
    with Cluster("platform", label="Machine Learning Platform"):
        Data_Preprocessing_Module = Node("Data Preprocessing Module")
        Model_Training_Module = Node("Model Training Module")
        Model_Evaluation_Module = Node("Model Evaluation Module")
        UI = Node("User Interface")
        Data_Storage_and_Management = Node("Data Storage and Management")

    with Cluster("entities", label="Entities"):
        Pandas = Node("Pandas")
        Scikit_Learn = Node("Scikit-Learn")
        TensorFlow_Keras = Node("TensorFlow/Keras")
        Cloud_Platform = Node("Cloud Platform")
        Python = Node("Python")

    with Cluster("relationships", label="Relationships"):
        Data_Preprocessing_Module >> Model_Training_Module >> Model_Evaluation_Module >> Data_Storage_and_Management
        UI >> Data_Preprocessing_Module >> Model_Training_Module >> Model_Evaluation_Module

    with Cluster("context", label="Context"):
        Python_Programming_Experience = Node("Python Programming Experience")
        Machine_Learning_Concepts = Node("Machine Learning Concepts")
        Data_Analysis = Node("Data Analysis")
