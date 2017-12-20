# XML External entities

# Typically parsing XML files is done by using external gems like Nokogiri. In Nokogiri using external entities
# is turned off by default. Always check it in the documentation. If you want to be sure - turn off parsing external
# entities explicitly.

# Example of turning off parsing external entities in Nokogiri gem
require 'nokogiri'
xml = '<!DOCTYPE root [ <!ENTITY ent SYSTEM \"file:///etc/passwd\"> ]>\n<root><e>&ent;</e></root>'
parsed_xml = Nokogiri::XML.parse(xml) { |config| config.nonet } # "nonet" stands for No External Entities

# parsed_xml.children.children.children.text should return now empty string
