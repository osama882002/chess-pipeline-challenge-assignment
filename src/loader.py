import os
import pandas as pd

from logger import logger

def fetch_drive_data(
    url: str,
    local_filename: str
    ) -> pd.DataFrame:


    local_path = os.path.join(
        "data",
        "raw",
        local_filename
    )

    if os.path.exists(local_path):

        logger.info(f"Loading cached file: {local_path}")

        print(f"[+] Loading cached file: {local_path}")

        return pd.read_csv(local_path)

    logger.info(f"Downloading {local_filename}")

    print(f"[!] Downloading {local_filename}")

    try:

        file_id = url.split("/")[-2]

        direct_url = (f"https://docs.google.com/uc?export=download&id={file_id}")

        df = pd.read_csv(direct_url)

        os.makedirs(
            os.path.dirname(local_path),
            exist_ok=True
        )

        df.to_csv(local_path, index=False)

        logger.info(f"Saved file to {local_path}")

        return df

    except Exception as e:

        logger.error(str(e))

        print(f"[-] {e}")

        return pd.DataFrame()

