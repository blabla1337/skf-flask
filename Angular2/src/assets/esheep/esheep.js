/*
 * Project:
 *                eSheep - Webpage
 *
 * Date:
 *                04.april 2018
 *
 * Author:
 *                Adriano Petrucci (http://esheep.petrucci.ch)
 *
 * Version:       0.9.0
 *
 * Introduction:
 *                As "wrapper" for the OpenSource C# project
 *                (see https://github.com/Adrianotiger/desktopPet),
 *                this javascript "class" was written to get the animations also inside your
 *                webpage. It doesn't work like the Windows version, but show much animations from it.
 *
 * Description:
 *                Add a walking pet (sheep to your home page) with just a few lines of code!
 *                Will add a lovely sheep (stray sheep) and this will walk around your page and over
 *                all <hr>s and <div>s with a border. You can also select another animation, using your
 *                personal XML file or one from the database.
 *
 * How to use:
 *                Add this line in your <header>:
 *                <script src="https://adrianotiger.github.io/web-esheep/src/esheep.js"></script>
 *                Add this lines in your <body> (at the end if possible):
 *                <script>
                    var pet = new eSheep();
                    pet.Start();
                  </script>
 *                That's all!
 *
 * Requirement:
 *                Tested on IE11, Edge and Opera
 *
 * Changelog:
 *                Version 0.9.0 - 11.07.2019:
 *                  - Updated animation link to the main project animation
 *                  - Recompiled with new Yarn version (security vulnerability)
 *                Version 0.8.0 - 29.05.2018:
 *                  - Moved animation files to github
 *                  - Added options to the script 
 *                  - Load an animation from the GitHub animations from the popup window
 *                Version 0.7.1 - 04.04.2018:
 *                  - Add max-width: none to ensure the image is properly shown
 *                Version 0.7 - 13.11.2017:
 *                  - better Javascript structure
 *                  - GitHub version (https://github.com/Adrianotiger/web-esheep)
 *                  - Childs animations added
 *                  - Better comments
 *                  - Replaced alerts with console.error
 *                Version 0.5 - 12.07.2017:
 *                  - animations starts only once the image was loaded (thanks RedSparr0w)
 *                Version 0.x:
 *                  - still beta versions...
 */

const VERSION = '0.9.1';              // web eSheep version
const ACTIVATE_DEBUG = false;         // show log on console
const DEFAULT_XML = "https://raw.githubusercontent.com/blabla1337/skf-flask/main/Angular2/src/assets/esheep/animation.xml"; // default XML animation
const COLLISION_WITH = ["div", "hr", "button", "input"]; // elements on page to detect for collisions

  /*
   * eSheep class.
   * Create a new class of this type if you want a new pet. Will create the components for the pet.
   * Once created, you can call [variableName].Start() to start the animation with your desired pet.
   */
class eSheep
{  
    /* Parameters for options [default]:
     * - allowPets: [none], all
     * - allowPopup: [yes], no
     */
  constructor(options, isChild)
  {
    this.userOptions = options ? options : {allowPets : "none", allowPopup : "yes"};
    if(!this.userOptions.allowPopup) this.userOptions.allowPopup = "yes";
    if(!this.userOptions.allowPets) this.userOptions.allowPets = "none";
        
      // CORS: Cross calls are not accepted by new browsers.
    this.animationFile = DEFAULT_XML;

    this.id = Date.now() + Math.random();

    this.DOMdiv = document.createElement("div");    // Div added to webpage, containing the sheep
    this.DOMdiv.setAttribute("id", this.id);
    this.DOMimg = document.createElement("img");    // Tile image, will be positioned inside the div
    this.DOMinfo = document.createElement("div");   // about dialog, if you press on the sheep

    this.parser = new DOMParser();                  // XML parser
    this.xmlDoc = null;                             // parsed XML Document
    this.prepareToDie = false;                      // when removed, animations should be stopped

    this.isChild = (isChild != null);               // Child will be removed once they reached the end

    this.tilesX = 1;                                // Quantity of images inside Tile
    this.tilesY = 1;                                // Quantity of images inside Tile
    this.imageW = 1;                                // Width of the sprite image
    this.imageH = 1;                                // Height of the sprite image
    this.imageX = 1;                                // Position of sprite inside webpage
    this.imageY = 1;                                // Position of sprite inside webpage
    this.flipped = false;                           // if sprite is flipped
    this.dragging = false;                          // if user is dragging the sheep
    this.infobox = false;                           // if infobox is visible
    this.animationId = 0;                           // current animation ID
    this.animationStep = 0;                         // current animation step
    this.animationNode = null;                      // current animation DOM node
    this.sprite = new Image();                      // sprite image (Tiles)
    this.HTMLelement = null;                        // the HTML element where the pet is walking on
    this.randS = Math.random() * 100;               // random value, will change when page is reloaded

    this.screenW = window.innerWidth
                  || document.documentElement.clientWidth
                  || document.body.clientWidth;     // window width

    this.screenH = window.innerHeight
                  || document.documentElement.clientHeight
                  || document.body.clientHeight;    // window height
  }

    /*
     * Start new animation on the page.
     * if animation is not set, the default sheep will be taken
     */
  Start(animation)
  {
    if(typeof animation !== 'undefined' &&
      animation != null)
    {
      this.animationFile = animation;
    }

    var ajax = new XMLHttpRequest();
    var sheepClass = this;

    ajax.open("GET", this.animationFile, true);
    ajax.addEventListener("readystatechange", function() {
      if(this.readyState == 4)
      {
        if(this.status == 200)
            // successfully loaded XML, parse it and create first esheep.
          sheepClass._parseXML(this.responseText);
        else
          console.error("XML not available:" + this.statusText + "\n" + this.responseText);
      }
    });
    ajax.send(null);
  }

  remove() {
    this.prepareToDie = true;
    this.DOMinfo.Hide();
    setTimeout(()=>{
      this.DOMdiv = this.DOMimg = this.DOMinfo = null;
      document.getElementById(this.id).outerHTML='';
    }, 500);
  }

    /*
     * Parse loaded XML, contains spawn, animations and childs
     */
  _parseXML(text)
  {
    this.xmlDoc = this.parser.parseFromString(text,'text/xml');
    var image = this.xmlDoc.getElementsByTagName('image')[0];
    this.tilesX = image.getElementsByTagName("tilesx")[0].textContent;
    this.tilesY = image.getElementsByTagName("tilesy")[0].textContent;
      // Event listener: Sprite was loaded =>
      //   play animation only when the sprite is loaded
    this.sprite.addEventListener("load", () =>
    {
      if(ACTIVATE_DEBUG) console.log("Sprite image loaded");
      var attribute =
      "width:" + (this.sprite.width) + "px;" +
      "height:" + (this.sprite.height) + "px;" +
      "position:absolute;" +
      "top:0px;" +
      "left:0px;" +
      "max-width: none;";
      this.DOMimg.setAttribute("style", attribute);
        // prevent to move image (will show the entire sprite sheet if not catched)
      this.DOMimg.addEventListener("dragstart", e => {e.preventDefault(); return false;});
      this.imageW = this.sprite.width / this.tilesX;
      this.imageH = this.sprite.height / this.tilesY;
      attribute =
        "width:" + (this.imageW) + "px;" +
        "height:" + (this.imageH) + "px;" +
        "position:fixed;" +
        "top:" + (this.imageY) + "px;" +
        "left:" + (this.imageX) + "px;" +
        "transform:rotatey(0deg);" +
        "cursor:move;" +
        "z-index:2000;" +
        "overflow:hidden;";
      this.DOMdiv.setAttribute("style", attribute);
      this.DOMdiv.appendChild(this.DOMimg);

      if(this.isChild)
        this._spawnChild();
      else
        this._spawnESheep();
    });


    this.sprite.src = 'data:image/png;base64,' + image.getElementsByTagName("png")[0].textContent;
    this.DOMimg.setAttribute("src", this.sprite.src);

    // Mouse move over eSheep, check if eSheep should be moved over the screen
    this.DOMdiv.addEventListener("mousemove", e => 
    {
      if(!this.dragging && e.buttons==1 && e.button==0)
      {
        this.dragging = true;
        this.HTMLelement = null;
        var childsRoot = this.xmlDoc.getElementsByTagName('animations')[0];
        var childs = childsRoot.getElementsByTagName('animation');
        for(var k=0;k<childs.length;k++)
        {
          if(childs[k].getElementsByTagName('name')[0].textContent == "drag")
          {
            this.animationId = childs[k].getAttribute("id");
            this.animationStep = 0;
            this.animationNode = childs[k];
            break;
          }
        }
      }
    });
    // Add event listener to body, if mouse moved too fast over the dragging eSheep
    document.body.addEventListener("mousemove", e => 
    {
      if(this.dragging)
      {
        this.imageX = parseInt(e.clientX) - this.imageW/2;
        this.imageY = parseInt(e.clientY) - this.imageH/2;

        this.DOMdiv.style.left = this.imageX + "px";
        this.DOMdiv.style.top = this.imageY + "px";
        this.DOMinfo.style.left = parseInt(this.imageX + this.imageW/2) + "px";
        this.DOMinfo.style.top = this.imageY + "px";
      }
    });
    // Window resized, recalculate eSheep bounds
    document.body.addEventListener("resize", () => 
    {
      this.screenW = window.innerWidth
                || document.documentElement.clientWidth
                || document.body.clientWidth;

      this.screenH = window.innerHeight
                || document.documentElement.clientHeight
                || document.body.clientHeight;

      if(this.imageY + this.imageH > this.screenH)
      {
        this.imageY = this.screenH - this.imageH;
        this.DOMdiv.style.top = this.imageY + "px";
      }
      if(this.imageX + this.imageW > this.screenW)
      {
        this.imageX = this.screenW - this.imageW;
        this.DOMdiv.style.left = this.imageX + "px";
      }
    });
    // Don't allow contextmenu over the sheep
    this.DOMdiv.addEventListener("contextmenu", e => {
      e.preventDefault();
      return false;
    });
    // Mouse released
    this.DOMdiv.addEventListener("mouseup", e => {
      if(this.dragging)
      {
        this.dragging = false;
      }
      else if(this.infobox)
      {
        this.DOMinfo.Hide();
        this.infobox = false;
      }
    });
    // Mouse released over the info box
    this.DOMinfo.addEventListener("mouseup", e => {
      this.DOMinfo.Hide();
      this.infobox = false;
    });
   
      // Add about and sheep elements to the body
    document.body.appendChild(this.DOMinfo);
    document.body.appendChild(this.DOMdiv);
        
    this.DOMinfo.Show = () => {
      this.DOMinfo.style.display = "block";
      this.DOMinfo.style.transform = "translate(-50%, -100%) scale(1.0)";
    }
    this.DOMinfo.Hide = () => {
      this.DOMinfo.style.transform = "translate(-50%, -50%) scale(0.1)";
      setTimeout(()=>{this.DOMinfo.style.display = "none";}, 300);
    }
  };

    /*
     * Set new position for the pet
     * If absolute is true, the x and y coordinates are used as absolute values.
     * If false, x and y are added to the current position
     */
  _setPosition(x, y, absolute)
  {
    if (this.DOMdiv) {
      if(absolute)
      {
        this.imageX = parseInt(x);
        this.imageY = parseInt(y);
      }
      else
      {
        this.imageX = parseInt(this.imageX) + parseInt(x);
        this.imageY = parseInt(this.imageY) + parseInt(y);
      }
      this.DOMdiv.style.left = this.imageX + "px";
      this.DOMdiv.style.top = this.imageY + "px";
    }
  }

    /*
     * Spawn new esheep, this is called if the XML was loaded successfully
     */
  _spawnESheep()
  {
    var spawnsRoot = this.xmlDoc.getElementsByTagName('spawns')[0];
    var spawns = spawnsRoot.getElementsByTagName('spawn');
    var prob = 0;
    for(var i=0;i<spawns.length;i++)
      prob += parseInt(spawns[0].getAttribute("probability"));
    var rand = Math.random() * prob;
    prob = 0;
    for(i=0;i<spawns.length;i++)
    {
      prob += parseInt(spawns[i].getAttribute("probability"));
      if(prob >= rand || i == spawns.length-1)
      {
        this._setPosition(
          this._parseKeyWords(spawns[i].getElementsByTagName('x')[0].textContent),
          this._parseKeyWords(spawns[i].getElementsByTagName('y')[0].textContent),
          true
        );
        if(ACTIVATE_DEBUG) console.log("Spawn: " + this.imageX + ", " + this.imageY);
        this.animationId = spawns[i].getElementsByTagName('next')[0].textContent;
        this.animationStep = 0;
        var childsRoot = this.xmlDoc.getElementsByTagName('animations')[0];
        var childs = childsRoot.getElementsByTagName('animation');
        for(var k=0;k<childs.length;k++)
        {
          if(childs[k].getAttribute("id") == this.animationId)
          {
            this.animationNode = childs[k];

              // Check if child should be loaded toghether with this animation
            var childsRoot = this.xmlDoc.getElementsByTagName('childs')[0];
            var childs = childsRoot.getElementsByTagName('child');
            for(var j=0;j<childs.length;j++)
            {
              if(childs[j].getAttribute("animationid") == this.animationId)
              {
                if(ACTIVATE_DEBUG) console.log("Child from Spawn");
                var eSheepChild = new eSheep(null, true);
                eSheepChild.animationId = childs[j].getElementsByTagName('next')[0].textContent;
                var x = childs[j].getElementsByTagName('x')[0].textContent;//
                var y = childs[j].getElementsByTagName('y')[0].textContent;
                eSheepChild._setPosition(this._parseKeyWords(x), this._parseKeyWords(y), true);
                // Start animation
                eSheepChild.Start(this.animationFile);
                break;
              }
            }
            break;
          }
        }
        break;
      }
    }
      // Play next step
    this._nextESheepStep();
  }

    /*
     * Like spawnESheep, but for Childs
     */
  _spawnChild()
  {
    var childsRoot = this.xmlDoc.getElementsByTagName('animations')[0];
    var childs = childsRoot.getElementsByTagName('animation');
    for(var k=0;k<childs.length;k++)
    {
      if(childs[k].getAttribute("id") == this.animationId)
      {
        this.animationNode = childs[k];
        break;
      }
    }
    this._nextESheepStep();
  }

    // Parse the human readable expression from XML to a computer readable expression
  _parseKeyWords(value)
  {
    value = value.replace(/screenW/g, this.screenW);
    value = value.replace(/screenH/g, this.screenH);
    value = value.replace(/areaW/g, this.screenH);
    value = value.replace(/areaH/g, this.screenH);
    value = value.replace(/imageW/g, this.imageW);
    value = value.replace(/imageH/g, this.imageH);
    value = value.replace(/random/g, Math.random()*100);
    value = value.replace(/randS/g, this.randS);
    value = value.replace(/imageX/g, this.imageX);
    value = value.replace(/imageY/g, this.imageY);

    var ret = 0;
    try
    {
      ret = eval(value);
    }
    catch(err)
    {
      console.error("Unable to parse this position: \n'" + value + "'\n Error message: \n" + err.message);
    }
    return ret;
  }

    /*
     * Once the animation is over, get the next animation to play
     */
  _getNextRandomNode(parentNode)
  {
    var baseNode = parentNode.getElementsByTagName('next');
    var childsRoot = this.xmlDoc.getElementsByTagName('animations')[0];
    var childs = childsRoot.getElementsByTagName('animation');
    var prob = 0;
    var nodeFound = false;

      // no more animations (it was the last one)
    if(baseNode.length == 0)
    {
        // If it is a child, remove the child from document
      if(this.isChild)
      {
        // remove child
        if(ACTIVATE_DEBUG) console.log("Remove child");
        document.body.removeChild(this.DOMinfo);
        document.body.removeChild(this.DOMdiv);
        delete this;
      }
        // else, spawn sheep again
      else
      {
        this._spawnESheep();
      }
      return false;
    }

    for(var k=0;k<baseNode.length;k++)
    {
      prob += parseInt(baseNode[k].getAttribute("probability"));
    }
    var rand = Math.random() * prob;
    var index = 0;
    prob = 0;
    for(k=0;k<baseNode.length;k++)
    {
      prob += parseInt(baseNode[k].getAttribute("probability"));
      if(prob >= rand)
      {
        index = k;
        break;
      }
    }
    for(k=0;k<childs.length;k++)
    {
      if(childs[k].getAttribute("id") == baseNode[index].textContent)
      {
        this.animationId = childs[k].getAttribute("id");
        this.animationStep = 0;
        this.animationNode = childs[k];
        nodeFound = true;
        break;
      }
    }

    if(nodeFound) // create Child, if present
    {
      var childsRoot = this.xmlDoc.getElementsByTagName('childs')[0];
      var childs = childsRoot.getElementsByTagName('child');
      for(k=0;k<childs.length;k++)
      {
        if(childs[k].getAttribute("animationid") == this.animationId)
        {
          if(ACTIVATE_DEBUG) console.log("Child from Animation");
          var eSheepChild = new eSheep(null, true);
          eSheepChild.animationId = childs[k].getElementsByTagName('next')[0].textContent;
          var x = childs[k].getElementsByTagName('x')[0].textContent;//
          var y = childs[k].getElementsByTagName('y')[0].textContent;
          eSheepChild._setPosition(this._parseKeyWords(x), this._parseKeyWords(y), true);
          eSheepChild.Start(this.animationFile);
          break;
        }
      }
    }

    return nodeFound;
  }

    /*
     * Check if sheep is walking over a defined HTML TAG-element
     */
  _checkOverlapping()
  {
    var x = this.imageX;
    var y = this.imageY + this.imageH;
    var rect;
    var margin = 20;
    if(this.HTMLelement) margin = 5;
    for(var index in COLLISION_WITH)
    {
      var els = document.body.getElementsByTagName(COLLISION_WITH[index]);

      for(var i=0;i<els.length;i++)
      {
        rect = els[i].getBoundingClientRect();

        if(y > rect.top - 2 && y < rect.top + margin)
        {
          if(x > rect.left && x < rect.right - this.imageW)
          {
            var style = window.getComputedStyle(els[i]);
            if((style.borderTopStyle != "" && style.borderTopStyle != "none") && style.display != "none")
            {
              return els[i];
            }
          }
        }
      }
    }
    return false;
  }

    /*
     * Try to get the value of a node (from the current animationNode), if it is not possible returns the defaultValue
     */
  _getNodeValue(nodeName, valueName, defaultValue)
  {
    if(!this.animationNode || !this.animationNode.getElementsByTagName(nodeName)) return;
    if(this.animationNode.getElementsByTagName(nodeName)[0].getElementsByTagName(valueName)[0])
    {
      var value = this.animationNode.getElementsByTagName(nodeName)[0].getElementsByTagName(valueName)[0].textContent;

      return this._parseKeyWords(value);
    }
    else
    {
      return defaultValue;
    }
  }

    /*
     * Next step (each frame is a step)
     */
  _nextESheepStep()
  {
    if(this.prepareToDie) return;
    
    var x1 = this._getNodeValue('start','x',0);
    var y1 = this._getNodeValue('start','y',0);
    var off1 = this._getNodeValue('start','offsety',0);
    var opa1 = this._getNodeValue('start','opacity',1);
    var del1 = this._getNodeValue('start','interval',1000);
    var x2 = this._getNodeValue('end','x',0);
    var y2 = this._getNodeValue('end','y',0);
    var off2 = this._getNodeValue('end','offsety',0);
    var opa2 = this._getNodeValue('end','interval',1);
    var del2 = this._getNodeValue('end','interval',1000);

    var repeat = this._parseKeyWords(this.animationNode.getElementsByTagName('sequence')[0].getAttribute('repeat'));
    var repeatfrom = this.animationNode.getElementsByTagName('sequence')[0].getAttribute('repeatfrom');
    var gravity = this.animationNode.getElementsByTagName('gravity');
    var border = this.animationNode.getElementsByTagName('border');

    var steps = this.animationNode.getElementsByTagName('frame').length +
                (this.animationNode.getElementsByTagName('frame').length - repeatfrom) * repeat;

    var index;

    if(this.animationStep < this.animationNode.getElementsByTagName('frame').length)
      index = this.animationNode.getElementsByTagName('frame')[this.animationStep].textContent;
    else if(repeatfrom == 0)
      index = this.animationNode.getElementsByTagName('frame')[this.animationStep % this.animationNode.getElementsByTagName('frame').length].textContent;
    else
      index = this.animationNode.getElementsByTagName('frame')[parseInt(repeatfrom) + parseInt((this.animationStep - repeatfrom) % (this.animationNode.getElementsByTagName('frame').length - repeatfrom))].textContent;

    this.DOMimg.style.left = (- this.imageW * (index % this.tilesX)) + "px";
    this.DOMimg.style.top = (- this.imageH * parseInt(index / this.tilesX)) + "px";

    if(this.dragging || this.infobox)
    {
      this.animationStep++;
      setTimeout(this._nextESheepStep.bind(this), 50);
      return;
    }

    if(this.flipped)
    {
      x1 = -x1;
      x2 = -x2;
    }

    if(this.animationStep == 0)
      this._setPosition(x1, y1, false);
    else
      this._setPosition(
                          parseInt(x1) + parseInt((x2-x1)*this.animationStep/steps),
                          parseInt(y1) + parseInt((y2-y1)*this.animationStep/steps),
                          false);

    this.animationStep++;

    if(this.animationStep >= steps)
    {
      if(this.animationNode.getElementsByTagName('action')[0])
      {
        switch(this.animationNode.getElementsByTagName('action')[0].textContent)
        {
          case "flip":
            if(this.DOMdiv.style.transform == "rotateY(0deg)")
            {
              this.DOMdiv.style.transform = "rotateY(180deg)";
              this.flipped = true;
            }
            else
            {
              this.DOMdiv.style.transform = "rotateY(0deg)";
              this.flipped = false;
            }
            break;
          default:

            break;
        }
      }
      if(!this._getNextRandomNode(this.animationNode.getElementsByTagName('sequence')[0])) return;
    }

    var setNext = false;

    if(border && border[0] && border[0].getElementsByTagName('next'))
    {
      if(x2<0 && this.imageX < 0)
      {
        this.imageX = 0;
        setNext = true;
      }
      else if(x2 > 0 && this.imageX > this.screenW - this.imageW)
      {
        this.imageX = this.screenW - this.imageW;
        this.DOMdiv.style.left = parseInt(this.imageX) + "px";
        setNext = true;
      }
      else if(y2 < 0 && this.imageY < 0)
      {
        this.imageY = 0;
        setNext = true;
      }
      else if(y2 > 0 && this.imageY > this.screenH - this.imageH)
      {
        this.imageY = this.screenH - this.imageH;
        setNext = true;
      }
      else if(y2 > 0)
      {
        if(this._checkOverlapping())
        {
          if(this.imageY > this.imageH)
          {
            this.HTMLelement = this._checkOverlapping();
            this.imageY = Math.ceil(this.HTMLelement.getBoundingClientRect().top) - this.imageH;
            setNext = true;
          }
        }
      }
      else if(this.HTMLelement)
      {
        if(!this._checkOverlapping())
        {
          if(this.imageY + this.imageH > this.HTMLelement.getBoundingClientRect().top + 3 ||
             this.imageY + this.imageH < this.HTMLelement.getBoundingClientRect().top - 3)
          {
            this.HTMLelement = null;
          }
          else if(this.imageX < this.HTMLelement.getBoundingClientRect().left)
          {
            this.imageX = parseInt(this.imageX + 3);
            setNext = true;
          }
          else
          {
            this.imageX = parseInt(this.imageX - 3);
            setNext = true;
          }
          this.DOMdiv.style.left = parseInt(this.imageX) + "px";
        }
      }
      if(setNext)
      {
        if(!this._getNextRandomNode(border[0])) return;
      }
    }
    if(!setNext && gravity && gravity[0] && gravity[0].getElementsByTagName('next'))
    {
      if(this.imageY < this.screenH - this.imageH - 2)
      {
        if(this.HTMLelement == null)
        {
          setNext = true;
        }
        else
        {
          if(!this._checkOverlapping())
          {
            setNext = true;
            this.HTMLelement = null;
          }
        }

        if(setNext)
        {
          if(!this._getNextRandomNode(gravity[0])) return;
        }
      }
    }
    if(!setNext)
    {
      if(this.imageX < - this.imageW && x2 < 0 ||
        this.imageX > this.screenW && x2 > 0 ||
        this.imageY < - this.imageH && y1 < 0 ||
        this.imageY > this.screenH && y2 > 0)
      {
        setNext = true;
        if(!this.isChild) {
          this._spawnESheep();
        }
        return;
      }
    }

    setTimeout(
      this._nextESheepStep.bind(this),
      parseInt(del1) + parseInt((del2 - del1) * this.animationStep / steps)
    );
  }

};