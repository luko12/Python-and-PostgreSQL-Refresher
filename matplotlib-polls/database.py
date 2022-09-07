import os
import psycopg2
from dotenv import load_dotenv


SELECT_POLLS = "SELECT * FROM POLLS;"
SELECT_OPTIONS_IN_POLL = """
SELECT options.text, SUM(votes) FROM options
JOIN polls ON options.poll_id = polls.id
JOIN votes ON options.id = votes.option_id
WHERE polls.id = %s
GROUP BY options.text;"""