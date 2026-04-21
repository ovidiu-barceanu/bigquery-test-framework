from google.cloud import bigquery

def run_query():
    client = bigquery.Client()

    query = """
    SELECT
        title,
        score,
        view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags LIKE '%python%'
    ORDER BY view_count DESC
    LIMIT 5
    """

    results = client.query(query)

    for row in results:
        print(f"Title: {row.title}")
        print(f"Score: {row.score}, Views: {row.view_count}")
        print("-" * 50)

if __name__ == "__main__":
    run_query()