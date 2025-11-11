# Integrity Filter - Operational Risk Assessment

## 🎯 Purpose

**Operational filter for AI-assisted research** based on Miyai et al. (2025) "Jr. AI Scientist and Its Risk Report".

Prevents common pitfalls identified in AI-generated research:
1. ❌ Ideas working by chance (no theoretical justification)
2. ❌ Citation fabrication or irrelevance  
3. ❌ Experiments claimed but not performed
4. ❌ Metric hacking (optimizing for appearance vs substance)
5. ❌ Overconfidence in projections/estimates

---

## 🚀 Quick Start

### Basic Usage

```python
from integrity_filter import IntegrityFilter

# Initialize
filter = IntegrityFilter(project_name="my_analysis")

# Validate hypothesis BEFORE analysis
filter.validate_hypothesis(
    hypothesis_text="Colombia succeeded due to adequate support",
    baseline_source="Dixon & Landau (2025)",
    theoretical_basis="Framework predicts success with SP > 0.65",
    testable=True
)

# Validate claims DURING analysis
filter.validate_claim(
    claim="Chile plebiscite: 62% rejection",
    evidence_type="verified",
    source="SERVEL official data Sept 2022"
)

# Generate report AFTER analysis
filter.calculate_project_risk()
filter.generate_report()
```

---

## 📊 Evidence Types & Verification Scores

| Type | Weight | Description | Example |
|------|--------|-------------|---------|
| **verified** | 1.00 | Official data, published sources | SERVEL election results |
| **calculated** | 0.85 | Derived from verified inputs | CF = [PE × (1-Gap)] / CLI |
| **estimated** | 0.65 | Proxy measures, interpolation | Elite support from polling |
| **inferred** | 0.45 | Logical derivation | Cultural distance from surveys |
| **projected** | 0.25 | Counterfactuals, forecasts | Chile "if passed" scenario |

---

## 🎨 Risk Levels

```
🟢 LOW      (>85% verified): Ready for publication
🟡 MODERATE (70-85%):         Revision suggested
🟠 HIGH     (50-70%):         Major revision required
🔴 CRITICAL (<50%):           Not ready for publication
```

---

## 📋 Complete Workflow Example

See `example_with_integrity_filter.py` for full working example.

### Step-by-Step Integration

```python
# 1. Initialize at start of analysis
filter = IntegrityFilter(project_name="figure4_analysis")

# 2. Validate hypotheses BEFORE running code
filter.validate_hypothesis(
    hypothesis_text="Colombia FSI improved 1991-2025",
    baseline_source="Dixon & Landau (2025)",
    theoretical_basis="Transformative success predicts narrowing gap",
    testable=True
)

# 3. Load data and validate sources
import pandas as pd
df = pd.read_csv('../DATA/analysis_results/colombia_cf.csv')
filter.validate_claim(
    claim=f"Loaded {len(df)} Colombia data points",
    evidence_type="verified",
    source="../DATA/analysis_results/colombia_cf.csv"
)

# 4. Calculate metrics and validate each claim
fsi = (1 - df['Gap']) * 100
filter.validate_claim(
    claim=f"Colombia FSI improved from {fsi.iloc[0]:.1f}% to {fsi.iloc[-1]:.1f}%",
    evidence_type="calculated",
    source="FSI = (1-Gap)×100%, Gap from verified CSV",
    theoretical_justification="Expected per H1: transformative success",
    external_validation="World Bank data shows social spending increase"
)

# 5. Check for metric optimization (hacking detection)
filter.check_metric_optimization(
    metric_name="FSI",
    metric_values={"Colombia": 88.0, "Chile": 22.8, "Argentina": 23.0}
)

# 6. Generate final report with risk assessment
risk = filter.calculate_project_risk()
report_path = filter.generate_report()

# 7. Decision point based on risk level
if risk['risk_level'] in ['LOW', 'MODERATE']:
    print("✅ APPROVED: Proceed with analysis")
else:
    print("❌ NOT APPROVED: Address integrity issues first")
```

---

## 🔍 What Filter Checks

### Hypothesis Validation (Pre-Analysis)

- ✅ Theoretical justification present and substantial (>20 chars)
- ✅ Baseline paper properly cited (author + year pattern)
- ✅ Hypothesis is empirically testable
- ✅ No circular reasoning (hypothesis doesn't assume conclusion)

### Claim Validation (During Analysis)

- ✅ Evidence level appropriate for claim strength
- ✅ Data source documented (file path, citation)
- ✅ Projections include stated limitations
- ✅ Calculated claims include explicit formula
- ✅ External validation provided where available

### Metric Optimization Detection (Post-Analysis)

- ✅ Variance not suspiciously uniform (all values similar)
- ✅ No "perfect separation" (too convenient)
- ✅ Not too many round numbers (suggests fabrication)

---

## 📤 Output Reports

### JSON Report
```json
{
  "metadata": {
    "project_name": "figure4_fiscal_sustainability",
    "generated_at": "2025-11-11T04:31:03",
    "framework": "Miyai et al. (2025)"
  },
  "risk_assessment": {
    "risk_level": "MODERATE",
    "verification_score": 0.7375,
    "total_claims": 8,
    "evidence_breakdown": {
      "verified": 2,
      "calculated": 4,
      "projected": 2
    }
  },
  "recommendations": [
    "Increase proportion of verified claims",
    "Reduce reliance on projections"
  ]
}
```

### Markdown Report (Human-Readable)
```markdown
# Integrity Assessment Report

**Risk Level**: MODERATE 🟡
**Verification Score**: 73.8%

## Recommendations
- Increase verified claims (currently <30%)
- Reduce projections (currently >20%)

## Hypotheses (3)
[Detailed hypothesis breakdown...]

## Claims (8)
[Evidence type, source, score for each claim...]
```

---

## 🎓 Academic Justification

### Based on Miyai et al. (2025) Framework

> "Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper"
> arXiv:2511.04583

**Key Risks Identified:**
1. Ideas working by chance without theory
2. Citation fabrication
3. Unreported experiments
4. Metric hacking
5. Overconfidence without validation

**Our Implementation:**
- Real-time validation (not post-hoc)
- Quantitative risk scoring (verification weights)
- Automated report generation (JSON + Markdown)
- Decision thresholds (LOW/MODERATE/HIGH/CRITICAL)

---

## 🔧 Integration with Existing Workflow

### Before Filter (Manual Checks)
```python
# Analyst manually tracks:
# - "Did I cite baseline properly?"
# - "Is this claim verified or estimated?"
# - "Am I being overconfident?"
# ❌ Easy to forget, inconsistent application
```

### After Filter (Automated Checks)
```python
# Filter automatically tracks:
filter.validate_hypothesis(...)  # Forces theoretical justification
filter.validate_claim(...)       # Requires evidence level + source
filter.calculate_project_risk()  # Aggregates verification score
# ✅ Systematic, reproducible, auditable
```

---

## 📊 Example: Figure 4 Analysis

**Scenario**: Generate FSI temporal evolution figure

**Without Filter:**
- Claim: "Colombia improved, Chile failed"
- Evidence: Unclear provenance
- Risk: Potentially weak justification

**With Filter:**
```bash
$ python3 example_with_integrity_filter.py

✅ Hypothesis H1 validated (no risks)
✅ Claim [verified] validated: Colombia data from official CSV
✅ Claim [calculated] validated: FSI = (1-Gap)×100%
⚠️  Claim [projected] validated: Chile counterfactual (3 limitations stated)
🟡 Risk Level: MODERATE (73.8% verified)
✅ APPROVED: Proceed with Figure 4
```

**Result**: 
- 8 claims tracked
- 2 verified (25%)
- 4 calculated (50%)
- 2 projected (25%)
- **Risk: MODERATE** → Approved with suggested improvements

---

## 🚨 When Filter Blocks Analysis

### Example: CRITICAL Risk

```python
filter.validate_claim(
    claim="Chile would have collapsed economically",
    evidence_type="projected",
    source="My intuition"
)
# ❌ Warning: WEAK_EVIDENCE + NO_SOURCE + NO_LIMITS

filter.calculate_project_risk()
# 🔴 Risk Level: CRITICAL (<50% verified)
# ❌ NOT APPROVED: Major revision required
```

**Fix**: Add verified data, proper sources, state limitations

---

## 💡 Best Practices

### Do's ✅
- ✅ Validate ALL hypotheses before analysis
- ✅ Tag EVERY claim with evidence type
- ✅ Document data sources explicitly
- ✅ State limitations for projections
- ✅ Generate report BEFORE publication

### Don'ts ❌
- ❌ Don't skip hypothesis validation
- ❌ Don't claim "calculated" without formula
- ❌ Don't use "verified" for estimates
- ❌ Don't ignore risk warnings
- ❌ Don't fabricate external validation

---

## 🔗 Related Tools

### In This Repo
- `colombia_h1_analysis.py` - H1 validation with Reality Filter
- `chile_h2_analysis.py` - H2 validation with data provenance
- `argentina_paradox_analysis.py` - Novel finding with transparent estimation

### External References
- Miyai et al. (2025) - Jr. AI Scientist framework
- Dixon & Landau (2025) - Baseline paper for our analysis
- EPT metrics reference - Operational definitions

---

## 📞 Support & Citation

### How to Cite This Tool

```bibtex
@software{integrity_filter_2025,
  author = {Lerer, Ignacio Adrián},
  title = {Integrity Filter for AI-Assisted Research},
  year = {2025},
  note = {Based on Miyai et al. (2025) Jr. AI Scientist Risk Framework},
  url = {https://github.com/adrianlerer/FROM-UTOPIANISM-TO-FOSSILIZATION}
}
```

### Questions?

- Check `example_with_integrity_filter.py` for working code
- Run `python3 integrity_filter.py` for test suite
- Review generated reports in `../OUTPUTS/`

---

**Last Updated**: November 2025  
**Framework**: Miyai et al. (2025) arXiv:2511.04583  
**License**: MIT (same as repo)
