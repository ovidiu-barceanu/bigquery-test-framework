-- =====================================================
-- DATA QUALITY TEST: posts_questions
-- 0 rows = PASS
-- =====================================================

WITH base_data AS (
    SELECT
        id,
        title,
        view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
),

-- =====================================================
-- TEST 1: NULL title
-- =====================================================
null_title AS (
    SELECT
        'NULL_TITLE' AS test_name,
        id
    FROM base_data
    WHERE title IS NULL
),

-- =====================================================
-- TEST 2: NULL view_count
-- =====================================================
null_view_count AS (
    SELECT
        'NULL_VIEW_COUNT' AS test_name,
        id
    FROM base_data
    WHERE view_count IS NULL
),

-- =====================================================
-- TEST 3: Negative view_count
-- =====================================================
negative_view_count AS (
    SELECT
        'NEGATIVE_VIEW_COUNT' AS test_name,
        id
    FROM base_data
    WHERE view_count < 0
),

-- =====================================================
-- TEST 4: Duplicate IDs
-- =====================================================
duplicate_ids AS (
    SELECT
        'DUPLICATE_ID' AS test_name,
        id
    FROM base_data
    GROUP BY id
    HAVING COUNT(*) > 1
)

-- =====================================================
-- FINAL RESULT: all failed rows
-- =====================================================
SELECT * FROM null_title
UNION ALL
SELECT * FROM null_view_count
UNION ALL
SELECT * FROM negative_view_count
UNION ALL
SELECT * FROM duplicate_ids