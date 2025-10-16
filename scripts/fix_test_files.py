"""
Script to fix test files and add proper screenshot support.
"""
import os
import re
from pathlib import Path


def fix_test_file(file_path):
    """Fix a single test file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix common issues
        content = fix_imports(content)
        content = fix_method_signatures(content)
        content = fix_try_except_blocks(content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Fixed: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False


def fix_imports(content):
    """Fix import statements."""
    # Remove duplicate imports
    lines = content.split('\n')
    unique_imports = []
    seen_imports = set()
    
    for line in lines:
        if line.strip().startswith('from ') or line.strip().startswith('import '):
            if line.strip() not in seen_imports:
                unique_imports.append(line)
                seen_imports.add(line.strip())
        else:
            unique_imports.append(line)
    
    return '\n'.join(unique_imports)


def fix_method_signatures(content):
    """Fix method signatures to include proper parameters."""
    # Fix UI test methods
    ui_methods = re.findall(r'def (test_\w+)\(self\):', content)
    for method in ui_methods:
        if 'ui' in content:
            # Add proper parameters for UI tests
            old_signature = f'def {method}(self):'
            new_signature = f'def {method}(self, driver, home_page, login_page, signup_page, account_info_page, products_page, cart_page, checkout_page, contact_page, test_data):'
            content = content.replace(old_signature, new_signature)
    
    # Fix API test methods
    api_methods = re.findall(r'def (test_\w+)\(self\):', content)
    for method in api_methods:
        if 'api' in content:
            # API tests don't need additional parameters
            pass
    
    return content


def fix_try_except_blocks(content):
    """Fix try/except blocks in test methods."""
    # Find test methods and add proper try/except
    test_methods = re.findall(r'def (test_\w+)\(.*?\):', content)
    
    for method in test_methods:
        # Check if method already has proper try/except
        method_pattern = rf'def {method}\(.*?\):.*?(?=\n    def|\nclass|\Z)'
        method_match = re.search(method_pattern, content, re.DOTALL)
        
        if method_match:
            method_content = method_match.group(0)
            
            # Check if it needs fixing
            if 'try:' in method_content and 'except AssertionError' in method_content:
                continue  # Already properly formatted
            
            # Fix the method
            if 'try:' in method_content:
                # Method has try but needs proper except blocks
                content = fix_existing_try_block(content, method)
            else:
                # Method needs try/except added
                content = add_try_except_to_method(content, method)
    
    return content


def fix_existing_try_block(content, method_name):
    """Fix existing try blocks."""
    # This is a simplified fix - in practice, you'd need more sophisticated parsing
    return content


def add_try_except_to_method(content, method_name):
    """Add try/except to a method."""
    # Find the method
    method_pattern = rf'def {method_name}\(.*?\):.*?(?=\n    def|\nclass|\Z)'
    method_match = re.search(method_pattern, content, re.DOTALL)
    
    if not method_match:
        return content
    
    method_content = method_match.group(0)
    
    # Check if it already has try/except
    if 'try:' in method_content:
        return content
    
    # Add try/except
    lines = method_content.split('\n')
    new_lines = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('"""') and i > 0:
            # Found the docstring end, add try after it
            new_lines.append(line)
            new_lines.append('        try:')
        elif line.strip() and not line.strip().startswith('def ') and not line.strip().startswith('"""'):
            # This is a test step, indent it
            new_lines.append('            ' + line.strip())
        else:
            new_lines.append(line)
    
    # Add except blocks at the end
    new_lines.append('        except AssertionError as e:')
    new_lines.append(f'            logger.error(f"Assertion failed in {method_name}: {{e}}")')
    new_lines.append('            raise e')
    new_lines.append('        except Exception as e:')
    new_lines.append(f'            logger.error(f"Test failed with error in {method_name}: {{e}}")')
    new_lines.append('            raise e')
    
    new_method_content = '\n'.join(new_lines)
    content = content.replace(method_content, new_method_content)
    
    return content


def main():
    """Main function to fix all test files."""
    test_dirs = ['tests/api', 'tests/ui']
    fixed_files = 0
    total_files = 0
    
    for test_dir in test_dirs:
        if os.path.exists(test_dir):
            for file_path in Path(test_dir).glob('test_*.py'):
                total_files += 1
                if fix_test_file(file_path):
                    fixed_files += 1
    
    print(f"\n📊 Summary:")
    print(f"Total files processed: {total_files}")
    print(f"Successfully fixed: {fixed_files}")
    print(f"Failed to fix: {total_files - fixed_files}")


if __name__ == "__main__":
    main()
