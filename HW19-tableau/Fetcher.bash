#!/bin/bash

YR2017=`pwd`/2017
YR2018=`pwd`/2018

if [ ! -d $YR2017 ]; then
    mkdir $YR2017
    echo $YR2017
fi
if [ ! -d $YR2018 ]; then
    mkdir $YR2018
    echo $YR2018
fi

## get the zip(s) for 2017, 2018 data
wget https://s3.amazonaws.com/tripdata/201701-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201702-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201703-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201704-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201705-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201706-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201707-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201708-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201709-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201710-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201711-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201712-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201801-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201802-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201803-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201804-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201805-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201806-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201807-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201808-citibike-tripdata.csv.zip
wget https://s3.amazonaws.com/tripdata/201809-citibike-tripdata.csv.zip

## unzip csv files
unzip 201701-citibike-tripdata.csv.zip
unzip 201702-citibike-tripdata.csv.zip
unzip 201703-citibike-tripdata.csv.zip
unzip 201704-citibike-tripdata.csv.zip
unzip 201705-citibike-tripdata.csv.zip
unzip 201706-citibike-tripdata.csv.zip
unzip 201707-citibike-tripdata.csv.zip
unzip 201708-citibike-tripdata.csv.zip
unzip 201709-citibike-tripdata.csv.zip
unzip 201710-citibike-tripdata.csv.zip
unzip 201711-citibike-tripdata.csv.zip
unzip 201712-citibike-tripdata.csv.zip
unzip 201801-citibike-tripdata.csv.zip
unzip 201802-citibike-tripdata.csv.zip
unzip 201803-citibike-tripdata.csv.zip
unzip 201804-citibike-tripdata.csv.zip
unzip 201805-citibike-tripdata.csv.zip
unzip 201806-citibike-tripdata.csv.zip
unzip 201807-citibike-tripdata.csv.zip
unzip 201808-citibike-tripdata.csv.zip
unzip 201809-citibike-tripdata.csv.zip

## capture the header line
## use later when combining CSV file(s)
head -n 1 201701-citibike-tripdata.csv > citibike-tripdata--header.csv

## remove the first line (header) all files
sed -i '1d' 201701-citibike-tripdata.csv
sed -i '1d' 201702-citibike-tripdata.csv
sed -i '1d' 201703-citibike-tripdata.csv
sed -i '1d' 201704-citibike-tripdata.csv
sed -i '1d' 201705-citibike-tripdata.csv
sed -i '1d' 201706-citibike-tripdata.csv
sed -i '1d' 201707-citibike-tripdata.csv
sed -i '1d' 201708-citibike-tripdata.csv
sed -i '1d' 201709-citibike-tripdata.csv
sed -i '1d' 201710-citibike-tripdata.csv
sed -i '1d' 201711-citibike-tripdata.csv
sed -i '1d' 201712-citibike-tripdata.csv
sed -i '1d' 201801-citibike-tripdata.csv
sed -i '1d' 201802-citibike-tripdata.csv
sed -i '1d' 201803-citibike-tripdata.csv
sed -i '1d' 201804-citibike-tripdata.csv
sed -i '1d' 201805-citibike-tripdata.csv
sed -i '1d' 201806-citibike-tripdata.csv
sed -i '1d' 201807-citibike-tripdata.csv
sed -i '1d' 201808-citibike-tripdata.csv
sed -i '1d' 201809-citibike-tripdata.csv

## move csv files to year folders
mv 2017*.csv $YR2017
mv 2018*.csv $YR2018

## combine
cat 2017/*.csv >> citibike-tripdata--2017.csv
cat 2018/*.csv >> citibike-tripdata--2018.csv

## combine (dataset(s))

# Aug2017.May2018
cat 2017/201708-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2017/201709-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2017/201710-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2017/201711-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2017/201712-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2018/201801-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2018/201802-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2018/201803-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2018/201804-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv
cat 2018/201805-citibike-tripdata.csv >> citibike-tripdata-Aug2017.May2018.csv

# 2017,2018 even months
cat 2017/201702-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2017/201704-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2017/201706-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2017/201708-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2017/201710-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2017/201712-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2018/201802-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2018/201804-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2018/201806-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv
cat 2018/201808-citibike-tripdata.csv >> citibike-tripdata-2017.2018-even_months.csv

# 2017,2018 odd months
cat 2017/201701-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2017/201703-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2017/201705-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2017/201707-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2017/201709-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2017/201711-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2018/201801-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2018/201803-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2018/201805-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2018/201807-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
cat 2018/201809-citibike-tripdata.csv >> citibike-tripdata-2017.2018-odd_months.csv
