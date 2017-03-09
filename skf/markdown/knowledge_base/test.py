
import markdown_to_json, json
from markdown_to_json.scripts.md_to_json import get_markdown_ast
from markdown_to_json.markdown_to_json import Renderer, CMarkASTNester

def jsonify_md(markdown_file):
    nester = CMarkASTNester()
    renderer = Renderer()
    ast = get_markdown_ast(markdown_file)
    nested = nester.nest(ast)
    rendered = renderer.stringify_dict(nested)
    result = json.dumps(rendered)
    return result

#item = jsonify_md("1-knowledge_base--Filename_injection_Path_traversel--.md")
item = jsonify_md("3-knowledge_base--xss_injection--.md")
print(item)
