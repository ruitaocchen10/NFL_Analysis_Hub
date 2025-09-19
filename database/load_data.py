import nfl_data_py as nfl

def export_injury_data():
    # Load data from nfl-data-py
    print("Loading injury data from nflfastR...")
    injury_data = nfl.import_injuries([2023])
    print(f"Loaded {len(injury_data)} injury reports")
    
    # Export as CSV
    injury_data.to_csv('injury_reports.csv', index=False)
    print("Data exported as injury_reports.csv")
    print("You can now import this CSV into PostgreSQL")

if __name__ == "__main__":
    export_injury_data()