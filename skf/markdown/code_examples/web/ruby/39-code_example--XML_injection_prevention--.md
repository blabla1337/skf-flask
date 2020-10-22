# XML Injection Prevention
-------

## Example:


    // Whenever you are using XML parsers you must sanitize or encode all userinput before
    // including this input into your XML file.

    // Some methods like below, the Dom document already encodes the input before storing it
    // into the XML. But beware, since this encoded input is still a threat whenever you are
    // displaying the this data on screen as HTML output. This encoded data should be escaped
    // at all times before displaying.

    // Whenever your XML function does not encode your data on the fly, you may want to write
    // your own function for achieving this. See the code examples and search for "Input encoding"
    // for more detailed information.

    require 'nokogiri'

    xml_doc = Nokogiri::XML('<employees><employee><name></name></employee></employees>')

    xml_doc.css('employees employee name').first.content = params[:name]

    // In Nokogiri gem HTML Encoding is done by default. Printing xml_doc.to_xml should return
    // => "<?xml version=\"1.0\"?>\n<employees>\n  <employee>\n    <name>&lt;script&gt;alert(\"1\")&lt;/script&gt;</name>\n  </employee>\n</employees>\n"

    // Always check if user input is properly encoded, because displaying XML may lead to multiple vulnerabilities, for instance - XSS.
