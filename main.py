import module.data_processing as dp
import module.api_integration as api
import module.threat_analysis as ta
import module.visualization as viz

def main():
    print("Welcome to Threatelligence")
    # Load data
    data = dp.load_data("data/sample_data.csv")
    print("Data Loaded Successfully")

    # Fetch additional threat intelligence data
    api_data = api.fetch_data()
    print("API Data Retrieved")

    # Combine data
    combined_data = dp.combine_data(data, api_data)
    print("Data Combined Successfully")

    # Perform threat analysis
    analysis_results = ta.analyze_threats(combined_data)
    print("Threat Analysis Completed")

    # Visualize results
    viz.visualize_data(analysis_results)
    print("Visualization Generated")

if __name__ == "__main__":
    main()
