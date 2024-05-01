update_env:
	@echo "Updating the 'temperature_predictions' Conda environment from environment.yml..."
	conda env update --name temperature_predictions --file environment.yml
	@echo "Please activate the Conda environment with the following command: conda activate temperature_predictions"