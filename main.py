from dotenv import load_dotenv


from utils.crawler import get_file_upload_urls
from utils.upload import upload_modified_requests
from utils.report import show_file_upload_urls, show_report

if __name__ == "__main__":
    load_dotenv()
    file_upload_urls = []
    test_report = []

    # http://localhost/user/file_upload_vuln-main/index.php
    main_url = input("Type url: ")
    get_file_upload_urls(main_url, file_upload_urls=file_upload_urls)

    show_file_upload_urls(file_upload_urls)

    for file_upload_url in file_upload_urls:
        test_report.append(upload_modified_requests(file_upload_url))

    show_report(test_report, file_upload_urls)