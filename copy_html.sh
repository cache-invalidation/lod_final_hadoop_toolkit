#!/bin/bash

echo "Moving html from input/ to input_html/"
ssh -p 20000 team5@176.118.164.173 hdfs dfs -mkdir -p input_html
ssh -p 20000 team5@176.118.164.173 hdfs dfs -cp input/*.html input_html
ssh -p 20000 team5@176.118.164.173 hdfs dfs -get input_html
ssh -p 20000 team5@176.118.164.173 hdfs dfs -rm -R input_html
scp -r -P 20000 team5@176.118.164.173:/home/team5/input_html /root/input_html
ssh -p 20000 team5@176.118.164.173 rm -rf input_html
echo "Files succesfully copied!"

python3 mapper.py
