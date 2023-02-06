# Type checking

In order to ensure the security of your software, it is crucial to perform proper input validation on both syntactic and semantic levels.

Syntactic validation ensures that the syntax of structured fields, such as Social Security Numbers, dates, and currency symbols, is correct. This can be achieved through checks such as verifying the correct format of a date or ensuring that a currency symbol is in the correct form.

Semantic validation, on the other hand, focuses on the correctness of values within the specific business context. For example, it would check if a start date is prior to an end date or if a price falls within an acceptable range. This type of validation helps to enforce business rules and prevents attackers from exploiting weaknesses in your software by entering invalid data.

It is recommended to perform input validation as early as possible in the processing of user requests, in order to detect and prevent unauthorized input from being processed by your application. This will help to ensure the integrity and security of your software, protecting both your users and your business.

Type checking is an essential component of secure software development. By performing both syntactic and semantic validation, software developers can prevent unauthorized input from being processed by the application. This is achieved by verifying that the structure and values of input data are correct, according to the specific business context.

Type checking helps to catch errors early in the processing stage, which can prevent potential security vulnerabilities from being exploited. For example, a date field may be rejected if the start date is after the end date, or a phone number may be rejected if it doesn't match the expected format.

Furthermore, type checking helps to maintain the integrity of data throughout the application and ensures that data processing is consistent and reliable. As a result, type checking is a key component in maintaining the overall security and stability of an application.

It is important for software developers to understand the importance of type checking and to implement it as part of their development process. This will help to minimize the risk of security vulnerabilities, which could potentially result in loss of data, system downtime, or reputational damage.

---

## Implementing input validation¶
Input validation can be implemented using any programming technique that allows effective enforcement of syntactic and semantic correctness, for example:

- Data type validators are available natively in web application frameworks (such as Django Validators, Apache Commons Validators etc).
- Validation against JSON Schema and XML Schema (XSD) for input in these formats.
- Type conversion (e.g. Integer.parseInt() in Java, int() in Python) with strict exception handling
- Minimum and maximum value range check for numerical parameters and dates, minimum and maximum length check for strings.
An array of allowed values for small sets of string parameters (e.g. days of the week).
- Regular expressions for any other structured data covering the whole input string (^...$) and not using "any character" wildcard (such as . or \S)

---

### When using regular expressions
**Disclaimer**: when using regular expressions make sure that they are not too heavy to process. This could cause a DOS. More info can be found here [RegexDos](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

---

## Example time!
Now, let's take the following example:

```python
@app.route("/home", methods=['POST'])
def home():
    sizeImg = request.form['size']
    os.system('convert static/img/bones.png -resize '+sizeImg+'% static/img/bones.png')
    return render_template("index.html")
```

This piece of code is used to resize the size of an image. Fairly simple, straightforward and also, super vulnerable!
In this case, concatenating the ```sizeImg``` variable into the ```os.system()``` will lead to a command injection. 

a fairly straightforward way to render this attack mitigated is to type-check the parameter that goes into the function like this.

```python
@app.route("/home", methods=['POST'])
def home():
    sizeImg = request.form['size']
    checked = checkType(request.form['size'])
    os.system('convert static/img/bones.png -resize '+checked+'% static/img/bones.png')
    return render_template("index.html")

def checkType(size):
    if not size.isnumeric():
        return 404
```

Other methods to type check are the following:

```python
#Data validation and settings management using Python type annotations
from pydantic import BaseModel, Field 

class MyPydanticModel(BaseModel):
    pageId: int = Field(..., max_length=5)
```

```c#
//EF code first
 public class Pages
 {
    public number pageId { get; set; }
 }
```

## A more complex example

The previous example was a bit easier and straightforward so let's take another one. So, instead of checking a simple type such as "float, string, number, etc" we could also verify more "structured text formats" such as:

- Date of birth
- Phone number
- Credit card number
- email address
- Alphanumeric string
- etc

```python
#Data validation and settings management using Python type annotations
from pydantic import BaseModel, Field, EmailStr 

class MyPydanticModel(BaseModel):
    email : EmailStr = Field(..., max_length=5)
```

```python
#Data validation and settings management using Python type annotations
from pydantic import BaseModel, ValidationError, validator

class UserModel(BaseModel):
    username: str

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v
```

Now, these examples lean very heavily on python's ```pydantic``` library. But each programming language should have a similar type of solution where you can create a centralized approach for checking and testing the types of input that you expect on your models.

#### Sources:
[RegexDos](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

---

## In summary

In conclusion, type-checking is an important aspect of secure software development. It helps to prevent security vulnerabilities by ensuring that the input received by the application meets the expected format and structure and that the values of these inputs are semantically valid in the specific context of the application. By implementing type-checking, developers can catch and reject unauthorized inputs early in the processing, reducing the risk of exploitation by attackers and ensuring the security and stability of the application.

### Lab time!

You will shortly engage with the hands-on security lab! In this lab, you will have the opportunity to witness the real-world consequences of a common type of vulnerability in web applications known as an injection flaw. You will gain a deeper understanding of how these types of attacks can be carried out, and the damage they can cause. By conducting various simulated security tasks, you will learn about the techniques used to detect and prevent injection flaws, and the steps that can be taken to mitigate the risk of such attacks. This lab will provide you with a hands-on experience that will help you better understand the importance of secure coding practices and the consequences of ignoring them. Get ready to dive into the world of injection flaws and see the impact they can have!