import os
import base64
import snowflake.connector
    
private_key_text = os.environ.get("SNOWFLAKE_PRIVATE_KEY")
    
ctx = snowflake.connector.connect(
    user='', # Get this from https://instacart.snowflakecomputing.com/console#/preferences
    account='',
    database='',
    private_key=base64.b64decode(private_key_text)
)
    
cs = ctx.cursor()

try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
    ctx.close()
