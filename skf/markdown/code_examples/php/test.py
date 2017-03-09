import markdown_to_json, json
from markdown_to_json.scripts.md_to_json import get_markdown_ast
from markdown_to_json.markdown_to_json import Renderer, CMarkASTNester

f = open('46-code_example--RFD_and_file_download_injection_prevention--.md', 'r')
content = f.read()


def jsonify_md(markdown_file):
    nester = CMarkASTNester()
    renderer = Renderer()
    ast = get_markdown_ast(markdown_file)
    nested = nester.nest(ast)
    rendered = renderer.stringify_dict(nested)
    result = json.dumps(rendered)
    return result

item = jsonify_md("46-code_example--RFD_and_file_download_injection_prevention--.md")
#item = jsonify_md("1-code_example--File_upload--.md")
print(item)

#import CommonMark

#f = open('1-code_example--File_upload--.md', 'r')
#f = open('46-code_example--RFD_and_file_download_injection_prevention--.md', 'r')

#content = f.read()

#parser = CommonMark.Parser()
#ast = parser.parse(content)

#json = CommonMark.dumpJSON(ast)
#print(json)
