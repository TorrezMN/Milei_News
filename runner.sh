cd /home/torrezmn/Documentos/Milei_News/src

echo "Running argentina."
python3 main_argentina.py

echo "Running global."
python3 main_global.py




# Get current date and time
current_date=$(date '+%Y-%m-%d')
current_time=$(date '+%H:%M:%S')

# Append the log message to push_log.txt
echo "$current_date  $current_time | SE EJECUTO CORRECTAMENTE!" >> /home/torrezmn/Documentos/Milei_News/push_log.txt 


