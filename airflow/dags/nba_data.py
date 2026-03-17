def run():
    import requests
    import pandas as pd
    from dotenv import load_dotenv
    import os

    load_dotenv()

    BASE_URL = "https://api.server.nbaapi.com/api/playertotals"

    all_rows = []

    for season in range(2002, 2025):
    
        r = requests.get(f"{BASE_URL}?season={season}&page=1&pageSize=20")
        data = r.json()

        if not data['data']:
           continue

        pages = data['pagination']['pages']

        for page in range(1, pages + 1):
            r = requests.get(
            f"{BASE_URL}?season={season}&page={page}&pageSize=20"
        )
        all_rows.extend(r.json()['data'])

    df = pd.DataFrame(all_rows)
    import snowflake.connector
    from snowflake.connector.pandas_tools import write_pandas
    conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA'),
)
    df.columns = (
    df.columns
      .str.strip()
      .str.upper()
      .str.replace(" ", "_")
)
    write_pandas(conn, df, "PLAYERS_SEASON_DATA")
    conn.close()