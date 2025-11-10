#!/usr/bin/env python3
"""
Figure 2: Constitutional Fitness (CF) Trajectories Over Time
Tracks CF evolution for Colombia (1991-2025) vs Argentina (1949-2025)

Author: Ignacio Adrián Lerer
Date: November 2025
License: CC-BY 4.0
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def load_colombia_trajectory():
    """Load Colombia CF trajectory from CSV."""
    df = pd.read_csv('../DATA/analysis_results/colombia_constitutional_fitness.csv')
    return df['Year'].values, df['CF'].values

def load_argentina_trajectory():
    """Load Argentina CF trajectory from CSV."""
    df = pd.read_csv('../DATA/analysis_results/argentina_cf_trajectory.csv')
    return df['Year'].values, df['CF'].values

def generate_cf_trajectories():
    """
    Generate line chart showing CF evolution over time.
    
    Data Sources:
    - Colombia: author calculations based on Constitutional Court data [Estimación]
    - Argentina: author calculations based on CSJN cases + reform attempts [Estimación]
    """
    
    # Load data
    col_years, col_cf = load_colombia_trajectory()
    arg_years, arg_cf = load_argentina_trajectory()
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Plot trajectories
    ax.plot(col_years, col_cf, marker='o', linewidth=3, markersize=8, 
            color='#2ecc71', label='Colombia 1991 (Transformative)', linestyle='-')
    ax.plot(arg_years, arg_cf, marker='s', linewidth=3, markersize=8,
            color='#95a5a6', label='Argentina 1949 (Fossilized)', linestyle='--')
    
    # Threshold lines
    ax.axhline(y=0.70, color='green', linestyle=':', linewidth=2, 
               label='Transformative Threshold (CF > 0.70)', alpha=0.7)
    ax.axhline(y=0.20, color='red', linestyle=':', linewidth=2,
               label='Utopian Failure Threshold (CF < 0.20)', alpha=0.7)
    
    # Annotations for key events
    # Colombia peak (2005)
    peak_year_col = col_years[np.argmax(col_cf)]
    peak_cf_col = np.max(col_cf)
    ax.annotate(f'Peak: {peak_cf_col:.3f}\n(2005)',
                xy=(peak_year_col, peak_cf_col), xytext=(peak_year_col-5, peak_cf_col+0.05),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=10, fontweight='bold', color='green')
    
    # Argentina start
    ax.annotate(f'Art. 14bis\nAdoption\n({arg_years[0]})',
                xy=(arg_years[0], arg_cf[0]), xytext=(arg_years[0]+5, arg_cf[0]+0.08),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2),
                fontsize=10, fontweight='bold', color='gray')
    
    # Argentina end (fossilization)
    ax.annotate(f'Fossilized\n{arg_cf[-1]:.3f}\n({arg_years[-1]})',
                xy=(arg_years[-1], arg_cf[-1]), xytext=(arg_years[-1]-10, arg_cf[-1]+0.05),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=10, fontweight='bold', color='red')
    
    # Formatting
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Constitutional Fitness (CF)', fontsize=12, fontweight='bold')
    ax.set_title('Figure 2: Constitutional Fitness Trajectories Over Time\n' +
                 'Transformative Success (Colombia) vs Fossilized Utopianism (Argentina)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(-0.05, 1.05)
    ax.legend(loc='right', fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3, linestyle=':')
    
    # Add interpretation box
    textstr = 'Key Insights:\n' \
              '• Colombia: CF stable ~0.90 over 34 years (transformation succeeded)\n' \
              '• Argentina: CF decline 0.16 → 0.01 over 76 years (-93.1%)\n' \
              '• Colombia\'s high CF sustained despite gradual CLI increase\n' \
              '• Argentina trapped: cannot advance (implement) OR retreat (repeal)\n' \
              '• Fossilization = persistent utopianism + lock-in accumulation'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
    ax.text(0.02, 0.40, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)
    
    # Summary statistics box
    stats_text = f'Summary Statistics:\n' \
                 f'Colombia (1991-2025):\n' \
                 f'  Mean CF: {np.mean(col_cf):.3f}\n' \
                 f'  Std: {np.std(col_cf):.3f}\n' \
                 f'  Min: {np.min(col_cf):.3f}\n' \
                 f'  Max: {np.max(col_cf):.3f}\n\n' \
                 f'Argentina (1949-2025):\n' \
                 f'  Mean CF: {np.mean(arg_cf):.3f}\n' \
                 f'  Std: {np.std(arg_cf):.3f}\n' \
                 f'  Decline: {((arg_cf[-1]/arg_cf[0]-1)*100):.1f}%'
    props2 = dict(boxstyle='round', facecolor='lightblue', alpha=0.3)
    ax.text(0.98, 0.98, stats_text, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', horizontalalignment='right', bbox=props2)
    
    plt.tight_layout()
    
    # Save figure
    output_path = '../OUTPUTS/figure2_cf_trajectories.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Figure 2 saved to: {output_path}")
    print(f"   Colombia CF range: {np.min(col_cf):.3f} - {np.max(col_cf):.3f}")
    print(f"   Argentina CF decline: {arg_cf[0]:.3f} → {arg_cf[-1]:.3f} ({((arg_cf[-1]/arg_cf[0]-1)*100):.1f}%)")
    
    # PDF version
    pdf_path = '../OUTPUTS/figure2_cf_trajectories.pdf'
    plt.savefig(pdf_path, format='pdf', bbox_inches='tight')
    print(f"✅ PDF version saved to: {pdf_path}")
    
    plt.close()

if __name__ == "__main__":
    print("Generating Figure 2: CF Trajectories...")
    generate_cf_trajectories()
    print("Done!")
