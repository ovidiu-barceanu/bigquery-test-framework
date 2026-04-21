-- 0 rows = PASS

SELECT
    id,
    title,
    view_count
FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE view_count < 0