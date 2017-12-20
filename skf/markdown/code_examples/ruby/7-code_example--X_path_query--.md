# X Path query

require 'nokogiri'

class XPathControl
  # Define the allowed characters and input parameter and count level for the
  # user lockout like:
  # call(params[:filename], "<'>&")

  def call(user, input_param, allowed_characters)
    encoder = Encoder.new
    encoded = encoder.encode(user, input_param, allowed_characters)

    if encoded
      doc = Nokogiri::XML(File.read('file.xml'))

      # Assuming that you used the encoder function also for adding users, it will now retrieve the
      # user O'reily from the query
      query_result = doc.xpath("//lemonade[@supplier=\"#{doc}\"]/price")
    end
  end
end
