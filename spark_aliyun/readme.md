
## ssh into aliyun
```
ssh -o ServerAliveInterval=60 root@123.56.18.227
```
## install Java
sudo yum install -y bzip2
sudo yum search java|grep jdk
sudo yum install java-1.8.0-openjdk
java -version

## install spark
```bash
wget https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
sudo mkdir -p /usr/local/spark
sudo cp -r spark-3.5.0-bin-hadoop3.tgz /usr/local/spark
cd /usr/local/spark
sudo tar -zxvf spark-3.5.0-bin-hadoop3.tgz
vim ~/.bash_proﬁle
# 在末尾添加：
`
export SPARK_HOME=/usr/local/spark/spark-3.5.0-bin-hadoop3 
export PATH=$PATH:$SPARK_HOME/bin 
`
source ~/.bash_proﬁle
spark-shell
# 输⼊ ``:quit`` 返回原⽬录
cd /usr/local/spark/spark-3.5.0-bin-hadoop3/conf
sudo cp log4j2.properties.template log4j2.properties
sudo vim log4j2.properties
# change to: `log4j.logger.org.apache.spark.repl.MAIN=Info`
```
## install Anaconda
```bash
cd ~
wget https://mirrors.aliyun.com/anaconda/archive/Anaconda3-2023.09-0-Linux-x86_64.sh

# 全默认安装，如果之前有安装，需要删除原来安装的版本：
# rm -rf /usr/local/anaconda3
# rm ~/.condarc
sudo Anaconda3-2023.09-0-Linux-x86_64.sh
source ~/
```

## install anaconda packages
```bash
conda install -c conda-forge dask-ml
conda install pyspark

python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install findspark
pip install dask[complete]
```

# connect remote jupyter

```bash
jupyter notebook --allow-root --no-browser
# in local terminal
ssh -L 8888:localhost:8888 root@123.56.18.227
# browser url
http://localhost:8888/lab
```

pip list --format=freeze > requirements.txt

conda install -c conda-forge dask-ml
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyspark
pip install findspark
pip install dask[complete]