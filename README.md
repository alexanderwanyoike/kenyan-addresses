# Kenyan Addresses

Based on a recent project I needed lots of test data
and there were no really good solutions out there to get good kenyan addresses
therefore, I wrote a script that does this. It scrapes businesslist.co.ke 
for the company name and its corresponding address. So far it has 
defined set of cities it gets its data from but that can be changed
based on the categories cities.

## Prerequisites

- Python 3
- PIP 
- Virtual env


## Installation

Clone the project. once cloned you can run the following on the 
cloned directory 
```bash
python3 -m venv [cloned-directory]
```

Enter the cloned directory and install the required dependencies.
```bash
 pip install -r requirements.txt
```

Once installed you can then run the main script `main.py`

```bash
python main.py
```
