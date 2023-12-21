import xml.etree.ElementTree as xml


def indent(elem, level=0):
    indent_size = "  "
    i = "\n" + level * indent_size
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + indent_size
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def add_actions(data):
    actions = xml.SubElement(data, "actions")
    ojppmad = xml.SubElement(actions, "org.jenkinsci.plagins.pipeline.modeldefinition.actions.DeclarativeJobAction")
    ojppmad.set("plugin", "pipeline-model-definition@2.2151.ve32c9d209a_3f")
    ojppmadjpt = xml.SubElement(actions,
                                "org.jenkinsci.plagins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction")
    ojppmadjpt.set("plugin", "pipeline-model-definition@2.2151.ve32c9d209a_3f")
    xml.SubElement(ojppmadjpt, "jobProperties")
    xml.SubElement(ojppmadjpt, "triggers")
    xml.SubElement(ojppmadjpt, "parameters")
    xml.SubElement(ojppmadjpt, "options")


def add_properties(data):
    proparties = xml.SubElement(data, "proparties")
    hmpdp = xml.SubElement(proparties, "hudson.model.ParametersDefinitionProperty")
    pd = xml.SubElement(hmpdp, "parameterDefinitions")
    hmspd = xml.SubElement(pd, "hudson.model.StringParameterDefinition")
    name1 = xml.SubElement(hmspd, "name")
    name1.text = "name"
    defaultvalue = xml.SubElement(hmspd, "defaultValue")
    defaultvalue.text = "ilayda"
    trim = xml.SubElement(hmspd, "trim")
    trim.text = "true"


def add_definition(data):
    definition = xml.SubElement(data, "definition")
    definition.set("class", "org.jenkinsci.plugins.workflow.cpc.CpsFlowDefinition")
    definition.set("plugin", "workflow-cps@3806.va_3a_6988277b_2")
    script = xml.SubElement(definition, "script")
    script.text = "pipeline { agent any stages { stage(&apos;Hello&apos;) { steps { echo &apos;Hello World&apos;  } } } }"
    sandbox = xml.SubElement(definition, "sandbox")
    sandbox.text = "true"


def ornek():
    data = xml.Element("flow-definition")
    data.set("plugin", "workflow-job@1360.vc6700e3136f5")
    add_actions(data)
    description = xml.SubElement(data, "description")
    description.text = "Ilayda Ornek"
    keepdependencies = xml.SubElement(data, "keepDependencies")
    keepdependencies.text = "false"
    add_properties(data)
    add_definition(data)
    xml.SubElement(data, "triggers")
    disabled = xml.SubElement(data, "disabled")
    disabled.text = "false"
    indent(data)
    b_xml = xml.tostring(data, encoding="unicode")
    print(b_xml)
    return b_xml

def write_file(xml):
    file = open("config-ornek.xml", "w")
    file.write(xml)

xml = ornek()
write_file(xml)

