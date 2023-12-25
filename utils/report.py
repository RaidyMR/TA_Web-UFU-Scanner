from rich.console import Console
from rich.theme import Theme
from rich.table import Table

def show_file_upload_urls(file_upload_urls):
    console = Console()
    console.print("File Upload URLs \n", style="bold underline")

    table = Table(show_header=True, header_style="bold")
    table.add_column("URL")

    for file_upload_url in file_upload_urls:
        table.add_row(file_upload_url)

    console.print(table)
    console.print("\n\n")

def show_report(test_report, url_lists):
    custom_theme = Theme({
        "vulnerable": "bold red",
        "not vulnerable": "bold green",

        "high": "bold red",
        "medium": "bold yellow",
        "low": "bold green",
    })

    console = Console(theme=custom_theme)
    console.print("Vulnerability Report \n", style="bold underline")

    for i in range(len(test_report)):
        table = Table(
            title=url_lists[i],
            show_header=True, 
            header_style="bold",
        )
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Score/Severity")
        table.add_column("Status")

        score = 0
        for j in range(len(test_report[i])):
            table.add_row(
                test_report[i][j].get('ID'),
                test_report[i][j].get('Name'),
                test_report[i][j].get('Score') + "/" + test_report[i][j].get('Severity'),
                test_report[i][j].get('Status'),
                style="vulnerable" if test_report[i][j].get('Status') == "Vulnerable" else "not vulnerable"
            )
            if(test_report[i][j].get('Status') == "Vulnerable"):
                score += float(test_report[i][j].get('Score'))*10

        
        console.print(table,
            "Vulnerability Score: ", 
            score/len(test_report[i] * 10),
            style="bold",
        )
        console.print("\n")