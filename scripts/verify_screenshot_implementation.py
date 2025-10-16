"""
Script to verify screenshot implementation across all test files.
"""
import os
import re
from pathlib import Path


def check_screenshot_implementation(file_path):
    """Check if a test file has proper screenshot implementation."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = {
            'has_screenshot_imports': False,
            'has_try_except_blocks': False,
            'has_logger_usage': False,
            'has_screenshot_manager': False,
            'has_assertion_error_handling': False,
            'has_general_error_handling': False
        }
        
        # Check for screenshot imports
        if 'from utils.screenshot_utils import' in content:
            checks['has_screenshot_imports'] = True
        
        # Check for try/except blocks
        if 'try:' in content and 'except' in content:
            checks['has_try_except_blocks'] = True
        
        # Check for logger usage
        if 'logger.error' in content or 'logger.info' in content:
            checks['has_logger_usage'] = True
        
        # Check for ScreenshotManager usage
        if 'ScreenshotManager' in content:
            checks['has_screenshot_manager'] = True
        
        # Check for assertion error handling
        if 'except AssertionError' in content:
            checks['has_assertion_error_handling'] = True
        
        # Check for general error handling
        if 'except Exception' in content:
            checks['has_general_error_handling'] = True
        
        return checks
        
    except Exception as e:
        print(f"❌ Error checking {file_path}: {e}")
        return None


def main():
    """Main function to verify screenshot implementation."""
    test_dirs = ['tests/api', 'tests/ui']
    total_files = 0
    files_with_screenshots = 0
    files_without_screenshots = 0
    
    print("🔍 Checking Screenshot Implementation Across All Test Files\n")
    
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            print(f"📁 Checking {test_dir}:")
            
            for file_path in sorted(Path(test_dir).glob('test_*.py')):
                total_files += 1
                checks = check_screenshot_implementation(file_path)
                
                if checks:
                    # Count how many checks passed
                    passed_checks = sum(1 for check in checks.values() if check)
                    total_checks = len(checks)
                    
                    status = "✅" if passed_checks >= 4 else "⚠️" if passed_checks >= 2 else "❌"
                    
                    print(f"  {status} {file_path.name}: {passed_checks}/{total_checks} checks passed")
                    
                    if passed_checks >= 4:
                        files_with_screenshots += 1
                    else:
                        files_without_screenshots += 1
                        print(f"    Missing: {[k for k, v in checks.items() if not v]}")
                else:
                    files_without_screenshots += 1
                    print(f"  ❌ {file_path.name}: Error reading file")
    
    print(f"\n📊 Summary:")
    print(f"Total test files: {total_files}")
    print(f"Files with proper screenshot implementation: {files_with_screenshots}")
    print(f"Files needing screenshot implementation: {files_without_screenshots}")
    print(f"Coverage: {(files_with_screenshots/total_files)*100:.1f}%")
    
    if files_without_screenshots > 0:
        print(f"\n⚠️  {files_without_screenshots} files need screenshot implementation!")
    else:
        print(f"\n🎉 All {total_files} test files have proper screenshot implementation!")


if __name__ == "__main__":
    main()
