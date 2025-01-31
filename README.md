# Big-Data-Parking-Tickets

NYC Parking Violations Analysis using PySpark, HDFS, and MapReduce

🚀 Project Overview

This project analyzes 7M+ NYC parking violation records to uncover trends in ticket issuance. Given the dataset size, we leveraged Google Cloud Platform (GCP), HDFS (Hadoop Distributed File System), and MapReduce (PySpark) to efficiently store and process data.

🛠️ Technologies Used

Google Cloud Platform (GCP) → Hosted and processed large datasets.

Hadoop Distributed File System (HDFS) → Stored massive data efficiently.

PySpark & MapReduce → Distributed data processing.

Bash Scripting → Automated data retrieval and loading.

JSON Parsing → Processed raw data for analysis.

🔍 Problem Statement

Processing millions of parking violations locally is inefficient due to memory constraints. We used HDFS and MapReduce to handle large-scale data and answer:

When are tickets most likely to be issued?

What are the most ticketed car makes and years?

Where are the most tickets issued?

Which vehicle color gets the most tickets?

📂 Dataset & Preprocessing

Data Source: NYC Open Data API.

Data Format: JSON with 7M+ rows.

Data Loading: Bash scripts stored data in HDFS.

🚀 Data Retrieval (get_data_7M.sh)

Fetches 7 million records in batches:

curl "https://data.cityofnewyork.us/resource/pvqr-7yc4.json?\$limit=250000&\$offset=${offset}" -o temp_chunk.json

🏗️ Data Storage in HDFS (load_data.sh)

Uploads data to HDFS:

/usr/local/hadoop/bin/hdfs dfs -copyFromLocal data.json /p1/input/

📊 Key Findings

✅ Q1: When are tickets most issued? → 9 AM (614,149 tickets)
✅ Q2: Most common ticketed car? → 2021 Toyota (65,721 tickets)
✅ Q3: Where are most tickets issued? → NY County (1,453,362 tickets)
✅ Q4: Most ticketed car color? → Gray (GY) (1,347,195 tickets)

🏗️ Project Architecture

Below is a simple architecture diagram showing the project workflow:



🚀 How to Run This Project

Step 1: Start SSH Session on GCP

ssh your-username@your-gcp-instance

Step 2: Upload Data to HDFS

hdfs dfs -copyFromLocal data.json /p1/input/

Step 3: Run MapReduce Jobs

python mapper.py | sort | python reducer.py

Step 4: View Results

Results will display the most frequent violation hours, car makes, locations, and colors.

