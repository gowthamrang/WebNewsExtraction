echo $1
a='feature'
echo $1$a
echo "Flushing out old data"
#rm -r ../../data/$1$a
echo "Creating new directory structure"
mkdir -p ../../data/temp/Body ../../data/temp/Publish_date ../../data/temp/Title ../../data/$1$a/train
python prepare.py ../../data/train/field.csv ../../data/FullDataset ../../data/temp 
python helper.py ../../data/temp ../../data/$1$a $1

