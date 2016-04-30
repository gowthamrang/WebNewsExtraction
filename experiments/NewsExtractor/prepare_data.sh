echo "Flushing out old data"
rm -r ../../data/Datefeature
echo "Creating new directory structure"
mkdir -p ../../data/temp/Body ../../data/temp/Publish_date ../../data/temp/Title ../../data/Datefeature/cv1/train ../../data/Datefeature/cv2/train ../../data/Datefeature/cv3/train ../../data/Datefeature/cv4/train ../../data/Datefeature/cv5/train ../../data/Datefeature/cv1/test ../../data/Datefeature/cv2/test ../../data/Datefeature/cv3/test ../../data/Datefeature/cv4/test ../../data/Datefeature/cv5/test
python prepare.py ../../data/train/field.csv ../../data/V2.0 ../../data/temp 
python helper.py ../../data/temp ../../data/Datefeature Date

