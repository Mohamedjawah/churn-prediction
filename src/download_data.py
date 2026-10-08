from pathlib import Path
import urllib.request

URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

out = Path(__file__).resolve().parents[1] / "data" / "raw" / "churn.csv"
out.parent.mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(URL, out)
print(f"Saved to {out}")