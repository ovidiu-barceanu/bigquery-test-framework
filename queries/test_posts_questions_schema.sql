-- =====================================================
-- SCHEMA VALIDATION: expected vs actual
-- 0 rows = PASS
-- =====================================================

WITH expected_schema AS (
  -- define expected structure (ORDER matters)
  SELECT 1 AS ordinal_position, 'id' AS column_name, 'INT64' AS data_type UNION ALL
  SELECT 2, 'title', 'STRING' UNION ALL
  SELECT 3, 'view_count', 'INT64'
),

actual_schema AS (
  SELECT
    ordinal_position,
    column_name,
    data_type
  FROM `bigquery-public-data.stackoverflow.INFORMATION_SCHEMA.COLUMNS`
  WHERE table_name = 'posts_questions'
),

-- =====================================================
-- MISSING OR WRONG COLUMNS
-- =====================================================
missing_or_mismatch AS (
  SELECT
    'MISSING_OR_MISMATCH' AS test_name,
    e.ordinal_position,
    e.column_name,
    e.data_type
  FROM expected_schema e
  LEFT JOIN actual_schema a
    ON e.ordinal_position = a.ordinal_position
  WHERE
    a.column_name IS NULL
    OR e.column_name != a.column_name
    OR e.data_type != a.data_type
),

-- =====================================================
-- EXTRA COLUMNS
-- =====================================================
extra_columns AS (
  SELECT
    'EXTRA_COLUMN' AS test_name,
    a.ordinal_position,
    a.column_name,
    a.data_type
  FROM actual_schema a
  LEFT JOIN expected_schema e
    ON a.ordinal_position = e.ordinal_position
  WHERE e.column_name IS NULL
)

-- =====================================================
-- FINAL RESULT
-- =====================================================
SELECT * FROM missing_or_mismatch
UNION ALL
SELECT * FROM extra_columns