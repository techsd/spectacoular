# Project Architecture

## Introduction

This document provides a detailed analysis of the project's structure, including descriptions of files, components, dependencies, and configurations.

## Project Structure

The project is organized into several directories and files, each serving a specific purpose. Below is an overview of the main directories and files:

- `apps/`: Contains the main applications of the project.
  - `FreqBeamformingExample/`: Example application for frequency beamforming.
  - `Measurement_App/`: Main application for measurements.
- `docs/`: Contains documentation files.
- `tests/`: Contains test files.
- `README.md`: Provides an overview of the project.
- `EXAMPLE.md`: Contains practical examples of how to use the project's components and scenarios.
- `DIAGRAM.md`: Contains visual diagrams illustrating the architecture, sequence, and deployment of the project.
- `ARCHITECTURE.md`: This document, providing a detailed analysis of the project's structure.
- `UPDATE.md`: Contains a detailed description of changes, a plan for resolution, and a list of operations.
- `API.md`: Contains documentation on how to integrate and configure the project's API.

## Key Components

### FreqBeamformingExample

The `FreqBeamformingExample` directory contains the following key components:

- `main.py`: The main script for the frequency beamforming example application. It includes code to handle dynamic acoustic conditions such as rain, snow, wind, and thunder, as well as acoustic conditions like claps, explosions, and detonation waves. It also handles acoustic conditions from internal combustion engines and jet engines, various human, animal, and bird voices, and non-natural sounds like metal scraping, glass breaking, building destruction, and noises from flying projectiles.

### Measurement_App

The `Measurement_App` directory contains the following key components:

- `acoular_future/`: Contains future developments for the Acoular library.
  - `__init__.py`: Initializes the `acoular_future` module and includes import statements for new modules to handle dynamic acoustic conditions.
  - `fastFuncs.py`: Contains functions to handle dynamic acoustic conditions such as rain, snow, wind, and thunder, as well as acoustic conditions like claps, explosions, and detonation waves. It also handles acoustic conditions from internal combustion engines and jet engines, various human, animal, and bird voices, and non-natural sounds like metal scraping, glass breaking, building destruction, and noises from flying projectiles.
  - `spectra.py`: Contains code to handle dynamic acoustic conditions such as rain, snow, wind, and thunder, as well as acoustic conditions like claps, explosions, and detonation waves. It also handles acoustic conditions from internal combustion engines and jet engines, various human, animal, and bird voices, and non-natural sounds like metal scraping, glass breaking, building destruction, and noises from flying projectiles.
  - `tbeamform.py`: Contains code to handle dynamic acoustic conditions such as rain, snow, wind, and thunder, as well as acoustic conditions like claps, explosions, and detonation waves. It also handles acoustic conditions from internal combustion engines and jet engines, various human, animal, and bird voices, and non-natural sounds like metal scraping, glass breaking, building destruction, and noises from flying projectiles.
- `main.py`: The main script for the measurement application. It includes code to handle dynamic acoustic conditions such as rain, snow, wind, and thunder, as well as acoustic conditions like claps, explosions, and detonation waves. It also handles acoustic conditions from internal combustion engines and jet engines, various human, animal, and bird voices, and non-natural sounds like metal scraping, glass breaking, building destruction, and noises from flying projectiles.

## Dependencies

The project relies on several external libraries and tools to function correctly. Below is a list of the main dependencies:

- Python: The primary programming language used in the project.
- Acoular: A library for acoustic beamforming.
- NumPy: A library for numerical computations.
- Matplotlib: A library for creating visualizations.
- SciPy: A library for scientific computations.

## Configurations

The project includes several configuration files to manage different aspects of the project. Below is an overview of the main configuration files:

- `.github/`: Contains GitHub Actions workflows and configurations.
  - `actions/`: Contains custom GitHub Actions for setting up the environment.
    - `setup-conda/action.yml`: Sets up the conda environment with the specified Python version.
    - `setup-hatch/action.yml`: Sets up Python, upgrades pip, and installs hatch.
  - `workflows/`: Contains GitHub Actions workflows.
    - `checks.yml`: Defines the workflows for validating the citation metadata, checking for dead links in Markdown files, and ensuring all checks pass.

## Conclusion

This document provides a comprehensive overview of the project's structure, including descriptions of files, components, dependencies, and configurations. By understanding the architecture of the project, developers and stakeholders can better navigate and contribute to the project.

