"""
Script to add comprehensive screenshot support to all test files.
"""
import os
import re
from pathlib import Path


def add_screenshot_imports(content):
    """Add screenshot-related imports to test files."""
    imports_to_add = [
        "from utils.screenshot_utils import ScreenshotManager, screenshot_on_failure",
        "from utils.logger import logger"
    ]
    
    # Check if imports already exist
    for import_line in imports_to_add:
        if import_line not in content:
            # Find the last import statement
            import_pattern = r'^from .*$|^import .*$'
            lines = content.split('\n')
            last_import_index = -1
            
            for i, line in enumerate(lines):
                if re.match(import_pattern, line.strip()):
                    last_import_index = i
            
            if last_import_index >= 0:
                lines.insert(last_import_index + 1, import_line)
                content = '\n'.join(lines)
    
    return content


def add_screenshot_to_test_method(content, method_name):
    """Add screenshot handling to a test method."""
    # Find the test method
    method_pattern = rf'def {method_name}\(.*?\):'
    method_match = re.search(method_pattern, content, re.DOTALL)
    
    if not method_match:
        return content
    
    method_start = method_match.start()
    method_end = method_match.end()
    
    # Get the method content
    method_content = content[method_start:method_end]
    
    # Check if try/except already exists
    if 'try:' in method_content:
        return content
    
    # Find the method body
    body_pattern = rf'def {method_name}\(.*?\):\s*(.*?)(?=\n    def|\nclass|\Z)'
    body_match = re.search(body_pattern, content, re.DOTALL)
    
    if not body_match:
        return content
    
    method_body = body_match.group(1)
    indented_body = method_body
    
    # Create new method with try/except
    new_method = f"""def {method_name}(self):
        \"\"\"Test method with screenshot support.\"\"\"
        try:
{indented_body}
        except AssertionError as e:
            logger.error(f"Assertion failed in {method_name}: {{e}}")
            raise e
        except Exception as e:
            logger.error(f"Test failed with error in {method_name}: {{e}}")
            raise e"""
    
    # Replace the method
    content = content.replace(method_content, new_method)
    
    return content


def add_screenshot_to_ui_test(content):
    """Add screenshot support to UI test methods."""
    # Find all test methods
    test_methods = re.findall(r'def (test_\w+)\(', content)
    
    for method_name in test_methods:
        # Check if method already has try/except
        method_pattern = rf'def {method_name}\(.*?\):.*?(?=\n    def|\nclass|\Z)'
        method_match = re.search(method_pattern, content, re.DOTALL)
        
        if method_match and 'try:' not in method_match.group(0):
            content = add_screenshot_to_test_method(content, method_name)
    
    return content


def add_screenshot_to_api_test(content):
    """Add screenshot support to API test methods."""
    # Find all test methods
    test_methods = re.findall(r'def (test_\w+)\(', content)
    
    for method_name in test_methods:
        # Check if method already has try/except
        method_pattern = rf'def {method_name}\(.*?\):.*?(?=\n    def|\nclass|\Z)'
        method_match = re.search(method_pattern, content, re.DOTALL)
        
        if method_match and 'try:' not in method_match.group(0):
            content = add_screenshot_to_test_method(content, method_name)
    
    return content


def process_test_file(file_path):
    """Process a single test file to add screenshot support."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add imports
        content = add_screenshot_imports(content)
        
        # Add screenshot support based on file type
        if 'api' in str(file_path):
            content = add_screenshot_to_api_test(content)
        elif 'ui' in str(file_path):
            content = add_screenshot_to_ui_test(content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False


def main():
    """Main function to process all test files."""
    test_dirs = ['tests/api', 'tests/ui']
    updated_files = 0
    total_files = 0
    
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            for file_path in Path(test_dir).glob('test_*.py'):
                total_files += 1
                if process_test_file(file_path):
                    updated_files += 1
    
    print(f"\n📊 Summary:")
    print(f"Total files processed: {total_files}")
    print(f"Successfully updated: {updated_files}")
    print(f"Failed to update: {total_files - updated_files}")


if __name__ == "__main__":
    main()
