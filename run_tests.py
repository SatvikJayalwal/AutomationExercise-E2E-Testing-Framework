#!/usr/bin/env python3
"""
Test execution script for AutomationExercise testing framework.
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=False)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False


def main():
    """Main function to run tests."""
    parser = argparse.ArgumentParser(description='Run AutomationExercise tests')
    parser.add_argument('--type', choices=['all', 'api', 'ui', 'smoke', 'regression'], 
                       default='all', help='Type of tests to run')
    parser.add_argument('--browser', choices=['chrome', 'firefox', 'edge'], 
                       default='chrome', help='Browser to use')
    parser.add_argument('--headless', action='store_true', 
                       help='Run in headless mode')
    parser.add_argument('--parallel', type=int, default=1, 
                       help='Number of parallel workers')
    parser.add_argument('--report', action='store_true', 
                       help='Generate reports')
    parser.add_argument('--debug', action='store_true', 
                       help='Run in debug mode')
    
    args = parser.parse_args()
    
    # Set environment variables
    env_vars = {
        'BROWSER': args.browser,
        'HEADLESS': 'true' if args.headless else 'false',
        'DEBUG': 'true' if args.debug else 'false'
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
    
    # Build pytest command
    pytest_cmd = ['pytest']
    
    # Add markers based on type
    if args.type == 'api':
        pytest_cmd.extend(['-m', 'api'])
    elif args.type == 'ui':
        pytest_cmd.extend(['-m', 'ui'])
    elif args.type == 'smoke':
        pytest_cmd.extend(['-m', 'smoke'])
    elif args.type == 'regression':
        pytest_cmd.extend(['-m', 'regression'])
    
    # Add parallel execution
    if args.parallel > 1:
        pytest_cmd.extend(['-n', str(args.parallel)])
    
    # Add reporting options
    if args.report:
        pytest_cmd.extend([
            '--html=reports/report.html',
            '--self-contained-html',
            '--alluredir=reports/allure-results',
            '--junitxml=reports/junit.xml'
        ])
    
    # Add debug options
    if args.debug:
        pytest_cmd.extend(['-v', '-s', '--tb=long'])
    else:
        pytest_cmd.extend(['-v'])
    
    # Convert to string for subprocess
    command = ' '.join(pytest_cmd)
    
    # Run the tests
    success = run_command(command, f"Running {args.type} tests")
    
    if success and args.report:
        print("\n📊 Generating reports...")
        
        # Generate Allure report
        allure_cmd = "allure generate reports/allure-results -o reports/allure-report --clean"
        run_command(allure_cmd, "Generating Allure report")
        
        print("\n📁 Reports generated:")
        print("  - HTML Report: reports/report.html")
        print("  - Allure Report: reports/allure-report/index.html")
        print("  - JUnit XML: reports/junit.xml")
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())
