import csv, random, time, shutil, os, logging, hashlib, threading
from datetime import datetime


logging.basicConfig(filename="shuffle_log.txt", 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s'
                    )

sales_data_filename = "sales_data.csv"
backup_dirname = "sales_data_backup"
sleep_interval = 10

os.makedirs(backup_dirname, exist_ok=True)

prev_hash = None
exit_flag = False

def listen_for_exit():
    global exit_flag
    while True:
        user_input = input("Enter 'q' to quit: ").strip().lower()
        if user_input == 'q':
            exit_flag = True
            print("Exiting the program...")
            break

# Start the input listener thread
input_thread = threading.Thread(target=listen_for_exit, daemon=True)
input_thread.start()

while not exit_flag:
    try: 
        with open(sales_data_filename, mode='r', newline='', encoding='utf-8') as sales_data_csvfile:
            content = sales_data_csvfile.read()
            sales_data_csvfile.seek(0)
            sales_data_reader = csv.reader(sales_data_csvfile)
            sales_data = list(sales_data_reader)
            print(content)

        current_hash = hashlib.md5(content.encode('utf-8')).hexdigest()

        if current_hash != prev_hash:
            # Backup code
            backup_filename = os.path.join(backup_dirname,
                         f"sales_data_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                         )
            
            shutil.copy(sales_data_filename, backup_filename)
            logging.info(f"Backed up {sales_data_filename} to {backup_filename}")

            # Shuffle code
            header = sales_data[0]
            rows = sales_data[1:]
            random.shuffle(rows)
            
            with open(sales_data_filename, mode='w', newline='', encoding='utf-8') as sales_data_csvfile:
                sales_data_writer = csv.writer(sales_data_csvfile)
                sales_data_writer.writerow(header)
                sales_data_writer.writerows(rows)

            logging.info(f"Shuffled the data in {sales_data_filename}")
            prev_hash = current_hash  # Update prev_hash after backup
        else:
            logging.info("Data has not changed since last shuffle. No action taken.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    time.sleep(10)
