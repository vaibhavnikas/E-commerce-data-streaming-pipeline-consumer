<h1 align="center">Introduction</h1>

<p>This repository is part of <b>Realtime E-commerce BI Dashboard</b> project. This project is divided into 3 repositories :</p>

<ul>
<li><a href="https://github.com/vaibhavnikas/E-commerce-data-streaming-pipeline-producer">E-commerce-data-streaming-pipeline-producer</a></li>
<li><a href="https://github.com/vaibhavnikas/E-commerce-data-streaming-pipeline-consumer">E-commerce-data-streaming-pipeline-consumer</a></li>
<li><a href="https://github.com/vaibhavnikas/Realtime-Ecommerce-BI-Dashboard">Realtime-Ecommerce-BI-Dashboard</a></li>
</ul>

<p>The <a href="https://github.com/vaibhavnikas/E-commerce-data-streaming-pipeline-producer">E-commerce-data-streaming-pipeline-producer</a> repo acts as the source system. It generates e-commerce transaction data and produces it to a Kafka topic: <b>e-commerce-transactions</b>.</p>
<p>The <a href="https://github.com/vaibhavnikas/E-commerce-data-streaming-pipeline-consumer">E-commerce-data-streaming-pipeline-consumer</a> processes transaction data from the Kafka topic and ingests it into the <b>fact_transaction</b> table within the PostgreSQL-based sales data warehouse.</p>
<p>The <a href="https://github.com/vaibhavnikas/Realtime-Ecommerce-BI-Dashboard">Realtime-Ecommerce-BI-Dashboard</a> reads data from the sales datawarehouse and displays realtime business insights onto the BI dashboard.</p>

<h2 align="center">E-commerce-data-streaming-pipeline-consumer</h2>
<p>This repo contains <b>data_ingestor.py</b> which runs a Kafka consumer. It consumes transaction data from the <b>e-commerce-transactions</b> Kafka topic and ingests the data into <b>fact_transaction</b> table of the sales datawarehouse.</p>


<h3>Technologies Used</h3>
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white">
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">

<h3>Installation</h3>
<ol>
<li>Clone this repository on your system.</li>
<li>Create a .env file and add the credentials mentioned in .env.example in .env file.</li>
<li>Run <b>pip install -r requirements.txt</b> to install project dependencies.</li>
<li>Run <b>data_ingestor.py</b> to start consuming transaction data from <b>e-commerce-transactions</b> Kafka topic and ingest the data in the <b>fact_transaction</b> table of the sales datawarehouse.</li>
</ol>