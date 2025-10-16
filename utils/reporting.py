"""
Reporting utilities for the AutomationExercise testing framework.
"""
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import allure
from allure_commons.types import AttachmentType
from config.config import REPORTS_DIR, ALLURE_RESULTS_DIR
from utils.logger import logger


class AllureReporter:
    """Allure reporting helper class."""
    
    def __init__(self):
        self.allure_results_dir = ALLURE_RESULTS_DIR
        self.allure_results_dir.mkdir(parents=True, exist_ok=True)
    
    def attach_screenshot(self, driver, name: str = "Screenshot"):
        """Attach screenshot to Allure report."""
        try:
            screenshot_path = driver.get_screenshot_as_png()
            allure.attach(
                screenshot_path,
                name=name,
                attachment_type=AttachmentType.PNG
            )
            logger.info(f"Screenshot attached to Allure report: {name}")
        except Exception as e:
            logger.error(f"Failed to attach screenshot: {e}")
    
    def attach_page_source(self, driver, name: str = "Page Source"):
        """Attach page source to Allure report."""
        try:
            page_source = driver.page_source
            allure.attach(
                page_source,
                name=name,
                attachment_type=AttachmentType.HTML
            )
            logger.info(f"Page source attached to Allure report: {name}")
        except Exception as e:
            logger.error(f"Failed to attach page source: {e}")
    
    def attach_text(self, content: str, name: str = "Text Content"):
        """Attach text content to Allure report."""
        try:
            allure.attach(
                content,
                name=name,
                attachment_type=AttachmentType.TEXT
            )
            logger.info(f"Text content attached to Allure report: {name}")
        except Exception as e:
            logger.error(f"Failed to attach text content: {e}")
    
    def attach_json(self, data: Dict[str, Any], name: str = "JSON Data"):
        """Attach JSON data to Allure report."""
        try:
            json_content = json.dumps(data, indent=2)
            allure.attach(
                json_content,
                name=name,
                attachment_type=AttachmentType.JSON
            )
            logger.info(f"JSON data attached to Allure report: {name}")
        except Exception as e:
            logger.error(f"Failed to attach JSON data: {e}")
    
    def add_step(self, step_name: str, step_description: str = ""):
        """Add a step to Allure report."""
        with allure.step(step_name):
            if step_description:
                logger.info(f"Allure step: {step_name} - {step_description}")
            else:
                logger.info(f"Allure step: {step_name}")


class TestReporter:
    """Test reporting helper class."""
    
    def __init__(self):
        self.reports_dir = REPORTS_DIR
        self.reports_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_test_summary(self, test_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate test execution summary."""
        total_tests = len(test_results)
        passed_tests = len([r for r in test_results if r.get('status') == 'passed'])
        failed_tests = len([r for r in test_results if r.get('status') == 'failed'])
        skipped_tests = len([r for r in test_results if r.get('status') == 'skipped'])
        
        summary = {
            'execution_time': datetime.now().isoformat(),
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': failed_tests,
            'skipped_tests': skipped_tests,
            'pass_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            'test_results': test_results
        }
        
        return summary
    
    def save_test_summary(self, summary: Dict[str, Any], filename: str = None):
        """Save test summary to JSON file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"test_summary_{timestamp}.json"
        
        file_path = self.reports_dir / filename
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            logger.info(f"Test summary saved: {file_path}")
        except Exception as e:
            logger.error(f"Failed to save test summary: {e}")
    
    def generate_failure_report(self, failed_tests: List[Dict[str, Any]]) -> str:
        """Generate failure report."""
        if not failed_tests:
            return "No test failures."
        
        report = "TEST FAILURE REPORT\n"
        report += "=" * 50 + "\n\n"
        
        for i, test in enumerate(failed_tests, 1):
            report += f"{i}. Test: {test.get('name', 'Unknown')}\n"
            report += f"   Status: {test.get('status', 'Unknown')}\n"
            report += f"   Error: {test.get('error', 'No error message')}\n"
            report += f"   Screenshot: {test.get('screenshot', 'No screenshot')}\n"
            report += "-" * 30 + "\n"
        
        return report
    
    def save_failure_report(self, failed_tests: List[Dict[str, Any]], filename: str = None):
        """Save failure report to text file."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"failure_report_{timestamp}.txt"
        
        file_path = self.reports_dir / filename
        report_content = self.generate_failure_report(failed_tests)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            logger.info(f"Failure report saved: {file_path}")
        except Exception as e:
            logger.error(f"Failed to save failure report: {e}")


class PerformanceReporter:
    """Performance reporting helper class."""
    
    def __init__(self):
        self.reports_dir = REPORTS_DIR
        self.reports_dir.mkdir(parents=True, exist_ok=True)
    
    def measure_page_load_time(self, driver, page_name: str) -> float:
        """Measure page load time."""
        try:
            # Get page load time from browser logs
            logs = driver.get_log('performance')
            for log in logs:
                if log['message']:
                    message = json.loads(log['message'])
                    if message['message']['method'] == 'Page.loadEventFired':
                        load_time = message['message']['params']['timestamp']
                        logger.info(f"Page load time for {page_name}: {load_time}ms")
                        return load_time
            return 0.0
        except Exception as e:
            logger.error(f"Failed to measure page load time: {e}")
            return 0.0
    
    def measure_api_response_time(self, response_time: float, api_name: str) -> None:
        """Log API response time."""
        logger.info(f"API response time for {api_name}: {response_time}ms")
        
        # Attach to Allure report
        allure.attach(
            f"API: {api_name}\nResponse Time: {response_time}ms",
            name=f"API Performance - {api_name}",
            attachment_type=AttachmentType.TEXT
        )
    
    def generate_performance_report(self, performance_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate performance report."""
        if not performance_data:
            return {}
        
        total_requests = len(performance_data)
        avg_response_time = sum(d.get('response_time', 0) for d in performance_data) / total_requests
        max_response_time = max(d.get('response_time', 0) for d in performance_data)
        min_response_time = min(d.get('response_time', 0) for d in performance_data)
        
        report = {
            'execution_time': datetime.now().isoformat(),
            'total_requests': total_requests,
            'average_response_time': avg_response_time,
            'max_response_time': max_response_time,
            'min_response_time': min_response_time,
            'performance_data': performance_data
        }
        
        return report
    
    def save_performance_report(self, performance_data: List[Dict[str, Any]], filename: str = None):
        """Save performance report."""
        report = self.generate_performance_report(performance_data)
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"performance_report_{timestamp}.json"
        
        file_path = self.reports_dir / filename
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            logger.info(f"Performance report saved: {file_path}")
        except Exception as e:
            logger.error(f"Failed to save performance report: {e}")


# Global reporter instances
allure_reporter = AllureReporter()
test_reporter = TestReporter()
performance_reporter = PerformanceReporter()
