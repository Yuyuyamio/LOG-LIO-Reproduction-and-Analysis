#!/usr/bin/env bash
set -e

# Evaluate LOG-LIO trajectory on M2DGR door_02 using evo APE.
# This assumes evo is installed in /home/fishcan/evo_venv.

cd "$(dirname "$0")/.."

source /home/fishcan/evo_venv/bin/activate
export MPLBACKEND=Agg

mkdir -p results/error_tables results/figures

evo_ape tum \
  results/trajectories/m2dgr_door_02_gt_tum.txt \
  results/trajectories/m2dgr_door_02_loglio_tum.txt \
  -a \
  --save_results results/error_tables/ape_door_02.zip \
  --save_plot results/figures/door_02_ape.pdf \
  > results/error_tables/ape_door_02.txt

cat results/error_tables/ape_door_02.txt
