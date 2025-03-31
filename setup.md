# PySpark and Hadoop Setup

## Step 1: Download and Install Hadoop
1. Visit the [Apache Hadoop Releases page](https://hadoop.apache.org/releases.html) and download the latest stable version of Hadoop.
2. Extract the archive:
   ```bash
   tar -xvzf hadoop-3.3.5.tar.gz
   ```
3. Move the extracted folder to your desired location:
   ```bash
   mv hadoop-3.3.5 /usr/local/hadoop
   ```

## Step 2: Download and Install Spark
1. Visit the [Apache Spark Download page](https://spark.apache.org/downloads.html).
2. Choose a version that is compatible with your Hadoop installation (e.g., Spark 3.5.5 with Hadoop 3).
3. Extract the archive:
   ```bash
   tar -xvzf spark-3.5.5-bin-hadoop3.tgz
   ```
4. Move the extracted folder:
   ```bash
   mv spark-3.5.5-bin-hadoop3 /usr/local/spark
   ```

## Step 3: Set Environment Variables
Edit your `~/.bash_profile` or `~/.zshrc` file and add the following lines:
```bash
export HADOOP_HOME=/usr/local/hadoop
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$HADOOP_HOME/bin:$SPARK_HOME/bin
export PYSPARK_PYTHON=python3
```
To apply the changes:
```bash
source ~/.bash_profile
```

## Step 4: Verify Installation
To check if everything is set up correctly, run the following commands:
```bash
hadoop version
spark-submit --version
```

## Step 5: Running Your PySpark Script
Use the following command to run your script:
```bash
spark-submit --packages org.apache.hadoop:hadoop-azure:3.3.1,com.microsoft.azure:azure-storage:7.0.0 src/product_sales_etl/product_sales_etl.py
```
