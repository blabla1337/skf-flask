## Description

Whenever user supplied input is embeded directly into a template when the application
makes use of a templeating engine (jinja2, twig, Freemarker), a malicious attacker can inject 
and execute template expressions. More often the injection of template expressions will ultimately 
lead to RCE vulnerabilities.

This type of vulnerability is also seen a lot through applications that let the user intentionally
modify the template to provide users a more flexible way to style the applications pages like
a wiki page or CMS system.

## Solution

User supplied input should never be used directly into a template that uses a templating engine.
The following example is a small python flask function that renders user supplied input 
as part of the template. This allows a malicious attacker to even execute arbitrary commands when.

  @app.errorhandler(404)
  def page_not_found(e):
      template = """
  <html>
  <p>{0}</p>
  </html>

  """.format(request.url)
      return render_template_string(template), 404

The prefered way to add the user supplied input to this template would be:

  @app.errorhandler(404)
  def page_not_found(e):
    input = request.url
    return render_template("errorpage.html", input = input), 404
    
Wheras the content of the errorpage.html would look like

  <html>
      <p>{{input}}</p>
  </html>

