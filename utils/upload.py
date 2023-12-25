from vulnerability_gap.c1 import C1_NoFilter
from vulnerability_gap.c2 import C2_XSS
from vulnerability_gap.c3 import C3_InsertHTMLtoPNG
from vulnerability_gap.c4 import C4_IncreaseSize
from vulnerability_gap.c5 import C5_ContentType
from vulnerability_gap.c6 import C6_FileExtension
from vulnerability_gap.c7 import C7_AddingResourceHeader
from vulnerability_gap.c8 import C8_ConvertHTMLtoEML
from vulnerability_gap.c9 import C9_ConvertingHTMLtoSVG
from vulnerability_gap.c10 import C10_HTMLComment

def upload_modified_requests(url):
    report_dict = []

    report_dict.append(C1_NoFilter.execute(url))
    report_dict.append(C2_XSS.execute(url))
    report_dict.append(C3_InsertHTMLtoPNG.execute(url))
    report_dict.append(C4_IncreaseSize.execute(url))
    report_dict.append(C5_ContentType.execute(url))
    report_dict.append(C6_FileExtension.execute(url))
    report_dict.append(C7_AddingResourceHeader.execute(url))
    report_dict.append(C8_ConvertHTMLtoEML.execute(url))
    report_dict.append(C9_ConvertingHTMLtoSVG.execute(url))
    report_dict.append(C10_HTMLComment.execute(url))

    # # remove modified files
    # modified_seed_path = "./resources/modified/C3_modified_seed.html"
    # os.remove(modified_seed_path)

    return report_dict