from vulnerability_gap.vg1 import VG1_NoFilter
from vulnerability_gap.vg2 import VG2_XSS
from vulnerability_gap.vg3 import VG3_InsertHTMLtoPNG
from vulnerability_gap.vg4 import VG4_IncreaseSize
from vulnerability_gap.vg5 import VG5_ContentType
from vulnerability_gap.vg6 import VG6_FileExtension
from vulnerability_gap.vg7 import VG7_AddingResourceHeader
from vulnerability_gap.vg8 import VG8_ConvertHTMLtoEML
from vulnerability_gap.vg9 import VG9_ConvertingHTMLtoSVG
from vulnerability_gap.vg10 import VG10_HTMLComment

def upload_modified_requests(url):
    report_dict = []

    report_dict.append(VG1_NoFilter.execute(url))
    report_dict.append(VG2_XSS.execute(url))
    report_dict.append(VG3_InsertHTMLtoPNG.execute(url))
    report_dict.append(VG4_IncreaseSize.execute(url))
    report_dict.append(VG5_ContentType.execute(url))
    report_dict.append(VG6_FileExtension.execute(url))
    report_dict.append(VG7_AddingResourceHeader.execute(url))
    report_dict.append(VG8_ConvertHTMLtoEML.execute(url))
    report_dict.append(VG9_ConvertingHTMLtoSVG.execute(url))
    report_dict.append(VG10_HTMLComment.execute(url))

    # # remove modified files
    # modified_seed_path = "./resources/modified/C3_modified_seed.html"
    # os.remove(modified_seed_path)

    return report_dict