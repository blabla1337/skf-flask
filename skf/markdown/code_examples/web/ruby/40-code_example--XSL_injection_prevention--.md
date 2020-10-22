# XSL Injection prevention
-------

## Example:


    // In order to prevent XSL injections you must enforce strict policy's whenever the
    // files are loaded from a source controlled by an possible attacker.

    // Let's say for example that the user can choose from several XSL files on your application.

    // ABC.xsl arranges your employee names on alphabetical order
    // CBA.xsl does not care and just shows the input by order of your XML file.

    // Before we want to attach the XSL files to the style sheet we first want to
    // do validation on the request to make sure the included file was one of our own pre
    // defined files, example:
    // check_pattern(params[:xslfile], "file1.xsl,file2.xsl,etc")

    require 'nokogiri'

    // Include the classes of which you want to use objects from
    require_relative 'classes'

    class IncludeXSL
      def including(param, white_list)
        // check "Whitelisting" for method declaration
        if check_pattern(param, white_list)
          document = Nokogiri::XML(File.read('input.xml'))
          template = Nokogiri::XSLT(File.read('template.xslt'))

          transformed_document = template.transform(document)
        end
      end
    end
