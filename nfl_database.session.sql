-- Drop the existing table if needed
DROP TABLE IF EXISTS injury_reports;

-- Create table that matches CSV structure exactly
CREATE TABLE injury_reports (
    season INTEGER,
    game_type VARCHAR(10),
    team VARCHAR(5),
    week INTEGER,
    gsis_id VARCHAR(25),
    position VARCHAR(10),
    full_name VARCHAR(100),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    report_primary_injury TEXT,
    report_secondary_injury TEXT,
    report_status VARCHAR(25),
    practice_primary_injury TEXT,
    practice_secondary_injury TEXT,
    practice_status VARCHAR(50),
    date_modified TIMESTAMP
);

COPY injury_reports FROM '/Users/ruitao/Desktop/NFL_Analysis_Hub/data/raw/injury_reports.csv' 
WITH (FORMAT csv, HEADER true);

SELECT COUNT(*) FROM injury_reports;
SELECT * FROM injury_reports LIMIT 5;

-- Check sample data
SELECT *
FROM injury_reports 
LIMIT 10;

SELECT position, week, full_name, report_primary_injury, report_secondary_injury, report_status, practice_status FROM injury_reports
WHERE position = 'QB'
ORDER BY week;

SELECT COUNT(*), week FROM injury_reports
WHERE position = 'QB' AND practice_status != 'Full Participation in Practice'
GROUP BY week
ORDER BY week;

SELECT team, COUNT(*) FROM injury_reports
WHERE position = 'QB' AND practice_status != 'Full Participation in Practice'
GROUP BY team
ORDER BY team;