#!/usr/bin/env python3
"""
Calculate non-dimensional wall quantities from OpenFOAM profile data.

This script calculates:
  - Y+ (non-dimensional wall distance): y * u_tau / nu
  - u+ (non-dimensional velocity): U / u_tau
  - Cf (skin friction coefficient): tau_w / (0.5 * rho * U_ref^2)

where:
  - y: distance from wall
  - u_tau: friction velocity = sqrt(|tau_w| / rho)
  - nu: kinematic viscosity
  - U: local velocity
  - tau_w: wall shear stress
  - rho: density
  - U_ref: reference velocity (at edge of boundary layer)
"""

import numpy as np
import pandas as pd
import argparse
import sys
from pathlib import Path


def read_profile_data(filepath):
    """Read OpenFOAM profile data from .xy file."""
    # Skip the header comment line starting with #
    data = pd.read_csv(filepath, delim_whitespace=True, comment='#', header=None)
    
    # Column names: distance, U_x, U_y, U_z, p, wallShearStress_x, wallShearStress_y, wallShearStress_z, yPlus
    column_names = ['distance', 'U_x', 'U_y', 'U_z', 'p', 'tau_x', 'tau_y', 'tau_z', 'yPlus_original']
    
    if len(data.columns) >= 9:
        data.columns = column_names[:len(data.columns)]
    
    return data


def calculate_wall_quantities(data, nu, rho, U_ref=None):
    """
    Calculate Y+, u+, and Cf from profile data.
    
    Parameters:
    -----------
    data : DataFrame
        Profile data with columns for velocity and wall shear stress
    nu : float
        Kinematic viscosity [m^2/s]
    rho : float
        Fluid density [kg/m^3]
    U_ref : float, optional
        Reference velocity for Cf calculation [m/s]
        If None, uses maximum U_x value from the profile
    
    Returns:
    --------
    DataFrame
        Original data plus calculated quantities
    """
    
    # Use maximum velocity as reference if not provided
    if U_ref is None:
        U_ref = data['U_x'].max()
        print(f"Reference velocity (U_ref) not provided. Using maximum U_x = {U_ref:.6f} m/s")
    
    # Calculate magnitude of velocity
    data['U_mag'] = np.sqrt(data['U_x']**2 + data['U_y']**2 + data['U_z']**2)
    
    # Calculate magnitude of wall shear stress
    data['tau_mag'] = np.sqrt(data['tau_x']**2 + data['tau_y']**2 + data['tau_z']**2)
    
    # Friction velocity: u_tau = sqrt(|tau_w| / rho)
    # Get wall shear stress (at wall, typically last point)
    tau_wall = data['tau_mag'].iloc[-1]
    u_tau = np.sqrt(abs(tau_wall) / rho)
    
    print(f"Wall shear stress magnitude: {tau_wall:.6e} Pa")
    print(f"Friction velocity (u_tau): {u_tau:.6e} m/s")
    
    # Calculate dimensionless quantities
    # Y+ = y * u_tau / nu
    # Here, 'distance' is interpreted as y (wall normal distance)
    data['Y+'] = data['distance'] * u_tau / nu
    
    # u+ = U / u_tau
    data['u+'] = data['U_mag'] / u_tau
    
    # Cf = tau_w / (0.5 * rho * U_ref^2)
    # Use local shear stress for local Cf
    data['Cf'] = data['tau_mag'] / (0.5 * rho * U_ref**2)
    
    # Store parameters used
    data.attrs['nu'] = nu
    data.attrs['rho'] = rho
    data.attrs['U_ref'] = U_ref
    data.attrs['u_tau'] = u_tau
    data.attrs['tau_wall'] = tau_wall
    
    return data


def save_results(data, output_file):
    """Save results to CSV file."""
    # Select columns to save
    cols_to_save = ['distance', 'U_x', 'U_y', 'U_z', 'U_mag', 'tau_mag', 'p', 
                    'Y+', 'u+', 'Cf', 'yPlus_original']
    
    # Only save columns that exist
    cols_to_save = [col for col in cols_to_save if col in data.columns]
    
    output_data = data[cols_to_save]
    
    # Create header with parameters
    header_lines = [
        "# Non-dimensional wall quantities calculated from OpenFOAM profile data",
        f"# Kinematic viscosity (nu): {data.attrs['nu']} m^2/s",
        f"# Density (rho): {data.attrs['rho']} kg/m^3",
        f"# Reference velocity (U_ref): {data.attrs['U_ref']} m/s",
        f"# Friction velocity (u_tau): {data.attrs['u_tau']} m/s",
        f"# Wall shear stress magnitude: {data.attrs['tau_wall']} Pa",
        "#",
        "# Columns: " + " | ".join(cols_to_save)
    ]
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(header_lines) + '\n')
    
    # Append data
    output_data.to_csv(output_file, mode='a', sep='\t', index=False, 
                       header=False, float_format='%.12e')
    
    print(f"\nResults saved to: {output_file}")


def print_summary(data):
    """Print summary of calculated quantities."""
    print("\n" + "="*70)
    print("Summary of Non-dimensional Wall Quantities")
    print("="*70)
    print(f"{'Parameter':<30} {'Min':<15} {'Max':<15} {'Mean':<15}")
    print("-"*70)
    print(f"{'Y+ (non-dim. wall dist.)':<30} {data['Y+'].min():<15.6e} {data['Y+'].max():<15.6e} {data['Y+'].mean():<15.6e}")
    print(f"{'u+ (non-dim. velocity)':<30} {data['u+'].min():<15.6e} {data['u+'].max():<15.6e} {data['u+'].mean():<15.6e}")
    print(f"{'Cf (skin friction coeff.)':<30} {data['Cf'].min():<15.6e} {data['Cf'].max():<15.6e} {data['Cf'].mean():<15.6e}")
    print("-"*70)
    print(f"{'Distance (y)':<30} {data['distance'].min():<15.6e} {data['distance'].max():<15.6e}")
    print(f"{'Velocity magnitude (U)':<30} {data['U_mag'].min():<15.6e} {data['U_mag'].max():<15.6e}")
    print(f"{'Wall shear stress (tau)':<30} {data['tau_mag'].min():<15.6e} {data['tau_mag'].max():<15.6e}")
    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Calculate non-dimensional wall quantities from OpenFOAM profile data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with default parameters
  python3 calculate_dimensionless_quantities.py profile0.xy
  
  # Specify all parameters
  python3 calculate_dimensionless_quantities.py profile0.xy -nu 2e-3 -rho 1.0 -U_ref 2.0
  
  # Save results to custom output file
  python3 calculate_dimensionless_quantities.py profile0.xy -o results.txt
        """
    )
    
    parser.add_argument('input_file', 
                       help='Input profile data file (.xy format)')
    parser.add_argument('-nu', '--kinematic-viscosity', type=float, default=2e-3,
                       help='Kinematic viscosity [m^2/s] (default: 2e-3)')
    parser.add_argument('-rho', '--density', type=float, default=1.0,
                       help='Fluid density [kg/m^3] (default: 1.0)')
    parser.add_argument('-U_ref', '--reference-velocity', type=float, default=None,
                       help='Reference velocity [m/s] for Cf calculation (default: max velocity in profile)')
    parser.add_argument('-o', '--output', type=str, default=None,
                       help='Output file name (default: input_file_with_suffix)')
    
    args = parser.parse_args()
    
    # Check if input file exists
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{args.input_file}' not found")
        sys.exit(1)
    
    print(f"Reading profile data from: {args.input_file}")
    print(f"Parameters: nu={args.kinematic_viscosity} m^2/s, rho={args.density} kg/m^3")
    
    # Read data
    data = read_profile_data(args.input_file)
    print(f"Data loaded: {len(data)} points")
    
    # Calculate quantities
    data = calculate_wall_quantities(data, args.kinematic_viscosity, args.density, args.reference_velocity)
    
    # Print summary
    print_summary(data)
    
    # Save results
    if args.output is None:
        stem = input_path.stem
        args.output = f"{stem}_analysis.txt"
    
    save_results(data, args.output)
    
    # Print sample of results
    print("Sample of results (first 5 and last 5 rows):")
    print(data[['distance', 'U_x', 'Y+', 'u+', 'Cf']].head())
    print("...")
    print(data[['distance', 'U_x', 'Y+', 'u+', 'Cf']].tail())


if __name__ == '__main__':
    main()
