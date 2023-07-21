import os
import yaml
import csv

def process_user_data():
    csv_file = "xconomy.csv"
    csv_file_npc = "xconomynon.csv"
    header = ["UID", "player", "balance", "hidden"]
    header_npc = ["account", "balance"]
    
    # Check if the csv files already exist
    csv_exists = os.path.isfile(csv_file)
    csv_npc_exists = os.path.isfile(csv_file_npc)
    
    # If the csv files exist, we'll append to them; otherwise, create new ones.
    mode = 'a' if csv_exists else 'w'
    mode_npc = 'a' if csv_npc_exists else 'w'
    
    with open(csv_file, mode, newline='', encoding='utf-8') as f, \
         open(csv_file_npc, mode_npc, newline='', encoding='utf-8') as f_npc:
        writer = csv.writer(f)
        writer_npc = csv.writer(f_npc)
        
        if not csv_exists:
            writer.writerow(header)
        if not csv_npc_exists:
            writer_npc.writerow(header_npc)
        
        for filename in os.listdir("userdata"):
            if filename.endswith(".yml"):
                filepath = os.path.join("userdata", filename)
                with open(filepath, "r", encoding='utf-8') as yml_file:
                    data = yaml.safe_load(yml_file)
                    is_npc = data.get("npc", False)
                    if is_npc:
                        npc_name = data.get("npc-name", "")
                        money = data.get("money", "")
                        writer_npc.writerow([npc_name, money])
                    else:
                        account_name = data.get("last-account-name", "")
                        money = data.get("money", "")
                        filename_without_extension = os.path.splitext(filename)[0]
                        writer.writerow([filename_without_extension, account_name, money, 0])

    print("CSV export complete.")

if __name__ == "__main__":
    process_user_data()
