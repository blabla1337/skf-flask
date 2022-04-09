# Question
 
What is the problem here?
 
```
def post(self, request):
    query = json.loads(request.POST.get('q'))
    search_params = query.get('parameters', [])
    xpath = query.get("xpath")
    search = ""
    for param in search_params:
        value = re.sub(param.get('regex', ''), '', param.get('value'))
        if '/' in param.get('key'):
            query = '{} = "{}"'.format(param.get('key'), value)
        else:
            search = search.case_property_query(
                param.get('key'),
                value,
                clause=param.get('clause'),
                fuzzy=param.get('fuzzy'),
            )
```
 
-----SPLIT-----
 
# Answer

It is an Regular Expression Injection issue. User supplied data are being used to create regular expression and the attacker has full control over query criteria.