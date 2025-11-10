# Quick Start Guide

**Get results in 5 minutes** ⚡

## 1. Clone Repository

```bash
git clone https://github.com/adrianlerer/FROM-UTOPIANISM-TO-FOSSILIZATION.git
cd FROM-UTOPIANISM-TO-FOSSILIZATION
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Analysis

### Colombia 1991 (Transformative Success)
```bash
cd ANALYSIS/
python colombia_h1_analysis.py
```

**Expected Output**:
```
H1 VERDICT: Colombia 1991
✓ CONFIRMED: SP = 0.683 (> 0.65 threshold)
✓ CONFIRMED: CLI_1991 = 0.135 (< 0.5, paths open)
✓ CONFIRMED: Gap 35% → 12% (narrowing)
✓ CONFIRMED: PE 0.398 → 0.881 (increasing)
OVERALL: Dixon & Landau H1 VALIDATED
```

### Chile 2022 (Utopian Failure)
```bash
python chile_h2_analysis.py
```

**Expected Output**:
```
H2 VERDICT: Chile 2022
✓ CONFIRMED: SP = 0.304 (< 0.35, negative selection)
✓ CONFIRMED: CLI = 0.81 (> 0.65, blocked pathways)
✓ CONFIRMED: Gap = 77.2% (> 60%, massive unfunded)
✓ CONFIRMED: CF = 0.004 (< 0.20, utopian failure)
Chile 99.3% LESS FIT than Colombia
```

### Argentina Paradox (Fossilized Utopianism)
```bash
python argentina_paradox_analysis.py
```

**Expected Output**:
```
NOVEL INSIGHT (NOT IN DIXON & LANDAU):
Argentina shows FOSSILIZED UTOPIANISM:
- CLI: 0.45 (1949) → 0.87 (2025)
- Reform success: 0/23 attempts (0% rate)
- System TRAPPED in permanent dysfunctional equilibrium
```

## 4. View Results

All CSV outputs are saved to `DATA/analysis_results/`:
```bash
cd ../DATA/analysis_results/
ls -l *.csv
```

## 5. Read the Paper

```bash
cd ../../PAPER/
# Open DIXON_LANDAU_EPT_PAPER_EXECUTIVE_DRAFT.md
```

## Key Findings (30-second version)

| Metric | Colombia 1991 | Chile 2022 | Argentina 1949 |
|--------|---------------|------------|----------------|
| **Constitutional Fitness** | 0.913 ✅ | 0.004 ❌ | 0.160 → 0.011 🪦 |
| **Popular Support** | 75% | 38.14% | ~55% |
| **Lock-in (CLI)** | 0.135 | 0.810 | 0.45 → 0.87 |
| **Outcome** | Transformation | Rejection | Fossilization |

**Discovery**: Chile's failure was **predictable** 7 months before the $10M plebiscite using Constitutional Fitness calculation.

## Next Steps

- Read full paper: `PAPER/DIXON_LANDAU_EPT_PAPER_EXECUTIVE_DRAFT.md`
- Explore methodology: `DOCUMENTATION/dixon_landau_ept_conceptual_mapping.md`
- Check data sources: CSV files in `DATA/analysis_results/`

## Questions?

Open a GitHub issue or see CONTRIBUTING.md
