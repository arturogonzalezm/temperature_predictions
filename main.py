from src.temperature_predictor import ClimateData


def main():
    climate_data = ClimateData()
    climate_data.read_input()
    climate_data.process_data()
    climate_data.print_interpolated_values()


if __name__ == "__main__":
    main()
