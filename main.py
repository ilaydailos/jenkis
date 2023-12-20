import xml.etree.ElementTree as BULUT

def indent(elem, level=0):
    indent_size= " "
    i="\n" + level * indent_size
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text= i + indent_size
        if not elem.tail or not elem.tail.strip():
            elem.tail= i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail= i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail=i
def print_blt():
    data = BULUT.Element("Bilgilerim")
    kedim1 = BULUT.SubElement(data,"kedim")
    kedim1.set("cinsi", "british")
    kedim1.text = "BIDIK"
    ismim = BULUT.SubElement(data, "ismim")
    ismim.set("cinsiyeti" , "kadin")
    ismim.text = "ilayda"
    okulum = BULUT.SubElement(data , "okulum")
    okulum.set("tipi" , "universite")
    okulum.text = "Aksaray Universitesi"
    indent(data)
    b_xml = BULUT.tostring(data, encoding="unicode")
    print(b_xml)






print_blt()