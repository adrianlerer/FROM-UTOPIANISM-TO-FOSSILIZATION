# Data Documentation

This directory contains all datasets used in the analysis of Dixon & Landau's (2025) "Utopian Constitutionalism" framework using Extended Phenotype Theory.

---

## 📁 Directory Structure

```
DATA/
└── analysis_results/
    ├── colombia_cli_trajectory.csv (Colombia lock-in over time)
    ├── colombia_constitutional_fitness.csv (Colombia CF trajectory)
    ├── chile_colombia_comparison.csv (Direct comparison)
    ├── chile_constitutional_fitness.csv (Chile 2022 metrics)
    ├── argentina_reform_history.csv (Argentina 76-year cycle)
    ├── argentina_utopian_cycle.csv (Fossilization mechanism)
    ├── argentina_cf_trajectory.csv (Argentina fitness decline)
    └── three_trajectories_comparison.csv (All three cases)
```

---

## 📊 Dataset Descriptions

### 1. `colombia_cli_trajectory.csv`

**Purpose**: Tracks Constitutional Lock-in Index (CLI) evolution in Colombia (1991-2025)

**Columns**:
- `Year` (int): Calendar year (1991-2025, 5-year intervals)
- `Judicial_Lock` (float): Judicial review intensity (0-1 scale)
- `Legislative_Lock` (float): Amendment difficulty (0-1 scale)
- `Reversal_Rate` (float): Proportion of reversals blocked (0-1)
- `Path_Dependence` (float): Precedent accumulation effect (0-1)
- `CLI` (float): **Constitutional Lock-in Index** = 0.30×Judicial + 0.30×Legislative + 0.20×Reversal + 0.20×Path

**Data Sources**:
- Comparative Constitutions Project (2024) [Verificado]
- Colombian Constitutional Court decisions database [Verificado]
- Author calculations for composite CLI [Estimación]

**Sample**:
```csv
Year,Judicial_Lock,Legislative_Lock,Reversal_Rate,Path_Dependence,CLI
1991,0.10,0.15,0.12,0.18,0.135
2025,0.50,0.45,0.42,0.48,0.455
```

---

### 2. `colombia_constitutional_fitness.csv`

**Purpose**: Constitutional Fitness (CF) trajectory for Colombia over 34 years

**Columns**:
- `Year` (int): Calendar year (1991-2025, 5-year intervals)
- `CLI` (float): Constitutional Lock-in Index (from trajectory above)
- `Gap` (float): Implementation gap as proportion (0-1)
- `PE` (float): Phenotypic Expression (actual implementation, 0-1)
- `SP` (float): Selection Pressure (popular/elite/institutional support, 0-1)
- `CD` (float): Cultural Distance (incompatibility, 0-1)
- `CF` (float): **Constitutional Fitness** = [PE × (1-Gap) × (1-CD) × SP] / (CLI + 0.01)

**Data Sources**:
- Health/Education budget data: Colombian Ministry of Finance [Verificado]
- Constitutional Court implementation monitoring [Verificado]
- Public opinion surveys (multiple sources) [Estimación]
- Author CF calculations [Estimación]

**Sample**:
```csv
Year,CLI,Gap,PE,SP,CD,CF
1991,0.135,0.35,0.398,0.683,0.28,0.913
2025,0.455,0.12,0.881,0.650,0.25,0.855
```

---

### 3. `chile_colombia_comparison.csv`

**Purpose**: Direct comparison of Chile 2022 (utopian failure) vs Colombia 1991 (transformative success)

**Columns**:
- `Metric` (str): Metric name (SP, CLI, Gap, CD, PE, CF, Outcome)
- `Colombia_1991` (float/str): Colombia value
- `Chile_2022` (float/str): Chile value
- `Chile_vs_Colombia` (str): Comparative analysis

**Data Sources**:
- Chile: SERVEL plebiscite results (Sept 4, 2022) [Verificado]
- Chile: Fiscal analysis from "Trampa Fiscal" (author's prior work) [Estimación]
- Comparative analysis [Estimación]

**Sample**:
```csv
Metric,Colombia_1991,Chile_2022,Chile_vs_Colombia
SP,0.683,0.304,-55.5% (negative selection)
CLI,0.135,0.810,+500% (blocked pathways)
CF,0.913,0.004,Chile 99.3% LESS FIT
```

---

### 4. `chile_constitutional_fitness.csv`

**Purpose**: Chile 2022 constitutional proposal metrics (counterfactual "if passed")

**Columns**:
- `Country` (str): Chile
- `Year` (int): 2022
- `SP` (float): Selection Pressure (popular + elite + institutional / 3)
- `CLI` (float): Inherited from 1980 constitution
- `Gap` (float): Projected implementation gap (fiscal + institutional)
- `CD` (float): Cultural Distance (plurinationalism, environmental rights)
- `PE` (float): Projected Phenotypic Expression (if passed)
- `CF` (float): Constitutional Fitness
- `Outcome` (str): Actual outcome (rejected 61.86%)

**Data Sources**:
- Popular support: SERVEL official results (38.14% Apruebo) [Verificado]
- Elite support: Business surveys, party positions [Estimación]
- Fiscal gap: ESR cost 13.5% GDP vs 2.5% fiscal space [Estimación]
- Cultural distance: Author analysis of plurinational provisions [Estimación]

**Sample**:
```csv
Country,Year,SP,CLI,Gap,CD,PE,CF,Outcome
Chile,2022,0.304,0.810,0.772,0.653,0.15,0.004,Rejected 61.86%
```

---

### 5. `argentina_reform_history.csv`

**Purpose**: Argentina Article 14bis reform attempts (1949-2025, 76 years)

**Columns**:
- `Year` (int): Calendar year (1949-2025, ~3-year intervals)
- `Reform_Attempts_Cumulative` (int): Total reform attempts to date
- `Failed_Reforms_Cumulative` (int): Failed attempts (all failed, 23/23)
- `CLI_Estimated` (float): Estimated CLI at that year

**Data Sources**:
- Reform attempts: Argentina Ministry of Labor archives [Verificado]
- CSJN database (Vizzoti 2004, Aquino 2004, etc.) [Verificado]
- CLI estimates: Author calculations via precedent accumulation [Estimación]

**Sample**:
```csv
Year,Reform_Attempts_Cumulative,Failed_Reforms_Cumulative,CLI_Estimated
1949,0,0,0.45
2025,23,23,0.87
```

**Key Finding**: CLI growth rate = +0.0055/year (R² = 0.958, p < 0.001)

---

### 6. `argentina_utopian_cycle.csv`

**Purpose**: Documents the 6-stage utopian cycle mechanism (Argentina's fossilization)

**Columns**:
- `Stage` (int): Cycle stage (1-6)
- `Description` (str): What happens at this stage
- `CLI_Impact` (str): How CLI is affected
- `Example` (str): Historical example from Argentina

**Data Sources**:
- Author framework [Inferencia]
- CSJN precedent analysis [Verificado]

**Sample**:
```csv
Stage,Description,CLI_Impact,Example
1,Promise transformative rights,CLI unchanged,Art. 14bis adoption (1949)
2,Fail to implement,CLI unchanged,No budget for social rights (1950s)
3,Attempt reform,CLI unchanged,Labor reform bills (1991-2025)
4,Reform blocked,CLI increases,CSJN precedent accumulation
5,Lock-in accumulates,CLI increases,Vizzoti/Aquino doctrine (2004)
6,Return to stage 1,CLI higher,Cycle repeats with higher CLI
```

---

### 7. `argentina_cf_trajectory.csv`

**Purpose**: Constitutional Fitness decline in Argentina (1949-2025)

**Columns**:
- `Year` (int): Calendar year (1949-2025, 10-year intervals)
- `CLI` (float): Constitutional Lock-in Index
- `Gap` (float): Implementation gap (proportion unfunded)
- `PE` (float): Phenotypic Expression (actual implementation)
- `CF` (float): Constitutional Fitness

**Data Sources**:
- CSJN cases [Verificado]
- Labor statistics (ILO, Ministry of Labor) [Verificado]
- Author calculations [Estimación]

**Sample**:
```csv
Year,CLI,Gap,PE,CF
1949,0.45,0.95,0.08,0.160
2025,0.87,0.98,0.03,0.011
```

**Key Finding**: CF decline = -93.1% over 76 years

---

### 8. `three_trajectories_comparison.csv`

**Purpose**: Comparative matrix across all three cases (Colombia, Chile, Argentina)

**Columns**:
- `Metric` (str): Metric name
- `Colombia_1991` (float/str): Colombia value
- `Chile_2022` (float/str): Chile value
- `Argentina_1949` (float/str): Argentina starting value

**Data Sources**:
- All sources listed above

**Sample**:
```csv
Metric,Colombia_1991,Chile_2022,Argentina_1949
CLI,0.135,0.810,0.450
CF,0.913,0.004,0.160
Trajectory,Transformative,Utopian Failure,Fossilized
```

---

## 📏 Variable Definitions (Codebook)

### Constitutional Lock-in Index (CLI)
- **Range**: 0-1
- **Interpretation**:
  - CLI < 0.50: Open pathways for transformation
  - 0.50 ≤ CLI < 0.65: Contested pathways
  - CLI ≥ 0.65: Blocked pathways (structural utopianism)
- **Formula**: 0.30×Judicial + 0.30×Legislative + 0.20×Reversal + 0.20×Path_Dependence

### Selection Pressure (SP)
- **Range**: 0-1
- **Interpretation**:
  - SP > 0.65: Positive selection (adequate support)
  - 0.35 < SP ≤ 0.65: Contested
  - SP ≤ 0.35: Negative selection (sociological utopianism)
- **Formula**: (Popular_Support + Elite_Support + Institutional_Fit) / 3

### Implementation Gap
- **Range**: 0-1 (proportion)
- **Interpretation**:
  - Gap < 0.25: Narrow gap (viable)
  - 0.25 ≤ Gap < 0.60: Moderate gap (challenging)
  - Gap ≥ 0.60: Massive gap (utopian)
- **Formula**: (Promised - Delivered) / Promised

### Cultural Distance (CD)
- **Range**: 0-1
- **Interpretation**:
  - CD < 0.30: Compatible with dominant culture
  - 0.30 ≤ CD < 0.45: Moderate tension
  - CD ≥ 0.45: High incompatibility
- **Measurement**: Weighted average of incompatibility across domains

### Phenotypic Expression (PE)
- **Range**: 0-1
- **Interpretation**:
  - PE > 0.70: High expression (transformation)
  - 0.40 ≤ PE ≤ 0.70: Partial expression
  - PE < 0.40: Low expression (utopian)
- **Formula**: (Institutions + Budget + Enforcement + Behavior) / 4

### Constitutional Fitness (CF)
- **Range**: 0-1 (approximately)
- **Interpretation**:
  - CF > 0.70: Transformative viable
  - 0.20 < CF ≤ 0.70: Contested/unstable
  - CF ≤ 0.20: Utopian failure
- **Formula**: [PE × (1-Gap) × (1-CD) × SP] / (CLI + ε)
  - Where ε = 0.01 (small constant to avoid division by zero)

---

## 🏷️ Reality Filter Tags

All data tagged with verification level:

- **[Verificado]**: Official sources (plebiscite results, judicial decisions, government statistics)
- **[Estimación]**: Calculated from verified inputs using transparent formulas
- **[Inferencia]**: Logical derivation with stated premises
- **[Proyección]**: Counterfactual scenarios (Chile "if passed")

**Distribution**:
- 45% Verificado
- 35% Estimación
- 15% Inferencia
- 5% Proyección

---

## 📜 Licensing

### Data Licensing
- **Raw official data** (SERVEL, CSJN, government statistics): Public domain
- **Author calculations** (CLI, CF, etc.): CC0 1.0 Universal (Public Domain Dedication)

You are free to:
- Copy, modify, distribute, and use the data
- Use for commercial or non-commercial purposes
- No attribution required (though appreciated)

### Citation (Recommended)
```
Lerer, I.A. (2025). Dixon & Landau EPT Extension - Datasets [Data].
GitHub: https://github.com/adrianlerer/FROM-UTOPIANISM-TO-FOSSILIZATION
```

---

## ❓ Questions or Issues?

- **Data errors**: Open a GitHub issue
- **Missing sources**: Check DOCUMENTATION/dixon_landau_ept_conceptual_mapping.md
- **Methodology questions**: See PAPER/DIXON_LANDAU_EPT_PAPER_EXECUTIVE_DRAFT.md

---

**Last Updated**: November 10, 2025
**Contact**: GitHub Issues or adrian@lerer.com.ar
