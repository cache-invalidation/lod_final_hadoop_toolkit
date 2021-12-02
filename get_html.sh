#/bin/bash
#=============================================================================#
#                      Cache Invalidation, @fckxorg (c) 2021                  #
# This script gathers all .html files from hdfs directory and moves to        #
# another.                                                                    #
#                                                                             #
# ARGS:                                                                       #
# $1: input directory that contains .html files                               #
# $2: output directory. If it doesn't exist the script will make one.         #
#=============================================================================#

echo "Moving .html from "$1" to "$2" ..."
hdfs dfs -mkdir -p $2
hdfs dfs -cp $1/*.html
echo "Done!"
