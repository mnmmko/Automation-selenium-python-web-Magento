import os
import sys
from behave.__main__ import main as behave_main


if os.path.exists("reports"):
    import shutil
    shutil.rmtree("reports")
os.makedirs("reports", exist_ok=True)


args = [
    "--tags=@smoke",  # Run specific tags (or remove to run all)
    "--format", "pretty",
    "--format", "json.pretty",
    "--outfile", "reports/report.json",
    "--format", "html",
    "--outfile", "reports/report.html",
    "Features"
]

# Run Behave
if __name__ == "__main__":
    sys.exit(behave_main(args))
