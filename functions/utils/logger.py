import pandas as pd
from datetime import datetime
import os

LOG_FILE = "function_history_log.csv"

def log_function_use(function_name, input_value, result_status):
    log_entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Function": function_name,
        "Input": input_value,
        "Result/Status": result_status
    }

    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([log_entry])

    df.to_csv(LOG_FILE, index=False)
