# Inventory Report 📝

## Project Context 💡
This project is a report generator that receives input files path containing stock data and outputs a report about those data in a simple or complete format. Supported files type: CSV, JSON, XML.

### Acquired Knowledge 📖
In this project, I was able to:
- Apply Oriented Objects Programming concepts in Python;
- Apply design patterns;
- Reading and writing files (XML, CSV, JSON).

## Main Technologies 🧰
<table>
    <thead>
        <tr>
            <th>Python</th>
            <th>Pytest</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">
               <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" 
                       alt="python" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
            <td align="center">
                <a href="https://docs.pytest.org/en/7.3.x/" target="_blank" rel="noreferrer"> 
                   <img 
                       src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/200px-Pytest_logo.svg.png" 
                       alt="pytest" 
                       width="40" 
                       height="40"
                    /> 
                </a>
            </td>
        </tr>
    </tbody>
</table>

## Running the application ⚙️

1. Clone the repository and enter it
```
git clone git@github.com:ImVictorM/Inventory-Report.git && cd Inventory-Report
```
2. Create the virtual environment
```
python3 -m venv .venv && source .venv/bin/activate
```
3. Install the dependencies
```
python3 -m pip install -r dev-requirements.txt
```
4. Install the main package
```
pip install .
```
5. Choose the report type you want

- report types: `simples` or `completo`
```
inventory_report {file_path} {report_type}
```
Example:
```
inventory_report inventory_report/data/inventory.csv simples
```

## Testing 🛠️
To run all tests:
```
python3 -m pytest
```
Running only one test file:
```
python3 -m pytest {test_file_path}.py
```
Test using docker-compose:
```
docker-compose run --rm inventory pytest
```
