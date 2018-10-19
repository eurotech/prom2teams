import prom2teams.processor

def test_processor():

    with open("tests/test_processor/template.j2", 'r') as template_file:
        template = template_file.read()
    processor = prom2teams.processor.Processor(template, ["http://localhost:18080/"])

    with open("tests/test_processor/alert.json", 'r') as alert_file:
        alert = alert_file.read()

    processor.process(alert)
