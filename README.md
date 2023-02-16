# ipd-py

A set of scripts useful for studying the Iterated Prisoner's Dilemma.

*This code has been developed for Assignment 1 of COMP-3710 (Artificial Intelligence) at the University of Windsor, Winter 2023*

## Optimization Strategies Used

3 different optimization strategies have been implemented for trying to find the best deterministic strategy of the Iterated Prisoner's Dilemma:

1. Genetic Algorithm
    - Runnable via the `genetic.py` script
2. Hill Climbing
    - Runnable via the `hill_climbing.py` script
3. Tabu Search
    - Runnable via the `tabu.py` script

## Contributors

The following people helped make this project possible:

- Jeremie Bornais
- Justin Bornais
- Zach Hutz
- Caden Quiring

## License

View the license for this codebase [here](LICENSE).

## Explanation of Files and Directories

- 📂 data/
  - this folder contains raw data for each experimental run of each script
- 📂 extracted/
  - this folder contains the numerical "score" value for each experimental run of each script, extracted from the raw data
- 🐍 [compare_all_generated_strategies.py](compare_all_generated_strategies.py)
  - this script compares all of the different generated strategies to find the best ones
- 🐍 [compare_best_strategies.py](compare_best_strategies.py)
  - this script compares all of the best strategies as well as some human-defined strategies
- 📃 [comparison_all_generated_strategies.csv](comparison_all_generated_strategies.csv)
  - this file contains the output of `compare_all_generated_strategies.py`
- 📃 [comparison_best_strategies.csv](comparison_best_strategies.csv)
  - this file contains the output of `compare_best_strategies.py`
- 📃 [encodings.md](encodings.md)
  - contains helpful information regarding encodings of strategies
- 🐍 [extract_data.py](extract_data.py)
  - this script reads in raw data from `data/`, extracts it, and outputs it to `extracted/`
- 🐍 [gen_strats.py](gen_strats.py)
  - this script generated a user-defined number of random strategies and outputs to `random_strategies.txt`
- 🐍 [genetic.py](genetic.py)
  - this script runs the Genetic Algorithm optimization method
- 🐍 [hill_climbing.py](hill_climbing.py)
  - this script runs the Hill Climbing optimization method
- 🐍 [player_utils.py](hill_climbing.py)
  - this file contains shared code that two or more optimization methods use
- 📃 [random_strategies.txt](random_strategies.txt)
  - a list of randomly generated strategies, created by `gen_strats.py`
- 📃 [README.md](README.md)
  - you're reading this right now!
- 🐍 [tabu.py](tabu.py)
  - this script runs the Tabu Search optimization method
