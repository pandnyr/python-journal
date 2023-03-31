from rich.console import Console
from rich.table import Table
import pandas as pd

table = Table(title="Trade Journal")
rows = [
    ["10.01.2002", "eurusd", "long", "1.09812", "1.09004", "0.2", "$200","5"],
    ["21.21.2002", "eurcad", "short"],
    ["12.05.2002", "usdjpy", "long"],
]
columns = ["Date", "Pair", "Bias","Open Price","Close Price","Lot","PNL","% Change"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style='bright_green')

console = Console()
console.print(table)

islem = input("işlem giriniz: ")
if islem == "1":
    
    pair = input("Pair giriniz : ")
    print(row.__add__(pair))
    console.print(table)