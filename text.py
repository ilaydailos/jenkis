import xml.etree.ElementTree as pr1

def indent(elem, level=0):
    indent_size= "  "
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
def add_properties(data):
    properties = pr1.SubElement(data, "properties")
    parametersdproperty = pr1.SubElement(properties, "hudson.model.ParametersDefinitionProperty")
    parameterdefinitions = pr1.SubElement(parametersdproperty, "parameterDefinitions")
    stringparameterdefinition = pr1.SubElement(parameterdefinitions, "hudson.model.StringParameterDefinition")
    name = pr1.SubElement(stringparameterdefinition, "name")
    name.text = "isim"
    defaultvalue = pr1.SubElement(stringparameterdefinition, "defaultValue")
    defaultvalue.text = "Ilayda"
    trim = pr1.SubElement(stringparameterdefinition, "trim")
    trim.text = "false"
def add_scm(data):
    scm = pr1.SubElement(data, "scm")
    scm.set("class", "hudson.plugins.git.GitSCM")
    scm.set("plugin", "git@5.2.1")
    configversion = pr1.SubElement(scm, "configVersion")
    configversion.text = "2"
    userremoteconfigs = pr1.SubElement(scm, "userRemoteConfigs")
    hpguserremoteconfig = pr1.SubElement(userremoteconfigs, "hudson.plugins.git.UserRemoteConfig")
    url = pr1.SubElement(hpguserremoteconfig, "url")
    url.text = "https://github.com/ilaydailos/pokeapi.git"
    branches = pr1.SubElement(scm, "branches")
    branchspec = pr1.SubElement(branches, "hudson.plugins.git.BranchSpec")
    name1 = pr1.SubElement(branchspec, "name")
    name1.text = "*/main"
    dgsc = pr1.SubElement(scm, "doGenerateSubmoduleConfigurations")
    dgsc.text = "false"
    submodulecfg = pr1.SubElement(scm, "submoduleCfg")
    submodulecfg.set("class", "empty-list")
    pr1.SubElement(scm, "extensions")
def add_builders(data):
    builders = pr1.SubElement(data, "builders")
    hts = pr1.SubElement(builders, "hudson.tasks.Shell")
    command = pr1.SubElement(hts, "command")
    command.text = "ls && python3 main.py $id"
    pr1.SubElement(hts, "configuredLocalRules")


def print_project():
    data = pr1.Element("project")
    pr1.SubElement(data, "actions")
    description = pr1.SubElement(data , "description")
    description.text=" "
    keepDependencies = pr1.SubElement(data ,"keepDependencies")
    keepDependencies.text = "false"
    add_properties(data)
    add_scm(data)
    canroam = pr1.SubElement(data , "canRoam")
    canroam.text = "true"
    disabled = pr1.SubElement(data, "disabled")
    disabled.text = "false"
    bbwdb = pr1.SubElement(data, "blockBuildWhenDownstreamBuilding")
    bbwdb.text = "false"
    bbwub = pr1.SubElement(data, "blockBuildWhenUpstreamBuilding")
    bbwub.text = "false"
    pr1.SubElement(data , "triggers")
    concurrentbuild = pr1.SubElement(data, "concurrentBuild")
    concurrentbuild.text = "false"
    add_builders(data)
    pr1.SubElement(data , "publishers")
    pr1.SubElement(data , "buildWrappers")
    indent(data)
    b_xml = pr1.tostring(data, encoding="unicode")
    print(b_xml)
    return b_xml
def write_file(xml):
    file = open("config.xml", "w")
    file.write(xml)
xml = print_project()
write_file(xml)















