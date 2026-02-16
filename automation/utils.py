from datetime import datetime
from pathlib import Path

def save_screenshot(driver, test_name: str) -> str:
    screenshots_dir = Path(__file__).parent / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{test_name}_{timestamp}.png"
    path = screenshots_dir / filename

    driver.save_screenshot(str(path))
    return str(path)
